def first_step(poly_str):
    # Inicializa o dicionário vazio
    poly_dict = {}
    # Separa a string pelos sinais de adição
    monomials = poly_str.split("+")
    for monomial in monomials:
        # Separa o coeficiente e o grau do monômio
        parts = monomial.strip().split("x^")
        if len(parts) == 1:
            # Se não houver um grau especificado, assume que é 1
            coef_str = parts[0].strip()
            try:
                coef = float(coef_str)
            except ValueError:
                continue
            exp = 1
        else:
            # Converte o coeficiente e o grau em floats
            coef_str, exp_str = map(str.strip, parts)
            try:
                coef = float(coef_str)
                exp = float(exp_str)
            except ValueError:
                continue
        # Adiciona o monômio ao dicionário
        poly_dict[int(exp)] = coef
    return poly_dict
