import pandas as pd

def main():
    data_file = pd.read_excel("BasedeDatos_completa_2018_2021.xlsx")
    filter_data = data_file.loc[data_file["Investigador Responsable y/o principal"] == "César Augusto Marín López", ["Investigador Responsable y/o principal", "Palabras clave"]]
    print(filter_data)

if __name__ == "__main__":
    main()

    