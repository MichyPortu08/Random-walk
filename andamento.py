import matplotlib.pyplot as plt
import numpy as np

n = 50

# Generazione dei passi casuali: +1 (testa) o -1 (croce)
passi = np.random.choice([1, -1], size=n)

guadagno = np.cumsum(np.insert(passi, 0, 0))

plt.plot(range(n + 1), guadagno, marker='o', markersize=4, linestyle='-', color='red')
plt.axhline(10, color='blue', linestyle='--', linewidth=1, label='G = 10') 
plt.legend()
plt.xlabel('Iterazione (x)')
plt.ylabel('Guadagno (y)')
plt.title('Simulazione Random Walk (n=50)')
plt.grid(True)

# Salva il risultato
plt.savefig('fig/random_walk_simulazione.png')