#coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import scipy.stats as stats
import os 

# Créer un dossier pour les graphiques s'il n'existe pas
output_dir = "graphiques_lois"
os.makedirs(output_dir, exist_ok=True)

# Dictionnaire pour stocker les distributions
distributions = {}

#Création des axes et graduations
XLIM = (-5, 10)
YLIM = (0, 1)
XTICKS = np.arange(-5, 11, 1)
YTICKS = np.arange(0, 1.1, 0.1)

# Fonctions de calcul
def moyenne_loi_discrete(valeurs, probabilites):
    return np.sum(valeurs * probabilites)

def ecart_type_loi_discrete(valeurs, probabilites):
    moyenne = moyenne_loi_discrete(valeurs, probabilites)
    variance = np.sum((valeurs - moyenne)**2 * probabilites)
    return np.sqrt(variance)

def moyenne_loi_continue(x, pdf):
    return np.trapezoid(x * pdf, x)

def ecart_type_loi_continue(x, pdf):
    moyenne = moyenne_loi_continue(x, pdf)
    variance = np.trapezoid((x - moyenne)**2 * pdf, x)
    return np.sqrt(variance)

# Fonction pour configurer les graphiques
def configure_et_sauvegarder(nom_fichier):
    plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)
    plt.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
    plt.xlim(XLIM)
    plt.ylim(YLIM)
    plt.xticks(XTICKS)
    plt.yticks(YTICKS)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f"{nom_fichier}.png"), dpi=300, bbox_inches='tight')

# Style par défaut pour les graphiques discrets
def style_stem_plot(markerline, stemlines, baseline, color='#5B7FA6'):
    plt.setp(stemlines, linewidth=3, color=color)
    plt.setp(markerline, markersize=10, color=color, markerfacecolor=color)
    plt.setp(baseline, linewidth=2.5, color=color)


# LOI DE DIRAC
point_concentration = 2
x = np.linspace(-4, 4, 1000)
plt.figure(figsize=(12, 7))
plt.plot(x, np.zeros_like(x), color='#5B7FA6', linewidth=2.5)
plt.plot([point_concentration, point_concentration], [0, 1], 
         color='#5B7FA6', linewidth=3, marker='o', markersize=8, 
         markerfacecolor='#5B7FA6')
configure_et_sauvegarder("loi_dirac")

#LOI UNIFORME DISCRÈTE
a, b = 1, 6
valeurs = np.arange(a, b + 1)
n = len(valeurs)
probabilites = np.ones(n) / n
distributions['uniforme_discrete'] = (valeurs.copy(), probabilites.copy())
plt.figure(figsize=(12, 7))
markerline, stemlines, baseline = plt.stem(valeurs, probabilites, 
                                            linefmt='#5B7FA6', 
                                            markerfmt='o', 
                                            basefmt='#5B7FA6')
style_stem_plot(markerline, stemlines, baseline)
configure_et_sauvegarder("loi_uniforme_discrete")

# LOI BINOMIALE 
n = 10
p = 0.5
valeurs = np.arange(0, n + 1)
probabilites = stats.binom.pmf(valeurs, n, p)
distributions['binomiale'] = (valeurs.copy(), probabilites.copy())
plt.figure(figsize=(12, 7))
markerline, stemlines, baseline = plt.stem(valeurs, probabilites, 
                                            linefmt='#5B7FA6', 
                                            markerfmt='o', 
                                            basefmt='#5B7FA6')
style_stem_plot(markerline, stemlines, baseline)
configure_et_sauvegarder("loi_binomiale")

# LOI DE POISSON 
lambda_param = 3
valeurs = np.arange(0, 15)
probabilites = stats.poisson.pmf(valeurs, lambda_param)
distributions['poisson'] = (valeurs.copy(), probabilites.copy())
plt.figure(figsize=(12, 7))
markerline, stemlines, baseline = plt.stem(valeurs, probabilites, 
                                            linefmt='#5B7FA6', 
                                            markerfmt='o', 
                                            basefmt='#5B7FA6')
style_stem_plot(markerline, stemlines, baseline)
configure_et_sauvegarder("loi_poisson")

