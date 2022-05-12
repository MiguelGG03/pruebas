import pandas as pd
import matplotlib as plt
import numpy as np

def main():
    
    df=pd.read_csv('vehicles(1500).csv')
    
    print(df.head(10))
    
    r = df.groupby("region").agg({"price" : 'mean'})

    print(r)

    price=r['price'].tolist()
    
    region=['auburn' ,
             'bellingham' ,
             'birmingham' ,
             'el paso' ,
             'erie' ,
             'fayetteville' ,
             'florida keys' ,
             'greensboro' ,
             'hudson valley' ,
             'la crosse' ,
             'medford-ashland' ,
             'prescott' ,
             'skagit / island / SJI' ,
             'worcester / central MA' ]


    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

    recipe = ["375 g flour",
            "75 g sugar",
            "250 g butter",
            "300 g berries"]

    #data = [float(x.split()[0]) for x in recipe]
    #ingredients = [x.split()[-1] for x in recipe]

    data=[1,2,3,4,15]
    ingredients=['a','b','c','d','e']



    def func(pct, allvals):
        absolute = int(np.round(pct/100.*np.sum(allvals)))
        return "{:.1f}%\n({:d} g)".format(pct, absolute)


    wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                    textprops=dict(color="w"))

    ax.legend(wedges, ingredients,
            title="Regiones",
            loc="center right",
            bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotexts, size=8, weight="bold")

    ax.set_title("Media Precios por Región")

    plt.show()





if __name__=='__main__':
    main()