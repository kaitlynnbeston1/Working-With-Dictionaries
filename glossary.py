# Making the glossary
glossary = {
    "conditional test": "a test where Python checks whether something is true or false.",
    "print statement": "a function in Python which prints text to a terminal.",
    "list": "A list of strings, intigers, and/or floats in Python. Allows you to do things like find the sum of a bunch of items or easily pull items for other perposes.",
    "for loop": "A loop in Python that does something for every item in a list.",
    "tuple": "Similar to a list, only items within a tuple cannot be modified.",
    }


# Preparing to print by assigning variables
w1 = glossary["conditional test"]
w2 = glossary["for loop"]
w3 = glossary["list"]
w4 = glossary["print statement"]
w5 = glossary["tuple"]


# Printing the glossary
print(f"Conditional Test: \n {w1} \n \n For loops: \n {w2} \n \n List: \n {w3} \n \n Print statement: \n {w4} \n \n Tuple: \n {w5}")