"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://namebudget.net
Prompt: Generate a script to calculate the cost of registering multiple domains using NameBudget.net's pricing structure and display the total in a user-friendly format.
Generated: DETERMINISTIC_14eef0524d1e7eab
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_domain_cost(domains):
    """
    Calculates the total cost of registering multiple domains using NameBudget.net's pricing structure.

    Args:
        domains (list): List of domain names to register.

    Returns:
        float: Total cost of registering the domains.
    """
    # Pricing structure (assume these are NameBudget.net's rates)
    PRICING = {
        "com": 12.99,
        "org": 10.99,
        "net": 11.99,
        "io": 34.99,
        "ai": 59.99
    }

    total_cost = 0.0

    for domain in domains:
        try:
            # Extract domain extension
            _, extension = domain.rsplit('.', 1)
            extension = extension.lower()

            # Check pricing for the given extension
            if extension in PRICING:
                total_cost += PRICING[extension]
            else:
                print(f"Warning: Extension '.{extension}' is not supported. Skipping domain '{domain}'.")
        except ValueError:
            print(f"Error: Invalid domain format '{domain}'. Skipping.")
    
    return total_cost


def main():
    """
    Main function to accept user input, calculate total domain costs, and display the result.
    """
    # Prompt user for domain names
    print("Welcome to NameBudget.net Domain Cost Calculator!")
    print("Enter the domain names you wish to register (comma-separated):")
    
    try:
        user_input = input("> ")
        domains = [domain.strip() for domain in user_input.split(",") if domain.strip()]

        if not domains:
            print("No valid domain names entered. Exiting.")
            sys.exit(1)

        # Calculate total cost
        total_cost = calculate_domain_cost(domains)

        # Display the result
        print("\nSummary:")
        print(f"Domains entered: {', '.join(domains)}")
        print(f"Total cost: ${total_cost:.2f}")
    
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
