def jacobi_method(iterations=4):
    print("Método de Jacobi:")
    x, y, z = 0, 0, 0
    for i in range(iterations):
        x_new = y + z
        y_new = (2 - x + 5 * z) / 2
        z_new = (3 * x - y - 1) / 4
        print(f"Iteración {i+1}: x = {x_new:.6f}, y = {y_new:.6f}, z = {z_new:.6f}")
        x, y, z = x_new, y_new, z_new
    print()

def gauss_seidel_method(iterations=4):
    print("Método de Gauss-Seidel:")
    x, y, z = 0, 0, 0
    for i in range(iterations):
        x = y + z
        y = (2 - x + 5 * z) / 2
        z = (3 * x - y - 1) / 4
        print(f"Iteración {i+1}: x = {x:.6f}, y = {y:.6f}, z = {z:.6f}")
    print()

# Ejecutar ambos métodos
jacobi_method()
gauss_seidel_method()
