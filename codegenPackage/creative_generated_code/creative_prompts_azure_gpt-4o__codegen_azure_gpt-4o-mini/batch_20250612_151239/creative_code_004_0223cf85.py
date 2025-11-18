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
 * A simple program to calculate leasing costs for equipment and vehicles.
 * This program is designed for DBM Financial Services leasing facilities for MSMEs.
 */
public class LeasingCalculator {

    // Constants for the leasing calculations
    private static final double INTEREST_RATE = 0.05; // 5% interest rate
    private static final int LEASE_TERM_YEARS = 3; // Default lease term in years

    /**
     * Main method to run the leasing cost calculator.
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            // Input: Get the cost of the equipment
            System.out.print("Enter the cost of the equipment/vehicle: ");
            double cost = Double.parseDouble(scanner.nextLine());

            // Input: Get the residual value
            System.out.print("Enter the estimated residual value after lease term: ");
            double residualValue = Double.parseDouble(scanner.nextLine());

            // Calculate the monthly leasing cost
            double monthlyCost = calculateMonthlyLeasingCost(cost, residualValue, LEASE_TERM_YEARS, INTEREST_RATE);

            // Output: Display the monthly leasing cost
            System.out.printf("The monthly leasing cost is: %.2f%n", monthlyCost);
        } catch (NumberFormatException e) {
            System.err.println("Invalid input. Please enter numeric values.");
        } catch (Exception e) {
            System.err.println("An unexpected error occurred: " + e.getMessage());
        } finally {
            // Close the scanner resource
            scanner.close();
        }
    }

    /**
     * Calculates the monthly leasing cost.
     *
     * @param cost           The total cost of the equipment/vehicle.
     * @param residualValue  The estimated residual value after the lease term.
     * @param leaseTermYears The duration of the lease in years.
     * @param interestRate   The annual interest rate.
     * @return The calculated monthly leasing cost.
     */
    public static double calculateMonthlyLeasingCost(double cost, double residualValue, int leaseTermYears, double interestRate) {
        // Calculate the depreciated cost over the lease term
        double depreciatedCost = cost - residualValue;
        
        // Calculate monthly interest rate
        double monthlyInterestRate = interestRate / 12;

        // Calculate the total number of payments
        int totalPayments = leaseTermYears * 12;

        // Calculate monthly lease payment using the formula
        double monthlyLeasePayment = (depreciatedCost / totalPayments) + (cost * monthlyInterestRate);

        return monthlyLeasePayment;
    }
}
```
