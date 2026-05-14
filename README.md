# A₀ = dr(N) — Linear Diophantine Representation Systems

**Author:** Bilal el Issaoui · Amsterdam · 2026  

---

## Overview

This repository develops an exact theory for counting and characterizing solutions to
linear Diophantine equations of the form:

```
N = p·A + q·B        (2D)
N = p·A + q·B + r·C  (3D)
N = p·A + q·B + r·C + s·D  (4D)
```

with A, B, C, D ≥ 0 integers, under the structural condition **p ≡ 1 (mod q)**.

The theory proceeds in three steps: the 2D core theorem, its 3D extension, and the
4D representation count. Each step is formally stated, proven, and illustrated with
a concrete example.

---

## Part I — The 2D Core Theorem

### Setup

Fix p and q with **p ≡ 1 (mod q)**. For a given N, consider all solutions (A, B) ∈ ℕ²
to N = p·A + q·B. Among all valid A-values, define:

```
A₀ = the minimal non-negative A such that N = p·A + q·B has a solution with B ≥ 0
```

Define the **digital root** of N with respect to q as:

```
dr(N) = ((N − 1) mod q) + 1    for N > 0,  with dr(0) = 0
```

For q = 9 this coincides with the classical digital root (repeated digit sum until
one digit remains). For general q it is the unique value in {0, 1, ..., q−1} with
N ≡ dr(N) (mod q), adjusted to lie in {1, ..., q} for N > 0.

---

### Theorem 1 (Core Theorem) — A₀ = dr(N)

**Statement:** Let p, q be positive integers with p ≡ 1 (mod q). For any N ≥ 0,
the minimal A-coefficient in N = p·A + q·B (with A, B ≥ 0) equals the
generalized digital root of N modulo q:

```
A₀ = N mod q       (where we take the representative in {0, 1, ..., q−1})
```

More precisely: A₀ is the unique value in {0, 1, ..., q−1} with A₀ ≡ N (mod q),
provided N ≥ p·A₀ (otherwise no solution exists).

**Proof:**

For N = p·A + q·B to have a solution, we need q·B = N − p·A ≥ 0, so A ≤ N/p.
Also B = (N − p·A)/q must be a non-negative integer, so:

```
N − p·A ≡ 0 (mod q)
⟺  p·A ≡ N (mod q)
```

Since p ≡ 1 (mod q), we have p·A ≡ A (mod q). Therefore:

```
A ≡ N (mod q)
```

The smallest non-negative A satisfying this is A₀ = N mod q (in {0, ..., q−1}).
This A₀ is valid as long as N − p·A₀ ≥ 0, i.e., N ≥ p·A₀. □

---

### Example — Additive Structure: N = 100 + 300 = 400

System: p = 19, q = 9. Check: 19 ≡ 1 (mod 9). ✓

**A₀ is additive:**

```
A₀(100) = 100 mod 9 = 1
A₀(300) = 300 mod 9 = 3
A₀(400) = 400 mod 9 = 4

A₀(100) + A₀(300) = 1 + 3 = 4 = A₀(400)  ✓
```

**Solutions are additive:** every solution for N=100 combined with every solution
for N=300 produces a valid solution for N=400.

Solutions for N=100:
```
(A=1, B=9)   →  19×1 + 9×9  = 100
```

Solutions for N=300:
```
(A=3,  B=27)  →  19×3  + 9×27 = 300
(A=12, B=8)   →  19×12 + 9×8  = 300
```

Adding each pair:
```
(1,9) + (3,27)  = (4,36)   →  19×4  + 9×36 = 400  ✓
(1,9) + (12,8)  = (13,17)  →  19×13 + 9×17 = 400  ✓
```

Both results are exactly the complete solution set of N=400. The additive structure
is not coincidental — it follows directly from the linearity of the equation.

---

## Part II — The 3D Extension

### Setup

