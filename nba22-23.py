import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

# Lendo base de jogadores da temporada 2014-2015


jogadores_url = "https://raw.githubusercontent.com/felipejf95/NBA/main/Outras%20bases/teste/Team%20Stats%202022-2023.csv"

jogadores = pd.read_csv("./Outras bases/teste/2022-2023 NBA Player Stats - Regular.csv")