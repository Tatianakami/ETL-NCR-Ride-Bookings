def transform(df):
    """Transforma os dados: adiciona coluna de status e aplica desconto"""
    if 'status' not in df.columns:
        df['status'] = 'Pending'
    if 'price' in df.columns:
        df['discounted_price'] = df['price'] * 0.9
    return df

if __name__ == "__main__":
    from extract import extract
    df = extract()
    df_t = transform(df)
    print(df_t.head())
