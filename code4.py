### 4- l'utilisation du même module n pour plusieurs utilisateurs

import sympy
from sympy import gcdex

def common_modulus_attack(n, e1, e2, c1, c2):
    """
    Implémente l'attaque au module commun.
    - n : Modulus RSA partagé.
    - e1, e2 : Exposants publics différents.
    - c1, c2 : Cryptogrammes.
    Retourne le message clair M.
    """
    # Calcul des coefficients a, b et du gcd tel que a*e1 + b*e2 = gcd(e1, e2)
    a, b, gcd = gcdex(e1, e2)
    if gcd != 1:
        raise ValueError("e1 et e2 doivent être premiers entre eux.")
    
    # Calcul du message clair M
    m1 = pow(c1, a, n)  # Calcul de c1^a mod n
    m2 = pow(c2, b, n)  # Calcul de c2^b mod n
    return (m1 * m2) % n

# Simulation de l'attaque
def simulate_common_modulus_vulnerability():
    """
    Simule l'attaque au module commun avec deux exposants publics.
    """
    print("=== Simulation de la faiblesse : module commun partagé ===\n")
    
    # Étape 1 : Générer un même module RSA
    p = sympy.randprime(10000, 50000)  # Premier
    q = sympy.randprime(10000, 50000)  # Deuxième
    n = p * q  # Module RSA
    
    # Étape 2 : Définir deux exposants publics coprimes
    e1 = 7
    e2 = 11  # Exposants publics relativement petits
    
    # Étape 3 : Chiffrer le même message clair M
    m = 1234  # Message clair commun
    c1 = pow(m, e1, n)  # Cryptogramme 1
    c2 = pow(m, e2, n)  # Cryptogramme 2
    print(f"Message clair : {m}")
    print(f"Cryptogramme 1 : {c1} (e1 = {e1})")
    print(f"Cryptogramme 2 : {c2} (e2 = {e2})\n")
    
    # Étape 4 : Exécuter l'attaque
    print("Tentative de récupération du message clair...")
    recovered_m = common_modulus_attack(n, e1, e2, c1, c2)
    if recovered_m == m:
        print(f"Message récupéré avec succès : {recovered_m}")
    else:
        print("Échec de la récupération du message clair.")

# Exécution de la simulation
simulate_common_modulus_vulnerability()
