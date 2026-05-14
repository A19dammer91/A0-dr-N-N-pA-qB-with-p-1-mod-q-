# core.py — Layer 1: General version (any pair with p ≡ 1 mod q)
# Author: Bilal el Issaoui, Amsterdam, 2026
# DOI: https://doi.org/10.5281/zenodo.20044995

def a0_general(n, p, q):
    """Minimal A-value: always equals the digital root of N."""
    assert p % q == 1
    return n % q

def r_general(n, p, q):
    """Number of representations of N in the system pA + qB."""
    a0 = n % q
    fm = n // p
    if a0 > fm:
        return 0
    return (fm - a0) // q + 1

def all_representations_general(n, p, q):
    """All non-negative representations (A, B) of N = pA + qB."""
    a0 = n % q
    result = []
    a = a0
    while a <= n // p:
        result.append((a, (n - p * a) // q))
        a += q
    return result