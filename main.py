import pandas as pd
import numpy as np

dane = pd.read_excel("test1.xlsx")
za2015=dane[dane["Rok"]==2015]
PLza2015=za2015[za2015["Państwo"]=="PL"]