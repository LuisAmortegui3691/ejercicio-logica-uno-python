import locale


# Configurar locale a colombiano para formato de moneda
locale.setlocale(locale.LC_ALL, 'es_CO.utf8')  # Puede variar según tu sistema operativo


menu = {
    1: {'articulo':'control PS5', 'precio':349900},
    2: {'articulo':'control xbox one turtle', 'precio':329000},
    3: {'articulo':'diademas turtle over ear PS5 - PS4', 'precio':539000},
    4: {'articulo':'Control para Switch Negro', 'precio':299900},
    5: {'articulo':'Volante XBOX|PC Negro', 'precio':699900}
}

def resumen_compra(orden):
    print('resumen de la compra...')
    subtotal = calcular_subtolal(orden)
    impuesto = calucular_Impuesto(subtotal)
    nombres = [item['articulo'] for item in orden]
    total = round(subtotal + impuesto, 2)
    return nombres, total

def calucular_Impuesto(subtotal):
    print('Calculando impuestos...')
    impuestos = round(subtotal * 0.19, 2)
    return impuestos

def  calcular_subtolal(orden):
    print('Calculando subtotal...')
    subtotal = sum([item['precio'] for item in orden])
    return subtotal

def imprimir_orden(orden):
    print(f'Usted ha elegido {str(len(orden))} elmentos')
    for select in orden:
        print(f'{select['articulo']} por un precio de $ {select['precio']}')
    return orden

def mostrar_menu():
    print('Menu')
    for seleccion in menu:
        print(f'{seleccion}. {menu[seleccion]['articulo'] : <35} | {menu[seleccion]['precio'] : >5}')
    print()

def traer_orden():
    mostrar_menu()
    orden = []
    contador = 1
    for i in range(3):
        item = input(f'Por favor ingrese el producto # {str(contador)} de 3 productos: ')
        contador += 1
        orden.append(menu[int(item)])
    # print(orden)
    return orden

def main():
    orden = traer_orden()
    imprimir_orden(orden)

    subtotal = calcular_subtolal(orden)
    subtotal_formato = locale.currency(subtotal, grouping=True)
    print(f'El subtotal de su compra es {subtotal_formato}') 

    impuestos = calucular_Impuesto(subtotal)
    impuestos_formato = locale.currency(impuestos, grouping=True)
    print(f'El precio de los impuestos es de {impuestos_formato}')

    # resumen de la operacion
    nombres, total = resumen_compra(orden)
    print(f'Los articulos elegidos son {nombres}')
    print(f'El precio total de la compra es de {locale.currency(total, grouping=True)}')

if __name__ == '__main__':
    # print(__name__)
    main()







