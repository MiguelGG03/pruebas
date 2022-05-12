import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#FUNCION PARA QUE FUNCIONE EL GRAFICO

def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return "{:.1f}%\n({:d} €)".format(pct, absolute)


#LECTURA DDE DATOS

df=pd.read_csv('vehicles_1500.csv')


#SELECCIONAR DATOS

region = df.groupby("region").agg({"price" : 'mean', "year" : 'max'})
solo_precios = region['price'].tolist()

#LISTA CON LOS NOMBRES

nombres=['auburn','birmingham']

def tarta_with_labels(datos,nombres,titulo):

       fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

       data = datos
       ingredients = nombres

       wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                          textprops=dict(color="w"))

       ax.legend(wedges, ingredients,
              title="Leyenda",
              loc="center left",
              bbox_to_anchor=(1, 0, 0.5, 1))

       plt.setp(autotexts, size=8, weight="bold")

       ax.set_title(titulo)

       plt.show()
       plt.savefig("imagenes/Tarta_RegionesyPrecios.png")

def main():
       print(region)
       print(solo_precios)
       tarta_with_labels(solo_precios,nombres,'REGIONES Y PRECIOS')


if __name__=='__main__':
      main()
  
#tarta_with_labels(self,datos,nombres,titulo)

