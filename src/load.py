def load(df, output_file="data/output.csv"):
    """Salva o DataFrame transformado em CSV"""
    df.to_csv(output_file, index=False)
    print(f"Arquivo salvo em {output_file}")

if __name__ == "__main__":
    from extract import extract
    from transform import transform
    df = extract()
    df_t = transform(df)
    load(df_t)
