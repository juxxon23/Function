import pandas as pd


def main():
    df = pd.read_excel("BasedeDatos_completa_2018_2021.xlsx")
    columns = df.columns
    authors = df[columns[2]]
    authors_keywords = []
    
    for author in authors:
        filter_data = df.loc[df[columns[2]] == author, [columns[2], columns[9]]]
        authors_keywords.append(filter_data)
    
    final_indexes = []
    for author in authors_keywords:
        a = author
        a_keywords = []
        row_indexes = []
        for row in a.index:
            a_keywords.append(a.loc[row]['Palabras clave'])
            if len(a_keywords) == 1:
                final_indexes.append(row)
            else:
                row_indexes.append(row)
                
        df_copy = df.drop(df.index[row_indexes])
        keyword = a_keywords[0].split(',')
        for word in a_keywords:
            word = word.split(',')
            if word != keyword:
                for w in word:
                    if w not in keyword:
                        keyword.append(w)
        
        keyword = ','.join(keyword)
        df_copy.loc[final_indexes[-1],['Palabras clave']] = keyword # NO ASIGNA!!!
        
    # Un nombre completo (Se puede filtrar si tiene un punto o no), realmente solo hay 2 nombres duplicados con punto. (César Augusto Marín López. y Diana Marcela Rengifo Arias.)
    # Falta tener en cuenta las copias de los nombres que estan en grupos.
    

if __name__ == "__main__":
    main()

    