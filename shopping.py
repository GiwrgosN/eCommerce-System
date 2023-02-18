"""
    Author  : Georgios Nikolaidis
"""

import json
list_of_products = []  # Initialize the list of product IDs.
# This list ie being used to check whether the given ID is unique or not.
# We use a list because based on the application that we are trying to create
# new products are going to be inserted all the time and maybe deleted.
# Therefore, it is better to use a list for this purpose.


################ Function definition area ##############################

def check_Type(intput_variable, expected_type) ->bool:
    """
    Check whether the user input has the expected type or not
    :param intput_variable: The input variable to check the type
    :param expected_type: The expected type of the input
    :return: True if it is correct type otherwise return false
    """
    return isinstance(intput_variable, expected_type)


def check_unique(list_of_products: list, id_to_check: str) -> bool:
    """
    Check if the given id already exists. If it exists return False
    otherwise return True
    :param list_of_products: List with the IDs of the products so far of type `list`
    Each element of the list is of type `str`
    :param id_to_check: ID to be checked whether it is unique or not based
    on the list_of_products. This is of type `str`
    :return: Return True if ID is unique otherwise return False
    """
    Flag = True  # Flag used for the final result
    for product in list_of_products:
        if product == id_to_check:
            return False  # ID is not unique
    return Flag  # If the loops completes it means that the id is unique


def check_sequence(id_to_check: str) -> bool:
    """
    Check if all the digits in the sequence are between 0 and 9 including
    the border values and if the length of the sequence is 13.
    :param id_to_check: The sequence of digits to check of type `str`
    :return: True if the all the conditions are met otherwise return False
    """
    for digit in id_to_check:  # First we check for the range
        if 0 <= int(digit) <= 9:
            continue  # Valid so continue with the next digit
        else:
            return False  # We found a number out of the expected range
    if len(id_to_check) == 13:  # Finally we check for the length
        return True  # All the conditions are met
    else:
        return False  # The string length condition is not met


def print_Help():
    """ Print help menu """
    print('Please type one of the available options: ')
    print('[A] - Add a new product to the cart')
    print('[R] - Remove a product from the cart')
    print('[S] - Print a summary of the cart')
    print('[Q] - Change the quantity of a product')
    print('[E] - Export a JSON version of the cart')
    print('[T] - Terminate the program')
    print('[H] - List the supported commands')


