import pandas as pd

def extract(file_path="data/ncr_ride_bookings.csv"):
    """Lê o CSV e retorna um DataFrame"""
    return pd.read_csv(file_path)

if __name__ == "__main__":
    df = extract()
    print(df.head())
