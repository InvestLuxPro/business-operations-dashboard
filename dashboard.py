from analysis import (
    load_data,
    get_total_revenue,
    get_revenue_by_region,
    get_top_product,
    get_monthly_revenue,
)
from charts import plot_revenue_by_region, plot_monthly_revenue


def main():
    file_path = "data/sales_data.csv"
    df = load_data(file_path)

    total_revenue = get_total_revenue(df)
    revenue_by_region = get_revenue_by_region(df)
    top_product, top_product_revenue = get_top_product(df)
    monthly_revenue = get_monthly_revenue(df)

    print("\n📊 Business Operations Dashboard")
    print("-" * 35)
    print(f"💰 Total Revenue: ${total_revenue:,.2f}")
    print(f"🌎 Top Region: {revenue_by_region.idxmax()} (${revenue_by_region.max():,.2f})")
    print(f"🏆 Top Product: {top_product} (${top_product_revenue:,.2f})")
    print("\n📍 Revenue by Region:")
    print(revenue_by_region)

    plot_revenue_by_region(revenue_by_region)
    plot_monthly_revenue(monthly_revenue)


if __name__ == "__main__":
    main()