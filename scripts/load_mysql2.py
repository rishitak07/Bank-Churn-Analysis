import os
import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

path = Path(__file__).resolve().parent.parent / "data" / "clean_bank_churn.csv"
df = pd.read_csv(path)
df.columns = [c.lower() for c in df.columns]

PASSWORD = os.getenv("DB_PASSWORD","your_password_here")
engine = create_engine(
    f"mysql+pymysql://root:{PASSWORD}@127.0.0.1:3306/bank_churn"
)

df.to_sql("bank_churn", engine, if_exists="replace", index=False)
print("Loaded rows:", len(df))