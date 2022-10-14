import pandas as pd

# @author: Grimpoteuthis


def getFilteredData():
    df = pd.read_excel("BasedeDatos_completa_2018-2021.xlsx")
    columns = df.columns 
    authors = df[columns[2]]
    authors_keywords = [df.loc[df[columns[2]] == author.rstrip(), [columns[2], columns[9]]] for author in authors] # Filtra autores con sus respectivas palabras clave.
    AFK = {} # Diccionario {author:[keywords]}
    
    for author in authors_keywords:
        # Agrupa las palabras clave de cada autor y se almacena en el diccionario.
        keywords = []
        for row in author.index:
            keywords.append(author.loc[row][columns[9]])
            AFK[author.loc[row][columns[2]]] = keywords

    for author in AFK:
        # Crea un string con todas las palabras clave sin repetir por cada autor.
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

    zipped = [(author, AFK[author]) for author in AFK] # Lista de tuplas [(author, keywords)]
    rr = pd.DataFrame(zipped, columns=[columns[2], columns[9]]) # DataFrame con los datos filtrados.   


if __name__ == "__main__":
    getFilteredData()   