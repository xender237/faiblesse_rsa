### 2- Attaque par factorisation avec ∣𝑝−𝑞∣ petit

import sympy
import math

def generate_close_primes_key():
    """Generate an RSA key with p and q very close."""
    p = sympy.randprime(10**5, 10**5 + 500)  # Prime in a narrow range
    q = sympy.randprime(10**5, 10**5 + 500)  # Close to p
    while p == q:  # Ensure p and q are distinct
        q = sympy.randprime(10**5, 10**5 + 500)
    n = p * q
    return {"p": p, "q": q, "n": n}

def fermat_factorization(n):
    """Use Fermat's method to factorize n."""
    x = math.isqrt(n) + 1  # Start just above sqrt(n)
    y2 = x**2 - n
    while not sympy.is_square(y2):  # Check if y2 is a perfect square
        x += 1
        y2 = x**2 - n
    y = int(math.sqrt(y2))
    p = x + y
    q = x - y
    return p, q

# Simulation of the vulnerability
def simulate_close_primes_vulnerability():
    print("=== Simulation de la faiblesse : |p - q| petit ===\n")
    
    # Step 1: Generate RSA key with close primes
    key_data = generate_close_primes_key()
    p, q, n = key_data["p"], key_data["q"], key_data["n"]
    print(f"Clés générées avec des premiers proches :")
    print(f"p = {p}")
    print(f"q = {q}")
    print(f"n = {n}\n")
    
    # Step 2: Factorize n using Fermat's method
    print("Tentative de factorisation de n avec l'algorithme de Fermat...")
    start_time = time.time()
    recovered_p, recovered_q = fermat_factorization(n)
    elapsed_time = time.time() - start_time
    print(f"Facteurs trouvés : p = {recovered_p}, q = {recovered_q}")
    print(f"Temps de factorisation : {elapsed_time:.6f} secondes")

# Run the simulation
simulate_close_primes_vulnerability()