Now add a third variable: N = p·A + q·B + r·C, with A, B, C ≥ 0 and the condition
**r | q** (r divides q). For each fixed C, the inner system N − r·C = p·A + q·B
is a 2D problem. The total count is:

```
R₃(N) = Σ_{C=0}^{⌊N/r⌋} R₂(N − r·C;  p, q)
```

where R₂(m; p, q) counts solutions to m = p·A + q·B.

---

### Theorem 4.2 — O(1) R₃ Kernel

**Statement:** For the system N = p·A + q·B + r·C with p ≡ 1 (mod q) and r | q,
define:

```
a₀  = N mod r
m   = N // p
M   = N − p·a₀
J   = (m − a₀) // r
Mq  = M mod q
period = q // r
K   = (J + 1) // period
t   = (J + 1) mod period
```

Then:

```
R₃(N) = ((J+1)·M − p·r·J·(J+1)/2 − R_corr) // q  +  (J+1)
```

where R_corr = K · one_cycle + partial, with:

```
one_cycle = Σ_{j=0}^{period−1} (Mq − r·j) mod q
partial   = Σ_{j=0}^{t−1}      (Mq − r·j) mod q
```

**Complexity:** O(1) — independent of N.

---

### Example — Additive Structure: N = 100 + 300 = 400

System: p = 19, q = 9, r = 3.

The minimal-A solutions for each N:

```
N=100: (A=1, B=9, C=0)  →  19×1 + 9×9 + 3×0 = 100
N=300: (A=0, B=33, C=1) →  19×0 + 9×33 + 3×1 = 300
```

Adding component-wise:

```
(1,9,0) + (0,33,1) = (1,42,1)  →  19×1 + 9×42 + 3×1 = 19 + 378 + 3 = 400  ✓
```

The A₀ values still add: A₀(100) + A₀(300) = 1 + 0 = 1 = A₀(400) mod 9. ✓

Representation counts:
```
R₃(100) =   13
R₃(300) =  109
R₃(400) =  168
```

---

### Example — Intermediate values for (19, 9, 3), N = 171

```
a₀=0, m=9, M=171, J=3, Mq=0, period=3, K=1, t=1
one_cycle = 9,  partial = 0,  R_corr = 9
R₃ = (4×171 − 19×3×3×4/2 − 9) // 9 + 4
   = (684 − 342 − 9) // 9 + 4
   = 333 // 9 + 4 = 37 + 4 = 41
```

Verified against brute force: R₃(171; 19,9,3) = 41. ✓

---

## Part III — The 4D Extension

### Setup

Add a fourth variable: N = p·A + q·B + r·C + s·D, with the additional condition
**s = r**. For each fixed D, the inner system N − s·D = p·A + q·B + r·C is
a 3D problem:

```
R₄(N) = Σ_{D=0}^{⌊N/s⌋} R₃(N − s·D;  p, q, r)
```

The key structural insight for s = r: **J(D) is monotone decreasing** as D increases.
This means the D-values group into blocks where J is constant, and within each block
the computation has closed-form structure.

---

### Theorem 5.1 — O(J_max) Σ₄

**Statement:** The correction sum Σ₄ = Σ_{D} R_corr(D) for s = r systems is computable
by iterating over J-blocks rather than D-values, using the following closed-form
components:

**1. Block length** — for all J < J_max, the block length equals p (proven constant).

**2. K-sum** — the sum of K-values over J = 1, ..., J_max has the closed form:

```
Σ_{i=1}^{m} floor(i/k)  =  k·(Q−1)·Q/2  +  Q·(rem+1)
where  Q = floor(m/k),  rem = m mod k
```

No iteration over J is needed for this term.

**3. one_cycle** — proven constant for all s = r blocks (independent of D within a block).

**4. sum_mod_sequence** — computed in true O(log q) via the ACL floor_sum primitive:

```
Σ_{D=a}^{b} (C − r·D) mod q
```

