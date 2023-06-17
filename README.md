## Malpoly

A little Python library to do some operations with polynomials. I might use this for school next year.


### Defining a polynomial

```python
from malpoly import Polynomial

P = Polynomial.build((
    (2, 3),  # 2*x**3
    (7, 2),  # 7*x**2,
    (-6, 1), # -6*x
    (18, 0), # +18
))
```

### Evaluating polynomials

```python
p: Polynomial = ...

y = p(5)  # get the value at x=5
```

### Getting the derivative of a polynomial

```python
p: Polynomial = ...

dp_dx = p.derivative()
```

### Finding zero using Newton Rafson method

```python
p: Polynomial = ...

print(p.newton_rafson())
```

### Finding zero using bruteforce

```python
p: Polynomial = ...

print(p.bruteforce_roots()
```
