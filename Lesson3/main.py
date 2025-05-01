def divide(a: int, b: int):
    """Divides a by b with exception handling

    Args:
        a (int): dividend
        b (int): divisor

    Returns:
        float: quotient
    """

    try:
        quotient = a/b
    except ZeroDivisionError:
        print("You can't divide by zero")
    except TypeError:
        print("Parameter must be a number")
    else:
        return quotient

def main():
    results = []
    results.append(divide(5, "a"))
    results.append(divide(5, 0))
    results.append(divide(5, 2))
    for result in results:
        if result is not None:
            print(result)

    """
    Expected output:
    Parameter must be a number
    You can't divide by zero
    2.5
    """


if __name__ == "__main__":
    main()
