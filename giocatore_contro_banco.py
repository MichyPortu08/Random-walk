import matplotlib.pyplot as plt
import numpy as np

RA, RB = 10, 1000
n_simulazioni = 100
esiti = []

for i in range(n_simulazioni):
    guadagno = 0
    while -RA < guadagno < RB:
        passo = np.random.choice([1, -1])
        guadagno += passo

    esiti.append(1 if guadagno == RB else -1)

plt.scatter(range(1, n_simulazioni + 1), esiti, marker='x', color=['green' if e == 1 else 'red' for e in esiti])
plt.axhline(0, color='black', linewidth=0.8)
plt.yticks([-1, 1], ['Banco vince (-1)', 'A vince (+1)'])
plt.xlabel('Numero Partita')
plt.ylabel('Esito Finale')
plt.title(f'Esiti finali: RA={RA}, RB={RB}')
plt.savefig('fig/esiti_vittoria_rovina.png')