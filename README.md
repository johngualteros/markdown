# Examaple markdown
***
### _the problem_
>Write a function that applies a discount to a price and another that applies VAT to a price.
Write a third function that receives a dictionary with the prices and percentages of a basket
of the purchase, and one of the previous functions, and use the last function to apply the
discounts or VAT on the products in the basket and return the final price of the basket.

***
* language:
  * python 

```python
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

print(applyIvaAndDiscount(dictionary))
```