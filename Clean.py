```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("telecom_churn.csv")

print("Dataset loaded successfully!")
print(df.head())

# Basic information
print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nChurn Count:")
print(df["churn"].value_counts())


# 1. Churn Distribution
churn_count = df["churn"].value_counts()

plt.figure(figsize=(6, 4))
plt.bar(churn_count.index.astype(str), churn_count.values)

plt.title("Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.savefig("charts/churn_distribution.png")
plt.show()
plt.close()


# 2. Churn by Gender
gender_churn = pd.crosstab(df["gender"], df["churn"])

gender_churn.plot(kind="bar", figsize=(7, 4))

plt.title("Churn by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.legend(title="Churn")

plt.tight_layout()
plt.savefig("charts/churn_by_gender.png")
plt.show()
plt.close()


# 3. Churn by Telecom Partner
partner_churn = pd.crosstab(
    df["telecom_partner"],
    df["churn"]
)

partner_churn.plot(kind="bar", figsize=(8, 5))

plt.title("Churn by Telecom Partner")
plt.xlabel("Telecom Partner")
plt.ylabel("Number of Customers")
plt.xticks(rotation=45)
plt.legend(title="Churn")

plt.tight_layout()
plt.savefig("charts/churn_by_partner.png")
plt.show()
plt.close()


# 4. Churn by Age Group
df["age_group"] = pd.cut(
    df["age"],
    bins=[0, 20, 30, 40, 50, 60, 100],
    labels=["Below 20", "21-30", "31-40", "41-50", "51-60", "60+"]
)

age_churn = pd.crosstab(
    df["age_group"],
    df["churn"]
)

age_churn.plot(kind="bar", figsize=(8, 5))

plt.title("Churn by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.legend(title="Churn")

plt.tight_layout()
plt.savefig("charts/churn_by_age.png")
plt.show()
plt.close()


# 5. Churn by State
state_churn = pd.crosstab(
    df["state"],
    df["churn"]
)

top_states = df["state"].value_counts().head(10).index

state_churn = state_churn.loc[
    state_churn.index.isin(top_states)
]

state_churn.plot(kind="bar", figsize=(10, 5))

plt.title("Churn by Top 10 States")
plt.xlabel("State")
plt.ylabel("Number of Customers")
plt.xticks(rotation=45)
plt.legend(title="Churn")

plt.tight_layout()
plt.savefig("charts/churn_by_state.png")
plt.show()
plt.close()


# 6. Average Data Usage by Churn
data_churn = df.groupby("churn")["data_used"].mean()

plt.figure(figsize=(6, 4))
plt.bar(data_churn.index.astype(str), data_churn.values)

plt.title("Average Data Usage by Churn")
plt.xlabel("Churn")
plt.ylabel("Average Data Used")

plt.tight_layout()
plt.savefig("charts/data_usage_vs_churn.png")
plt.show()
plt.close()


# 7. Average Salary by Churn
salary_churn = df.groupby("churn")["estimated_salary"].mean()

plt.figure(figsize=(6, 4))
plt.bar(salary_churn.index.astype(str), salary_churn.values)

plt.title("Average Estimated Salary by Churn")
plt.xlabel("Churn")
plt.ylabel("Average Estimated Salary")

plt.tight_layout()
plt.savefig("charts/salary_vs_churn.png")
plt.show()
plt.close()


print("\nAnalysis completed successfully!")
print("All 7 charts have been saved in the charts folder.")
```
