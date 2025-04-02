import math

def main():
    try:
      
        num = float(input("Enter a number: "))

        # Calculate square root
        sqrt_result = math.sqrt(num)
        print(f"Square root of {num} is {sqrt_result}")

        # Calculate natural logarithm
        log_result = math.log(num)
        print(f"Natural logarithm (ln) of {num} is {log_result}")

        # Calculate sine (assuming num is in radians)
        sin_result = math.sin(num)
        print(f"Sine of {num} radians is {sin_result}")

    except ValueError as e:
        print(f"Error: {e}. Please enter a positive number for square root and logarithm calculations.")

if __name__ == "__main__":
    main()