is evaluated without iteration by reversing the summation index and applying floor_sum.

**Complexity:** O(J_max) = O(N/(p·r))  
**Speedup:** factor ≈ p over O(N/s) direct iteration.

---

### Theorem 5.2 — O(J_max) R₄

**Statement:** For s = r, the full 4D representation count

```
R₄(N) = #{ (A,B,C,D) ∈ ℕ⁴ : p·A + q·B + r·C + s·D = N }
```

is computable in O(J_max) = O(N/(p·r)) by iterating over J-blocks.

**Complexity:** O(J_max) = O(N/(p·r))  
**Speedup:** factor ≈ p compared to O(N/s)

---

### Example — Additive Structure: N = 100 + 300 = 400

System: p = 19, q = 9, r = 3, s = 3.

The minimal-A solutions:

```
N=100: (A=1, B=9,  C=0, D=0)  →  19×1 + 9×9  + 3×0 + 3×0 = 100
N=300: (A=0, B=33, C=1, D=0)  →  19×0 + 9×33 + 3×1 + 3×0 = 300
```

Adding component-wise:

```
(1,9,0,0) + (0,33,1,0) = (1,42,1,0)
→  19×1 + 9×42 + 3×1 + 3×0 = 19 + 378 + 3 + 0 = 400  ✓
```

Representation counts:
```
R₄(100) =      163
R₄(300) =    4,077
R₄(400) =    7,816
```

J-block structure for N=400, system (19,9,3,3):
```
J_max = 6
D-iterations (direct): 134
J-iterations (new):      8
Speedup: 16.8×
```

---

### Example — System (37, 9, 3, 3), N = 171

```
J_max = 1,  J-blocks = 2,  D-iterations = 58,  J-iterations = 2
Speedup: 29×

R₄(171; 37,9,3,3) = 674
```

Verified against brute force.

---

## Complexity Hierarchy

| Method | Complexity |
|---|---|
| Brute force | O(N³ / (p·q·r)) |
| Via R₃ kernel | O(N/s) |
| Via J-block structure (s = r) | O(N/(p·r)) |
| Full closed-form without J-iteration | open problem |

---

## Verified Performance — Anchor System (19, 9, 3, 3)

| N | D-iterations | J-iterations | Speedup |
|---|---|---|---|
| 171 | 58 | 4 | 14.5× |
| 513 | 172 | 10 | 17.2× |
| 1,710 | 571 | 31 | 18.4× |
| 51,300 | 17,101 | 901 | 19.0× |
| 171,000 | 57,001 | 3,001 | 19.0× |

Verified against brute force (N ≤ 500) and against the original R₃ kernel (N ≤ 1,000,000).
All results exact.

---

## Mathematical Primitives

### `floor_sum(n, m, a, b)`
Computes Σ_{i=0}^{n-1} floor((a·i + b) / m) in O(log m) via the AtCoder Library
recursive reduction. Fundamental primitive for all closed-form summations.

### `sum_mod_sequence(C, r, q, n_start, n_end)`
Computes Σ_{D=n_start}^{n_end} (C − r·D) mod q in true O(log q). Derivation:
decompose (x mod q) = x − q·floor(x/q), reverse the summation index i = n_end − D
so the floor becomes Σ floor((r·i + b)/q), then apply floor_sum directly.
Negative b handled by shifting up by a multiple of q.

### `sum_floor_i_div_k(m, k)`
Computes Σ_{i=1}^{m} floor(i/k) in O(1) via the closed formula:
k·(Q−1)·Q/2 + Q·(rem+1), where Q = floor(m/k), rem = m mod k.
Used for the K-sum in Σ₄.

---

## Citation

Bilal el Issaoui,
DOI: 

Bilal el Issaoui, *The 19-9 System: A₀ = dr(N)*, Zenodo, 2026.  
DOI: https://doi.org/10.5281/zenodo.20168954, https://doi.org/10.5281/zenodo.20044995

