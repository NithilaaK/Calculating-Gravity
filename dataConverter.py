import csv
import pandas as pd

rows = []

with open("starChart.csv",'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        rows.append(row)

headers = rows[0]
star_data = rows[1:]

df = pd.read_csv("starChart.csv")
star_masses = df["Mass"].tolist()
star_radiuses = df["Radius"].tolist()

si_star_masses = []
for mass in star_masses:
    si_m = float(mass)*1.989e+30
    si_star_masses.append(si_m)

si_star_radiuses = []
for radius in star_radiuses:
    si_r = float(radius)* 6.957e+8
    si_star_radiuses.append(si_r)

masses = si_star_masses
radiuses = si_star_radiuses
star_names = df["Name"].tolist()

star_gravities = []
for index,data in enumerate(star_names):
  gravity = (6.674e-11*float(masses[index]))/(float(radiuses[index])*float(radiuses[index]))
  star_gravities.append(gravity)

print(masses[0]) 
print(radiuses[0])
print(star_gravities[0])

df = df.assign(Gravity=star_gravities)
df.to_csv("starsChart.csv", index=False)