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

/**
 * Represents a bank account with an account number, balance, and transaction history.
 */
class Account {
    private int accountNumber;
    private double balance;
    private List<Transaction> transactions;

    public Account(int accountNumber, double initialBalance) {
        this.accountNumber = accountNumber;
        this.balance = initialBalance;
        this.transactions = new ArrayList<>();
        // Record the initial deposit as a transaction
        transactions.add(new Transaction("Initial Deposit", initialBalance));
    }

    /**
     * Deposits money into the account.
     * 
     * @param amount the amount to deposit
     */
    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            transactions.add(new Transaction("Deposit", amount));
            System.out.println("Deposited: $" + String.format("%.2f", amount));
        } else {
            System.out.println("Invalid deposit amount.");
        }
    }

    /**
     * Withdraws money from the account if sufficient funds are available.
     * 
     * @param amount the amount to withdraw
     */
    public void withdraw(double amount) {
        if (amount > 0 && balance >= amount) {
            balance -= amount;
            transactions.add(new Transaction("Withdrawal", -amount));
            System.out.println("Withdrawn: $" + String.format("%.2f", amount));
        } else if (amount <= 0) {
            System.out.println("Invalid withdrawal amount.");
        } else {
            System.out.println("Insufficient funds.");
        }
    }

    /**
     * Displays the current balance and transaction history.
     */
    public void displayAccountInfo() {
        System.out.println("Account Number: " + accountNumber);
        System.out.println("Current Balance: $" + String.format("%.2f", balance));
        System.out.println("Transaction History:");
        for (Transaction transaction : transactions) {
            transaction.displayTransaction();
        }
    }
}

/**
 * Represents a transaction with a description and amount.
 */
class Transaction {
    private String description;
    private double amount;

    public Transaction(String description, double amount) {
        this.description = description;
        this.amount = amount;
    }

    /**
     * Displays the transaction details.
     */
    public void displayTransaction() {
        String transactionType = (amount > 0) ? "Deposit" : "Withdrawal";
        System.out.println(transactionType + ": $" + String.format("%.2f", Math.abs(amount)));
    }
}

public class BankingSystem {
    private List<Account> accounts;
    private Scanner scanner;

    public BankingSystem() {
        this.accounts = new ArrayList<>();
        this.scanner = new Scanner(System.in);
    }

    /**
     * Creates a new bank account with an initial balance.
     */
    public void createAccount() {
        System.out.print("Enter account number: ");
        int accountNumber = scanner.nextInt();
        System.out.print("Enter initial balance: $");
        double initialBalance = scanner.nextDouble();
        accounts.add(new Account(accountNumber, initialBalance));
        System.out.println("Account created successfully.");
    }

    /**
     * Manages an existing bank account.
     */
    public void manageAccount() {
        if (accounts.isEmpty()) {
            System.out.println("No accounts available.");
            return;
        }
        System.out.println("Available accounts:");
        for (int i = 0; i < accounts.size(); i++) {
            System.out.println((i + 1) + ". Account Number: " + accounts.get(i).accountNumber);
        }
        System.out.print("Choose an account: ");
        int choice = scanner.nextInt() - 1;
        if (choice >= 0 && choice < accounts.size()) {
            Account selectedAccount = accounts.get(choice);
            while (true) {
                System.out.println("\n1. Deposit");
                System.out.println("2. Withdraw");
                System.out.println("3. Display Account Info");
                System.out.println("4. Back");
                System.out.print("Choose an option: ");
                int option = scanner.nextInt();
                switch (option) {
                    case 1:
                        System.out.print("Enter deposit amount: $");
                        double depositAmount = scanner.nextDouble();
                        selectedAccount.deposit(depositAmount);
                        break;
                    case 2:
                        System.out.print("Enter withdrawal amount: $");
                        double withdrawalAmount = scanner.nextDouble();
                        selectedAccount.withdraw(withdrawalAmount);
                        break;
                    case 3:
                        selectedAccount.displayAccountInfo();
                        break;
                    case 4:
                        return;
                    default:
                        System.out.println("Invalid option. Please choose a valid option.");
                }
            }
        } else {
            System.out.println("Invalid account choice.");
        }
    }

    /**
     * Runs the banking system.
     */
    public void run() {
        while (true) {
            System.out.println("\n1. Create Account");
            System.out.println("2. Manage Account");
            System.out.println("3. Exit");
            System.out.print("Choose an option: ");
            int option = scanner.nextInt();
            switch (option) {
                case 1:
                    createAccount();
                    break;
                case 2:
                    manageAccount();
                    break;
                case 3:
                    System.out.println("Exiting...");
                    return;
                default:
                    System.out.println("Invalid option. Please choose a valid option.");
            }
        }
    }

    public static void main(String[] args) {
        BankingSystem bankingSystem = new BankingSystem();
        bankingSystem.run();
    }
}
```
