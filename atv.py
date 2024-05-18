pi = 3.14
def circunferencia(raio):
    circunferencia = pi*2*raio
    return circunferencia
raio_do_circulo = float(input("Digite o raio do círculo: "))
resultado = circunferencia(raio_do_circulo)
print(f"A circunferência do círculo é aproximadamente {resultado:.1f}.")