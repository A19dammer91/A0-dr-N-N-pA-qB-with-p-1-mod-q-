# system_19_9.py — Layer 2: Specific to the 19-9 system
# Author: Bilal el Issaoui, Amsterdam, 2026
# DOI: https://doi.org/10.5281/zenodo.20044995

def digital_root(n):
    """Digital root of N."""
    if n == 0:
        return 0
    return 1 + (n - 1) % 9

def r(n, p=19, q=9):
    """Number of representations of N in the 19-9 system."""
    a0 = n % q
    fm = n // p
    if a0 > fm:
        return 0
    return (fm - a0) // q + 1

def all_representations(n, p=19, q=9):
    """All non-negative representations (A, B) of N = 19A + 9B."""
    a0 = n % q
    result = []
    a = a0
    while a <= n // p:
        result.append((a, (n - p * a) // q))
        a += q
    return result

def symmetry_point(n, p=19, q=9):
    """Find the symmetry point where dr(A) = dr(B) = dr(N)."""
    r_val = digital_root(n)
    for a, b in all_representations(n, p, q):
        if digital_root(a) == r_val and digital_root(b) == r_val:
            return (a, b)
    return None

def g(k, p=19, q=9):
    """Family boundary: every N >= G(k) has at least k representations."""
    return p * q * (k - 1) + (p - 1) * (q - 1)

# Verification
assert r(958) == 6
assert r(6666) == 39
assert symmetry_point(958) == (40, 22)
assert symmetry_point(6666) == (24, 690)
assert g(10) == 1683