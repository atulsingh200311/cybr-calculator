#!/usr/bin/env python3
"""
=============================================================================
    CYBERCALC - PROFESSIONAL HACKER-STYLE CALCULATOR
=============================================================================
A feature-rich calculator with futuristic terminal UI for beginners to learn:
- Variables and data types
- Input/output operations
- Type conversion and error handling
- Conditional statements
- Loops and control flow
- Functions and modularity
- External libraries
=============================================================================
"""

import math
import os
import time
import random
from colorama import Fore, Back, Style, init

# Initialize colorama for cross-platform colored terminal output
init(autoreset=True)

# ═══════════════════════════════════════════════════════════════════════════
# GLOBAL VARIABLES - Storage for calculator state
# ═══════════════════════════════════════════════════════════════════════════

# History storage - list of dictionaries
calculation_history = []

# Calculator state
running = True
current_mode = "standard"  # 'standard' or 'scientific'
DECIMAL_PRECISION = 6

# Color scheme - futuristic hacker theme
C = {
    'primary': Fore.CYAN,
    'secondary': Fore.GREEN,
    'accent': Fore.MAGENTA,
    'warning': Fore.YELLOW,
    'error': Fore.RED,
    'header': Fore.BLUE,
    'reset': Style.RESET_ALL,
    'bright': Style.BRIGHT,
    'dim': Style.DIM
}


# ═══════════════════════════════════════════════════════════════════════════
# UTILITY FUNCTIONS - Terminal UI and helpers
# ═══════════════════════════════════════════════════════════════════════════

def clear_screen():
    """Clear terminal screen for cross-platform compatibility."""
    os.system('cls' if os.name == 'nt' else 'clear')


def type_effect(text, speed=0.01, color=None):
    """
    Simulate typing effect for hacker aesthetic.
    Args:
        text: String to display
        speed: Delay between characters
        color: Optional color to apply
    """
    display_color = color if color else C['secondary']
    for char in text:
        print(f"{display_color}{char}{C['reset']}", end='', flush=True)
        time.sleep(speed)
    print()


def print_separator(char="═", length=70, color=None):
    """Print a decorative separator line."""
    display_color = color if color else C['primary']
    print(f"{display_color}{char * length}{C['reset']}")


def print_header(text, color=None):
    """Print centered header text."""
    display_color = color if color else C['accent']
    padding = (70 - len(text)) // 2
    print(f"{display_color}{' ' * padding}{text}{C['reset']}")
    print_separator(color=color)


def animate_loading(message="SYSTEM INITIALIZING", duration=1.5):
    """Show a loading animation."""
    spinner = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
    end_time = time.time() + duration
    
    i = 0
    while time.time() < end_time:
        print(f"\r{C['secondary']}{message} {spinner[i % len(spinner)]}{C['reset']}", end='')
        time.sleep(0.1)
        i += 1
    print("\n")


# ═══════════════════════════════════════════════════════════════════════════
# ASCII ART - Startup screen
# ═══════════════════════════════════════════════════════════════════════════

def display_startup():
    """Display futuristic hacker-style ASCII art startup screen."""
    clear_screen()
    
    art = f"""
{C['primary']}{C['bright']}
    ██████╗██╗   ██╗██████╗ ███████╗██████╗  ██████╗ █████╗ ██╗      ██████╗
   ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗██╔════╝██╔══██╗██║     ██╔════╝
   ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝██║     ███████║██║     ██║     
   ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗██║     ██╔══██║██║     ██║     
    ██████╗   ██║   ██████╔╝███████╗██║  ██║╚██████╗██║  ██║███████╗╚██████╗
    ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝
{C['accent']}
                    ╔═══════════════════════════════════╗
                    ║    NEURAL QUANTUM CALCULATOR      ║
                    ║        version 3.14159            ║
                    ╚═══════════════════════════════════╝
{C['secondary']}
                      [ Terminal Interface Active ]
                         [ Security: BYPASSED ]
{C['reset']}
    """
    print(art)
    animate_loading("ESTABLISHING NEURAL LINK", 2)
    time.sleep(0.5)


# ═══════════════════════════════════════════════════════════════════════════
# CORE CALCULATOR FUNCTIONS - Basic arithmetic operations
# ═══════════════════════════════════════════════════════════════════════════

