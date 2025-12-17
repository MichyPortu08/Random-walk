import matplotlib.pyplot as plt
import numpy as np

# Parametri del problema
n_giorni = 360
n_simulazioni = 100
prezzo_iniziale = 23300
variazione = 0.02
limite_k = 30  # Il giorno 2k richiesto

# Inizializzazione variabili per il conteggio
count_mai_tornate = 0
plt.figure(figsize=(12, 7))

for i in range(n_simulazioni):
    # Generazione dei passi della marcia a caso (+1 aumento, -1 diminuzione)
    passi = np.random.choice([1, -1], size=n_giorni)
    
    # Calcolo della posizione relativa (guadagno cumulativo) per trovare i ritorni a zero
    # Questo serve per identificare l'ultimo istante in cui il prezzo era uguale a quello iniziale
    guadagno_relativo = np.cumsum(np.insert(passi, 0, 0))
    
    # Identificazione dell'ultimo ritorno all'origine (valore iniziale)
    ritorni_zero = np.where(guadagno_relativo == 0)[0]
    ultimo_ritorno = ritorni_zero[-1] if len(ritorni_zero) > 0 else 0
    
    # Calcolo dell'andamento reale del prezzo (variazione del 2% composta)
    prezzi = [prezzo_iniziale]
    for p in passi:
        if p == 1:
            nuovo_prezzo = prezzi[-1] * (1 + variazione)
        else:
            nuovo_prezzo = prezzi[-1] * (1 - variazione)
        prezzi.append(nuovo_prezzo)
    
    # Verifica condizione Arcoseno: l'ultimo ritorno avviene entro i primi 30 giorni
    # Se l'ultimo ritorno è <= 30, significa che nei restanti 330 giorni non torna mai al valore iniziale
    soddisfa_condizione = ultimo_ritorno <= limite_k
    
    if soddisfa_condizione:
        count_mai_tornate += 1
        colore = 'blue'  # Blu per chi non torna più al valore iniziale dopo il giorno 30
        alpha = 0.6
        linewidth = 1.2
    else:
        colore = 'gray'  # Grigio per chi attraversa ancora il valore iniziale dopo il giorno 30
        alpha = 0.2
        linewidth = 0.7
    
    plt.plot(range(n_giorni + 1), prezzi, color=colore, alpha=alpha, linewidth=linewidth)

# Calcolo Probabilità Teorica (Legge dell'Arcoseno)
# Formula: (2/pi) * arcsin(sqrt(k/n)) dove 2n=360 e 2k=30
p_teorica = (2 / np.pi) * np.arcsin(np.sqrt(15 / 180))

# Aggiunta elementi grafici
plt.axhline(prezzo_iniziale, color='black', linestyle='--', linewidth=1.5, label='Prezzo Iniziale (23.300€)')
plt.axvline(limite_k, color='red', linestyle='-', linewidth=2, label=f'Limite 30 Giorni (x=30)')

# Formattazione Grafico
plt.title(f'Simulazione 100 Azioni Apple (360gg)\n'
          f'andamento che riprende valore iniziale entro 30 giorni: {count_mai_tornate/n_simulazioni:.2%} | '
          f'Teoria: {p_teorica:.2%}')
plt.xlabel('Giorni')
plt.ylabel('Valore Azioni (€)')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.savefig('fig/simulazioni_apple_360_giorni.png')
plt.show()

# Stampa dei risultati testuali
print(f"Risultati su {n_simulazioni} simulazioni:")
print(f"Numero di azioni che non tornano al valore iniziale dopo il giorno 30: {count_mai_tornate}")
print(f"Probabilità misurata: {count_mai_tornate/n_simulazioni:.4f}")
print(f"Probabilità teorica (Arcoseno): {p_teorica:.4f}")