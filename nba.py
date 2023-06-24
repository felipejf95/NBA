import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

# Lendo base de jogadores da temporada 2014-2015

jogadores_url = "https://raw.githubusercontent.com/felipejf95/NBA/main/players_stats_14-15.csv"

jogadores = pd.read_csv(jogadores_url)

# Lendo base dos times desde 2000

times_url = "https://raw.githubusercontent.com/felipejf95/NBA/main/nba_team_stats_00_to_21.csv"

times = pd.read_csv(times_url)


# Filtrando o ano de interesse, 2014-2015

dados_2014 = times[times['SEASON'] == '2014-15']
d = dados_2014.head().values

# Escolhendo o time Houston Rockets

rck = dados_2014[dados_2014['TEAM'] == 'Houston Rockets']
#print(rck)


#print (dados_2014.head())



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

# Filtrando os times dos jogadores lideres de pontos
rck = dados_2014[dados_2014['TEAM'] == 'Houston Rockets']
ock = dados_2014[dados_2014['TEAM'] == 'Houston Oklahoma City Thunder']
gsw = dados_2014[dados_2014['TEAM'] == 'Golden State Warriors']

# Filtrando os times dos jogadores lideres de Assistencias
lac = dados_2014[dados_2014['TEAM'] == 'Los Angeles Clippers']
wiz = dados_2014[dados_2014['TEAM'] == 'Whasinton Wizards']
den = dados_2014[dados_2014['TEAM'] == 'Denver Nuggets']

# Filtrando os times dos jogadorres lideres de Rebotes

det = dados_2014[dados_2014['TEAM'] == 'Detroit Pistons']
bulls = dados_2014[dados_2014['TEAM'] == 'Chicago Bulls']



array = lider_pontos.head()
p1 = array.values[0]
p2 = array.values[1]
#print (p1[3])
#print (p2[3])



