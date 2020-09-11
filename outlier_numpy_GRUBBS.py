import pandas as pd
import numpy as np



#a = [float(x) for x in input().split()]
a = [12.13,12.12,12.13,12.12,12.2]
print(a)

df=np.array(a)
print('Data input: ', df)

print('------------')
tamanho = df.shape[0]
media = np.mean(df)
stdev = np.nanstd(df, ddof=1)
print('Average = ', media)
print('Standard Deviation = ', stdev)
print('Sample size: ', tamanho)


if tamanho == 3:
    Valor = (1.155*stdev)+media
    teste = df[df < Valor]
    print('------------')
    print('Valor critico: ', Valor)
    print(df)
    print('------------')
    if tamanho != teste.shape[0]:
        print('Outliers: ', df[df > Valor])
        print("Outliers removed!")
        print(teste)
        print('------------')
    else:
        print('No outliers detected!')
        print('------------')

elif tamanho == 4:
    Valor = (1.481*stdev)+media
    teste = df[df < Valor]
    print('------------')
    print('Valor critico: ', Valor)
    print(df)
    print('------------')
    if tamanho != teste.shape[0]:
        print('Outliers: ', df[df > Valor])
        print("Outliers removed!")
        print(teste)
        print('------------')
    else:
        print('No outliers detected!')
        print('------------')

elif tamanho == 5:
    Valor = (1.715*stdev)+media
    teste = df[df < Valor]
    print('------------')
    print('Valor critico: ', Valor)
    print(df)
    print('------------')
    if tamanho != teste.shape[0]:
        print('Outliers: ', df[df > Valor])
        print("Outliers removed!")
        print(teste)
        print('------------')
    else:
        print('No outliers detected!')
        print('------------')

elif tamanho == 6:
    Valor = (1.887*stdev)+media
    teste = df[df < Valor]
    print('------------')
    print('Valor critico: ', Valor)
    print(df)
    print('------------')
    if tamanho != teste.shape[0]:
        print('Outliers: ', df[df > Valor])
        print("Outliers removed!")
        print(teste)
        print('------------')
    else:
        print('No outliers detected!')
        print('------------')

elif tamanho == 7:
    Valor = (2.020*stdev)+media
    teste = df[df < Valor]
    print('------------')
    print('Valor critico: ', Valor)
    print(df)
    print('------------')
    if tamanho != teste.shape[0]:
        print('Outliers: ', df[df > Valor])
        print("Outliers removed!")
        print(teste)
        print('------------')
    else:
        print('No outliers detected!')
        print('------------')

elif tamanho == 8:
    Valor = (2.216*stdev)+media
    teste = df[df < Valor]
    print('------------')
    print('Valor critico: ', Valor)
    print(df)
    print('------------')
    if tamanho != teste.shape[0]:
        print('Outliers: ', df[df > Valor])
        print("Outliers removed!")
        print(teste)
        print('------------')
    else:
        print('No outliers detected!')
        print('------------')

elif tamanho == 9:
    Valor = (2.215*stdev)+media
    teste = df[df < Valor]
    print('------------')
    print('Valor critico: ', Valor)
    print(df)
    print('------------')
    if tamanho != teste.shape[0]:
        print('Outliers: ', df[df > Valor])
        print("Outliers removed!")
        print(teste)
        print('------------')
    else:
        print('No outliers detected!')
        print('------------')

elif tamanho == 10:
    Valor = (2.290*stdev)+media
    teste = df[df < Valor]
    #no_outlier = np.delete(df, np.argwhere(df > Valor)) Another method
    print('------------')
    print('Valor critico: ', Valor)
    print(df)
    print('------------')
    if tamanho != teste.shape[0]:
        print('Outliers: ', df[df > Valor])
        print("Outliers removed!")
        print(teste)
        print('------------')
    else:
        print('No outliers detected!')
        print('------------')