def add_Product_Functionality() -> bool:
    """ Implement add product functionality of the shopping cart. If the
    user tries to enter a product which already exists or enters a non valid
    value for one of the fields, the action won't be executed, the equivalent messages
    will be printed, informing the user what went wrong.

     :return: Return True if the product has been added otherwise return False """

    print('Adding a new product: ')
    Product_type = input('Please select the type of the product from the list [Clothing, Food, Laptop]: ')
    if Product_type not in ('Clothing', 'Food', 'Laptop'):
        print('Please select a valid product type.')
        add_Product_Functionality()
    else:
        if Product_type == 'Clothing':  # Add a new clothing to the cart
            inserted_name       = str(input('Insert its name: '))        # The user types the values
            try:
                inserted_price      = float(input('Insert its price (£): '))     # for the parameters of the clothing
            except:
                print('Value for the price field must be a float type')
                print('The product {} has not been added to the cart'.format(inserted_name))
                print('Please try again!')
                return False
            try:
                inserted_quantity   = int(input('Insert its quantity: '))
            except:
                print('Value for the quantity field must be a int type')
                print('The product {} has not been added to the cart'.format(inserted_name))
                print('Please try again!')
                return False
            inserted_identifier = str(input('Insert its EAN code: '))
            inserted_brand      = str(input('Insert its brand: '))
            inserted_size       = str(input('Insert its size: '))
            inserted_material   = str(input('Insert its material: '))
            # Create a new Clothing object to be added to the cart
            Clothing_to_add = Clothing(inserted_name, inserted_price, inserted_quantity, inserted_identifier, inserted_brand, inserted_size, inserted_material)
            if len(Clothing_to_add.__dict__.keys()) != 7:  # Not all variables we passed correctly by the user
                print('The product {} has not been added to the cart'.format(inserted_name))
                print('Please make sure that you insert the correct values. ')
                return False
            Our_Shopping_Cart.addProduct(Clothing_to_add)  # Add clothing to the shopping cart
            print('The product {} has been added to the cart.'.format(inserted_name))
            print('The cart contains {} product(s).'.format(len(Our_Shopping_Cart.getContents())))
            return True  # Flag that the addition has been completed successfully
        elif Product_type == 'Food':  # Add a new food to the cart
            inserted_name        = str(input('Insert its name: '))        # The user types the values
            try:
                inserted_price      = float(input('Insert its price (£): '))
            except:
                print('Value for the price field must be a float type')
                print('The product {} has not been added to the cart'.format(inserted_name))
                print('Please try again!')
                return False
            try:
                inserted_quantity   = int(input('Insert its quantity: '))
            except:
                print('Value for the quantity field must be a int type')
                print('The product {} has not been added to the cart'.format(inserted_name))
                print('Please try again!')
                return False
            inserted_identifier  = str(input('Insert its EAN code: '))
            inserted_brand       = str(input('Insert its brand: '))
            inserted_date        = str(input('Insert its expiry date: '))
            try:
                inserted_gluten_free = input('Insert True if it is gluten free otherwise False: ')
                if inserted_gluten_free.lower() not in ('false', 'true'):
                    raise ValueError()
                inserted_gluten_free = bool(inserted_gluten_free)
            except:
                print('Value for the gluten_free field must be a bool type')
                print('The product {} has not been added to the cart'.format(inserted_name))
                print('Please try again!')
                return False
            try:
                inserted_vegan       = input('Insert True if it is suitable for vegans otherwise False: ')
                if inserted_vegan.lower() not in ('false', 'true'):
                    raise ValueError()
                inserted_vegan       = bool(inserted_vegan)
            except:
                print('Value for the inserted_vegan field must be a bool type')
                print('The product {} has not been added to the cart'.format(inserted_name))
                print('Please try again!')
                return False
            # Create a new Food object to be added to the cart
            Food_to_add = Food(inserted_name, inserted_price, inserted_quantity, inserted_identifier, inserted_brand, inserted_date, inserted_gluten_free, inserted_vegan)
            if len(Food_to_add.__dict__.keys()) != 8:  # Not all variables we passed correctly by the user
                print('The product {} has not been added to the cart'.format(inserted_name))
                print('Please make sure that you insert the correct values. ')
                return False
            Our_Shopping_Cart.addProduct(Food_to_add)  # Add Food to the shopping cart
            print('The product {} has been added to the cart.'.format(inserted_name))
            print('The cart contains {} product(s).'.format(len(Our_Shopping_Cart.getContents())))
            return True  # Flag that the addition has been completed successfully
        else:  # Add a new laptop to the cart
            inserted_name       = str(input('Insert its name: '))        # The user types the values
            try:
                inserted_price      = float(input('Insert its price (£): '))
            except:
                print('Value for the price field must be a float type')
                print('The product {} has not been added to the cart'.format(inserted_name))
                print('Please try again!')
                return False
            try:
                inserted_quantity   = int(input('Insert its quantity: '))
            except:
                print('Value for the quantity field must be a int type')
                print('The product {} has not been added to the cart'.format(inserted_name))
                print('Please try again!')
                return False
            inserted_identifier = str(input('Insert its EAN code: '))
            inserted_brand      = str(input('Insert its brand: '))
            inserted_year       = str(input('Insert its year of release: '))
            try:
                inserted_RAM        = int(input('Insert its RAM: '))
            except:
                print('Value for the RAM field must be a int type')
                print('The product {} has not been added to the cart'.format(inserted_name))
                print('Please try again!')
                return False
            Laptop_to_add       = Laptop(inserted_name, inserted_price, inserted_quantity, inserted_identifier, inserted_brand, inserted_year, inserted_RAM)
            if len(Laptop_to_add.__dict__.keys()) != 7:  # Not all variables we passed correctly by the user
                print('The product {} has not been added to the cart.'.format(inserted_name))
                print('Please make sure that you insert the correct values. ')
                return False
            Our_Shopping_Cart.addProduct(Laptop_to_add)  # Add Laptop to the shopping cart
            print('The product {} has been added to the cart.'.format(inserted_name))
            print('The cart contains {} product(s).'.format(len(Our_Shopping_Cart.getContents())))
            return True  # Flag that the addition has been completed successfully
    return False  # Something went wrong

