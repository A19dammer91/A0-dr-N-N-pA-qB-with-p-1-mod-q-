# matryoshka.py — Layer 3: Complete Matryoshka calculator
# Author: Bilal el Issaoui, Amsterdam, 2026
# DOI: https://doi.org/10.5281/zenodo.20044995

def digit_sum(n):
    """Sum of all digits of N."""
    return sum(int(c) for c in str(n))

def digital_root(n):
    """Digital root of N."""
    while n >= 10:
        n = digit_sum(n)
    return n

def reduction_chain(n):
    """Complete reduction chain N → S(N) → ... → dr(N)."""
    chain = [n]
    current = n
    seen = {n}
    while current >= 10:
        nxt = digit_sum(current)
        if nxt not in seen:
            chain.append(nxt)
            seen.add(nxt)
        current = nxt
    return chain

def all_representations(n, p=19, q=9):
    """All non-negative representations (A, B) of N = pA + qB."""
    if n < 0:
        return []
    a0 = n % q
    result = []
    a = a0
    while a <= n // p:
        b = (n - p * a) // q
        if p * a + q * b == n and b >= 0:
            result.append((a, b))
        a += q
    return result

def link_chain_to_representations(n, p=19, q=9):
    """Link every value in the reduction chain to its A-coordinate."""
    chain = reduction_chain(n)
    reps = all_representations(n, p, q)
    a_values = {a for a, _ in reps}
    dr_n = digital_root(n)
    coupling = []
    for ci in chain:
        if ci in a_values:
            b = next(b for a, b in reps if a == ci)
            ver = p * ci + q * b
            coupling.append({
                'ci': ci, 'present': True, 'B': b,
                'verification': ver, 'correct': ver == n,
            })
        else:
            coupling.append({
                'ci': ci, 'present': False, 'B': None,
                'verification': None, 'correct': False,
            })
    symmetry_points = [
        (a, b) for a, b in reps
        if digital_root(a) == dr_n and digital_root(b) == dr_n
    ]
    a0 = n % q
    r_formula = (n // p - a0) // q + 1 if a0 <= n // p else 0
    return {
        'N': n, 'p': p, 'q': q, 'dr_N': dr_n, 'A0': a0,
        'chain': chain,
        'chain_str': ' -> '.join(str(c) for c in chain),
        'R': len(reps), 'R_formula': r_formula,
        'representations': reps, 'coupling': coupling,
        'symmetry_points': symmetry_points,
    }

# Verification
result = link_chain_to_representations(958)
assert result['dr_N'] == 4
assert result['A0'] == 4
assert result['R'] == 6
assert result['symmetry_points'] == [(40, 22)]