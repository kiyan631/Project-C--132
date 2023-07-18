import pandas as pd
import matplotlib.pyplot as mp


df = pd.read_csv('final.csv')

mass = df['Mass'].to_list()
radius = df['Radius'].to_list()
distance = df['Distance'].to_list()
gravity = df['Gravity'].to_list()


mass.sort()
radius.sort()
distance.sort()
gravity.sort()

mp.plot(radius , mass)  
mp.title("Radius VS Mass")
mp.xlabel("Radius")
mp.ylabel("Mass")
mp.show()

mp.plot(mass , gravity)
mp.title("Mass VS Gravity")
mp.xlabel("Mass")
mp.ylabel("Grvaity")
mp.show()

mp.scatter(radius , mass)
mp.xlabel("Radius")
mp.ylabel("Mass")
mp.show()