def remove_Product_Functionality():
    """ This function implements the remove option from the cart
      The user will need to enter the EAN code of the product that
      he/she wants to remove from the cart. If the product does not exist
      no removal will take place and a message will be printed"""
    global list_of_products  # List of all EANs so far.
    EAN_to_remove = input('Please insert the EAN code of the product to remove: ')
    Found_Flag = False  # Indication of whether the product has been found in the cart
    for item in Our_Shopping_Cart.getContents():
        if item.unique_identifier == EAN_to_remove:  # Check whether this product exists in the cart
            Our_Shopping_Cart.removeProduct(item)
            list_of_products = [code for code in list_of_products if code != EAN_to_remove] # Remove this EAN from the list of the inserted EANs.
            print('Product {} with EAN: {} was removed from the cart'.format(item.name, EAN_to_remove))
            Found_Flag = True
    if Found_Flag == False: # The item was not found in the cart
        print('The item was not found in the cart!')
        print('Please use the option [E] to see the products in the cart!')


def change_quantity_Functionality():
    """ This function changes the quantity of a product in the cart.
    The user will need to enter the EAN code of the product and the
    new quantity """
    EAN_to_update = input('Please insert the EAN code of the product to update quantity: ')
    new_quantity  = input('Please enter the new quantity of the product: ')
    Updated_Flag  = False  # Indication of whether the product has been updated
    try:
        new_quantity = int(new_quantity)
    except:
        print('The new quantity must be a positive number.')
    for item in Our_Shopping_Cart.getContents():
        if item.unique_identifier == EAN_to_update:  # Check whether this product exists in the cart
            item.quantity = new_quantity  # We found the product so we update the quantity
            print('The quantity of the product has been updated successfully!')
            Updated_Flag = True
    if Updated_Flag == False:  # The item was not found in the cart
        print('The item was not found in the cart!')
        print('Please use the option [E] to see the products in the cart!')


def print_summary_Functionality():
    """ This function prints a summary of the things in the cart.
    It shows the name of the items, total price of each item = price*quantity
    and the total price of all the items in the cart."""

    print('This is the total of the expenses: ')
    total_ammount    = 0  # The total amount to be paid
    contents_of_cart = Our_Shopping_Cart.getContents()  # Get the contents of the cart
                                                        # each element in the list is of type Product
    for index, item in enumerate(contents_of_cart):     # Print the contents of the cart
        print("{} - {} * {} = £{}".format(index+1, item.quantity, item.name, item.quantity*item.price))
        total_ammount = total_ammount + item.quantity*item.price
    print('Total = £{}'.format(total_ammount))  # At the end print the total ammount

def print_JSON():
    """ Print the contents of the cart as JSON-formatted data dump """
    for item in Our_Shopping_Cart.getContents():
        print(150*'-')
        print(json.dumps(item.to_json(), indent=4))

################## END OF FUNCTION DEFINITION AREA #####################


class Product():
    """ This class implements the general form of a product sold
        in a simple eCommerce system."""
    def __init__(self, name: str, price: float, quantity: int, unique_identifier: str, brand: str):
        """
        Construct an instance of the class Product.
        :param name: The name of the product of type `str`.
        :param price: The price of the product of type `float`.
        :param quantity: The quantity of the product of type `int`.
        :param unique_identifier: 13 digit sequence unique code of type `str`.
        :param brand: The brand of the product of type `str`.
        """
        try:
            if check_Type(name, str):  # Check if the input for the name of the product is a string.
                self.name = name
            else:
                print('The value which was inserted for the variable name is not of type {}'.format('str'))
                raise ValueError()
            if check_Type(price, float) & (price > 0.0):  # Check if the price is a valid value.
                self.price = price
            else:
                print('The value for the variable price must be of type {} and a positive number '.format('float'))
                raise ValueError()
            if check_Type(quantity, int) & (quantity > 0):  # Check if the quantity is a valid value.
                self.quantity = quantity
            else:
                print('The value for the variable quantity must be of type {} and a positive number'.format('int'))
                raise ValueError()
            if (check_Type(unique_identifier, str)):   # We check if EAN is a string
                if check_sequence(unique_identifier):  # We check if EAN is a sequence of 13 digit integers from 0 to 9.
                    if check_unique(list_of_products, unique_identifier):  # Check if this EAN arleady exists.
                        self.unique_identifier = unique_identifier  # If it passes all the checks we initialise.
                        list_of_products.append(unique_identifier)  # Append ID to the list of IDs.
                    else:
                        print('The value which was inserted for the variable EAN corresponds to another product')
                        raise ValueError()
                else:
                    print('EAN must be a 13 digit number with each digit being between 0 and 9')
                    raise ValueError()
            else:
                print('The value which was inserted for the variable unique_identifier is not of type `str`')
                raise ValueError()
            if check_Type(brand, str):  # Check if type is of type `str`.
                self.brand = brand
            else:
                print('A product with the same EAN already exists. '.format('str'))
                raise ValueError()
        except:
            print('Something went wrong!')  # In this case the object will be created with fewer attributes than expected.


    def to_json(self) -> dict:
        """ Return attributes of instance in json format """
        dict_to_export = {
            'Product': [{
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity,
            'unique_identifier': self.unique_identifier,
            'brand': self.brand
            }]
        }
        return dict_to_export


