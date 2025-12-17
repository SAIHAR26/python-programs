import pandas as pd
data ={'Name':['tom','jerry','raja'],'age':[20,None,22]}
df=pd.DataFrame(data)
print(df)
df['age']=df['age'].fillna(df['age'].mean())
print(df)
