from transpiler import parse_macro_line
from interpreter import execute_macro

def test_macro_execution():
    # Example macro line
    macro_line = "click\t1000 400"

    # Parse the macro line
    parsed_macro = parse_macro_line(macro_line)
    print("Parsed Macro:", parsed_macro)

    # Execute the macro
    execute_macro(parsed_macro)

if __name__ == "__main__":
    test_macro_execution()
