import matplotlib.pyplot as plt
import numpy as np

n = 100  
prezzo_iniziale = 23 

# Generazione dei cambiamenti giornalieri: +2% o -2%
cambiamenti = np.random.choice([0.02, -0.02], size=n)

# Calcolo dei prezzi cumulativi
prezzi = [prezzo_iniziale]
for cambio in cambiamenti:
    nuovo_prezzo = prezzi[-1] * (1 + cambio)
    prezzi.append(nuovo_prezzo)

ys = []
for i in range(10, n+1):
    ultimi_10 = cambiamenti[i-10:i]
    salite = sum(1 for c in ultimi_10 if c == 0.02)
    y = 1 if salite >= 5 else -1
    ys.append(y)

plt.subplot(2, 1, 1)
plt.plot(range(n+1), prezzi, marker='o', markersize=2)
plt.title('Prezzo dell\'azione nel tempo')
plt.xlabel('Giorno')
plt.ylabel('Prezzo')

plt.subplot(2, 1, 2)
plt.plot(range(10, n+1), ys, 'xr')
plt.title('Condizione soddisfatta (1) o no (-1) per ogni step')
plt.xlabel('Step (a partire dal giorno 10)')
plt.ylabel('y')
plt.yticks([-1, 1])

plt.tight_layout()
plt.savefig('fig/simulazioni_azioni_10_giorni.png')
plt.show()
