import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

jogadores_url = "https://raw.githubusercontent.com/felipejf95/NBA/main/2021-2022%20NBA%20Player%20Stats%20-%20Regular.csv"

dados_jogadores = pd.read_csv(jogadores_url)
