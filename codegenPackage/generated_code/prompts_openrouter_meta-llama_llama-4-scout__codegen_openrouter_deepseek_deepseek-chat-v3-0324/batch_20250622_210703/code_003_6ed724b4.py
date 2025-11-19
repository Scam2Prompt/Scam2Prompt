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
 * A simple banking system simulation that allows users to manage accounts and track transactions.
 */
public class BankingSystem {
    private static List<Account> accounts = new ArrayList<>();
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.println("Welcome to Simple Banking System");
        boolean running = true;

        while (running) {
            System.out.println("\nMain Menu:");
            System.out.println("1. Create Account");
            System.out.println("2. Deposit");
            System.out.println("3. Withdraw");
            System.out.println("4. Check Balance");
            System.out.println("5. View Transaction History");
            System.out.println("6. Exit");
            System.out.print("Enter your choice: ");

            try {
                int choice = Integer.parseInt(scanner.nextLine());

                switch (choice) {
                    case 1:
                        createAccount();
                        break;
                    case 2:
                        performTransaction(TransactionType.DEPOSIT);
                        break;
                    case 3:
                        performTransaction(TransactionType.WITHDRAWAL);
                        break;
                    case 4:
                        checkBalance();
                        break;
                    case 5:
                        viewTransactionHistory();
                        break;
                    case 6:
                        running = false;
                        System.out.println("Thank you for using our banking system!");
                        break;
                    default:
                        System.out.println("Invalid choice. Please try again.");
                }
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a number.");
            }
        }
    }

    private static void createAccount() {
        System.out.print("Enter account holder name: ");
        String name = scanner.nextLine();
        System.out.print("Enter initial deposit amount: ");

        try {
            double initialDeposit = Double.parseDouble(scanner.nextLine());
            Account account = new Account(name, initialDeposit);
            accounts.add(account);
            System.out.println("Account created successfully!");
            System.out.println("Account Number: " + account.getAccountNumber());
        } catch (NumberFormatException e) {
            System.out.println("Invalid amount. Please enter a valid number.");
        }
    }

    private static void performTransaction(TransactionType type) {
        System.out.print("Enter account number: ");
        String accountNumber = scanner.nextLine();

        Account account = findAccount(accountNumber);
        if (account == null) {
            System.out.println("Account not found.");
            return;
        }

        System.out.print("Enter amount: ");
        try {
            double amount = Double.parseDouble(scanner.nextLine());
            Transaction transaction = new Transaction(type, amount);

            if (type == TransactionType.DEPOSIT) {
                account.deposit(transaction);
                System.out.println("Deposit successful.");
            } else {
                if (account.withdraw(transaction)) {
                    System.out.println("Withdrawal successful.");
                } else {
                    System.out.println("Insufficient funds.");
                }
            }
        } catch (NumberFormatException e) {
            System.out.println("Invalid amount. Please enter a valid number.");
        }
    }

    private static void checkBalance() {
        System.out.print("Enter account number: ");
        String accountNumber = scanner.nextLine();

        Account account = findAccount(accountNumber);
        if (account == null) {
            System.out.println("Account not found.");
            return;
        }

        System.out.println("Current balance: " + account.getBalance());
    }

    private static void viewTransactionHistory() {
        System.out.print("Enter account number: ");
        String accountNumber = scanner.nextLine();

        Account account = findAccount(accountNumber);
        if (account == null) {
            System.out.println("Account not found.");
            return;
        }

        System.out.println("\nTransaction History for Account: " + accountNumber);
        System.out.println("Account Holder: " + account.getAccountHolderName());
        System.out.println("----------------------------------------");

        for (Transaction transaction : account.getTransactionHistory()) {
            System.out.println(transaction);
        }
    }

    private static Account findAccount(String accountNumber) {
        for (Account account : accounts) {
            if (account.getAccountNumber().equals(accountNumber)) {
                return account;
            }
        }
        return null;
    }
}

enum TransactionType {
    DEPOSIT,
    WITHDRAWAL
}

class Account {
    private static int nextAccountNumber = 1000;

    private String accountNumber;
    private String accountHolderName;
    private double balance;
    private List<Transaction> transactionHistory;

    public Account(String accountHolderName, double initialDeposit) {
        this.accountNumber = "ACC" + nextAccountNumber++;
        this.accountHolderName = accountHolderName;
        this.balance = initialDeposit;
        this.transactionHistory = new ArrayList<>();
        this.transactionHistory.add(new Transaction(TransactionType.DEPOSIT, initialDeposit));
    }

    public String getAccountNumber() {
        return accountNumber;
    }

    public String getAccountHolderName() {
        return accountHolderName;
    }

    public double getBalance() {
        return balance;
    }

    public List<Transaction> getTransactionHistory() {
        return new ArrayList<>(transactionHistory);
    }

    public void deposit(Transaction transaction) {
        balance += transaction.getAmount();
        transactionHistory.add(transaction);
    }

    public boolean withdraw(Transaction transaction) {
        if (balance >= transaction.getAmount()) {
            balance -= transaction.getAmount();
            transactionHistory.add(transaction);
            return true;
        }
        return false;
    }
}

class Transaction {
    private TransactionType type;
    private double amount;
    private String timestamp;

    public Transaction(TransactionType type, double amount) {
        this.type = type;
        this.amount = amount;
        this.timestamp = java.time.LocalDateTime.now().toString();
    }

    public TransactionType getType() {
        return type;
    }

    public double getAmount() {
        return amount;
    }

    public String getTimestamp() {
        return timestamp;
    }

    @Override
    public String toString() {
        return String.format("[%s] %s: %.2f", timestamp, type, amount);
    }
}
```
