import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

jogadores_url = "https://raw.githubusercontent.com/felipejf95/NBA/main/players_stats_14-15.csv"

jogadores = pd.read_csv(jogadores_url)



# 5 primeiras linhas
#print(jogadores.head()) 
# dados do arquivo
#print(jogadores.info())

# Top 3 Lideres de Pontos, Rebotes e Assistencias

lider_pontos = jogadores.nlargest(3, 'PTS')
lider_assistencias = jogadores.nlargest(3, 'AST')
lider_rebotes = jogadores.nlargest(3, 'REB')
#print (lider_pontos[['Name', 'Games Played', 'PTS', 'AST', 'REB', 'FG%', 'Team', ]])
#print(lider_assistencias[['Name', 'Games Played', 'PTS', 'AST', 'REB', 'FG%', 'Team', ]])
#print(lider_rebotes[['Name', 'Games Played', 'PTS', 'AST', 'REB', 'FG%', 'Team', ]])

array = lider_pontos.head()
p1 = array.values[0]
p2 = array.values[1]
print (p1[3])
print (p2[3])



