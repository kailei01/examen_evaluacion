from data_reader import leer_datos , filtrar_calcular_media

def main():
    """
    Función principal que:
    lee datos de un archivo CSV
    calcula la media
    """
    datos= '/Users/kaileidengying/examen_evaluacion/data/datos_examen.csv'
    datos = leer_datos(datos)

    print(f'Mi media es: {filtrar_calcular_media(datos, "Examen_Kailei")}')

if __name__ == "__main__":
    main()
