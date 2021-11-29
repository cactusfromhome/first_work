# iepirkumu grozs
cart = []

def add_product(product):

    # lasīt, rakstīt, pievienot
    products_file = open('files/products.txt', 'r', encoding='utf-8')
    products = products_file.readlines()
    print(products)

    if product + '\n' in products:

        cart_file = open('files/cart.txt', 'a', encoding='utf-8')
        cart_file.write(product)

        cart.append(product)
        print(f'Grozam tika pievienots {product}')

    else:
        print('Diemžēl šis produkts nav pieejams')


def remove_product(product):

    cart_file = open('files/cart.txt', 'r', encoding='utf-8')
    cart = cart_file.readlines() # šajā failā ir ar '\n'
    cart_file.close()

    if product + '\n' in cart:
        cart.remove(product + '\n')
        print(f'No groza tika izņemts {product}')

    else:
        print('Produkta nav iepirkuma grozā')

def clear_all_products():

    cart_file = open('files/cart.txt', 'w', encoding='utf-8')
    cart_file.write('')
    cart_file.close()

    print('Iepirkumu grozs tika attīrīts')


while True:

    print("Choose action 'add', 'remove', 'reset', 'stop'")
    action = input('Action: ')

    if action == 'add':
        add_product(product=input('Enter product: '))

    if action == 'remove':
        remove_product(product=input('Enter product:'))

    if action == 'reset':
        clear_all_products()

    if action == 'stop':
        quit()

    print(cart)