from numpy.typing import _256Bit
import pandas as pd
import csv




#Mass=rows[2]
columns=["row","Star_name","Distance","Mass","Radius"]
df=pd.read_csv("bright_stars2.csv",names=columns)
df=df.iloc[1: , :]
del df["row"]
df=df[df["Distance"].notna()]
df=df[df["Mass"].notna()]
df=df[df["Radius"].notna()]

Mass=df["Mass"].tolist()
Radius=df["Radius"].tolist()
print(Mass)
planet_radius=[]
planet_mass=[]

for i in Mass:
    mass=(float(i))*0.000954588
    df["Mass"]=mass
   # planet_mass.append(solar)

for i in Radius:
    radius=(float(i))*0.102763
    #planet_radius.append(solar1)
    df["Madius"]=radius

#with open("want_to_merge.csv", "a+") as f: 
 #   csvwriter = csv.writer(f) 
  #  csvwriter.writerow(planet_mass) 
   # csvwriter.writerows(planet_radius)

df.to_csv("wanttomerge.csv")