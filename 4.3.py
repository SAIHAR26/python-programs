import pandas as pd
s=pd.Series([10,20,30])
print(s)
s2=s.reindex(['b','a','c','d'])
print(s2)
