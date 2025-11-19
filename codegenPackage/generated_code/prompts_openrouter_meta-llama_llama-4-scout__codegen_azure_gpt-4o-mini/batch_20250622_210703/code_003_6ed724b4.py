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

// Class representing a bank account
class BankAccount {
    private String accountNumber;
    private String accountHolder;
    private double balance;
    private List<String> transactions;

    // Constructor to initialize a new bank account
    public BankAccount(String accountNumber, String accountHolder) {
        this.accountNumber = accountNumber;
        this.accountHolder = accountHolder;
        this.balance = 0.0;
        this.transactions = new ArrayList<>();
    }

    // Method to deposit money into the account
    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            transactions.add("Deposited: $" + amount);
        } else {
            System.out.println("Deposit amount must be positive.");
        }
    }

    // Method to withdraw money from the account
    public void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            transactions.add("Withdrew: $" + amount);
        } else if (amount > balance) {
            System.out.println("Insufficient funds for withdrawal.");
        } else {
            System.out.println("Withdrawal amount must be positive.");
        }
    }

    // Method to get the current balance
    public double getBalance() {
        return balance;
    }

    // Method to print transaction history
    public void printTransactions() {
        System.out.println("Transaction history for account " + accountNumber + ":");
        for (String transaction : transactions) {
            System.out.println(transaction);
        }
    }
}

// Main class to run the banking system
public class SimpleBankingSystem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        BankAccount account = null;

        // User input for account creation
        System.out.print("Enter account number: ");
        String accountNumber = scanner.nextLine();
        System.out.print("Enter account holder name: ");
        String accountHolder = scanner.nextLine();
        
        // Create a new bank account
        account = new BankAccount(accountNumber, accountHolder);
        System.out.println("Account created successfully!");

        // Main loop for banking operations
        while (true) {
            System.out.println("\nChoose an option:");
            System.out.println("1. Deposit");
            System.out.println("2. Withdraw");
            System.out.println("3. Check Balance");
            System.out.println("4. View Transactions");
            System.out.println("5. Exit");
            System.out.print("Your choice: ");

            int choice = scanner.nextInt();
            switch (choice) {
                case 1:
                    System.out.print("Enter amount to deposit: ");
                    double depositAmount = scanner.nextDouble();
                    account.deposit(depositAmount);
                    break;
                case 2:
                    System.out.print("Enter amount to withdraw: ");
                    double withdrawAmount = scanner.nextDouble();
                    account.withdraw(withdrawAmount);
                    break;
                case 3:
                    System.out.printf("Current balance: $%.2f%n", account.getBalance());
                    break;
                case 4:
                    account.printTransactions();
                    break;
                case 5:
                    System.out.println("Exiting the banking system. Goodbye!");
                    scanner.close();
                    return;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }
}
```
