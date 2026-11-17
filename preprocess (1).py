from pathlib import Path
import pandas as pd

RAW = Path("data/raw/retail_transactions.csv")
OUT = Path("data/processed/retail_cleaned.csv")

def main():
    if not RAW.exists():
        raise FileNotFoundError(
            f"Place your permitted source CSV at: {RAW}"
        )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(RAW)

    print("Original shape:", df.shape)
    print("Missing values before cleaning:\n", df.isna().sum())
    print("Exact duplicate rows:", df.duplicated().sum())

    df.columns = (
        df.columns.str.strip().str.lower().str.replace(" ", "_")
    )

    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.strip()

    # Remove only exact duplicate rows.
    df = df.drop_duplicates()

    # Parse a date column if the source uses this column name.
    if "invoicedate" in df.columns:
        df["invoicedate"] = pd.to_datetime(
            df["invoicedate"], errors="coerce"
        )

    # Create revenue only when both columns are present.
    if {"quantity", "unitprice"}.issubset(df.columns):
        df["revenue"] = df["quantity"] * df["unitprice"]

    df.to_csv(OUT, index=False)
    print("Cleaned shape:", df.shape)
    print("Missing values after cleaning:\n", df.isna().sum())
    print("Saved:", OUT)

if __name__ == "__main__":
    main()