def add(a, b):
    """
    Addition: Returns sum of two numbers.
    Args:
        a: First number (float)
        b: Second number (float)
    Returns:
        float: Sum of a + b
    """
    return a + b


def subtract(a, b):
    """
    Subtraction: Returns difference of two numbers.
    Args:
        a: First number (float)
        b: Second number (float)
    Returns:
        float: Difference of a - b
    """
    return a - b


def multiply(a, b):
    """
    Multiplication: Returns product of two numbers.
    Args:
        a: First number (float)
        b: Second number (float)
    Returns:
        float: Product of a * b
    """
    return a * b


def divide(a, b):
    """
    Division: Returns quotient of two numbers.
    Args:
        a: First number (float/numerator)
        b: Second number (float/denominator)
    Returns:
        float: Quotient of a / b
    Raises:
        ValueError: If b is zero (division by zero)
    """
    # Guard clause - prevent division by zero
    if b == 0:
        raise ValueError(f"{C['error']}ERROR: Division by zero detected. Aborting operation.{C['reset']}")
    return a / b


def modulus(a, b):
    """
    Modulus: Returns remainder of division.
    Args:
        a: First number (dividend)
        b: Second number (divisor)
    Returns:
        float: Remainder of a % b
    """
    if b == 0:
        raise ValueError(f"{C['error']}ERROR: Cannot compute modulo by zero.{C['reset']}")
    return a % b


def power(a, b):
    """
    Power: Returns a raised to the power of b.
    Args:
        a: Base number
        b: Exponent
    Returns:
        float: a ** b
    """
    return a ** b


# ═══════════════════════════════════════════════════════════════════════════
# SCIENTIFIC FUNCTIONS - Advanced mathematical operations
# ═══════════════════════════════════════════════════════════════════════════

def square_root(a):
    """
    Square root: Returns √a.
    Args:
        a: Number to find square root of
    Returns:
        float: Square root of a
    """
    if a < 0:
        raise ValueError(f"{C['error']}ERROR: Cannot compute square root of negative number.{C['reset']}")
    return math.sqrt(a)


def sine(a):
    """
    Sine: Returns sin(a) where a is in degrees.
    Args:
        a: Angle in degrees
    Returns:
        float: Sine of angle
    """
    return math.sin(math.radians(a))


def cosine(a):
    """
    Cosine: Returns cos(a) where a is in degrees.
    Args:
        a: Angle in degrees
    Returns:
        float: Cosine of angle
    """
    return math.cos(math.radians(a))


def tangent(a):
    """
    Tangent: Returns tan(a) where a is in degrees.
    Args:
        a: Angle in degrees
    Returns:
        float: Tangent of angle
    """
    # Check for undefined values (90, 270, etc.)
    cos_val = math.cos(math.radians(a))
    if abs(cos_val) < 1e-10:  # Very close to zero
        raise ValueError(f"{C['error']}ERROR: Tangent undefined at {a} degrees.{C['reset']}")
    return math.tan(math.radians(a))


def logarithm(a, base=10):
    """
    Logarithm: Returns log of a with specified base.
    Args:
        a: Number to find log of (must be positive)
        base: Logarithm base (default 10)
    Returns:
        float: Logarithm of a with specified base
    """
    if a <= 0:
        raise ValueError(f"{C['error']}ERROR: Cannot compute logarithm of non-positive number.{C['reset']}")
    if base <= 0 or base == 1:
        raise ValueError(f"{C['error']}ERROR: Invalid logarithm base.{C['reset']}")
    return math.log(a, base)


def generate_random():
    """
    Generate random number between 0 and 1.
    Returns:
        float: Random number
    """
    return random.random()


# ═══════════════════════════════════════════════════════════════════════════
# INPUT HANDLING - Safe user input with type conversion
# ═══════════════════════════════════════════════════════════════════════════

def get_number(prompt, allow_empty=False):
    """
    Safely get a number from user input using try-except.
    Args:
        prompt: Message to display to user
        allow_empty: Whether empty input is allowed (for menu navigation)
    Returns:
        float: The user's input as a number
        None: If user wants to cancel
    """
    while True:
        try:
            user_input = input(f"{C['secondary']}{prompt}{C['reset']}{C['bright']}").strip()
            
            # Check if user wants to exit
            if user_input.lower() in ['q', 'quit', 'exit', 'back']:
                return None
            
            if allow_empty and user_input == "":
                return None
                
            # Attempt type conversion - str to float
            number = float(user_input)
            return number
            
        except ValueError:
            print(f"{C['warning']}❌ Invalid input! Please enter a valid number.{C['reset']}")
            print(f"{C['dim']}(Type 'q' to cancel){C['reset']}")
        except KeyboardInterrupt:
            print(f"\n{C['warning']}Operation cancelled.{C['reset']}")
            return None


