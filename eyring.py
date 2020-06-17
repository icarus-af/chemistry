import numpy as np
import statsmodels.api as sm
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import rcParams
from patsy import dmatrices
import seaborn as sns
import math
from uncertainties import ufloat
import uncertainties
from uncertainties.umath import *


rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Lato']
plt.rcParams['font.size'] = 12

df=pd.read_csv('eyring.csv')


print(df)

#x=df['T']
#y=df['lnk']

data=y, X = dmatrices('y ~ x', data=df, return_type='dataframe')


model=sm.OLS(y,X)
fit=model.fit()
print(fit.summary())

results=fit.params
errors=fit.bse



intercept=results['Intercept']
slope=results['x']
r2=round(fit.rsquared,3)

erro_intercept=errors['Intercept']
erro_slope=errors['x']

s=round(slope,2)
sr=round(erro_slope,2)
i=round(intercept,2)
ir=round(erro_intercept,2)


print('Slope: ', s, '+-', sr)
print('Intercept: ', i, '+-', ir)
print('R2: ', r2)

print('-----------------------')
#Contas
R=8.31446261815324


dS_calc=ufloat(i,ir)
dS=(dS_calc*R)

print('delta S: ', dS, 'J/mol K')

dH_calc=ufloat(s,sr)
dH=(-dH_calc*R)

print('delta H: ', dH, 'kJ/mol')

print('-----------------------')

ax = sns.regplot(x="x", y="y", data=df, scatter_kws={"color":'k', "label":'Pontos Amostrais'} , line_kws={"color":'r', "label":'Regressão Linear'}, truncate=True)

plt.xlabel('T / 10$^{-3}$ K', fontsize=14)
plt.ylabel(r'ln $\frac{k h}{k_{b} T}$', fontsize=14)

plt.xticks()
plt.yticks()
plt.text(0.25, 0.15,
    'y = {:.2f}x + {:.2f}\n\nR$^2$ = {:.3f}'.format(s, i, r2), ha='center', transform=ax.transAxes, weight='normal')
plt.legend()
plt.tight_layout()
plt.savefig('eyring.png')
plt.show()
