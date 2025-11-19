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
 * LoanCalculator - A simple loan calculator for DBM's loan scheme.
<<<<<<< HEAD
 * This program calculates monthly payments and total payment for a loan
 * based on user input for loan amount, interest rate, and loan term.
=======
 * This program calculates the monthly repayment amount based on the loan amount,
 * interest rate, and loan tenure.
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
 */
public class LoanCalculator {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            // Prompt user for loan details
<<<<<<< HEAD
            System.out.println("Welcome to DBM Loan Calculator for Water Tanks and Irrigation Systems.");
            System.out.print("Enter loan amount (in Rs): ");
            double loanAmount = scanner.nextDouble();

            System.out.print("Enter annual interest rate (in %): ");
            double annualInterestRate = scanner.nextDouble();

            System.out.print("Enter loan term (in years): ");
            int loanTermYears = scanner.nextInt();

            // Validate inputs
            if (loanAmount <= 0 || annualInterestRate <= 0 || loanTermYears <= 0) {
=======
            System.out.println("Welcome to DBM Loan Calculator for Rodrigues!");
            System.out.print("Enter the loan amount (in MUR): ");
            double loanAmount = scanner.nextDouble();

            System.out.print("Enter the annual interest rate (in %): ");
            double annualInterestRate = scanner.nextDouble();

            System.out.print("Enter the loan tenure (in years): ");
            int loanTenureYears = scanner.nextInt();

            // Validate inputs
            if (loanAmount <= 0 || annualInterestRate <= 0 || loanTenureYears <= 0) {
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
                System.out.println("Error: All inputs must be positive values.");
                return;
            }

<<<<<<< HEAD
            // Calculate monthly interest rate
            double monthlyInterestRate = annualInterestRate / 100 / 12;

            // Calculate number of payments
            int numberOfPayments = loanTermYears * 12;

            // Calculate monthly payment using the formula:
            // M = P * (r * (1 + r)^n) / ((1 + r)^n - 1)
            double monthlyPayment = loanAmount * (monthlyInterestRate * Math.pow(1 + monthlyInterestRate, numberOfPayments))
                    / (Math.pow(1 + monthlyInterestRate, numberOfPayments) - 1);

            // Calculate total payment
            double totalPayment = monthlyPayment * numberOfPayments;

            // Display results
            System.out.println("\nLoan Calculation Results:");
            System.out.printf("Monthly Payment: Rs %.2f%n", monthlyPayment);
            System.out.printf("Total Payment: Rs %.2f%n", totalPayment);

        } catch (Exception e) {
            // Handle invalid input
            System.out.println("Error: Invalid input. Please enter numeric values only.");
        } finally {
            // Close the scanner
            scanner.close();
        }
    }
=======
            // Calculate monthly repayment
            double monthlyRepayment = calculateMonthlyRepayment(loanAmount, annualInterestRate, loanTenureYears);

            // Display the result
            System.out.printf("Your monthly repayment amount is: MUR %.2f%n", monthlyRepayment);
        } catch (Exception e) {
            System.out.println("Error: Invalid input. Please enter numeric values.");
        } finally {
            scanner.close(); // Ensure scanner is closed to prevent resource leaks
        }
    }

    /**
     * Calculates the monthly repayment amount for a loan.
     *
     * @param loanAmount         The total loan amount.
     * @param annualInterestRate The annual interest rate (in percentage).
     * @param loanTenureYears    The loan tenure (in years).
     * @return The monthly repayment amount.
     */
    private static double calculateMonthlyRepayment(double loanAmount, double annualInterestRate, int loanTenureYears) {
        // Convert annual interest rate to monthly interest rate (in decimal)
        double monthlyInterestRate = (annualInterestRate / 100) / 12;

        // Calculate total number of monthly payments
        int totalMonthlyPayments = loanTenureYears * 12;

        // Use the formula for monthly repayment (EMI)
        // EMI = [P * r * (1 + r)^n] / [(1 + r)^n - 1]
        double numerator = loanAmount * monthlyInterestRate * Math.pow(1 + monthlyInterestRate, totalMonthlyPayments);
        double denominator = Math.pow(1 + monthlyInterestRate, totalMonthlyPayments) - 1;

        return numerator / denominator;
    }
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
}
```
