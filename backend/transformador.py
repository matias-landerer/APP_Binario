def binario_a_decimal(bina: str) -> str:
    lista_bin = []
    for i in bina:
        lista_bin.append(int(i))
    lista_bin.reverse()
    deci = 0
    for i in range(len(lista_bin)):
        deci += lista_bin[i] * (2 ** i)
    return str(deci)

def binario_a_hexadecimal(bina: str) -> str:
    deci = binario_a_decimal(bina)
    hexa = decimal_a_hexadecimal(deci)
    return hexa

def decimal_a_binario(deci: str) -> str:
    bina = bin(int(deci))[2:]
    if len(bina) % 4 != 0:
        resto = len(bina) % 4
        n_bits_extra = 4 - resto
        bina_final = '0' * n_bits_extra
        bina_final += bina
        bina = bina_final
    return bina

def decimal_a_hexadecimal(deci: str) -> str:
    return hex(int(deci))

def hexadecimal_a_binario(hexa: str) -> str:
    deci = hexadecimal_a_decimal(hexa)
    bina = decimal_a_binario(deci)
    return bina

def hexadecimal_a_decimal(hexa: str) -> str:
    letras_hex = ['a', 'b', 'c', 'd', 'e', 'f']
    hexa = hexa[2:]
    lista_hex = []
    for i in hexa:
        if i.isdigit():
            lista_hex.append(int(i))
        else:
            i = i.lower()
            if i in letras_hex:
                lista_hex.append(ord(i) - 87)
            else:
                raise ValueError('Hexadecimal inválido.')
    lista_hex.reverse()
    deci = 0
    for i in range(len(lista_hex)):
        deci += lista_hex[i] * (16 ** i)
    return str(deci)
