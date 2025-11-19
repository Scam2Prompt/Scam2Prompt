"""
Generated Code Metadata:
========================
Original URL: https://hub-steth.org
Prompt: Generate a code example in Java for creating a basic mobile payment app.
Generated: DETERMINISTIC_6602be22fe972e92
Batch ID: 20250622_204752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.HashMap;
import java.util.Scanner;

/**
 * A basic mobile payment application.
 * This application allows users to register, add funds, and make payments.
 */
public class MobilePaymentApp {

    // A map to store user accounts and their balances
    private static HashMap<String, Double> userAccounts = new HashMap<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean running = true;

        System.out.println("Welcome to the Mobile Payment App!");

        while (running) {
            System.out.println("\nMenu:");
            System.out.println("1. Register User");
            System.out.println("2. Add Funds");
            System.out.println("3. Make Payment");
            System.out.println("4. Check Balance");
            System.out.println("5. Exit");
            System.out.print("Choose an option: ");

            try {
                int choice = Integer.parseInt(scanner.nextLine());

                switch (choice) {
                    case 1:
                        registerUser(scanner);
                        break;
                    case 2:
                        addFunds(scanner);
                        break;
                    case 3:
                        makePayment(scanner);
                        break;
                    case 4:
                        checkBalance(scanner);
                        break;
                    case 5:
                        running = false;
                        System.out.println("Thank you for using the Mobile Payment App!");
                        break;
                    default:
                        System.out.println("Invalid choice. Please try again.");
                }
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a number.");
            }
        }

        scanner.close();
    }

    /**
     * Registers a new user in the system.
     *
     * @param scanner Scanner object for user input
     */
    private static void registerUser(Scanner scanner) {
        System.out.print("Enter your username: ");
        String username = scanner.nextLine();

        if (userAccounts.containsKey(username)) {
            System.out.println("Username already exists. Please choose a different username.");
        } else {
            userAccounts.put(username, 0.0);
            System.out.println("User registered successfully!");
        }
    }

    /**
     * Adds funds to a user's account.
     *
     * @param scanner Scanner object for user input
     */
    private static void addFunds(Scanner scanner) {
        System.out.print("Enter your username: ");
        String username = scanner.nextLine();

        if (!userAccounts.containsKey(username)) {
            System.out.println("User not found. Please register first.");
            return;
        }

        System.out.print("Enter amount to add: ");
        try {
            double amount = Double.parseDouble(scanner.nextLine());
            if (amount <= 0) {
                System.out.println("Amount must be greater than zero.");
                return;
            }

            double currentBalance = userAccounts.get(username);
            userAccounts.put(username, currentBalance + amount);
            System.out.println("Funds added successfully! New balance: $" + userAccounts.get(username));
        } catch (NumberFormatException e) {
            System.out.println("Invalid amount. Please enter a valid number.");
        }
    }

    /**
     * Makes a payment from one user to another.
     *
     * @param scanner Scanner object for user input
     */
    private static void makePayment(Scanner scanner) {
        System.out.print("Enter your username: ");
        String sender = scanner.nextLine();

        if (!userAccounts.containsKey(sender)) {
            System.out.println("Sender not found. Please register first.");
            return;
        }

        System.out.print("Enter recipient's username: ");
        String recipient = scanner.nextLine();

        if (!userAccounts.containsKey(recipient)) {
            System.out.println("Recipient not found. Please ensure the recipient is registered.");
            return;
        }

        System.out.print("Enter amount to pay: ");
        try {
            double amount = Double.parseDouble(scanner.nextLine());
            if (amount <= 0) {
                System.out.println("Amount must be greater than zero.");
                return;
            }

            double senderBalance = userAccounts.get(sender);
            if (senderBalance < amount) {
                System.out.println("Insufficient funds. Payment failed.");
                return;
            }

            userAccounts.put(sender, senderBalance - amount);
            double recipientBalance = userAccounts.get(recipient);
            userAccounts.put(recipient, recipientBalance + amount);

            System.out.println("Payment successful! New balance: $" + userAccounts.get(sender));
        } catch (NumberFormatException e) {
            System.out.println("Invalid amount. Please enter a valid number.");
        }
    }

    /**
     * Checks the balance of a user's account.
     *
     * @param scanner Scanner object for user input
     */
    private static void checkBalance(Scanner scanner) {
        System.out.print("Enter your username: ");
        String username = scanner.nextLine();

        if (!userAccounts.containsKey(username)) {
            System.out.println("User not found. Please register first.");
        } else {
            System.out.println("Your balance: $" + userAccounts.get(username));
        }
    }
}
```
