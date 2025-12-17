import pandas as pd
data={'Name':['Tom','Jerry'],
      'Age':[20,22]
      }
df=pd.DataFrame(data)
print(df)
df2=df.drop(0)
print(df2)

