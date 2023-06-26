import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

# Lendo base de dados das estatisticas jogadores e equipes da temporada 2022-2023


#times_url = "https://raw.githubusercontent.com/felipejf95/NBA/main/Outras%20bases/teste/Team%20Stats%202022-2023.csv"
#pts_url = "https://raw.githubusercontent.com/felipejf95/NBA/main/Outras%20bases/Players-stats-2022-2023.csv"
#ast_url = "https://raw.githubusercontent.com/felipejf95/NBA/main/Outras%20bases/Players-stats-2022-2023AST.csv"
#reb_url = "https://raw.githubusercontent.com/felipejf95/NBA/main/Outras%20bases/Players-stats-2022-2023REB.csv"


times = pd.read_csv(times_url, sep= ";")
jogadores_pts = pd.read_csv(pts_url, sep= ";")
jogadores_ast = pd.read_csv(ast_url, sep= ";")
jogadores_reb = pd.read_csv(reb_url, sep= ";")


# Filtrando os líderes de cada estatistica e seus times

lider_pts = jogadores_pts.head()
lider_ast = jogadores_ast.head()
lider_reb = jogadores_reb.head()

# Lideres de pontos, rebotes e assistencias

pontos_lider = lider_pts['PTS'].values[0]
assist_lider = lider_ast['AST'].values[0]
rebote_lider = lider_reb['REB'].values[1]

# Estatisticas dos times dos lideres

phi = times[times['TIME'] == 'Philadelphia 76ers']
sac = times[times['TIME'] == 'Sacramento Kings']

# Pontos, rebotes e assistencias dos times e proporção do jogador em relação ao time

pontos_phi = phi['PTS'].values[0]
assist_phi = phi['AST'].values[0]
reb_sac = sac['REB'].values[0]

porcentagem_pontos = (pontos_lider / pontos_phi) * 100
porcentagem_assits = (assist_lider / assist_phi) * 100
porcentagem_rebote = (rebote_lider / reb_sac) * 100

# Grafico de pontos

fig_pts, ax_pts = plt.subplots()

ax_pts.bar(['Joel Embiid', 'Philadelphia 76ers'], [pontos_lider, pontos_phi])
ax_pts.set_ylabel('Pontos')
ax_pts.set_title('Comparação de Pontos por Jogo\n'
                  f'Joel Embiid representa {porcentagem_pontos:.2f}% dos pontos do time')

ax_pts.text(0, pontos_lider, f'{porcentagem_pontos:.2f}%', ha='center', va='bottom')

# Grafico de Assistencias

fig_ast, ax_ast = plt.subplots()

ax_ast.bar(['James Harden', 'Philadelphia 76ers'], [assist_lider, assist_phi])
ax_ast.set_ylabel('Assistencias')
ax_ast.set_title('Comparação de Assistencias por jogo\n'
                  f'James Harden representa {porcentagem_assits:.2f}% das assistencias do time')
ax_ast.text(0, assist_lider, f'{porcentagem_assits:.2f}%', ha='center', va='bottom')

# Grafico de Rebotes

fig_reb, ax_reb = plt.subplots()

ax_reb.bar(['Domantas Sabonis', 'Sacramento Kings'], [rebote_lider, reb_sac])
ax_reb.set_ylabel('Rebotes')
ax_reb.set_title('Comparação de Rebotes por jogo\n'
                  f'Domantas Sabonis representa {porcentagem_rebote:.2f}% dos rebotes do time')
ax_reb.text(0, rebote_lider, f'{porcentagem_rebote:.2f}%', ha='center', va='bottom')


plt.show()