class Clothing(Product):
    """ This class is a special case of the class Product and it implements the class of a Clothing """


    def __init__(self, name: str, price: float, quantity: int, unique_identifier: str, brand: str, size: str, material: str):
        """
        Construct instance of the class Clothing. It inherits all the attributes of the parent class (Product)
        so for their description look at the dockstring of the class `Product`.

        :param size: Size of the clothing of type `str`.
        :param material: Material of the clothing of type `str`.
        """
        super().__init__(name, price, quantity, unique_identifier, brand)  # Call the constructor of the parent class
        if check_Type(size, str):  # Check if the size is of type `string`.
            self.size = size
        else:
            print('The value which was inserted for the variable size is not of type {}'.format('str'))
        if check_Type(material, str):
            self.material = material  # Check if the material is of type `string`.
        else:
            print('The value which was inserted for the variable material is not of type {}'.format('str'))


    def to_json(self) -> dict:
        """ Return attributes of instance in json format. """
        dict_to_export = {
            'Clothing': [{
                'name': self.name,
                'price': self.price,
                'quantity': self.quantity,
                'unique_identifier': self.unique_identifier,
                'brand': self.brand,
                'size': self.size,
                'material': self.material
            }]
        }
        return dict_to_export


class Food(Product):
    """ This class is a special case of the class Product and it implements the class of Food"""

    def __init__(self, name: str, price: float, quantity: int, unique_identifier: str, brand: str, expiry_date: str, gluten_free: bool, suitable_for_vegans: bool):
        """
        Construct instance of the class Food. It inherits all the attributes of the parent class (Product)
        so for their description look at the dockstring of the class `Product`.

        :param expiry_date: Expiration date of the food of type `str`.
        :param gluten_free: Flag whether this food is gluten free or not. Type `bool`.
        :param suitable_for_vegans: Flag whether this food is vegan or not. Type `bool`.
        """
        super().__init__(name, price, quantity, unique_identifier, brand)  # Call the constructor of the parent class
        if check_Type(expiry_date, str):  # Check if expiration date is of type `string`.
            self.expiry_date = expiry_date
        else:
            print('The value which was inserted for the variable expiry date is not of type {}'.format('str'))
        if check_Type(gluten_free, bool):  # Check if gluten free is of type `bool`.
            self.gluten_free = gluten_free
        else:
            print('The value which was inserted for the variable gluten free is not of type {}'.format('bool'))
        if check_Type(suitable_for_vegans, bool):  # Check if suitable for vegans is of type `bool`.
            self.suitable_for_vegans = suitable_for_vegans
        else:
            print('The value which was inserted for the variable suitable for vegans is not of type {}'.format('bool'))


    def to_json(self) -> dict:
        """ Return attributes of instance in json format. """
        dict_to_export = {
            'Food': [{
                'name': self.name,
                'price': self.price,
                'quantity': self.quantity,
                'unique_identifier': self.unique_identifier,
                'brand': self.brand,
                'expiry_date': self.expiry_date,
                'gluten_free': self.gluten_free,
                'suitable_for_vegans': self.suitable_for_vegans
            }]
        }

        return dict_to_export

