# Import necessary packages (Make sure to also include in "requirements.txt" in this repository.)
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Print Title for the App
st.title("Microsoft Stock Data Dashboard by Lydia Pelton")

# Read CSV file with stock data (CSV file must be in 'main' folder for your assignment 4 repository) 
df = pd.read_csv("msft.csv")

# Set up the 3 tabs on the Dashboard
tabs = st.tabs(["📋 Raw Data", "📈 Price Chart", "📊 Volume Chart","Fun Tab"])

# Tab 1: Raw Data
with tabs[0]:
    st.subheader(f"Raw Data for MSFT")
    st.dataframe(df, use_container_width=True)

# Tab 2: Closing Price Chart
with tabs[1]:
    st.subheader(f"Closing Price for MSFT")
    st.line_chart(df['Close'])

# Tab 3: Volume Chart
with tabs[2]:
    st.subheader(f"Volume for MSFT")
    st.bar_chart(df['Volume'])

# Tab 4: Something New
# Tab 4: Fun Tab - Dachshund outline
with tabs[3]:
    st.subheader("🐶")

    # Smooths a list of (x, y) points into a curved line (Catmull-Rom spline)
    def smooth(points, closed=True, n=20):
        pts = np.array(points, dtype=float)
        if closed:
            pts = np.vstack([pts[-1], pts, pts[0], pts[1]])
        else:
            pts = np.vstack([pts[0], pts, pts[-1]])
        t = np.linspace(0, 1, n, endpoint=False)[:, None]
        curve = []
        for i in range(1, len(pts) - 2):
            p0, p1, p2, p3 = pts[i - 1], pts[i], pts[i + 1], pts[i + 2]
            curve.append(0.5 * ((2 * p1) + (-p0 + p2) * t
                                + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t**2
                                + (-p0 + 3 * p1 - 3 * p2 + p3) * t**3))
        curve.append(pts[-2][None])
        return np.vstack(curve)

    # Body outline (starts at the nose, goes over the back, around the legs, under the belly)
    body = [
        (0.5, 5.6), (1.0, 6.3), (2.0, 6.9), (3.2, 7.0), (4.1, 6.5),   # head
        (4.5, 5.6), (5.5, 5.0), (8.0, 4.8), (12.0, 4.8), (15.0, 4.9), # neck + long back
        (16.4, 4.6), (16.6, 3.6), (16.2, 2.6),                        # rump
        (16.6, 1.5), (17.4, 0.8), (17.2, 0.4), (15.9, 0.4),           # back leg + paw
        (15.6, 1.0), (15.3, 2.0), (14.6, 2.4),
        (10.0, 2.3), (6.8, 2.0),                                      # belly
        (6.3, 1.4), (6.2, 0.7), (6.0, 0.4), (4.6, 0.4),               # front leg + paw
        (4.5, 0.8), (5.1, 1.1), (5.0, 1.8),
        (4.6, 2.8), (4.0, 3.8), (3.2, 4.6), (1.6, 4.9), (0.8, 5.1),   # chest, throat, chin
    ]
    ear = [(3.3, 6.8), (3.5, 5.8), (3.9, 5.0), (4.3, 5.4), (4.2, 6.4)]
    tail = [(16.2, 4.9), (17.0, 5.4), (17.6, 6.3), (17.7, 7.2), (17.4, 7.6)]

    fig, ax = plt.subplots(figsize=(10, 5))
    b = smooth(body, closed=True)
    e = smooth(ear, closed=False)
    tl = smooth(tail, closed=False)

    ax.fill(b[:, 0], b[:, 1], color="#c47a3a", alpha=0.25)    # light fill (delete for outline only)
    ax.plot(b[:, 0], b[:, 1], color="black", linewidth=2.5)
    ax.plot(e[:, 0], e[:, 1], color="black", linewidth=2.5)
    ax.plot(tl[:, 0], tl[:, 1], color="black", linewidth=2.5)

    # Nose and a happy closed eye
    ax.plot(0.55, 5.6, "o", color="black", markersize=8)
    eye_x = np.linspace(1.7, 2.3, 20)
    ax.plot(eye_x, 6.15 - 0.6 * (eye_x - 2.0) ** 2, color="black", linewidth=2)

    ax.set_xlim(-0.5, 19)
    ax.set_ylim(-0.5, 8.5)
    ax.set_aspect("equal")
    ax.grid(True, linestyle="--", alpha=0.4)
    ax.set_title("Dachshund Plot")
    ax.set_xlabel("Length of dog")
    ax.set_ylabel("Height of dog")

    st.pyplot(fig)
