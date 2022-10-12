import pandas as pd
#from collections import Counter

"""
-----------------------------------------------------------------------------
    To-Do
     - Graficar la red.
     - Comentar la funcion.

    Observaciones:
     - Corregir la base de datos: Nolberto Gutiérrez Posada - fila 54, la palabra 
       clave "logistica" no tiene tilde y genera dos logisticas en el investigador.

    @author: Grimpoteuthis
-----------------------------------------------------------------------------
"""

def getFilteredData():
    df = pd.read_excel("BasedeDatos_completa_2018-2021.xlsx")
    columns = df.columns
    authors = df[columns[2]]
    authors_keywords = []
    AFK = {} 
    
    for author in authors:
        filter_data = df.loc[df[columns[2]] == author.rstrip(), [columns[2], columns[9]]]
        authors_keywords.append(filter_data)
    
    for author in authors_keywords:
        keywords = []
        for row in author.index:
            keywords.append(author.loc[row][columns[9]])
            AFK[author.loc[row][columns[2]]] = keywords

    for author in AFK:
        if len(AFK[author]) > 1:
            keyword = AFK[author][0].split(',')
            for key in AFK[author]:
                key = key.split(',')
                if key != keyword:
                    for k in key:
                        if k not in keyword:
                            keyword.append(k)
            keyword = ','.join(keyword)
            AFK[author] = [keyword]

    authors_z = []
    keywords_z = []
    for author in AFK:
        authors_z.append(author)
        keywords_z.append(AFK[author])

    zipped = list(zip(authors_z, keywords_z))
    rr = pd.DataFrame(zipped, columns=[columns[2], columns[9]])
    #print(rr)
    #print(len(rr[columns[2]].unique()))


if __name__ == "__main__":
    getFilteredData()

    