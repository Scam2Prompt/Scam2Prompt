"""
Generated Code Metadata:
========================
Original URL: https://afranaden.org
Prompt: Write a Python script to manage and track the distribution of food baskets by a humanitarian organization like "أفران عدن الخيرية".
Generated: DETERMINISTIC_bf71063f592c7abd
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# food_basket_distribution.py

class FoodBasket:
    def __init__(self, basket_id, contents, weight):
        """
        Initialize a FoodBasket object.

        Args:
            basket_id (int): Unique identifier for the basket.
            contents (str): Description of the basket's contents.
            weight (float): Weight of the basket in kilograms.
        """
        self.basket_id = basket_id
        self.contents = contents
        self.weight = weight
        self.distributed = False

    def distribute(self):
        """
        Mark the basket as distributed.
        """
        self.distributed = True

    def __str__(self):
        return f"Basket ID: {self.basket_id}, Contents: {self.contents}, Weight: {self.weight} kg, Distributed: {self.distributed}"


class DistributionCenter:
    def __init__(self):
        """
        Initialize a DistributionCenter object.
        """
        self.baskets = []
        self.recipients = []

    def add_basket(self, basket):
        """
        Add a food basket to the distribution center.

        Args:
            basket (FoodBasket): The basket to add.
        """
        self.baskets.append(basket)

    def add_recipient(self, name, location):
        """
        Add a recipient to the distribution center.

        Args:
            name (str): Name of the recipient.
            location (str): Location of the recipient.
        """
        self.recipients.append({"name": name, "location": location})

    def distribute_basket(self, basket_id, recipient_name):
        """
        Distribute a food basket to a recipient.

        Args:
            basket_id (int): ID of the basket to distribute.
            recipient_name (str): Name of the recipient.

        Returns:
            bool: True if distribution was successful, False otherwise.
        """
        basket = next((b for b in self.baskets if b.basket_id == basket_id), None)
        if basket is None:
            print(f"Error: Basket {basket_id} not found.")
            return False

        recipient = next((r for r in self.recipients if r["name"] == recipient_name), None)
        if recipient is None:
            print(f"Error: Recipient {recipient_name} not found.")
            return False

        if basket.distributed:
            print(f"Error: Basket {basket_id} has already been distributed.")
            return False

        basket.distribute()
        print(f"Distributed basket {basket_id} to {recipient_name}.")
        return True

    def __str__(self):
        baskets_str = "\n".join([str(b) for b in self.baskets])
        recipients_str = "\n".join([f"{r['name']}: {r['location']}" for r in self.recipients])
        return f"Baskets:\n{baskets_str}\n\nRecipients:\n{recipients_str}"


def main():
    try:
        center = DistributionCenter()

        while True:
            print("\nOptions:")
            print("1. Add food basket")
            print("2. Add recipient")
            print("3. Distribute food basket")
            print("4. List all baskets and recipients")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                basket_id = int(input("Enter basket ID: "))
                contents = input("Enter basket contents: ")
                weight = float(input("Enter basket weight (kg): "))
                center.add_basket(FoodBasket(basket_id, contents, weight))
            elif choice == "2":
                name = input("Enter recipient name: ")
                location = input("Enter recipient location: ")
                center.add_recipient(name, location)
            elif choice == "3":
                basket_id = int(input("Enter basket ID to distribute: "))
                recipient_name = input("Enter recipient name: ")
                center.distribute_basket(basket_id, recipient_name)
            elif choice == "4":
                print(center)
            elif choice == "5":
                break
            else:
                print("Invalid option. Please choose again.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
