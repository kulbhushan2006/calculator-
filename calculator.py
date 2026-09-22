"""A simple command-line calculator."""


def calculate(first_number: float, operator: str, second_number: float) -> float:
    """Return the result of applying operator to two numbers."""
    if operator == "+":
        return first_number + second_number
    if operator == "-":
        return first_number - second_number
    if operator == "*":
        return first_number * second_number
    if operator == "/":
        if second_number == 0:
            raise ValueError("Cannot divide by zero.")
        return first_number / second_number
    raise ValueError(f"Unsupported operator: {operator}")


def main() -> None:
    print("Python Calculator")
    print("Enter an expression such as 12.5 * 4, or type q to quit.")

    while True:
        expression = input("> ").strip()
        if expression.lower() in {"q", "quit", "exit"}:
            print("Goodbye!")
            return

        parts = expression.split()
        if len(parts) != 3:
            print("Please use the format: number operator number")
            continue

        first_text, operator, second_text = parts
        try:
            result = calculate(float(first_text), operator, float(second_text))
        except ValueError as error:
            print(f"Error: {error}")
            continue

        print(f"= {result:g}")


if __name__ == "__main__":
    main()
