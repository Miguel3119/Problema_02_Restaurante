# ==========================================================
# Nombre del estudiante: Orlando Miguel Luna Delgado
# Grupo: 213022_731
# Programa: Ingeniería de Sistemas
# Curso: Fundamentos de Programación (Fase 5 - Evaluación Final POA)
# Problema seleccionado: Problema 2 - Promoción de Restaurante
# Código fuente: Autoría propia
# ==========================================================

# Matriz base de productos [Nombre, Categoría, Precio base]
MENU_RESTAURANTE = [
    ["Hamburguesa Especial", "Platos Fuertes", 30000.0],
    ["Papas a la Francesa", "Acompañantes", 10000.0],
    ["Perro Caliente Especial", "Platos Fuertes", 28000.0],
    ["Agua sin gas 500ml", "Bebidas", 5000.0],
    ["Helado Surtido", "Postres", 12000.0],
    ["Carne Asada", "Platos Fuertes", 40000.0],
    ["Lasaña Mixta", "Platos Fuertes", 22000.0]
]

PORCENTAJE_DESCUENTO = 0.15


# 1. FUNCIÓN: Captura la configuración de la promoción por teclado (Con return)
def solicitar_parametros_promocion():
    """Solicita la categoría objetivo y el umbral de precio de forma segura."""
    print("\n" + "=" * 70)
    print("        CONFIGURACIÓN DE PARÁMETROS DE LA PROMOCIÓN        ")
    print("=" * 70)
    categoria = input("Ingrese la categoría objetivo para el descuento (ej. Platos Fuertes): ").strip()

    while True:
        try:
            umbral = float(input("Ingrese el umbral de precio mínimo ($): "))
            if umbral < 0:
                print("El umbral no puede ser negativo. Intente de nuevo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Ingrese un valor numérico válido (ej. 25000).")

    return categoria, umbral


# 2. FUNCIÓN: Calcula el precio final de un producto (Con return)
def calcular_precio_final(categoria_prod, precio_base, categoria_obj, umbral):
    """Calcula el precio final aplicando el 15% si cumple AMBAS condiciones."""
    if categoria_prod.lower() == categoria_obj.lower() and precio_base > umbral:
        descuento = precio_base * PORCENTAJE_DESCUENTO
        precio_final = precio_base - descuento
        aplica_promocion = True
    else:
        precio_final = precio_base
        aplica_promocion = False

    return precio_final, aplica_promocion


# 3. PROCEDIMIENTO: Muestra la salida formateada (Sin return)
def mostrar_reporte_promocion(categoria_obj, umbral):
    """Muestra la tabla final con los precios recalculados."""
    print("\n" + "=" * 70)
    print("        RESTAURANTE LAS VEGAS - CARTA Y PROMOCIONES        ")
    print("=" * 70)
    print(f"Promoción activa: {PORCENTAJE_DESCUENTO*100:.0f}% Dto. en '{categoria_obj}' con precio > ${umbral:,.0f}\n")

    print(f"{'PRODUCTO':<23} | {'CATEGORÍA':<15} | {'P. BASE':<12} | {'P. FINAL':<12}")
    print("-" * 70)

    # Desempaquetado directo de cada elemento de la fila de la matriz
    for nombre, categoria, precio_base in MENU_RESTAURANTE:
        precio_final, aplica = calcular_precio_final(
            categoria, precio_base, categoria_obj, umbral
        )

        marca = " (*)" if aplica else ""
        print(f"{nombre:<23} | {categoria:<15} | ${precio_base:<11,.2f} | ${precio_final:<11,.2f}{marca}")

    print("-" * 70)
    print("(*) Productos con el 15% de descuento aplicado.")
    print("=" * 70)


# 4. FUNCIÓN PRINCIPAL: Controlador interactivo
def main():
    while True:
        categoria_obj, umbral = solicitar_parametros_promocion()
        mostrar_reporte_promocion(categoria_obj, umbral)

        opcion = input("\n¿Desea consultar otra categoría o umbral? (s/n): ").strip().lower()
        if opcion not in ["s", "si"]:
            print("\n" + "=" * 70)
            print(" ¡Gracias por utilizar el sistema del Restaurante Las Vegas! ")
            print("=" * 70)
            break


if __name__ == "__main__":
    main()