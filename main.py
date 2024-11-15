import struct


def float_to_ieee754(value: float, precision: str = "single") -> str:
    """Convert a float to IEEE 754 binary representation.

    Args:
        value (float): The input float value.
        precision (str): Precision type ('single' or 'double').

    Returns:
        str: The IEEE 754 binary representation.
    """
    if precision == "single":
        packed = struct.pack('>f', value)  # Pack as 32-bit float
        num_bits = 32
    elif precision == "double":
        packed = struct.pack('>d', value)  # Pack as 64-bit double
        num_bits = 64
    else:
        raise ValueError("Precision must be 'single' or 'double'.")

    binary_repr = ''.join(f"{byte:08b}" for byte in packed)  # Convert to binary string
    print(binary_repr)
    # Split into components
    if num_bits == 32:
        sign = binary_repr[0]
        exponent = binary_repr[1:9]
        mantissa = binary_repr[9:]
    elif num_bits == 64:
        sign = binary_repr[0]
        exponent = binary_repr[1:12]
        mantissa = binary_repr[12:]

    print(f"Sign: {sign}, Exponent: {exponent}, Mantissa: {mantissa}")


if __name__ == "__main__":
    num = float(input("Enter a float/double value: "))
    prec = input("Enter precision (single/double): ").strip().lower()
    print(f"IEEE 754 representation ({prec} precision):")
    float_to_ieee754(num, prec)