class Laptop(Product):
    """ This class is a special case of the class Product and it implements the class of a Laptop. """

    def __init__(self, name: str, price: float, quantity: int, unique_identifier: str, brand: str, year_released: str, RAM: int):
        """
        Construct instance of the class Laptop. It inherits all the attributes of the parent class (Product)
        so for their description look at the dockstring of the class `Product`.

        :param year_released: The year that the Laptop was released of type `str`.
        :param RAM: The RAM of the Laptop of type `int`.
        """
        super().__init__(name, price, quantity, unique_identifier, brand)  # Call the constructor of the parent class.
        if check_Type(year_released, str):  # Check if year released is of type `string`.
            self.year_released = year_released
        else:
            print('The value which was inserted for the variable year_released is not of type {}'.format('str'))
        if check_Type(RAM, int) & (RAM > 0):  # Check if RAM is of type `int`.
            self.RAM = RAM
        else:
            print('The value for the variable RAM must be of type {} and a positive number'.format('int'))


    def to_json(self) -> dict:
        """ Return attributes of instance in json format. """
        dict_to_export = {
            'Laptop': [{
                'name': self.name,
                'price': self.price,
                'quantity': self.quantity,
                'unique_identifier': self.unique_identifier,
                'brand': self.brand,
                'year_released': self.year_released,
                'RAM': self.RAM
            }]
        }
        return dict_to_export


class ShoppingCart():
    """ This class implements the entity of a shopping Cart in a session.
    We can add and remove products from the shopping cart, get the contents,
    and of course change the quantity of an existing product. """


    def __init__(self):
        """
         Constructor of the class Shopping Cart.
        :param list_of_items: The list which will contain the Products
        """
        self.__list_of_items = []  # I chose a list because
        # we want to be able to add and remove objects from the list
        # and since a list is a mutable object we can do these operations.
        # Furthermore, we expect that addProduct,removeProduct,changeProductQuantity
        # will be used more often compared to getContents.


    def addProduct(self, p: Product):
        """
        Add new product to the cart.
        :param p: The new product to be added of type `Product`
        """
        if check_Type(p, Product):
            self.__list_of_items.append(p)  # Append the new product to the shopping cart.
        else:
            print('Sorry! You tried to insert a value to the cart which is not a Product ')


    def removeProduct(self, p: Product):
        """
        Remove a product from the cart.
        :param p: The product to be removed from the cart of type `Product`.
        """
        if check_Type(p, Product):
            self.__list_of_items = [element for element in self.__list_of_items if element != p]
            # All the occurences of the same object will be removed from the list
        else:
            print('Sorry! You tried to remove a value from the cart which is not a Product ')


    def getContents(self):
        """ Return products of the cart in alphabetical order of product name """
        content_list = sorted(self.__list_of_items, key=lambda x: x.name)   # For this one I used code from the following
                                                                            # URL: https://stackoverflow.com/questions/403421/how-to-sort-a-list-of-objects-based-on-an-attribute-of-the-objects
                                                                            # Author: Kenan Banks
                                                                            # Date: 22/10/2022
        return content_list


    def changeProductQuantity(self, p: Product, q: int):
        """
        Change the quantity of the product p to q
        :param p: The product to be modified of type `Product`
        :param q: The new quantity of the product of type `int`
        """
        if (check_Type(p, Product)) & (check_Type(q, int)):  # Check if the inputs are valid
            for item in self.__list_of_items:
                if item == p:
                    item.quantity = q  # It will change the quantity of this object
                                       # If the object exits more than 1 it will affect
                                       # them as well
        else:
            print('Values given for the quantity change are not valid')


print('The program has started.')
print('Insert your next command (H for help):')
Our_Shopping_Cart = ShoppingCart()  #  Create a new instance of the class shopping card
                                    #  to store the products
while True:
    c = input("Type your next command:")
    if c not in ('A', 'R', 'S', 'Q', 'E', 'T', 'H'):
        print("Command not recognised. Please try again") # If the command is not valid
                                                          # print message
        continue        # Ask the user to type again
    else:
        if c == 'A':    # Add product to the cart
             add_Product_Functionality()  # For info about this function look at the start of the script.
        elif c == 'R':  # Remove product from the cart
             remove_Product_Functionality() # For info about this function look at the start of the script.
        elif c == 'S':  # Print summary of the cart
            print_summary_Functionality() # For info about this function look at the start of the script.
        elif c == 'Q':  # Change the quantity of a product
            change_quantity_Functionality() # For info about this function look at the start of the script.
        elif c == 'E':   # Generate JSON summary
            print_JSON() # For info about this function look at the start of the script.
        elif c == 'T':   # Quit
            break
        else:   # Print help menu
            print_Help()

print('Goodbye.')

