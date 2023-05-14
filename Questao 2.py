def string_to_polynomial(string):
    polynomial = {}
    terms = string.split("+")  # split the string into terms separated by "+"
    for term in terms:
        if "-" in term:  # if the term contains a "-", split it into coefficient and variable parts
            coefficient, variable = term.split("-")
            coefficient = int(coefficient)  # convert coefficient to integer
            coefficient *= -1  # negate the coefficient
            variable = "-" + variable  # add the "-" back to the variable part
        else:  # if the term does not contain a "-", split it into coefficient and variable parts
            coefficient, variable = term.split("x")
            coefficient = int(coefficient)  # convert coefficient to integer
        if variable == "":  # if the term is a constant, set the degree to 0
            degree = 0
        else:
            degree = int(variable[2:])  # extract the degree from the variable part
        polynomial[degree] = coefficient
    return polynomial
