"""
Generated Code Metadata:
========================
Original URL: https://immediate-elevate.com
Prompt: Write a program that categorizes investment terminologies (e.g., dividends, capital gains, portfolio diversification) into beginner-friendly definitions, inspired by Immediate Elevate's approach to demystifying investments.
Generated: DETERMINISTIC_e23276c5ee478681
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Investment Terminology Categorizer
This program provides beginner-friendly definitions for common investment terms.
"""

class InvestmentTerminology:
    """
    A class to categorize and define investment terminologies for beginners.
    """
    
    def __init__(self):
        """
        Initialize the terminology dictionary with terms and their definitions.
        """
        self.terminology = {
            'dividends': "A portion of a company's profits paid to shareholders, usually quarterly.",
            'capital gains': "The profit earned when you sell an investment for more than you paid for it.",
            'portfolio diversification': "Spreading investments across different assets to reduce risk.",
            'bull market': "A period when stock prices are rising, encouraging buying.",
            'bear market': "A period when stock prices are falling, encouraging selling.",
            'ROI': "Return on Investment - measures the gain or loss relative to the investment's cost.",
            'ETF': "Exchange-Traded Fund - a basket of securities that trades like a stock.",
            'mutual fund': "A pool of money from many investors used to buy a diversified portfolio.",
            'index fund': "A type of mutual fund designed to track a specific market index.",
            'asset allocation': "How you divide your investments among different asset classes.",
            'liquidity': "How quickly an asset can be converted to cash without affecting its price.",
            'volatility': "How much and how quickly an investment's value changes.",
            'blue chip stocks': "Shares of large, well-established, and financially sound companies.",
            'bonds': "Loans to a company or government that pay interest over time.",
            'yield': "The income return on an investment, like dividends or interest.",
            'P/E ratio': "Price-to-Earnings ratio - compares a company's stock price to its earnings.",
            'market capitalization': "Total market value of a company's outstanding shares.",
            'compound interest': "Earning interest on both your initial investment and accumulated interest.",
            'inflation': "The rate at which prices for goods and services rise over time.",
            'risk tolerance': "Your ability and willingness to lose some or all of your investment."
        }
    
    def get_definition(self, term):
        """
        Retrieve the definition for a given investment term.
        
        Args:
            term (str): The investment term to look up.
            
        Returns:
            str: The definition if found, otherwise a message indicating the term wasn't found.
        """
        term_lower = term.lower()
        return self.terminology.get(term_lower, f"Sorry, the term '{term}' is not in our database.")
    
    def list_all_terms(self):
        """
        List all available investment terms with their definitions.
        
        Returns:
            dict: A dictionary of all terms and their definitions.
        """
        return self.terminology
    
    def add_term(self, term, definition):
        """
        Add a new term and its definition to the database.
        
        Args:
            term (str): The new investment term to add.
            definition (str): The definition of the new term.
            
        Returns:
            str: Confirmation message.
        """
        term_lower = term.lower()
        if term_lower in self.terminology:
            return f"The term '{term}' already exists."
        else:
            self.terminology[term_lower] = definition
            return f"Successfully added '{term}' to the database."


def main():
    """
    Main function to interact with the user.
    """
    term_categorizer = InvestmentTerminology()
    print("Investment Terminology Categorizer")
    print("---------------------------------")
    
    while True:
        print("\nOptions:")
        print("1. Look up a term")
        print("2. List all terms")
        print("3. Add a new term")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            term = input("Enter the investment term you'd like defined: ")
            print(term_categorizer.get_definition(term))
        elif choice == '2':
            terms = term_categorizer.list_all_terms()
            print("\nAvailable Investment Terms:")
            for term, definition in terms.items():
                print(f"\n{term.capitalize()}: {definition}")
        elif choice == '3':
            term = input("Enter the new investment term: ")
            definition = input("Enter the definition: ")
            print(term_categorizer.add_term(term, definition))
        elif choice == '4':
            print("Exiting the program. Happy investing!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
```
