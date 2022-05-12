import pandas as pd

class limpiador:
    def __init__(self):
        df=pd.read_csv('vehicles(1500).csv')
        self.df=df

    def crear_lista_regiones(self):