# eCommerce-System

This project is an implementation of a simple eCommerce system. The program allows the users to:

- Add products.
- Remove products.
- Show a summary of their shopping session.
- Export the content of the shopping cart in JSON format.

## The script implements the following classes:
&nbsp;
![image](https://user-images.githubusercontent.com/43292736/219855517-4b77402b-5e56-46d2-bc3c-300c2c50a26d.png)

&nbsp;
## Class: Product
&nbsp;
### Attributes:
- name: The name of the product of type `str`.
- price: The price of the product of type `float`.
- quantity: The quantity of the product of type `int`.
- unique_identifier: 13 digit sequence unique code of type `str`.
- brand: The brand of the product of type `str`.

&nbsp;
### Methods:
- to_json: Return attributes of instance in json format.

&nbsp;
## Class: Clothing
&nbsp;
### Attributes:
- size: Size of the clothing of type `str`.
- material: Material of the clothing of type `str`.

&nbsp;
### Methods:
- to_json: Return attributes of instance in json format.


&nbsp;
## Class: Food
&nbsp;
### Attributes:
- expiry_date: Expiration date of the food of type `str`.
- gluten_free: Flag whether this food is gluten free or not. Type `bool`.
- suitable_for_vegans: Flag whether this food is vegan or not. Type `bool`.

&nbsp;
### Methods:
- to_json: Return attributes of instance in json format.


&nbsp;
## Class: Laptop
&nbsp;
### Attributes:
- year_released: The year that the Laptop was released of type `str`.
- RAM: The RAM of the Laptop of type `int`.

&nbsp;
### Methods:
- to_json: Return attributes of instance in json format.


&nbsp;
## Class: ShoppingCart
&nbsp;
### Attributes:
- list_of_items: The list which will contain the Products.

&nbsp;
### Methods:
- addProduct: Add new product to the cart.
- removeProduct: Remove a product from the cart.
- getContents: Return products of the cart in alphabetical order of product name.
- changeProductQuantity: Change the quantity of an already chosen product.



