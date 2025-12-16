import matplotlib.pyplot as plt
import numpy as np

n_steps = 50
n_iterations = 100

all_walks = np.zeros((n_steps + 1, n_iterations))

for i in range(n_iterations):
    passi_singoli = np.random.choice([1, -1], size=n_steps)
    all_walks[1:, i] = np.cumsum(passi_singoli)

guadagno_totale = np.sum(all_walks, axis=1)

plt.plot(range(n_steps + 1), guadagno_totale, marker='o', color='green', linewidth=1.5)
plt.axhline(0, color='black', linewidth=1, linestyle='--')
plt.xlabel('Step (n)')
plt.ylabel('Guadagno Totale per Step')
plt.title('Somma dei guadagni di 50 iterazioni per ogni step')
plt.grid(True, linestyle=':', alpha=0.7)

plt.savefig('fig/guadagno_totale_100_step.png')