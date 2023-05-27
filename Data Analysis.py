# -*- coding: utf-8 -*-
"""
Created on Tue May 23 11:11:28 2023

@author: anjan
"""

import pandas as pd
import numpy as np
df=pd.read_csv('C:\\Users\\anjan\\OneDrive\\Desktop\\Power BI pet project\data.csv', encoding = "ISO-8859-1")
print(df.count())
print(df.columns)
print(df['CustomerID'].shape)
print(df['CustomerID'].isna().sum())
(df['CustomerID'].isna().sum()/df['CustomerID'].shape[0])*100#25% customers are Null
'''To remove the 25% NULL Customer IDs '''
df_final=df.loc[df['CustomerID'].isna()==False]
print(df_final.count())

print(df_final['Description'].nunique())#3896
print(df_final['CustomerID'].nunique()) #4372
print(df_final['Country'].nunique())#37
df_final['Total Price']=df_final['Quantity']* df_final['UnitPrice']

df_final['InvoiceDate'].dtypes

df_final['Invoice Date']=pd.to_datetime(df_final['InvoiceDate'])
df_final['Invoice Date']=pd.to_datetime(df_final['Invoice Date'],format='%Y/%m/%d %H:%M:%S').dt.strftime('%Y/%m/%d')
df_final['Invoice Date']=pd.to_datetime(df_final['Invoice Date'],format='%Y-%m-%d')
df_final['Invoice Date'].dtypes
df_final[['InvoiceDate','Invoice Date']]
df_final
df_final.drop(columns=['InvoiceDate'],inplace=True)
df_final.columns
df_final.to_csv('Final Data updated.csv',index=False)

