# app/utils.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(countries):
    dfs = {}
    for country in countries:
        path = f"data/{country.lower().replace(' ', '_')}_clean.csv"
        dfs[country] = pd.read_csv(path)
        dfs[country]["Country"] = country
    return dfs

def plot_boxplot(dfs, metric):
    combined_df = pd.concat(dfs.values(), ignore_index=True)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=combined_df, x="Country", y=metric, ax=ax)
    ax.set_title(f"{metric} Distribution by Country")
    return fig

def get_summary_table(dfs):
    rows = []
    for country, df in dfs.items():
        row = {
            "Country": country,
            "GHI Mean": df["GHI"].mean(),
            "GHI Median": df["GHI"].median(),
            "GHI Std": df["GHI"].std(),
            "DNI Mean": df["DNI"].mean(),
            "DNI Median": df["DNI"].median(),
            "DNI Std": df["DNI"].std(),
            "DHI Mean": df["DHI"].mean(),
            "DHI Median": df["DHI"].median(),
            "DHI Std": df["DHI"].std(),
        }
        rows.append(row)
    return pd.DataFrame(rows)

def get_avg_ghi_ranking(dfs):
    rankings = []
    for country, df in dfs.items():
        avg_ghi = df["GHI"].mean()
        rankings.append({"Country": country, "GHI": avg_ghi})
    return pd.DataFrame(rankings).sort_values(by="GHI", ascending=False)
