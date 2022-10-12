import pandas as pd

"""
-----------------------------------------------------------------------------
    To-Do
     - Graficar la red.
     - Comentar la funcion.

    Observaciones:
     - Un nombre completo (Se puede filtrar si tiene un punto o no), 
       realmente solo hay 2 nombres duplicados con punto: César Augusto 
       Marín López y Diana Marcela Rengifo Arias.
     - Hay 9 grupos con varios autores (Hay proyectos con varios integrantes)

    @author: Grimpoteuthis
-----------------------------------------------------------------------------
"""

def getFilteredData():
    df = pd.read_excel("BasedeDatos_completa_2018_2021.xlsx") # "BasedeDatos_completa_2018_2021_corregida.xlsx"
    columns = df.columns
    authors = df[columns[2]]
    authors_keywords = []
    new_authors = []
    groups_del = []
    AFK = {} 
    
    for author in authors:
        filter_data = df.loc[df[columns[2]] == author, [columns[2], columns[9]]]
        authors_keywords.append(filter_data)
    
    for author in authors_keywords:
        keywords = []
        for row in author.index:
            keywords.append(author.loc[row][columns[9]])
            AFK[author.loc[row][columns[2]]] = keywords


    for group in AFK:
        if '\n' in group:
            for author in group.split('\n'):
                try:
                    AFK[author].append(','.join(AFK[group]))
                except KeyError:
                    new_authors.append([author, AFK[group]])
            groups_del.append(group)

    for key in groups_del:
        AFK.pop(key)
    
    for author_add in new_authors:
        AFK[author_add[0]] = author_add[1]

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
    print(rr)


if __name__ == "__main__":
    getFilteredData()

    