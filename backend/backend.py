import transformador

def decimal(deci: str) -> None:
    try:
        if not deci.isdigit():
            raise ValueError('Número decimal inválido.')
        
        bina = transformador.decimal_a_binario(deci)
        hexa = transformador.decimal_a_hexadecimal(deci)

        print(f'\nBinario: {bina}\nHexadecimal: {hexa}')
    
    except ValueError as error:
        print(error)

def binario(bina: str) -> None:
    try:
        for i in bina:
            if i not in ['0', '1']:
                raise ValueError('Número binario inválido.')
        
        deci = transformador.binario_a_decimal(bina)
        hexa = transformador.binario_a_hexadecimal(bina)

        print(f'\nDecimal: {deci}\nHexadecimal: {hexa}')

    except ValueError as error:
        print(error)

def hexadecimal(hexa: str) -> None:
    try:
        if (len(hexa) < 3) or (hexa[:2] != '0x' and hexa[:2] != '0X'):
            raise ValueError('Hexadecimal inválido.')
        
        deci = transformador.hexadecimal_a_decimal(hexa)
        bina = transformador.hexadecimal_a_binario(hexa)

        print(f'\nDecimal: {deci}\nBinario: {bina}')
    
    except ValueError as error:
        print(error)


if __name__ == '__main__':
    print('-----Bienvenido a Transformador de bases numéricas-----')
    print('\n¿Qué deseas transformar?')
    print('\n[1] Decimal\n[2] Binario\n[3] Hexadecimal\n[4] Salir de la app')
    respuesta = ''
    while respuesta != '4':
        respuesta = str(input('\nIngrese su opción (1, 2, 3 o 4): '))
        if respuesta not in ['1', '2', '3', '4']:
            print('Respuesta inválida.')
        elif respuesta == '1':
            numero = str(input('Ingrese el número: '))
            decimal(numero)
        elif respuesta == '2':
            numero = str(input('Ingrese el número: '))
            binario(numero)
        elif respuesta == '3':
            numero = str(input('Ingrese el número: '))
            hexadecimal(numero)