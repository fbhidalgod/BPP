import operaciones
import pandas as pd

try:
    X = "finanzas2020.csv"
    df = pd.read_csv(X, delimiter="\t")

    columnas = df.columns
    assert(len(columnas) == 12)

    for key in df:
        if any(df[key].isnull() == True):
            raise ValueError

    for key in df:
        df[key] = pd.to_numeric(df[key], errors="coerce", downcast='float')

    operaciones.menor(df)
    operaciones.mayor(df)
    operaciones.media(df)
    operaciones.total_gastos(df)
    operaciones.total_ingresos(df)
    operaciones.grafica(df)

except Exception as e:
    print(type(e), e)
