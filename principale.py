import sympy
import math
from sympy import gcd, gcdex

# === Faiblesse 1 : Utilisation d'exposants faibles ===
def low_exponent_attack(c, e, n):
    """
    Décrypte un message chiffré avec un petit exposant public (e.g., e = 3).
    Retourne le message clair si c'est possible.
    """
    m = int(sympy.root(c, e))  # Racine e-ième de c
    if pow(m, e, n) == c:
        return m
    else:
        return None

def simulate_low_exponent_vulnerability():
    n = 33_733_333  # Un module arbitraire
    e = 3  # Petit exposant public
    m = 42  # Message clair
    c = pow(m, e, n)  # Chiffrement
    decrypted_message = low_exponent_attack(c, e, n)
    return m, c, decrypted_message

# === Faiblesse 2 : Messages courts ===
def simulate_short_message_vulnerability():
    n = 101 * 103  # Petit module RSA
    e = 65537
    m = 2  # Très petit message
    c = pow(m, e, n)
    return m, c

# === Faiblesse 3 : Module commun ===
def common_modulus_attack(n, e1, e2, c1, c2):
    a, b, _ = gcdex(e1, e2)
    m1 = pow(c1, a, n)
    m2 = pow(c2, b, n)
    return (m1 * m2) % n

def simulate_common_modulus_vulnerability():
    p = sympy.randprime(1000, 5000)
    q = sympy.randprime(1000, 5000)
    n = p * q
    e1, e2 = 7, 11
    m = 42
    c1, c2 = pow(m, e1, n), pow(m, e2, n)
    recovered_m = common_modulus_attack(n, e1, e2, c1, c2)
    return m, c1, c2, recovered_m

# === Faiblesse 4 : Absence de padding ===
def simulate_no_padding_vulnerability():
    p, q = sympy.randprime(1000, 5000), sympy.randprime(1000, 5000)
    n, e = p * q, 65537
    m = 42
    c1 = pow(m, e, n)
    c2 = pow(m, e, n)
    return m, c1, c2

# === Faiblesse 5 : Injection de fautes ===
def inject_fault_during_decryption(c, d, n):
    faulty_d = d + 1
    return pow(c, faulty_d, n)

def simulate_fault_attack():
    p, q = sympy.randprime(1000, 5000), sympy.randprime(1000, 5000)
    n, e, phi = p * q, 65537, (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    m = 1234
    c = pow(m, e, n)
    m_correct = pow(c, d, n)
    m_faulty = inject_fault_during_decryption(c, d, n)
    factor = gcd(abs(m_correct - m_faulty), n)
    return m, c, m_correct, m_faulty, factor

# === Faiblesse 6 : Nombres premiers proches ===
def fermat_factorization(n):
    a = math.isqrt(n) + 1
    b2 = a * a - n
    while not math.isqrt(b2) ** 2 == b2:
        a += 1
        b2 = a * a - n
    b = math.isqrt(b2)
    return a - b, a + b

def simulate_close_primes_vulnerability():
    p = sympy.nextprime(1000000)
    q = sympy.nextprime(p + 10)
    n = p * q
    recovered_p, recovered_q = fermat_factorization(n)
    return p, q, n, recovered_p, recovered_q

# === Menu Principal ===
def main_menu():
    print("\n=== Programme de Simulation des Faiblesses RSA ===")
    print("1. Faiblesse 1 : Utilisation d'exposants faibles")
    print("2. Faiblesse 2 : Messages courts")
    print("3. Faiblesse 3 : Module commun")
    print("4. Faiblesse 4 : Absence de padding")
    print("5. Faiblesse 5 : Injection de fautes")
    print("6. Faiblesse 6 : Nombres premiers proches")
    print("7. Quitter")
    return input("Sélectionnez une option : ")

# === Lancement du Programme ===
def main():
    while True:
        choice = main_menu()
        if choice == "1":
            m, c, decrypted_message = simulate_low_exponent_vulnerability()
            print(f"Message clair : {m}\nCryptogramme : {c}\nMessage récupéré : {decrypted_message}")
        elif choice == "2":
            m, c = simulate_short_message_vulnerability()
            print(f"Message clair : {m}\nCryptogramme : {c}")
        elif choice == "3":
            m, c1, c2, recovered_m = simulate_common_modulus_vulnerability()
            print(f"Message clair : {m}\nCryptogramme 1 : {c1}\nCryptogramme 2 : {c2}\nMessage récupéré : {recovered_m}")
        elif choice == "4":
            m, c1, c2 = simulate_no_padding_vulnerability()
            print(f"Message clair : {m}\nCryptogramme 1 : {c1}\nCryptogramme 2 : {c2}")
        elif choice == "5":
            m, c, m_correct, m_faulty, factor = simulate_fault_attack()
            print(f"Message clair : {m}\nCryptogramme : {c}\nMessage déchiffré (correct) : {m_correct}\nMessage déchiffré (faute) : {m_faulty}\nFacteur trouvé : {factor}")
        elif choice == "6":
            p, q, n, recovered_p, recovered_q = simulate_close_primes_vulnerability()
            print(f"Module : {n}\nFacteurs originaux : p={p}, q={q}\nFacteurs récupérés : p={recovered_p}, q={recovered_q}")
        elif choice == "7":
            print("Au revoir !")
            break
        else:
            print("Option invalide, veuillez réessayer.")

# Démarrage du programme
if __name__ == "__main__":
    main()
