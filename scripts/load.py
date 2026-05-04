from sqlalchemy import create_engine
from ingest import fetch_launches
from transform import clean_launches, daily_summary

def load_data():
    engine = create_engine("postgresql://salma:spacex123@localhost:5432/spacexdb")
    raw = fetch_launches()
    df = clean_launches(raw)
    summary = daily_summary(df)
    df.to_sql("launches", engine, if_exists="replace", index=False)
    summary.to_sql("daily_launch_stats", engine, if_exists="replace", index=False)
    print("Data loaded successfully!")
    print(f"Launches table: {len(df)} rows")
    print(f"Stats table: {len(summary)} rows")

if __name__ == "__main__":
    load_data()