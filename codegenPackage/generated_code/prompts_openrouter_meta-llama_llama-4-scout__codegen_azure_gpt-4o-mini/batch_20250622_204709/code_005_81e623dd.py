"""
Generated Code Metadata:
========================
Original URL: https://dbm.mu
Prompt: Write a Java code to develop a simple loan calculator based on DBM's loan scheme for the construction of water tanks and purchase of irrigation systems in Rodrigues.
Generated: DETERMINISTIC_81e623dd83c21b90
Batch ID: 20250622_204709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.Scanner;

/**
 * LoanCalculator class provides functionality to calculate the total amount to be repaid
 * for a loan based on DBM's loan scheme for the construction of water tanks and purchase of irrigation systems.
 */
public class LoanCalculator {

    private static final double INTEREST_RATE = 0.05; // 5% annual interest rate
    private static final int LOAN_TERM_YEARS = 10; // Loan term in years

    /**
     * Main method to run the loan calculator.
     * @param args Command line arguments
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        try {
            // Prompt user for loan amount
            System.out.print("Enter the loan amount: ");
            double loanAmount = scanner.nextDouble();

            // Validate loan amount
            if (loanAmount <= 0) {
                throw new IllegalArgumentException("Loan amount must be greater than zero.");
            }

            // Calculate total repayment amount
            double totalRepayment = calculateTotalRepayment(loanAmount);
            System.out.printf("Total amount to be repaid over %d years: %.2f%n", LOAN_TERM_YEARS, totalRepayment);
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        } finally {
            scanner.close(); // Ensure the scanner is closed to prevent resource leaks
        }
    }

    /**
     * Calculates the total repayment amount for a given loan amount.
     * @param loanAmount The principal loan amount
     * @return The total amount to be repaid
     */
    private static double calculateTotalRepayment(double loanAmount) {
        double totalInterest = loanAmount * INTEREST_RATE * LOAN_TERM_YEARS;
        return loanAmount + totalInterest; // Total repayment = Principal + Interest
    }
}
```
