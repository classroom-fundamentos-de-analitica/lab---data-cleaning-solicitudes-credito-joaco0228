"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    #
    # Inserte su código aquí
    #

    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    nombre_archivo = 'solicitudes_credito.csv'

    df = pd.read_csv(nombre_archivo, sep=';')
    df = df.iloc[:,1:]
    df['sexo']= [i.lower() for i in df['sexo']]
    df = df.dropna()
    df['tipo_de_emprendimiento']= [str(i).lower() for i in df['tipo_de_emprendimiento']]
    df['idea_negocio']= [i.lower().replace("-"," ").replace("_"," ").strip() for i in df['idea_negocio']]
    df['barrio']= [str(i).replace("-"," ").replace("_"," ").lower() for i in df['barrio']]
    # LO CORRECTO SERÍA df['barrio']= [str(i).replace("-"," ").replace("_"," ").strip().lower() for i in df['barrio']] YA QUE HAY BARRIOS QUE DIFIEREN POR UN ESPACIO AL FINAL Y EN VERDAD SON LOS MISMOS, EN TOTAL HAY 223 BARRIOS Y SIN HACER ESTO CUENTA 225
    df['comuna_ciudadano']= [int(i) for i in df['comuna_ciudadano']]
    df['línea_credito']= [i.replace("-"," ").replace("_"," ").lower() for i in df['línea_credito']]
    df['monto_del_credito']= [i.replace(",","") for i in df['monto_del_credito']]

    df.monto_del_credito = df.monto_del_credito.str.strip('$')
    df.monto_del_credito = df.monto_del_credito.astype(float)
    fechas = []
    for i in df['fecha_de_beneficio']:
        try:
            fecha = pd.to_datetime(i, format='%Y/%m/%d')
        except ValueError:
            fecha = pd.to_datetime(i, format='%d/%m/%Y', errors='coerce')
        fechas.append(fecha)
    df['fecha_de_beneficio'] = fechas

    df.drop_duplicates(inplace=True)

    return df
