"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capitalupspips.com
Prompt: Create a secure investment tracking application in Java that allows users to monitor their profits and withdrawals based on the confirmed and pending statuses described on CapitalUpsPips.
Generated: DETERMINISTIC_823e4d8c945a4aa7
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * InvestmentTrackingApp: A secure application for monitoring profits and withdrawals.
 * Users can track confirmed and pending transactions.
 */
public class InvestmentTrackingApp {

    public static void main(String[] args) {
        InvestmentTracker tracker = new InvestmentTracker();

        // Welcome message
        System.out.println("Welcome to CapitalUpsPips Investment Tracker!");
        System.out.println("Track your profits and withdrawals securely.\n");

        // User interaction loop
        Scanner scanner = new Scanner(System.in);
        boolean exit = false;

        try {
            while (!exit) {
                System.out.println("Menu:");
                System.out.println("1. Add Transaction");
                System.out.println("2. View Transactions");
                System.out.println("3. View Balance");
                System.out.println("4. Exit");
                System.out.print("Enter your choice: ");

                int choice = scanner.nextInt();
                scanner.nextLine(); // Consume newline character

                switch (choice) {
                    case 1:
                        tracker.addTransaction(scanner);
                        break;

                    case 2:
                        tracker.viewTransactions();
                        break;

                    case 3:
                        tracker.viewBalance();
                        break;

                    case 4:
                        System.out.println("Exiting application. Goodbye!");
                        exit = true;
                        break;

                    default:
                        System.out.println("Invalid choice. Please try again.");
                }
            }
        } catch (Exception e) {
            System.err.println("An error occurred: " + e.getMessage());
            e.printStackTrace();
        } finally {
            scanner.close();
        }
    }
}

/**
 * TransactionType: Enum representing the type of transaction (Profit or Withdrawal).
 */
enum TransactionType {
    PROFIT, WITHDRAWAL
}

/**
 * TransactionStatus: Enum representing the status of the transaction (Confirmed or Pending).
 */
enum TransactionStatus {
    CONFIRMED, PENDING
}

/**
 * Transaction: Represents a single transaction with type, amount, and status.
 */
class Transaction {
    private final TransactionType type;
    private final double amount;
    private final TransactionStatus status;

    public Transaction(TransactionType type, double amount, TransactionStatus status) {
        this.type = type;
        this.amount = amount;
        this.status = status;
    }

    public TransactionType getType() {
        return type;
    }

    public double getAmount() {
        return amount;
    }

    public TransactionStatus getStatus() {
        return status;
    }

    @Override
    public String toString() {
        return "Transaction{" +
                "type=" + type +
                ", amount=" + amount +
                ", status=" + status +
                '}';
    }
}

/**
 * InvestmentTracker: Handles the core functionality of tracking investments.
 */
class InvestmentTracker {
    private final List<Transaction> transactions;

    public InvestmentTracker() {
        this.transactions = new ArrayList<>();
    }

    /**
     * Allows the user to add a new transaction.
     *
     * @param scanner The scanner instance for user input.
     */
    public void addTransaction(Scanner scanner) {
        try {
            System.out.print("Enter transaction type (1 for Profit, 2 for Withdrawal): ");
            int typeInput = scanner.nextInt();
            TransactionType type = (typeInput == 1) ? TransactionType.PROFIT : TransactionType.WITHDRAWAL;

            System.out.print("Enter transaction amount: ");
            double amount = scanner.nextDouble();

            System.out.print("Enter transaction status (1 for Confirmed, 2 for Pending): ");
            int statusInput = scanner.nextInt();
            TransactionStatus status = (statusInput == 1) ? TransactionStatus.CONFIRMED : TransactionStatus.PENDING;

            // Create and store transaction
            Transaction transaction = new Transaction(type, amount, status);
            transactions.add(transaction);

            System.out.println("Transaction successfully added.");
        } catch (Exception e) {
            System.err.println("Failed to add transaction. Please ensure valid input.");
            scanner.nextLine(); // Clear input buffer
        }
    }

    /**
     * Displays all transactions in the list.
     */
    public void viewTransactions() {
        System.out.println("\nAll Transactions:");
        if (transactions.isEmpty()) {
            System.out.println("No transactions recorded.");
        } else {
            for (Transaction transaction : transactions) {
                System.out.println(transaction);
            }
        }
    }

    /**
     * Calculates and displays the total balance based on confirmed transactions.
     * Profits are added, withdrawals are subtracted.
     */
    public void viewBalance() {
        double balance = 0.0;

        for (Transaction transaction : transactions) {
            if (transaction.getStatus() == TransactionStatus.CONFIRMED) {
                if (transaction.getType() == TransactionType.PROFIT) {
                    balance += transaction.getAmount();
                } else if (transaction.getType() == TransactionType.WITHDRAWAL) {
                    balance -= transaction.getAmount();
                }
            }
        }

        System.out.println("\nTotal Balance (Confirmed Transactions): $" + balance);
    }
}
```
