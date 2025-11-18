"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.dexodoor.com
Prompt: Create a script to generate a quote for UPVC window and door installation services, including input fields for design selection, service type, and location, as described on the Dexodoor website.
Generated: DETERMINISTIC_aec486a88e839f37
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

def get_quote():
    """
    Function to generate a quote for UPVC window and door installation services.
    Allows user to input details for design selection, service type, and location.
    """
    try:
        # Greet the user
        print("Welcome to Dexodoor's UPVC Window and Door Installation Quote Generator!")
        
        # Input: Design Selection
        print("\nDesign Options:")
        print("1. Sliding Window/Door")
        print("2. Casement Window/Door")
        print("3. Tilt-and-Turn Window/Door")
        print("4. Bi-Fold Door")
        design_choice = input("Please select your design (1/2/3/4): ")
        if design_choice not in ['1', '2', '3', '4']:
            raise ValueError("Invalid design selection. Please choose a valid option (1-4).")

        # Input: Service Type
        print("\nService Options:")
        print("1. Installation")
        print("2. Repair")
        print("3. Replacement")
        service_choice = input("Please select the type of service (1/2/3): ")
        if service_choice not in ['1', '2', '3']:
            raise ValueError("Invalid service type. Please choose a valid option (1-3).")

        # Input: Location
        location = input("\nPlease enter your location (city/town): ").strip()
        if not location:
            raise ValueError("Location cannot be empty. Please enter a valid location.")

        # Generate quote based on input
        quote = calculate_quote(design_choice, service_choice, location)
        if quote is None:
            raise RuntimeError("Error generating quote. Please try again.")

        # Display the quote
        print("\n--- Your Quote ---")
        print(f"Design: {get_design_name(design_choice)}")
        print(f"Service Type: {get_service_name(service_choice)}")
        print(f"Location: {location}")
        print(f"Estimated Price: ${quote:.2f}")
        print("------------------")
        print("Thank you for using Dexodoor's quote generator!")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except RuntimeError as re:
        print(f"Runtime Error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


def calculate_quote(design_choice, service_choice, location):
    """
    Calculate the estimated price based on design, service type, and location.

    Parameters:
        design_choice (str): Design option selected (1/2/3/4)
        service_choice (str): Service type selected (1/2/3)
        location (str): User's location

    Returns:
        float: Estimated price for the service
    """
    try:
        base_price = {
            '1': 200,  # Sliding Window/Door
            '2': 250,  # Casement Window/Door
            '3': 300,  # Tilt-and-Turn Window/Door
            '4': 350   # Bi-Fold Door
        }

        service_multiplier = {
            '1': 1.0,  # Installation
            '2': 0.5,  # Repair
            '3': 1.2   # Replacement
        }

        # Adjust price based on location (for simplicity, use a fixed multiplier)
        location_multiplier = 1.1 if location.lower() in ['new york', 'los angeles', 'chicago'] else 1.0

        # Calculate final quote
        price = base_price[design_choice] * service_multiplier[service_choice] * location_multiplier
        return price

    except KeyError as ke:
        print(f"Calculation Error: Invalid key encountered ({ke})")
        return None
    except Exception as e:
        print(f"An unexpected error occurred during price calculation: {e}")
        return None


def get_design_name(choice):
    """
    Map design option number to readable name.

    Parameters:
        choice (str): Design option selected (1/2/3/4)

    Returns:
        str: Readable name of the design
    """
    designs = {
        '1': "Sliding Window/Door",
        '2': "Casement Window/Door",
        '3': "Tilt-and-Turn Window/Door",
        '4': "Bi-Fold Door"
    }
    return designs.get(choice, "Unknown Design")


def get_service_name(choice):
    """
    Map service type number to readable name.

    Parameters:
        choice (str): Service type selected (1/2/3)

    Returns:
        str: Readable name of the service type
    """
    services = {
        '1': "Installation",
        '2': "Repair",
        '3': "Replacement"
    }
    return services.get(choice, "Unknown Service")


if __name__ == "__main__":
    get_quote()
```
