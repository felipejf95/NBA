import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

# Lendo base de dados das estatisticas jogadores e equipes da temporada 2022-2023


times_url = "https://raw.githubusercontent.com/felipejf95/NBA/main/dados/Team%20Stats%202022-2023.csv"
pts_url = "https://raw.githubusercontent.com/felipejf95/NBA/main/dados/Players-stats-2022-2023.csv"
ast_url = "https://raw.githubusercontent.com/felipejf95/NBA/main/dados/Players-stats-2022-2023AST.csv"
reb_url = "https://raw.githubusercontent.com/felipejf95/NBA/main/dados/Players-stats-2022-2023REB.csv"
sixer_url = "https://raw.githubusercontent.com/felipejf95/NBA/main/dados/Team-stats-2.csv"

times = pd.read_csv(times_url, sep= ";")
jogadores_pts = pd.read_csv(pts_url, sep= ";")
jogadores_ast = pd.read_csv(ast_url, sep= ";")
jogadores_reb = pd.read_csv(reb_url, sep= ";")
sixers = pd.read_csv(sixer_url)


# Filtrando os líderes de cada estatistica

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

# Estatisticas 76ers sem um dos jogadores

no_harden = sixers[sixers['-'] == 'No Harden']
noharden_w = no_harden['VIT'].values[0]
noharden_d = no_harden['DER'].values[0]

no_embiid = sixers[sixers['-'] == 'No Embiid']
noembiid_w = no_embiid['VIT'].values[0]
noembiid_d = no_embiid['DER'].values[0]


harden_noembiid = sixers[sixers['-'] == 'Harden no Embiid']
harden_noembiid_w = harden_noembiid['VIT'].values[0]
harden_noembiid_d = harden_noembiid['DER'].values[0]

embiid_noharden = sixers[sixers['-'] == 'Embiid no Harden']
embiid_noharden_w = embiid_noharden['VIT'].values[0]
embiid_noharden_d = embiid_noharden['DER'].values[0]


# Estatisticas Kings sem Sabonis

no_sabonis = sixers[sixers['-'] == 'No Sabonis']
with_sabonis = sixers[sixers['-'] == 'Sabonis']

no_sabonis_w = no_sabonis['VIT'].values[0]
no_sabonis_d = no_sabonis['DER'].values[0]

with_sabonis_w = with_sabonis['VIT'].values[0]
with_sabonis_d = with_sabonis['DER'].values[0]


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
ax_pts.set_ylabel('Pontos por jogo')
ax_pts.set_title('Comparação de Pontos por Jogo\n'
                  f'Joel Embiid representa {porcentagem_pontos:.2f}% dos pontos do time')

ax_pts.text(0, pontos_lider, f'{porcentagem_pontos:.2f}%', ha='center', va='bottom')

# Grafico de Assistencias

fig_ast, ax_ast = plt.subplots()

ax_ast.bar(['James Harden', 'Philadelphia 76ers'], [assist_lider, assist_phi])
ax_ast.set_ylabel('Assistencias por jogo')
ax_ast.set_title('Comparação de Assistencias por jogo\n'
                  f'James Harden representa {porcentagem_assits:.2f}% das assistencias do time')
ax_ast.text(0, assist_lider, f'{porcentagem_assits:.2f}%', ha='center', va='bottom')

# Grafico de Rebotes

fig_reb, ax_reb = plt.subplots()

ax_reb.bar(['Domantas Sabonis', 'Sacramento Kings'], [rebote_lider, reb_sac])
ax_reb.set_ylabel('Rebotes por jogo')
ax_reb.set_title('Comparação de Rebotes por jogo\n'
                  f'Domantas Sabonis representa {porcentagem_rebote:.2f}% dos rebotes do time')
ax_reb.text(0, rebote_lider, f'{porcentagem_rebote:.2f}%', ha='center', va='bottom')

# Grafico sem um dos jogadores

barras = ['Sem Harden', '',  'Sem Embiid', '', 'Harden sem Embiid', '', '', 'Embiid sem Harden']

altura_w = [noharden_w, 0, noembiid_w, 0, harden_noembiid_w, 0, 0, embiid_noharden_w]
altura_d = [noharden_d, 0, noembiid_d, 0, harden_noembiid_d, 0, 0, embiid_noharden_d]

largura_barra = 0.35

posicao_barra = range(len(barras))

# Plotagem

fig_six, ax_six = plt.subplots()
barras1 = ax_six.bar(posicao_barra, altura_w, largura_barra, label = 'Vitorias')
barras2 = ax_six.bar([p + largura_barra for p in posicao_barra], altura_d, largura_barra, label = 'Derrotas')
ax_six.set_ylabel('Record')
ax_six.set_title('Equipe sem um dos jogadores')
ax_six.set_xticks([p + largura_barra / 2 for p in posicao_barra])
ax_six.set_xticklabels(barras)
ax_six.legend()

# Adicionar Valor acima das barras

def adicionar_valores_barras(barras, alturas):
    for barra, altura in zip(barras, alturas):
        if altura:  # Verificar se a altura não é vazia ou nula
            ax_six.annotate('{}'.format(altura),
                        xy=(barra.get_x() + barra.get_width() / 2, altura),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom')

adicionar_valores_barras(barras1, altura_w)
adicionar_valores_barras(barras2, altura_d)

## ax_six.text


# Exportando os gráficos

# fig_pts.savefig('grafico_pts.png', dpi = 300)
# fig_ast.savefig('grafico_ast.png', dpi = 300)
# fig_reb.savefig('grafico_reb,png', dpi = 300)

# fig_six.savefig('grafico_six.png', dpi = 300) 


plt.show()