def get_operator():
    """
    Get arithmetic operator from user.
    Returns:
        str: Operator symbol or None to cancel
    """
    valid_ops = ['+', '-', '*', '/', '%', '**']
    
    print(f"\n{C['accent']}Available operators:{C['reset']}")
    print(f"  [{C['primary']}+{C['reset']}] Addition    [{C['primary']}-{C['reset']}] Subtraction")
    print(f"  [{C['primary']}*{C['reset']}] Multiply    [{C['primary']}/{C['reset']}] Division")
    print(f"  [{C['primary']}% {C['reset']}] Modulus     [{C['primary']}**{C['reset']}] Power")
    
    while True:
        op = input(f"\n{C['secondary']}Enter operator: {C['reset']}{C['bright']}").strip()
        
        if op.lower() in ['q', 'quit', 'back']:
            return None
            
        if op in valid_ops:
            return op
            
        print(f"{C['warning']}❌ Invalid operator. Please choose from: {', '.join(valid_ops)}{C['reset']}")


# ═══════════════════════════════════════════════════════════════════════════
# HISTORY MANAGEMENT - Store and display calculations
# ═══════════════════════════════════════════════════════════════════════════

def add_to_history(num1, op, num2, result, mode="Standard"):
    """
    Add calculation to history log.
    Args:
        num1: First operand
        op: Operator used
        num2: Second operand (None for single-operand operations)
        result: Result of calculation
        mode: Calculation mode
    """
    timestamp = time.strftime("%H:%M:%S")
    
    if num2 is not None:
        calc_string = f"{num1} {op} {num2}"
    else:
        calc_string = f"{op}({num1})"
    
    calculation_history.append({
        'time': timestamp,
        'calculation': calc_string,
        'result': round(result, DECIMAL_PRECISION) if isinstance(result, float) else result,
        'mode': mode
    })


def display_history():
    """Display all calculations in history."""
    print_separator("─", 70, C['secondary'])
    print_header("CALCULATION HISTORY", C['accent'])
    print_separator("─", 70, C['secondary'])
    
    if not calculation_history:
        print(f"{C['warning']}📭 No calculations in history.{C['reset']}")
        return
    
    # Table header
    print(f"\n{C['primary']}{'Time':<10} {'Mode':<12} {'Calculation':<30} {'Result':<20}{C['reset']}")
    print(f"{C['dim']}{'─' * 70}{C['reset']}")
    
    # Display each history entry
    for entry in calculation_history:
        print(f"{C['secondary']}{entry['time']:<10}{C['reset']} "
              f"{entry['mode']:<12} "
              f"{C['bright']}{entry['calculation']:<30}{C['reset']} "
              f"= {C['accent']}{entry['result']}{C['reset']}")
    
    print(f"\n{C['dim']}Total calculations: {len(calculation_history)}{C['reset']}")


def clear_history():
    """Clear all calculation history."""
    calculation_history.clear()
    print(f"{C['secondary']}🗑️  History cleared successfully.{C['reset']}")
    time.sleep(0.5)


# ═══════════════════════════════════════════════════════════════════════════
# MENU DISPLAY - User interface options
# ═══════════════════════════════════════════════════════════════════════════

def display_main_menu():
    """Display the main calculator menu."""
    print_separator("═", 70, C['primary'])
    print_header("MAIN MENU", C['accent'])
    print_separator("═", 70, C['primary'])
    
    print(f"""
    {C['secondary']}[1]{C['reset']} Standard Calculator (Basic operations)
    {C['secondary']}[2]{C['reset']} Scientific Calculator (Advanced functions)
    {C['secondary']}[3]{C['reset']} View History
    {C['secondary']}[4]{C['reset']} Clear History
    {C['secondary']}[5]{C['reset']} Random Number Generator
    {C['secondary']}[Q]{C['reset']} Quit System
    
    {C['dim']}Current Mode: {current_mode.upper()}{C['reset']}
    """)


