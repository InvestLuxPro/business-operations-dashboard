import matplotlib.pyplot as plt


def plot_revenue_by_region(revenue_by_region):
    """Create a bar chart for revenue by region."""
    plt.figure(figsize=(8, 5))
    revenue_by_region.plot(kind="bar")
    plt.title("Revenue by Region")
    plt.xlabel("Region")
    plt.ylabel("Revenue ($)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig("revenue_by_region.png")
    plt.show()


def plot_monthly_revenue(monthly_revenue):
    """Create a line chart for revenue over time."""
    plt.figure(figsize=(8, 5))
    monthly_revenue.plot(kind="line", marker="o")
    plt.title("Revenue Over Time")
    plt.xlabel("Date")
    plt.ylabel("Revenue ($)")
    plt.tight_layout()
    plt.savefig("revenue_over_time.png")
    plt.show()
