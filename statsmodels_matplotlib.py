#Essentials

import numpy as np
import statsmodels.api as sm
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import rcParams
from patsy import dmatrices

#Change font, font size, label distance

rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Lato']
rcParams['axes.labelpad'] = 15
plt.rcParams['font.size'] = 12

#Your data

df=pd.read_csv('data.csv')
print(df)

XX=df.iloc[:, 0]
YY=df.iloc[:, 1]

#Data to dmatrices (required by statsmodels?)

data=y, X = dmatrices('y ~ x', data=df, return_type='dataframe')
print('-----')
print(data)

#Model creation (OLS in this case)

model=sm.OLS(y,X)
fit=model.fit()

#Results

print(fit.summary())

results=fit.params
errors=fit.bse

#Results - labeling/rounding

intercept=results['Intercept']
slope=results['x']
r2=round(fit.rsquared_adj,3)

erro_intercept=errors['Intercept']
erro_slope=errors['x']

s=round(slope,2)
sr=round(erro_slope,2)
i=round(intercept,2)
ir=round(erro_intercept,2)

print('Slope: ', s, '+-', sr)
print('Intercept: ', i, '+-', ir)
print('Adj. R^2: ', r2)

#Graphing

x=np.linspace(min(XX), max(XX))

ax = plt.plot(x, s*x + i, linewidth=2.3, color='red', label='Regressão linear')
plt.scatter(XX,YY, color='black', label='Pontos amostrais')

plt.xlabel('X axis / units?')
plt.ylabel('Y axis / units?')

plt.xticks()
plt.yticks()
plt.text(0.85, 43.65, 'y = {:.2f}x + {:.2f}\n\nR$^2$ = {:.3f}'.format(s, i, r2), verticalalignment='center', horizontalalignment='center')
plt.legend()
plt.tight_layout()
plt.savefig('FigureName.png')
plt.show()
