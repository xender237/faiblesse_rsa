### 5- l'utilisation de padding insuffisant ou absent lors du chiffrement.

import sympy

# Génération d'une clé RSA simple sans padding
def generate_rsa_key_no_padding():
    """
    Génère une paire de clés RSA sans padding.
    """
    p = sympy.randprime(1000, 5000)
    q = sympy.randprime(1000, 5000)
    n = p * q
    e = 65537  # Exposant public
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)  # Exposant privé
    return {"p": p, "q": q, "n": n, "e": e, "d": d}

# Simulation du chiffrement sans padding
def simulate_no_padding_vulnerability():
    """
    Simule la faiblesse due à l'absence de padding dans le chiffrement RSA.
    """
    print("=== Simulation de la faiblesse : absence de padding ===\n")
    
    # Étape 1 : Générer une clé RSA
    rsa_key = generate_rsa_key_no_padding()
    n, e = rsa_key["n"], rsa_key["e"]
    print(f"Clé publique générée :\n - n = {n}\n - e = {e}\n")
    
    # Étape 2 : Chiffrement de deux messages identiques
    message1 = 42  # Message clair
    message2 = 42  # Même message clair
    c1 = pow(message1, e, n)  # Chiffrement du message 1
    c2 = pow(message2, e, n)  # Chiffrement du message 2
    
    print(f"Message 1 chiffré : {c1}")
    print(f"Message 2 chiffré : {c2}\n")
    
    # Étape 3 : Vérification de l'égalité des cryptogrammes
    if c1 == c2:
        print("Les deux messages produisent le même cryptogramme !")
        print("Cela montre que l'absence de padding rend le chiffrement déterministe et vulnérable.")
    else:
        print("Les cryptogrammes sont différents (ce qui est inattendu).")

# Exécution de la simulation
simulate_no_padding_vulnerability()