# LOI DE ZIPF-MANDELBROT
a = 2.0
N = 20
valeurs = np.arange(1, N + 1)
probabilites = (1 / valeurs**a) / np.sum(1 / valeurs**a)
distributions['zipf'] = (valeurs.copy(), probabilites.copy())
plt.figure(figsize=(12, 7))
markerline, stemlines, baseline = plt.stem(valeurs, probabilites, 
                                            linefmt='#5B7FA6', 
                                            markerfmt='o', 
                                            basefmt='#5B7FA6')
style_stem_plot(markerline, stemlines, baseline)
configure_et_sauvegarder("loi_zipf_mandelbrot")

# LOI DE POISSON (CONTINUE) 
lambda_param = 3
x_continue = np.linspace(0, 15, 1000)
y_continue = stats.poisson.pmf(np.round(x_continue).astype(int), lambda_param)
distributions['poisson_continue'] = (x_continue.copy(), y_continue.copy())
plt.figure(figsize=(12, 7))
plt.plot(x_continue, y_continue, color='#5B7FA6', linewidth=2.5)
plt.fill_between(x_continue, y_continue, alpha=0.3, color='#5B7FA6')
configure_et_sauvegarder("loi_poisson_continue")

#LOI NORMALE
mu = 0
sigma = 1
x = np.linspace(-4, 4, 1000)
y = stats.norm.pdf(x, mu, sigma)
distributions['normale'] = (x.copy(), y.copy())
plt.figure(figsize=(12, 7))
plt.plot(x, y, color='#5B7FA6', linewidth=2.5)
plt.fill_between(x, y, alpha=0.3, color='#5B7FA6')
configure_et_sauvegarder("loi_normale")

# LA LOI LOG-NORMALE 
s = 0.5
scale = 1
x = np.linspace(0.01, 5, 1000)
y = stats.lognorm.pdf(x, s, scale=scale)
distributions['lognormale'] = (x.copy(), y.copy())
plt.figure(figsize=(12, 7))
plt.plot(x, y, color='#5B7FA6', linewidth=2.5)
plt.fill_between(x, y, alpha=0.3, color='#5B7FA6')
configure_et_sauvegarder("loi_lognormale")

#LA LOI UNIFORME 
a = 1
b = 5
x = np.linspace(0, 6, 1000)
y = stats.uniform.pdf(x, loc=a, scale=b-a)
distributions['uniforme_continue'] = (x.copy(), y.copy())
plt.figure(figsize=(12, 7))
plt.plot(x, y, color='#5B7FA6', linewidth=2.5)
plt.fill_between(x, y, alpha=0.3, color='#5B7FA6')
configure_et_sauvegarder("loi_uniforme_continue")

# LA LOI DU CHI-DEUX (χ²)
df = 5
x = np.linspace(0, 20, 1000)
y = stats.chi2.pdf(x, df)
distributions['chi2'] = (x.copy(), y.copy())
plt.figure(figsize=(12, 7))
plt.plot(x, y, color='#5B7FA6', linewidth=2.5)
plt.fill_between(x, y, alpha=0.3, color='#5B7FA6')
configure_et_sauvegarder("loi_chi_deux")

# LA LOI DE PARETO 
b = 2.5
scale = 1
x = np.linspace(1, 5, 1000)
y = stats.pareto.pdf(x, b, scale=scale)
distributions['pareto'] = (x.copy(), y.copy())
plt.figure(figsize=(12, 7))
plt.plot(x, y, color='#5B7FA6', linewidth=2.5)
plt.fill_between(x, y, alpha=0.3, color='#5B7FA6')
configure_et_sauvegarder("loi_pareto")

print(f"\nTous les graphiques ont été enregistrés dans le dossier '{output_dir}/'")


# CALCUL DES STATISTIQUES
print("STATISTIQUES DES DISTRIBUTIONS")

# Lois discrètes
for nom in ['uniforme_discrete', 'binomiale', 'poisson', 'zipf']:
    v, p = distributions[nom]
    print(f"\n{nom.upper()}: moyenne={moyenne_loi_discrete(v, p):.4f}, écart-type={ecart_type_loi_discrete(v, p):.4f}")

# Lois continues
for nom in ['poisson_continue', 'normale', 'lognormale', 'uniforme_continue', 'chi2', 'pareto']:
    x, y = distributions[nom]
    print(f"\n{nom.upper()}: moyenne={moyenne_loi_continue(x, y):.4f}, écart-type={ecart_type_loi_continue(x, y):.4f}")

print("\n" + "="*70)