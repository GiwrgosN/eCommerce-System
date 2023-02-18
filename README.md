# eCommerce-System

This project is an implementation of a simple eCommerce system. The program allows the users to:

- Add products
- Remove products
- Show a summary of their shopping session
- Export the content of the shopping cart in JSON format

## The script implements the following classes:
&nbsp;
![image](https://user-images.githubusercontent.com/43292736/219855517-4b77402b-5e56-46d2-bc3c-300c2c50a26d.png)

&nbsp;
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
- to_json: Return attributes of instance in json format
