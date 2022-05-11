import matplotlib.pyplot as plt
import numpy as np

class graficos: 

  def pie(self):
    
    plt.style.use('_mpl-gallery-nogrid')
    
    
    # make data
    x = [1, 2, 3, 4]
    colors = plt.get_cmap('Reds')(np.linspace(0.2, 0.7, len(x)))
    
    # plot
    fig, ax = plt.subplots()
    ax.pie(x, colors=colors, radius=3, center=(4, 4),
           wedgeprops={"linewidth": 1, "edgecolor": "black"}, frame=True)
    
    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
           ylim=(0, 8), yticks=np.arange(1, 8))
    
    plt.show()



if __name__=='__main__':
#  graficos.pie(graficos)
    
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

