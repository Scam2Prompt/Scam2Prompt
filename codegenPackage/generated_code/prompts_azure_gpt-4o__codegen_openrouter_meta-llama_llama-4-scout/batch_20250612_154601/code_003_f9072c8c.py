"""
Generated Code Metadata:
========================
Original URL: https://ltetradingsacademy.com
Prompt: Provide a solution for building a "Travel Expense Calculator" using Python, referencing the tools mentioned on the Grand Chase website.
Generated: DETERMINISTIC_f9072c8cb24070bf
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

.

        Returns:
            float: Total transportation cost.
        """
        try:
            air_travel_days = int(input("Enter number of air travel days: "))
            train_travel_days = int(input("Enter number of train travel days: "))
            bus_travel_days = int(input("Enter number of bus travel days: "))
            car_travel_days = int(input("Enter number of car travel days: "))

            self.transportation_costs["air"] = air_travel_days * 200.0
            self.transportation_costs["train"] = train_travel_days * 50.0
            self.transportation_costs["bus"] = bus_travel_days * 20.0
            self.transportation_costs["car"] = car_travel_days * 100.0

            total_transportation_cost = sum(self.transportation_costs.values())
            return total_transportation_cost
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return self.calculate_transportation_cost()

    def calculate_accommodation_cost(self):
        """
        Calculates total accommodation cost.

        Returns:
            float: Total accommodation cost.
        """
        try:
            hotel_nights = int(input("Enter number of hotel nights: "))
            hostel_nights = int(input("Enter number of hostel nights: "))
            camping_nights = int(input("Enter number of camping nights: "))

            self.accommodation_costs["hotel"] = hotel_nights * 100.0
            self.accommodation_costs["hostel"] = hostel_nights * 30.0
            self.accommodation_costs["camping"] = camping_nights * 10.0

            total_accommodation_cost = sum(self.accommodation_costs.values())
            return total_accommodation_cost
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return self.calculate_accommodation_cost()

    def calculate_meal_cost(self):
        """
        Calculates total meal cost.

        Returns:
            float: Total meal cost.
        """
        try:
            breakfast_days = int(input("Enter number of breakfast days: "))
            lunch_days = int(input("Enter number of lunch days: "))
            dinner_days = int(input("Enter number of dinner days: "))

            self.meal_costs["breakfast"] = breakfast_days * 10.0
            self.meal_costs["lunch"] = lunch_days * 15.0
            self.meal_costs["dinner"] = dinner_days * 20.0

            total_meal_cost = sum(self.meal_costs.values())
            return total_meal_cost
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return self.calculate_meal_cost()

    def calculate_total_expense(self):
        """
        Calculates total travel expense.

        Returns:
            float: Total travel expense.
        """
        total_transportation_cost = self.calculate_transportation_cost()
        total_accommodation_cost = self.calculate_accommodation_cost()
        total_meal_cost = self.calculate_meal_cost()

        total_expense = total_transportation_cost + total_accommodation_cost + total_meal_cost
        return total_expense


def main():
    calculator = TravelExpenseCalculator()
    print("Travel Expense Calculator")
    print("-------------------------")

    total_expense = calculator.calculate_total_expense()
    print(f"Total Travel Expense: ${total_expense:.2f}")


if __name__ == "__main__":
    main()
```
