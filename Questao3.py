
def polynomial_to_string(polynomial):
    degrees = sorted(polynomial.keys(), reverse=True)
    terms = []
    for degree in degrees:
        coefficient = polynomial[degree]
        sign = "+" if coefficient >= 0 else "-"
        if abs(coefficient) != 1 or degree == 0:
            term = f"{abs(coefficient)}"  # convert coefficient to string
        else:
            term = ""
        if degree > 1:
            term += f"x^{degree}"
        elif degree == 1:
            term += "x"
        term = sign + term
        terms.append(term)
    return "".join(terms).lstrip("+")  # concatenate terms and remove "+" sign from the first term
