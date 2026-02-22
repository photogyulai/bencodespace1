import matplotlib.pyplot as plt
import numpy as np

# Adatok generálása
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Grafikon létrehozása
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Szinusz hullám', color='tab:blue', linewidth=2)

# Dekoráció
plt.title('Matplotlib teszt a GitHub Codespaces-ben')
plt.xlabel('X tengely (idő)')
plt.ylabel('Y tengely (amplitúdó)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# FONTOS: Felhőben nem tud felugrani ablak, ezért fájlba mentjük!
filename = "my_plot.png"
plt.savefig(filename)

print(f"Siker! A grafikon elmentve: {filename}")
