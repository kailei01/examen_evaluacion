from data_reader import leer_datos , filtrar_calcular_media

def main():
    datos= '/Users/kaileidengying/examen_evaluacion/data/datos_examen.csv'
    datos = leer_datos(datos)

    print(f'Mi media es: {filtrar_calcular_media(datos, "Examen_Kailei")}')

if __name__ == "__main__":
    main()
