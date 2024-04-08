import pandas as pd 

def leer_datos(datos):
    df = pd.read_csv(datos)
    df['TS'] = pd.to_datetime(df['TS'])
    return df

def filtrar_calcular_media(df, nombre):
    filtro = df[df['Tag'].str.contains(nombre)]
    media = filtro['Value'].mean()
    return media