### 6- les attaques basées sur des erreurs de calcul (Fault Attacks).

import sympy
from sympy import gcd

# Génération d'une clé RSA
def generate_rsa_key_fault_attack():
    """
    Génère une clé RSA pour simuler une attaque par injection de faute.
    """
    p = sympy.randprime(10000, 50000)
    q = sympy.randprime(10000, 50000)
    n = p * q
    e = 65537
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    return {"p": p, "q": q, "n": n, "e": e, "d": d}

# Fonction pour simuler une faute
def inject_fault_during_decryption(c, d, n):
    """
    Simule une erreur dans le calcul de M = C^d mod n.
    Ici, une petite erreur est injectée dans d.
    """
    faulty_d = d + 1  # Modifier légèrement l'exposant privé
    return pow(c, faulty_d, n)

# Simulation de l'attaque
def simulate_fault_attack():
    """
    Simule une attaque par injection de faute dans RSA.
    """
    print("=== Simulation de la faiblesse : attaques par injection de fautes ===\n")
    
    # Étape 1 : Générer une clé RSA
    rsa_key = generate_rsa_key_fault_attack()
    n, e, d = rsa_key["n"], rsa_key["e"], rsa_key["d"]
    p, q = rsa_key["p"], rsa_key["q"]
    print(f"Clé publique générée :\n - n = {n}\n - e = {e}\n")
    print(f"Clé privée : d = {d}\n")
    
    # Étape 2 : Chiffrer un message
    message = 1234  # Message clair
    c = pow(message, e, n)  # Cryptogramme
    print(f"Message clair : {message}")
    print(f"Message chiffré : {c}\n")
    
    # Étape 3 : Déchiffrement normal et avec faute
    m_correct = pow(c, d, n)  # Déchiffrement correct
    m_faulty = inject_fault_during_decryption(c, d, n)  # Déchiffrement avec faute
    
    print(f"Message déchiffré (correct) : {m_correct}")
    print(f"Message déchiffré (avec faute) : {m_faulty}\n")
    
    # Étape 4 : Exploiter la faute pour récupérer un facteur de n
    diff = abs(m_correct - m_faulty)
    factor = gcd(diff, n)  # Calcul du PGCD pour trouver un facteur de n
    if factor > 1:
        print(f"Facteur trouvé : {factor}")
        print(f"L'autre facteur est : {n // factor}")
    else:
        print("Aucun facteur récupéré, l'attaque a échoué.")

# Exécution de la simulation
simulate_fault_attack()
