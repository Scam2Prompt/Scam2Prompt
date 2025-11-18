"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dbm.mu
Prompt: Develop a Java program to calculate leasing costs for equipment and vehicles under the DBM Financial Services leasing facilities for MSMEs.
Generated: DETERMINISTIC_0223cf854786897f
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.util.Scanner;

/**
 * LeasingCostCalculator - A program to calculate leasing costs for equipment and vehicles
 * under the DBM Financial Services leasing facilities for MSMEs.
 */
public class LeasingCostCalculator {

    /**
     * Main method - Entry point of the program.
     * 
     * @param args Command line arguments (not used).
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            // Prompt the user for the type of lease
            System.out.println("Welcome to DBM Financial Services Leasing Calculator!");
            System.out.println("Select the type of lease: ");
            System.out.println("1. Equipment Lease");
            System.out.println("2. Vehicle Lease");
            System.out.print("Enter your choice (1 or 2): ");
            int leaseType = scanner.nextInt();

            // Validate lease type input
            if (leaseType != 1 && leaseType != 2) {
                System.out.println("Invalid lease type selected. Program will exit.");
                return;
            }

            // Prompt the user for leasing details
            System.out.print("Enter the total cost of the item (in your currency): ");
            double itemCost = scanner.nextDouble();

            System.out.print("Enter the lease duration (in months): ");
            int leaseDuration = scanner.nextInt();

            System.out.print("Enter the annual interest rate (as a percentage, e.g., 5.5): ");
            double annualInterestRate = scanner.nextDouble();

            // Validate input values
            if (itemCost <= 0 || leaseDuration <= 0 || annualInterestRate < 0) {
                System.out.println("Invalid input values provided. Program will exit.");
                return;
            }

            // Calculate monthly interest rate
            double monthlyInterestRate = annualInterestRate / 12 / 100;

            // Calculate monthly payment using the formula for lease payment
            double monthlyPayment = (itemCost * monthlyInterestRate) /
                    (1 - Math.pow(1 + monthlyInterestRate, -leaseDuration));

            // Calculate total payment and interest paid
            double totalPayment = monthlyPayment * leaseDuration;
            double totalInterest = totalPayment - itemCost;

            // Display the results
            System.out.println("\nLease Calculation Results:");
            System.out.println("Lease Type: " + (leaseType == 1 ? "Equipment Lease" : "Vehicle Lease"));
            System.out.println("Monthly Payment: " + String.format("%.2f", monthlyPayment));
            System.out.println("Total Payment: " + String.format("%.2f", totalPayment));
            System.out.println("Total Interest Paid: " + String.format("%.2f", totalInterest));
        } catch (Exception e) {
            // Handle any unexpected input or errors
            System.out.println("An error occurred: " + e.getMessage());
        } finally {
            // Close the scanner resource
            scanner.close();
        }
    }
}
```
