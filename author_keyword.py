import pandas as pd

"""
    To-Do
     - Falta tener en cuenta los duplicados en grupos con varios 
       integrantes.
     - Graficar la red.
     - Comentar la funcion.

    Observaciones:
     - Un nombre completo (Se puede filtrar si tiene un punto o no), 
       realmente solo hay 2 nombres duplicados con punto: César Augusto 
       Marín López y Diana Marcela Rengifo Arias.

"""

def main():
    df = pd.read_excel("BasedeDatos_completa_2018_2021.xlsx")
    columns = df.columns
    authors = df[columns[2]]
    authors_keywords = []
    AFK = {}
    
    for author in authors:
        filter_data = df.loc[df[columns[2]] == author, [columns[2], columns[9]]]
        authors_keywords.append(filter_data)
    
    for author in authors_keywords:
        keywords = []
        for row in author.index:
            keywords.append(author.loc[row]['Palabras clave'])
            AFK[author.loc[row]['Investigador Responsable y/o principal']] = keywords
    
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

    authors_z = authors.values.tolist()
    keywords_z = []
    for author in AFK:
        keywords_z.append(AFK[author])

    zipped = list(zip(authors_z, keywords_z))

    rr = pd.DataFrame(zipped, columns=['Investigador Responsable y/o principal', 'Palabras clave'])
    
    return rr


if __name__ == "__main__":
    main()

    