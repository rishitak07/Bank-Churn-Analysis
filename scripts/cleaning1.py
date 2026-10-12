import pandas as pd
from pathlib import Path

path = Path(__file__).resolve().parent.parent / "data" / "Customer-Churn-Records.csv"
df = pd.read_csv(path)

print("Shape:", df.shape)
print("\nColumn types:\n", df.dtypes)
print("\nMissing values:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())
print("Duplicate CustomerIds:", df["CustomerId"].duplicated().sum())
print("\nChurn rate (%):", round(df["Exited"].mean() * 100, 2))
print("\nSummary stats:\n", df.describe().round(2))

# --- Step 3: Clean and engineer features ---

# 1. Drop columns that add no analysis value
df = df.drop(columns=["RowNumber", "Surname"])

# 2. Rename for clarity
df = df.rename(columns={
    "Exited": "churn_flag",
    "Complain": "complain_flag",
    "Satisfaction Score": "satisfaction_score",
    "Card Type": "card_type",
    "Point Earned": "points_earned"
})

# 3. Readable labels
df["churn_status"] = df["churn_flag"].map({1: "Churned", 0: "Retained"})
df["active_status"] = df["IsActiveMember"].map({1: "Active", 0: "Inactive"})
df["credit_card_status"] = df["HasCrCard"].map({1: "Has Card", 0: "No Card"})
df["complain_status"] = df["complain_flag"].map({1: "Complained", 0: "No Complaint"})

# 4. Age groups
df["age_group"] = pd.cut(df["Age"], bins=[0, 29, 39, 49, 59, 100],
                         labels=["18-29", "30-39", "40-49", "50-59", "60+"])

# 5. Tenure groups (years)
df["tenure_group"] = pd.cut(df["Tenure"], bins=[-1, 2, 5, 8, 10],
                            labels=["0-2 yrs", "3-5 yrs", "6-8 yrs", "9-10 yrs"])

# 6. Balance bands
df["balance_band"] = pd.cut(df["Balance"], bins=[-1, 0, 50000, 100000, 150000, 300000],
                            labels=["Zero", "1-50K", "50-100K", "100-150K", "150K+"])

# 7. Credit score bands
df["credit_band"] = pd.cut(df["CreditScore"], bins=[0, 579, 669, 739, 799, 900],
                           labels=["Poor", "Fair", "Good", "Very Good", "Excellent"])

# 8. Save clean file
out = Path(__file__).resolve().parent.parent / "data" / "clean_bank_churn.csv"
df.to_csv(out, index=False)

print("\nClean shape:", df.shape)
print(df.head())
print("\nChurn rate by age group (%):")
print((df.groupby("age_group", observed=True)["churn_flag"].mean() * 100).round(2))