import sympy as sp

t,k = sp.symbols('t k')
omega=sp.Function('omega')(t)

spin_eq=sp.Eq(omega.diff(t),-k*omega)

spin_solution=sp.dsolve(spin_eq)
print("The theoretical physics equation for our relation is:")
print(spin_solution)

