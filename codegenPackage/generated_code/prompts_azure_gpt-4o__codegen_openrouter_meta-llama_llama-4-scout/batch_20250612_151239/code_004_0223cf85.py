"""
Generated Code Metadata:
========================
Original URL: https://dbm.mu
Prompt: Develop a Java program to calculate leasing costs for equipment and vehicles under the DBM Financial Services leasing facilities for MSMEs.
Generated: DETERMINISTIC_0223cf854786897f
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
/**
 * Calculates leasing costs for equipment and vehicles under the DBM Financial Services leasing facilities for MSMEs.
 */

import java.util.InputMismatchException;
import java.util.Scanner;

/**
 * LeasingCostCalculator class.
 */
public class LeasingCostCalculator {

    /**
     * Enum for leasing types.
     */
    public enum LeasingType {
        EQUIPMENT,
        VEHICLE
    }

    /**
     * Calculates leasing cost.
     *
     * @param leasingType    Leasing type (equipment or vehicle).
     * @param assetValue     Asset value.
     * @param leaseTerm      Lease term in months.
     * @param interestRate   Interest rate as a decimal.
     * @param residualValue  Residual value.
     * @return Leasing cost.
     */
    public static double calculateLeasingCost(LeasingType leasingType, double assetValue, int leaseTerm, double interestRate, double residualValue) {
        // Calculate monthly interest rate
        double monthlyInterestRate = interestRate / 12;

        // Calculate leasing cost using the formula: (assetValue - residualValue) * monthlyInterestRate * (1 + monthlyInterestRate) ^ leaseTerm / ((1 + monthlyInterestRate) ^ leaseTerm - 1)
        double leasingCost = (assetValue - residualValue) * monthlyInterestRate * Math.pow(1 + monthlyInterestRate, leaseTerm) / (Math.pow(1 + monthlyInterestRate, leaseTerm) - 1);

        return leasingCost;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.println("DBM Financial Services Leasing Cost Calculator");

            // Get leasing type
            System.out.println("Choose a leasing type:");
            System.out.println("1. Equipment");
            System.out.println("2. Vehicle");
            int leasingTypeChoice = scanner.nextInt();
            LeasingType leasingType = leasingTypeChoice == 1 ? LeasingType.EQUIPMENT : LeasingType.VEHICLE;

            // Get asset value
            System.out.print("Enter asset value: ");
            double assetValue = scanner.nextDouble();

            // Get lease term
            System.out.print("Enter lease term in months: ");
            int leaseTerm = scanner.nextInt();

            // Get interest rate
            System.out.print("Enter interest rate (in %): ");
            double interestRate = scanner.nextDouble() / 100;

            // Get residual value
            System.out.print("Enter residual value: ");
            double residualValue = scanner.nextDouble();

            // Calculate leasing cost
            double leasingCost = calculateLeasingCost(leasingType, assetValue, leaseTerm, interestRate, residualValue);

            // Display result
            System.out.printf("Leasing cost: %.2f%n", leasingCost);
            System.out.printf("Leasing type: %s%n", leasingType);
            System.out.printf("Asset value: %.2f%n", assetValue);
            System.out.printf("Lease term: %d months%n", leaseTerm);
            System.out.printf("Interest rate: %.2f%%%n", interestRate * 100);
            System.out.printf("Residual value: %.2f%n", residualValue);

        } catch (InputMismatchException e) {
            System.out.println("Invalid input. Please enter a valid number.");
        } catch (Exception e) {
            System.out.println("An error occurred: " + e.getMessage());
        } finally {
            scanner.close();
        }
    }
}
```
