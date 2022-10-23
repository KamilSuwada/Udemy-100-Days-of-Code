from hashlib import new
import os
import pandas as p


CWD = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(CWD, "squirrel_data.csv")
data = p.read_csv(path)



grays = data[data["Primary Fur Color"] == "Gray"]
cinnamons = data[data["Primary Fur Color"] == "Cinnamon"]
blacks = data[data["Primary Fur Color"] == "Black"]


d = {
    "colours" : ["gray", "cinnamon", "black"],
    "count" : [len(grays), len(cinnamons), len(blacks)]
}


newData = p.DataFrame(d)

print(newData)