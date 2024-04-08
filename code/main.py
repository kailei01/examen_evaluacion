from data_reader import leer_datos, filtrar_calcular_media

def main():
    datos='../data/datos_examen.csv'
    print(leer_datos(datos))
    print(filtrar_calcular_media(datos,'Examen_Kailei'))

if __name__ == "__main__":
    main()
