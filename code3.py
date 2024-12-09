### 3- exposant public faible (𝑒=3)

import sympy

# Fonction pour simuler la faiblesse d'un petit e
def small_e_attack(n, e, c):
    """
    Attaque sur un petit e (e.g., e = 3) lorsque M^e < n.
    - n : Modulus RSA.
    - e : Exposant public.
    - c : Message chiffré.
    Retourne le message original si possible.
    """
    # Calcul de la racine e-ième entière de c
    m = sympy.root(c, e)
    if m.is_integer:
        return int(m)
    else:
        return None

# Simulation de la faiblesse
def simulate_small_e_vulnerability():
    """
    Simule la faiblesse lorsque e = 3 et M^e < n.
    """
    print("=== Simulation de la faiblesse : exposant public faible (e = 3) ===\n")
    
    # Étape 1 : Définir des valeurs pour n, e, et un petit message M
    p = sympy.randprime(1000, 5000)  # Premier nombre
    q = sympy.randprime(1000, 5000)  # Deuxième nombre
    n = p * q  # Modulus RSA
    e = 3  # Petit exposant public
    m = 42  # Message clair petit (M^e < n)
    
    # Étape 2 : Chiffrement du message
    c = pow(m, e, n)  # Chiffrement RSA
    print(f"Message clair : {m}")
    print(f"Message chiffré : {c}\n")
    
    # Étape 3 : Attaque pour récupérer le message original
    print("Tentative de récupération du message original à partir du cryptogramme...")
    recovered_m = small_e_attack(n, e, c)
    if recovered_m is not None:
        print(f"Message récupéré avec succès : {recovered_m}")
    else:
        print("Échec de la récupération du message.")

# Exécution de la simulation
simulate_small_e_vulnerability()
