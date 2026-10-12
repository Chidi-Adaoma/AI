
import sys
import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt

print("=" * 50)
print("ENVIRONMENT CHECK")
print("=" * 50)
print(f"Python version:      {sys.version.split()[0]}")
print(f"NumPy version:       {np.__version__}")
print(f"Pandas version:      {pd.__version__}")
print(f"Scikit-learn version:{sklearn.__version__}")
print("=" * 50)

# --- Quick sanity exercise: create and inspect a dataset ---
np.random.seed(42)

# Simulate: hours studied vs exam score
hours = np.random.uniform(1, 10, 50)
noise = np.random.normal(0, 5, 50)
scores = 10 + 8 * hours + noise  # true relationship + noise

df = pd.DataFrame({
    "hours_studied": hours.round(2),
    "exam_score": scores.round(2),
})

print("\nFirst 5 rows:")
print(df.head())

print("\nBasic stats:")
print(df.describe())

# Save it so we can use it in later days
df.to_csv("../../data/raw/day01_hours_scores.csv", index=False)
print("\nSaved to data/raw/day01_hours_scores.csv")

# Quick plot
plt.figure(figsize=(8, 5))
plt.scatter(df["hours_studied"], df["exam_score"], alpha=0.7)
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Day 1: Simulated Data")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("../../data/raw/day01_plot.png", dpi=100)
print("Saved plot to data/raw/day01_plot.png")