# A₀ = dr(N) — A Complete Theory for N = pA + qB with p ≡ 1 (mod q)

**Author:** Bilal el Issaoui · Amsterdam · 2026


Central Result

For any system **N = pA + qB** with **p ≡ 1 (mod q)**, the minimal A-coefficient always equals the digital root of N:


A₀ = N mod q = dr(N)
...

B vanishes completely modulo q — A₀ is determinable in one step. No search required.

The exact representation count follows directly:

```
R(N) = floor((floor(N/p) - A₀) / q) + 1
```

---

## Matryoshka Structure

Every value in the reduction chain N → S(N) → ... → dr(N) appears as an A-coordinate in the representations of N — without exception.

Example for N = 958 (dr = 4):

```
Chain:         958 → 22 → 4
A-coordinates: ..., 4, ..., 22, ..., 40, ...
                    ↑        ↑
                  dr(N)    S(N)
```

---

## Extension to Higher Dimensions

**3D:** N = pA + qB + rC with r | q — exact O(1) formula for R₃(N):

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

**4D:** N = pA + qB + rC + sD with s | r | q — exact R₄(N) via kernel summation in O(N/s), verified against brute force across 8 systems. Full O(1) closure for R₄ remains an open problem — see `sigma4_analysis.py`.

---

## Files

| File | Description |
|------|-------------|
| `core.py` | General pA + qB for any p ≡ 1 (mod q) |
| `system_19_9.py` | The 19-9 system with digital root, symmetry points, G(k) boundary |
| `matryoshka.py` | Full Matryoshka calculator — reduction chain linked to A-coordinates |
| `sigma4_analysis.py` | 4D extension, exact R₄ kernel, block structure, complexity analysis |

---

## Quick Start

```python
from system_19_9 import all_representations, digital_root

N = 958
reps = all_representations(N)
print(f"dr({N}) = {digital_root(N)}")  # 4
print(f"A₀     = {reps[0][0]}")        # 4 — always equal to dr(N)
print(f"R({N}) = {len(reps)}")         # 6
```

```python
from matryoshka import link_chain_to_representations

result = link_chain_to_representations(958)
print(result['chain_str'])  # 958 -> 22 -> 4
# Every value in the chain appears as an A-coordinate — verified.
```

---

## Publication

**"Minimal Coefficients Equal Digital Roots: A Complete Theory for N = pA + qB with p ≡ 1 (mod q)"**
Zenodo · [https://doi.org/10.5281/zenodo.19474707](https://doi.org/10.5281/zenodo.19474707)
