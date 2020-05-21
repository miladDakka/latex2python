from sympy.parsing.latex import parse_latex

# This class takes a latex formula and a defined relationship symbol
# as inputs and returns that same formula in Python friendly format,
# attempting to ease new Python users that may have LaTeX experience
# into the world of Python!
class LaTeX2Python:
    def __init__(self, formula):
        self.formula = formula

    # This function does the brunt work of converting tex 
    # expressions to Python suitable code snippets
    def latex_to_python(self, formula):
        try:
            return(parse_latex(formula))
        except:
            pass



