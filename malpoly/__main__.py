from malpoly import Polynomial

if __name__ == "__main__":
    p = Polynomial.build(((1, 5), (-1, 2), (-18, 0)))

    print(f"f({p.newton_rafson()}) ≈ 0")
    print(f"f(x) = {p}")
    print(f"f'(x) = {p.derivative()}")
    print(f"F(f') = {p.derivative().primitive()}")
    print(f"I(1, 5, f(x)dx) = {p.integrate(1, 5)}")
