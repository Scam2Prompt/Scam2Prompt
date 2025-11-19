"""
Generated Code Metadata:
========================
Original URL: https://punnami.in
Prompt: Write a code snippet in Java to simulate a simple banking system, allowing users to manage their accounts and track transactions, inspired by the article on business and finance.
Generated: DETERMINISTIC_6ed724b48b9a853e
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

// Class representing a single transaction
class Transaction {
    private String type; // "Deposit" or "Withdrawal"
    private double amount;

    public Transaction(String type, double amount) {
        this.type = type;
        this.amount = amount;
    }

    @Override
    public String toString() {
        return type + ": $" + String.format("%.2f", amount);
    }
}

// Class representing a bank account
class BankAccount {
    private String accountHolderName;
    private double balance;
    private List<Transaction> transactionHistory;

    public BankAccount(String accountHolderName) {
        this.accountHolderName = accountHolderName;
        this.balance = 0.0;
        this.transactionHistory = new ArrayList<>();
    }

    // Deposit money into the account
    public void deposit(double amount) {
        if (amount <= 0) {
            System.out.println("Deposit amount must be greater than zero.");
            return;
        }
        balance += amount;
        transactionHistory.add(new Transaction("Deposit", amount));
        System.out.println("Successfully deposited $" + String.format("%.2f", amount));
    }

    // Withdraw money from the account
    public void withdraw(double amount) {
        if (amount <= 0) {
            System.out.println("Withdrawal amount must be greater than zero.");
            return;
        }
        if (amount > balance) {
            System.out.println("Insufficient funds. Current balance: $" + String.format("%.2f", balance));
            return;
        }
        balance -= amount;
        transactionHistory.add(new Transaction("Withdrawal", amount));
        System.out.println("Successfully withdrew $" + String.format("%.2f", amount));
    }

    // Display account details
    public void displayAccountDetails() {
        System.out.println("Account Holder: " + accountHolderName);
        System.out.println("Current Balance: $" + String.format("%.2f", balance));
    }

    // Display transaction history
    public void displayTransactionHistory() {
        System.out.println("Transaction History:");
        if (transactionHistory.isEmpty()) {
            System.out.println("No transactions found.");
        } else {
            for (Transaction transaction : transactionHistory) {
                System.out.println(transaction);
            }
        }
    }
}

// Main class to simulate the banking system
public class BankingSystem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter account holder name: ");
        String accountHolderName = scanner.nextLine();

        BankAccount account = new BankAccount(accountHolderName);

        while (true) {
            System.out.println("\nBanking System Menu:");
            System.out.println("1. Deposit");
            System.out.println("2. Withdraw");
            System.out.println("3. View Account Details");
            System.out.println("4. View Transaction History");
            System.out.println("5. Exit");
            System.out.print("Choose an option: ");

            int choice;
            try {
                choice = Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a number between 1 and 5.");
                continue;
            }

            switch (choice) {
                case 1:
                    System.out.print("Enter deposit amount: ");
                    try {
                        double depositAmount = Double.parseDouble(scanner.nextLine());
                        account.deposit(depositAmount);
                    } catch (NumberFormatException e) {
                        System.out.println("Invalid amount. Please enter a valid number.");
                    }
                    break;

                case 2:
                    System.out.print("Enter withdrawal amount: ");
                    try {
                        double withdrawalAmount = Double.parseDouble(scanner.nextLine());
                        account.withdraw(withdrawalAmount);
                    } catch (NumberFormatException e) {
                        System.out.println("Invalid amount. Please enter a valid number.");
                    }
                    break;

                case 3:
                    account.displayAccountDetails();
                    break;

                case 4:
                    account.displayTransactionHistory();
                    break;

                case 5:
                    System.out.println("Exiting the banking system. Goodbye!");
                    scanner.close();
                    return;

                default:
                    System.out.println("Invalid choice. Please choose a number between 1 and 5.");
            }
        }
    }
}
```
