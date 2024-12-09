###  1- Faiblesse due à une clé de taille insuffisante


import sympy
import time

def generate_small_rsa_key():
    """Generate a small RSA key pair with vulnerable small n."""
    start_time = time.time()
    
    # Step 1: Generate two small prime numbers
    p = sympy.randprime(1000, 5000)  # Random prime between 4 digits
    q = sympy.randprime(1000, 5000)
    n = p * q  # RSA modulus
    phi = (p - 1) * (q - 1)  # Euler's totient function
    
    # Step 2: Choose a public exponent e
    e = 65537  # Common choice for RSA
    d = pow(e, -1, phi)  # Compute private key exponent
    
    elapsed_time = time.time() - start_time
    return {"p": p, "q": q, "n": n, "e": e, "d": d, "time": elapsed_time}

def factorize_small_n(n):
    """Factorize n to demonstrate the vulnerability."""
    start_time = time.time()
    factors = sympy.factorint(n)  # Factorize n
    elapsed_time = time.time() - start_time
    return factors, elapsed_time

# Main simulation
def simulate_small_key_vulnerability():
    print("=== Simulation de la faiblesse : Taille de clé insuffisante ===\n")
    
    # Generate a small RSA key
    key_data = generate_small_rsa_key()
    print("Clés RSA générées :")
    print(f"p = {key_data['p']}")
    print(f"q = {key_data['q']}")
    print(f"n = {key_data['n']}")
    print(f"e = {key_data['e']}")
    print(f"d = {key_data['d']}")
    print(f"Temps de génération : {key_data['time']:.6f} secondes\n")
    
    # Factorize n to simulate an attack
    print("Tentative de factorisation de n...")
    factors, elapsed_time = factorize_small_n(key_data["n"])
    print(f"n = {key_data['n']}")
    print("Facteurs trouvés :")
    for factor, multiplicity in factors.items():
        print(f"{factor}^{multiplicity}", end=" ")
    print(f"\nTemps de factorisation : {elapsed_time:.6f} secondes")

# Run the simulation
simulate_small_key_vulnerability()