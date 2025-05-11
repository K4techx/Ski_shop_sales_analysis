def tax_calculator (subtotal, tax_rate):
    """ takes in a subtotal and a tax rate and returns total levied
   
    Args:
       subtotal(float, int): takes the amount if transaction
       tax_rate(float, optional): tax_rate accordinf to the store location. set to 0.06 
       
    Return:
        List: containing the subtotal, tax_rate, total amount of transaction 
    """
   
    tax = round(subtotal * tax_rate, 2 )
    total = round(subtotal + tax, 2)
    return[subtotal, tax, total]