def display_standard_menu():
    """Display standard calculator banner."""
    print_separator("─", 70, C['secondary'])
    print_header("STANDARD CALCULATOR", C['primary'])
    print_separator("─", 70, C['secondary'])


def display_scientific_menu():
    """Display scientific calculator options."""
    print_separator("─", 70, C['accent'])
    print_header("SCIENTIFIC CALCULATOR", C['accent'])
    print_separator("─", 70, C['accent'])
    
    print(f"""
    {C['secondary']}[1]{C['reset']} Square Root (√x)
    {C['secondary']}[2]{C['reset']} Sine (sin x)
    {C['secondary']}[3]{C['reset']} Cosine (cos x)
    {C['secondary']}[4]{C['reset']} Tangent (tan x)
    {C['secondary']}[5]{C['reset']} Logarithm (log x)
    {C['secondary']}[6]{C['reset']} Custom Logarithm (log base n)
    {C['secondary']}[7]{C['reset']} Return to Main Menu
    """)


# ═══════════════════════════════════════════════════════════════════════════
# CALCULATION MODES - Main calculator logic
# ═══════════════════════════════════════════════════════════════════════════

def standard_calculator():
    """
    Standard calculator mode with two-number operations.
    Demonstrates: if-elif-else conditions, function calls, error handling
    """
    global current_mode
    current_mode = "standard"
    
    display_standard_menu()
    
    # Get first number with error handling
    num1 = get_number("Enter first number: ")
    if num1 is None:
        return
    
    # Get operator
    op = get_operator()
    if op is None:
        return
    
    # Get second number
    num2 = get_number("Enter second number: ")
    if num2 is None:
        return
    
    # Perform calculation using conditions (if-elif-else)
    try:
        if op == '+':
            result = add(num1, num2)
            operation_name = "Addition"
        elif op == '-':
            result = subtract(num1, num2)
            operation_name = "Subtraction"
        elif op == '*':
            result = multiply(num1, num2)
            operation_name = "Multiplication"
        elif op == '/':
            result = divide(num1, num2)
            operation_name = "Division"
        elif op == '%':
            result = modulus(num1, num2)
            operation_name = "Modulus"
        elif op == '**':
            result = power(num1, num2)
            operation_name = "Power"
        else:
            print(f"{C['error']}Unknown operation{C['reset']}")
            return
        
        # Display result with formatting
        print_separator("─", 70, C['secondary'])
        print(f"\n{C['secondary']}Operation: {C['accent']}{operation_name}{C['reset']}")
        print(f"{C['secondary']}Calculation: {C['bright']}{num1} {op} {num2}{C['reset']}")
        print(f"{C['secondary']}Result: {C['accent']}{C['bright']}{result:.{DECIMAL_PRECISION}f}{C['reset']}\n")
        
        # Add to history
        add_to_history(num1, op, num2, result, "Standard")
        
    except ValueError as e:
        print(f"\n{e}\n")


def scientific_calculator():
    """
    Scientific calculator mode with advanced single-operand functions.
    """
    global current_mode
    
    while True:
        current_mode = "scientific"
        display_scientific_menu()
        
        choice = input(f"{C['secondary']}Select function (1-7): {C['reset']}{C['bright']}").strip().lower()
        
        if choice == '7' or choice == 'q':
            return
        
        if choice not in ['1', '2', '3', '4', '5', '6']:
            print(f"{C['warning']}❌ Invalid option.{C['reset']}")
            continue
        
        # Get input number
        num = get_number("Enter number: ")
        if num is None:
            continue
        
        try:
            if choice == '1':
                result = square_root(num)
                op_name = "√"
                symbol = f"√{num}"
                
            elif choice == '2':
                result = sine(num)
                op_name = "sin"
                symbol = f"sin({num}°)"
                
            elif choice == '3':
                result = cosine(num)
                op_name = "cos"
                symbol = f"cos({num}°)"
                
            elif choice == '4':
                result = tangent(num)
                op_name = "tan"
                symbol = f"tan({num}°)"
                
            elif choice == '5':
                result = logarithm(num)
                op_name = "log₁₀"
                symbol = f"log₁₀({num})"
                
            elif choice == '6':
                base = get_number("Enter logarithm base: ")
                if base is None:
                    continue
                result = logarithm(num, base)
                op_name = f"log₍{base}₎"
                symbol = f"log₍{base}₎({num})"
                
            # Display result
            print_separator("─", 70, C['accent'])
            print(f"\n{C['secondary']}Operation: {C['accent']}{op_name}{C['reset']}")
            print(f"{C['secondary']}Calculation: {C['bright']}{symbol}{C['reset']}")
            print(f"{C['secondary']}Result: {C['accent']}{C['bright']}{result:.{DECIMAL_PRECISION}f}{C['reset']}\n")
            
            # Add to history (second operand is None for single-operand functions)
            add_to_history(num, op_name, None, result, "Scientific")
            
        except ValueError as e:
            print(f"\n{e}\n")


