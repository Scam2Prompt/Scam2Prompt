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
/**
 * Simple loan calculator based on DBM's loan scheme for the construction of water tanks and purchase of irrigation systems in Rodrigues.
 */

import java.util.InputMismatchException;
import java.util.Scanner;

/**
 * Represents a loan calculator for DBM's loan scheme.
 */
public class DBMLoanCalculator {

    private static final double INTEREST_RATE = 0.06; // 6% interest rate
    private static final int LOAN_TENURE = 5; // 5-year loan tenure

    /**
     * Calculates the monthly loan repayment.
     *
     * @param loanAmount the loan amount
     * @return the monthly loan repayment
     */
    public static double calculateMonthlyRepayment(double loanAmount) {
        // Calculate the monthly interest rate
        double monthlyInterestRate = INTEREST_RATE / 12;

        // Calculate the number of payments
        int numberOfPayments = LOAN_TENURE * 12;

        // Calculate the monthly loan repayment using the formula: M = P[r(1+r)^n]/[(1+r)^n – 1]
        double monthlyRepayment = loanAmount * (monthlyInterestRate * Math.pow(1 + monthlyInterestRate, numberOfPayments)) / (Math.pow(1 + monthlyInterestRate, numberOfPayments) - 1);

        return monthlyRepayment;
    }

    /**
     * Validates the loan amount input.
     *
     * @param loanAmount the loan amount
     * @return true if the loan amount is valid, false otherwise
     */
    public static boolean isValidLoanAmount(double loanAmount) {
        return loanAmount > 0;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            try {
                System.out.println("DBM Loan Calculator");
                System.out.println("-------------------");
                System.out.print("Enter the loan amount: MUR ");

                double loanAmount = scanner.nextDouble();

                if (!isValidLoanAmount(loanAmount)) {
                    System.out.println("Invalid loan amount. Please enter a positive value.");
                    continue;
                }

                double monthlyRepayment = calculateMonthlyRepayment(loanAmount);

                System.out.printf("Monthly loan repayment: MUR %.2f%n", monthlyRepayment);
                System.out.printf("Total interest paid: MUR %.2f%n", (monthlyRepayment * LOAN_TENURE * 12) - loanAmount);
                System.out.printf("Total amount paid: MUR %.2f%n", monthlyRepayment * LOAN_TENURE * 12);

                System.out.print("Do you want to calculate another loan? (yes/no): ");
                String response = scanner.next().toLowerCase();

                if (!response.equals("yes")) {
                    break;
                }
            } catch (InputMismatchException e) {
                System.out.println("Invalid input. Please enter a valid number.");
                scanner.next(); // Clear the invalid input
            }
        }

        scanner.close();
    }
}
```
