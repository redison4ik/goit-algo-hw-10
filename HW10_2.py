import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Визначення функції та межі інтегрування
def f(x):
    return 1 / x

a = 1
b = 10

# Метод Монте-Карло
N = 100000  # кількість точок
x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(0, f(a), N)

under_curve = y_rand < f(x_rand)
monte_carlo_integral = (b - a) * 2 * np.sum(under_curve) / N

# Обчислення інтеграла
real_integral, _ = quad(f, a, b)

# Візуалізація
x_vals = np.linspace(a, b, 500)
y_vals = f(x_vals)
plt.plot(x_vals, y_vals, label='f(x) = 1/x', color='blue')
plt.fill_between(x_vals, y_vals, alpha=0.2, color='gray', label='Площа під кривою')
plt.scatter(x_rand[:1000], y_rand[:1000], s=1, alpha=0.3, color='red', label='Точки Монте-Карло')
plt.title("Метод Монте-Карло для обчислення інтеграла")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()

# Результати
print(f"Інтеграл методом Монте-Карло ≈ {monte_carlo_integral:.4f}")
print(f"Точне значення інтеграла (quad) = {real_integral:.4f}")
print(f"Похибка = {abs(monte_carlo_integral - real_integral):.6f}")
