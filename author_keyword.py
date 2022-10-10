import pandas as pd


def main():
    df = pd.read_excel("BasedeDatos_completa_2018_2021.xlsx")
    columns = df.columns
    authors = df[columns[2]] # A esto le faltaria una verificacion de duplicados
    authors_keywords = []
    
    for author in authors:
        filter_data = df.loc[df[columns[2]] == author, [columns[2], columns[9]]]
        authors_keywords.append(filter_data)
    
    # Agrupar las palabras claves por nombre
    nolberto = authors_keywords[1]
    nolberto_keywords = []
    row_indexes = []
    for row in nolberto.index:
        nolberto_keywords.append(nolberto.loc[row]['Palabras clave'])
        if len(nolberto_keywords) > 1:
            row_indexes.append(row) 
    
    df_copy = df.drop(df.index[row_indexes])

    keyword = nolberto_keywords[0].split(',')
    for word in nolberto_keywords:
        word = word.split(',')
        if word != keyword:
            for w in word:
                if w not in keyword:
                    keyword.append(w)

    keyword = ','.join(keyword) #Falta guardar el string en la palabra clave de df_copy        

    
    # examinar las palabras claves a traves de strings

    
    #author_fixed = df.drop(df.index[[1,5,4]]) Borrar las copias del autor y dejar solo la primera aparicion. Esto va en el ciclo.
    #for i in authors_keywords:
    #    print(i)
    
    #print(authors_keywords)
    # Un nombre completo (Se puede filtrar si tiene un punto o no), realmente solo hay 2 nombres duplicados con punto. (César Augusto Marín López. y Diana Marcela Rengifo Arias.)
    # Varias palabras clave (Es un string por lo que se pueden analizar directamente coincidencias)
    # Se pueden separar las palabras claves como una lista de strings y verificar si cada una se encuentra en el string de palabras claves anterior.
    # Luego agregar lo que no esta con una coma al inicio.
    # Falta tener en cuenta las copias de los nombres que estan en grupos.
    

    #print(authors_keywords[0]["Palabras clave"][0])


if __name__ == "__main__":
    main()

    