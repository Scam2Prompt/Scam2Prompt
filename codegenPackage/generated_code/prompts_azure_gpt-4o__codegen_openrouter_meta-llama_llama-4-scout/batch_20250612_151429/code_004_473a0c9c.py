"""
Generated Code Metadata:
========================
Original URL: https://cabinet-customs.com.ua
Prompt: Generate a program to calculate the import costs of a passenger car using the "Automobile Calculator" feature described on the Single Window Portal.
Generated: DETERMINISTIC_473a0c9cadb697c0
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import math

class AutomobileCalculator:
    """
    Calculates the import costs of a passenger car.
    """

    def __init__(self, 
                 vehicle_value: float, 
                 freight_cost: float, 
                 insurance_cost: float, 
                 customs_duty_rate: float, 
                 gst_rate: float, 
                 pst_rate: float):
        """
        Initializes the AutomobileCalculator.

        Args:
        - vehicle_value (float): The value of the vehicle.
        - freight_cost (float): The freight cost of the vehicle.
        - insurance_cost (float): The insurance cost of the vehicle.
        - customs_duty_rate (float): The customs duty rate.
        - gst_rate (float): The GST rate.
        - pst_rate (float): The PST rate.
        """

        self.vehicle_value = vehicle_value
        self.freight_cost = freight_cost
        self.insurance_cost = insurance_cost
        self.customs_duty_rate = customs_duty_rate / 100  # Convert to decimal
        self.gst_rate = gst_rate / 100  # Convert to decimal
        self.pst_rate = pst_rate / 100  # Convert to decimal

    def calculate_customs_value(self) -> float:
        """
        Calculates the customs value of the vehicle.

        Returns:
        - float: The customs value.
        """
        return self.vehicle_value + self.freight_cost + self.insurance_cost

    def calculate_customs_duty(self) -> float:
        """
        Calculates the customs duty.

        Returns:
        - float: The customs duty.
        """
        customs_value = self.calculate_customs_value()
        return customs_value * self.customs_duty_rate

    def calculate_gst(self) -> float:
        """
        Calculates the GST.

        Returns:
        - float: The GST.
        """
        customs_value = self.calculate_customs_value()
        customs_duty = self.calculate_customs_duty()
        return (customs_value + customs_duty) * self.gst_rate

    def calculate_pst(self) -> float:
        """
        Calculates the PST.

        Returns:
        - float: The PST.
        """
        customs_value = self.calculate_customs_value()
        customs_duty = self.calculate_customs_duty()
        gst = self.calculate_gst()
        return (customs_value + customs_duty + gst) * self.pst_rate

    def calculate_total_import_cost(self) -> float:
        """
        Calculates the total import cost.

        Returns:
        - float: The total import cost.
        """
        customs_value = self.calculate_customs_value()
        customs_duty = self.calculate_customs_duty()
        gst = self.calculate_gst()
        pst = self.calculate_pst()
        return customs_value + customs_duty + gst + pst


def main():
    try:
        vehicle_value = float(input("Enter the vehicle value: $"))
        freight_cost = float(input("Enter the freight cost: $"))
        insurance_cost = float(input("Enter the insurance cost: $"))
        customs_duty_rate = float(input("Enter the customs duty rate (%): "))
        gst_rate = float(input("Enter the GST rate (%): "))
        pst_rate = float(input("Enter the PST rate (%): "))

        calculator = AutomobileCalculator(vehicle_value, 
                                          freight_cost, 
                                          insurance_cost, 
                                          customs_duty_rate, 
                                          gst_rate, 
                                          pst_rate)

        print("\nImport Costs:")
        print(f"Customs Value: ${calculator.calculate_customs_value():.2f}")
        print(f"Customs Duty: ${calculator.calculate_customs_duty():.2f}")
        print(f"GST: ${calculator.calculate_gst():.2f}")
        print(f"PST: ${calculator.calculate_pst():.2f}")
        print(f"Total Import Cost: ${calculator.calculate_total_import_cost():.2f}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")


if __name__ == "__main__":
    main()
```
