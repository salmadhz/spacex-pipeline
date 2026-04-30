import pandas as pd
from ingest import fetch_launches

def clean_launches(raw_list):
    df= pd.DataFrame(raw_list)
    df = df[["name", "date_utc", "success", "rocket", "launchpad"]]
    df["success"] = df["success"].fillna(False)
    df["success"] = df["success"].astype(int)
    df["date_utc"] =pd.to_datetime(df["date_utc"])
    return df


def daily_summary(df):
    df["year"] = df["date_utc"].dt.year
    summary = df.groupby("year")["success"].agg(
        total = "count",
        successes = "sum"
    ) .reset_index()
    return summary

if __name__ == "__main__":
    raw = fetch_launches()
    df = clean_launches(raw)
    print("the dimension of your dataframe is (number of rows(launches),number of columns):")
    print(df.shape)
    print(df.head())
    summary = daily_summary(df)
    print(summary)
