#let us import all the functions in order/sequense , from the modular_functions file.
import modular_functions as functions


"""
I'll be creating global variables here, and passing them to the functions as params. 
Since its a small project, It is scalable and modular.
core should be error handling.
"""

def extract_data(url):
    """
    We'll be using this function to extract tabular data from the given url. since it is tabular data in htlm, we'll directly parse it from pandas html function.
    """
    