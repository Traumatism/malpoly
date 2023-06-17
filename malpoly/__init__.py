from typing import Optional, Generator, Tuple, Self, Reversible

Numeric = complex | float | int
Monomial = Tuple[Numeric, int]


class Polynomial:

    def __init__(
        self,
        coefficient: Numeric,
        degree: int,
        child: Optional[Self],
    ) -> None:

        assert self.degree >= 0, "Degree must be positive"

        self.coefficient = coefficient
        self.degree = degree
        self.child = child

    def __repr__(self) -> str:
        o = ""

        if abs(self.coefficient) != 1:
            o += str(self.coefficient)

        elif self.coefficient == -1:
            o += "-"

        o += "x"               if self.degree > 0 else ""
        o += f"^{self.degree}" if self.degree > 1 else ""
        o += repr(self.child)  if self.child      else ""

        return o

    def is_root(self, x: Numeric) -> bool:
        return self(x) == 0

    def bruteforce_roots(
        self, a: Numeric = -100., b: Numeric = 100., step: Numeric = .5
    ) -> Generator[float, None, None]:

        while a < b:
            if self.is_root(a):
                yield a

            a += step

    def __call__(self, x: Numeric) -> Numeric:
        y = self.coefficient * x ** self.degree

        if self.child:
            y += self.child(x)

        return y

    @classmethod
    def build(cls, A: Reversible[Monomial]) -> Self:
        last = None

        for coef, deg in reversed(A):
            last = Polynomial(coef, deg, last)

        return last

    def derivative(self) -> Self:
        return Polynomial(
            self.coefficient * self.degree,
            self.degree - 1,
            self.child.derivative() if self.child and self.child.degree > 0 else None
        )

    def newton_rafson(self, x = 1, precision = 30):
        if precision == 0:
            return x

        return self.newton_rafson(
            x - self(x) / self.derivative()(x),
            precision - 1
        )
