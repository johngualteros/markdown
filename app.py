"""
Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio.
Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta
de la compra, y una de las funciones anteriores, y utilice la función pasada para aplicar los
descuentos o el IVA a los productos de la cesta y devolver el precio final de la cesta.
"""

def applyDiscounted(percentageValue,price):
    discount = (percentageValue * price) /100
    return price - discount

def applyIva(iva,price):
    iva = price * iva
    return price + iva

def applyIvaAndDiscount(dictionary):
    dictionaryFinal = {}
    index = 0
    applyDiscount = str(input('you wanna apply discount: ')).lower()
    if applyDiscount == 'yes':
        percentage = int(input('Enter a percentage: '))
        for price in dictionary.values():
            index = index + 1
            dictionaryFinal[index] = applyDiscounted(percentage,price)
    else:
        iva = float(input('Enter a Iva: '))
        for price in dictionary.values():
            index = index + 1
            dictionaryFinal[index] = applyIva(iva, price)

    return dictionaryFinal

dictionary={
    '1' : 2000,
    '2' : 4000,
    '3' : 8500
}

print(dictionary)
print(applyDiscounted(10,2000))
print(applyIva(0.11,2000))
print(applyIvaAndDiscount(dictionary))