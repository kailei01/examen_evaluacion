import pandas as pd 

def leer_datos(datos):
    """
    función que te lees una base de datos
    datos: base de datos
    leer los datos y pasar la columna de TS a datetime
    """
    df = pd.read_csv(datos)
    df['TS'] = pd.to_datetime(df['TS'])
    return df

def filtrar_calcular_media(df, nombre):
    """
    función que calcula la media de los Values según el nombre
    df: base de datos
    nombre: nombre del alumno 
    se hace un filtrado de la base de datos según el nombre
    una vez hecho el filtrado hacer la media
    """
    filtro = df[df['Tag'].str.contains(nombre)]
    media = filtro['Value'].mean()
    return media