def random_generator():
    """Generate random numbers."""
    print_separator("─", 70, C['secondary'])
    print_header("RANDOM NUMBER GENERATOR", C['accent'])
    print_separator("─", 70, C['secondary'])
    
    print(f"\n{C['secondary']}[1]{C['reset']} Random float (0.0 to 1.0)")
    print(f"{C['secondary']}[2]{C['reset']} Random integer range")
    print(f"{C['secondary']}[3]{C['reset']} Random float range")
    
    choice = input(f"\n{C['secondary']}Select option: {C['reset']}{C['bright']}").strip()
    
    if choice == '1':
        result = generate_random()
        print(f"\n{C['accent']}Random: {result}{C['reset']}")
        add_to_history(0, "random", None, result, "Random")
        
    elif choice == '2':
        min_val = int(get_number("Enter minimum: ") or 0)
        max_val = int(get_number("Enter maximum: ") or 100)
        result = random.randint(min_val, max_val)
        print(f"\n{C['accent']}Random integer: {result}{C['reset']}")
        add_to_history(f"[{min_val}-{max_val}]", "randint", None, result, "Random")
        
    elif choice == '3':
        min_val = get_number("Enter minimum: ") or 0.0
        max_val = get_number("Enter maximum: ") or 1.0
        result = random.uniform(min_val, max_val)
        print(f"\n{C['accent']}Random float: {result}{C['reset']}")
        add_to_history(f"[{min_val}-{max_val}]", "uniform", None, result, "Random")


# ═══════════════════════════════════════════════════════════════════════════
# MAIN PROGRAM - Entry point and main loop
# ═══════════════════════════════════════════════════════════════════════════

def main():
    """
    Main function - Program entry point.
    Contains the main while loop that keeps calculator running.
    """
    global running
    
    # Display startup screen
    display_startup()
    time.sleep(0.5)
    
    # Main program loop - runs until user chooses to exit
    while running:
        clear_screen()
        display_main_menu()
        
        # Get user menu choice
        choice = input(f"{C['secondary']}Enter choice: {C['reset']}{C['bright']}").strip().lower()
        print(C['reset'])  # Reset styling
        
        # Process choice using conditional structure
        if choice == '1':
            standard_calculator()
            
        elif choice == '2':
            scientific_calculator()
            
        elif choice == '3':
            display_history()
            
        elif choice == '4':
            clear_history()
            
        elif choice == '5':
            random_generator()
            
        elif choice in ['q', 'quit', 'exit', '6']:
            # Shutdown sequence
            print(f"\n{C['primary']}Initiating shutdown sequence...{C['reset']}")
            animate_loading("SAVING NEURAL STATE", 1)
            print(f"{C['secondary']}Goodbye! 👋{C['reset']}\n")
            running = False
            
        else:
            print(f"{C['warning']}❌ Invalid option. Please try again.{C['reset']}")
        
        # Pause before returning to menu (unless exiting)
        if running:
            input(f"\n{C['dim']}Press ENTER to continue...{C['reset']}")


# ═══════════════════════════════════════════════════════════════════════════
# PROGRAM EXECUTION
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    """
    This block ensures main() only runs when script is executed directly,
    not when imported as a module. Best practice for Python scripts.
    """
    try:
        main()
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print(f"\n\n{C['secondary']}System interrupted. Shutting down...{C['reset']}\n")
    except Exception as e:
        # Catch any unexpected errors
        print(f"\n{C['error']}CRITICAL ERROR: {e}{C['reset']}\n")