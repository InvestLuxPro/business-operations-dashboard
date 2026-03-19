import pandas as pd


def load_data(file_path):
    """Load sales data from a CSV file."""
    df = pd.read_csv(file_path)
    df["date"] = pd.to_datetime(df["date"])
    return df


def get_total_revenue(df):
    """Return total revenue."""
    return df["revenue"].sum()


def get_revenue_by_region(df):
    """Return revenue grouped by region."""
    return df.groupby("region")["revenue"].sum().sort_values(ascending=False)


def get_top_product(df):
    """Return the product with the highest total revenue."""
    product_revenue = df.groupby("product")["revenue"].sum()
    return product_revenue.idxmax(), product_revenue.max()


def get_monthly_revenue(df):
    """Return revenue grouped by date."""
    return df.groupby("date")["revenue"].sum().sort_index()