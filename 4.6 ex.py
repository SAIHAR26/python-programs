import pandas as pd
data={'name':['Tom','jerry'],'Age':[20,22]}
df=pd.DataFrame(data)
print(df)
print(df.loc[0,'name'])
