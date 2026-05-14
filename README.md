# A₀ = dr(N) — A Complete Theory for N = pA + qB with p ≡ 1 (mod q)

**Author:** Bilal el Issaoui · Amsterdam · 2026  

The Central Result

For any linear Diophantine system of the form **N = pA + qB** where **p ≡ 1 (mod q)**, the minimal non-negative A-coefficient — denoted A₀ — is always equal to the **digital root** of N:

A₀ = N mod q = dr(N)

This follows directly from the congruence p ≡ 1 (mod q): B vanishes completely modulo q, leaving A₀ determinable in a single step. No search required.

The number of representations is then exact:

R(N) = floor((floor(N/p) - A₀) / q) + 1


The Matryoshka Structure

Every value in the reduction chain N → S(N) → ... → dr(N) appears as an A-coordinate in the representations of N — without exception. The structure scales without loss: the innermost layer is always dr(N).

Example for N = 958:

Reduction chain:  958 → 22 → 4
A-coordinates:    ..., 4, ..., 22, ..., 40, ...
                       ↑        ↑
                     dr(N)    S(N)   both present as A-values

This is not coincidence. It is a direct consequence of the coupling structure.


Extension to Higher Dimensions

The theory extends naturally to three and four dimensions.

**3D:** N = pA + qB + rC with r | q

The A-C coupling A + rC ≡ N (mod q) collapses the 3D search space to a single dimension. This yields an **exact O(1) formula** for R₃(N):

```python
def r3_kernel(n, p, q, r):
    a0 = n % r;  m = n // p;  M = n - p * a0
    J = (m - a0) // r;  Mq = M % q;  period = q // r
    K = (J + 1) // period;  t = (J + 1) % period
    one_cycle = sum((Mq - r*j) % q for j in range(period))
    partial   = sum((Mq - r*j) % q for j in range(t))
    R_corr = K * one_cycle + partial
    return ((J+1)*M - p*r*J*(J+1)//2 - R_corr) // q + (J+1)
```

**4D:** N = pA + qB + rC + sD with s | r | q

R₄(N) is computed exactly via kernel summation in **O(N/s)**. The block structure of the correction term Σ₄ is fully characterized for s = r systems. Full O(1) closure for R₄ remains an **open problem** — see `sigma4_analysis.py`.



## Quick Start

```python
from system_19_9 import all_representations, digital_root

N = 958
reps = all_representations(N)
print(f"dr({N}) = {digital_root(N)}")   # 4
print(f"A₀     = {reps[0][0]}")         # 4  — always equal to dr(N)
print(f"R({N}) = {len(reps)}")          # 6
```

```python
from matryoshka import link_chain_to_representations

result = link_chain_to_representations(958)
print(result['chain_str'])   # 958 -> 22 -> 4
# Every value in the chain appears as an A-coordinate — verified.
```


**Proved and verified:**
- A₀ = dr(N) for all N in any system with p ≡ 1 (mod q)
- Exact closed-form R(N) for 2D
- Matryoshka theorem: full reduction chain embedded in A-coordinates
- Exact O(1) formula for R₃(N; p, q, r)
- Exact R₄(N) via kernel method: O(N/s), verified against brute force across 8 systems
- Block structure of Σ₄ for s = r systems: exact and verified


## Publication

Full theoretical treatment with proofs:  
**"Minimal Coefficients Equal Digital Roots: A Complete Theory for N = pA + qB with p ≡ 1 (mod q)"**  
Zenodo · [https://doi.org/10.5281/zenodo.19474707](https://doi.org/10.5281/zenodo.19474707)
