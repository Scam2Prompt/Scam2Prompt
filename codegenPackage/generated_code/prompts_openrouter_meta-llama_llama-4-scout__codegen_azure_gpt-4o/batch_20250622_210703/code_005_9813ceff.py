"""
Generated Code Metadata:
========================
Original URL: https://azalearesidence.com
Prompt: Write a code snippet in Java to calculate mortgage payments for properties in Jakarta, taking into account the location and features of Azalea Residence.
Generated: DETERMINISTIC_9813ceffbcce9dba
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.Scanner;

public class MortgageCalculator {

    // Constants for Azalea Residence in Jakarta
    private static final double BASE_INTEREST_RATE = 0.045; // 4.5% annual interest rate
    private static final int LOAN_TERM_YEARS = 20; // Default loan term in years
    private static final double LOCATION_PREMIUM = 0.02; // 2% premium for Azalea Residence location
    private static final double FEATURE_PREMIUM = 0.01; // 1% premium for additional features

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            // Input: Property price
            System.out.print("Enter the property price (in IDR): ");
            double propertyPrice = scanner.nextDouble();

            // Input: Down payment
            System.out.print("Enter the down payment (in IDR): ");
            double downPayment = scanner.nextDouble();

            // Input: Additional features premium (true/false)
            System.out.print("Does the property have additional features? (true/false): ");
            boolean hasAdditionalFeatures = scanner.nextBoolean();

            // Calculate loan amount
            double loanAmount = propertyPrice - downPayment;

            // Calculate interest rate based on location and features
            double interestRate = BASE_INTEREST_RATE + LOCATION_PREMIUM;
            if (hasAdditionalFeatures) {
                interestRate += FEATURE_PREMIUM;
            }

            // Calculate monthly mortgage payment
            double monthlyPayment = calculateMonthlyPayment(loanAmount, interestRate, LOAN_TERM_YEARS);

            // Output: Monthly payment
            System.out.printf("Your monthly mortgage payment is: IDR %.2f%n", monthlyPayment);

        } catch (Exception e) {
            System.err.println("Error: Invalid input. Please try again.");
        } finally {
            scanner.close();
        }
    }

    /**
     * Calculates the monthly mortgage payment using the formula for fixed-rate mortgages.
     *
     * @param loanAmount   The total loan amount (principal).
     * @param annualRate   The annual interest rate (as a decimal).
     * @param loanTermYears The loan term in years.
     * @return The monthly mortgage payment.
     */
    private static double calculateMonthlyPayment(double loanAmount, double annualRate, int loanTermYears) {
        // Convert annual interest rate to monthly interest rate
        double monthlyRate = annualRate / 12;

        // Total number of payments (months)
        int totalPayments = loanTermYears * 12;

        // Formula for monthly payment: M = P[r(1+r)^n] / [(1+r)^n - 1]
        double numerator = loanAmount * monthlyRate * Math.pow(1 + monthlyRate, totalPayments);
        double denominator = Math.pow(1 + monthlyRate, totalPayments) - 1;

        return numerator / denominator;
    }
}
```
