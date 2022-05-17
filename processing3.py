import pandas as pd
columns=["row","Star_name","Distance","Mass","Radius"]
df1=pd.read_csv("wanttomerge.csv",names=columns)
df1=df1.iloc[1: , :]
del df1["row"]

columns=["Star_name","Distance","Mass","Radius","luminosity"]
df2=df2=pd.read_csv("bright_starts.csv",names=columns)
df2=df2.iloc[1: , :]

final=pd.concat([df1,df2],axis=0)
final.to_csv("final.csv",index=True)

