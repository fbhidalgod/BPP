import pandas as pd
import numpy
import matplotlib.pyplot as plt

def mayor(df):
    max = 0
    for key in df:
        if df[key].sum() > max:
            max = df[key].sum()
            mes_max = key

    print('El mes que más se ha ahorrado ha sido',mes_max, 'con', max,'€')

def menor(df):
    min = 0
    for key in df:
        if df[key].sum() < min:
            min = df[key].sum()
            mes_min = key

    print('El mes que más se ha gastado ha sido',mes_min,'con', min,'€')

def media(df):
    print('La media de gastos durante el año ha sido',df.sum().mean(),'€')

def total_gastos(df):
    tot = 0
    for key, values in df.items():
        for i,x in values.items():
            if x < 0:
                tot += x

    print('El total gastado durante el año ha sido',tot,'€')


def total_ingresos(df):
    tot = 0
    for key, values in df.items():
        for i,x in values.items():
            if x >= 0:
                tot += x

    print('El total ingresado durante el año ha sido',tot,'€')

def grafica(df):
    xbar = []
    ybar = []

    for key in df:
        xbar.append(df[key].sum())
        ybar.append(key)


    fig, ax = plt.subplots()
    ax.bar(ybar, xbar)
    plt.show()
