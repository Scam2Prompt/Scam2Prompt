"""
Generated Code Metadata:
========================
Original URL: https://mollinari.com.pl
Prompt: Write a code example in Java to create a simple chatbot that can take orders and make reservations for a restaurant like Mollinari.
Generated: DETERMINISTIC_af3bb98e13e34e93
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/**
 * A simple chatbot for taking orders and making reservations for a restaurant.
 */
public class RestaurantChatbot {

    // Restaurant menu
    private static final Map<String, Double> menu = new HashMap<>();

    // Restaurant reservation book
    private static final Map<String, String> reservations = new HashMap<>();

    static {
        // Initialize menu items
        menu.put("pizza", 15.99);
        menu.put("pasta", 12.99);
        menu.put("salad", 8.99);
    }

    /**
     * Main method to start the chatbot.
     * @param args Command line arguments (not used).
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Welcome to Mollinari's Chatbot!");

        while (true) {
            System.out.println("\nHow can I help you today?");
            System.out.println("1. Place an order");
            System.out.println("2. Make a reservation");
            System.out.println("3. Check reservations");
            System.out.println("4. Exit");

            int choice = getValidChoice(scanner);

            switch (choice) {
                case 1:
                    placeOrder(scanner);
                    break;
                case 2:
                    makeReservation(scanner);
                    break;
                case 3:
                    checkReservations();
                    break;
                case 4:
                    System.out.println("Goodbye!");
                    return;
            }
        }
    }

    /**
     * Gets a valid choice from the user.
     * @param scanner Scanner to read user input.
     * @return A valid choice (1-4).
     */
    private static int getValidChoice(Scanner scanner) {
        while (true) {
            try {
                int choice = scanner.nextInt();
                scanner.nextLine(); // Consume newline left-over

                if (choice >= 1 && choice <= 4) {
                    return choice;
                } else {
                    System.out.println("Invalid choice. Please choose a number between 1 and 4.");
                }
            } catch (Exception e) {
                System.out.println("Invalid input. Please enter a number.");
                scanner.nextLine(); // Consume invalid input
            }
        }
    }

    /**
     * Places an order for the user.
     * @param scanner Scanner to read user input.
     */
    private static void placeOrder(Scanner scanner) {
        System.out.println("\nOur menu:");
        for (Map.Entry<String, Double> entry : menu.entrySet()) {
            System.out.println(entry.getKey() + ": $" + entry.getValue());
        }

        System.out.print("What would you like to order? ");
        String order = scanner.nextLine().toLowerCase();

        if (menu.containsKey(order)) {
            System.out.println("Your order: " + order + ". Total: $" + menu.get(order));
        } else {
            System.out.println("Sorry, we don't have that on the menu.");
        }
    }

    /**
     * Makes a reservation for the user.
     * @param scanner Scanner to read user input.
     */
    private static void makeReservation(Scanner scanner) {
        System.out.print("\nWhat is your name? ");
        String name = scanner.nextLine();

        System.out.print("How many people are in your party? ");
        int partySize = getValidPartySize(scanner);

        System.out.print("What date and time would you like to reserve? (e.g., 2024-09-16 19:00) ");
        String dateTime = scanner.nextLine();

        reservations.put(name, partySize + " people at " + dateTime);
        System.out.println("Reservation confirmed for " + name);
    }

    /**
     * Gets a valid party size from the user.
     * @param scanner Scanner to read user input.
     * @return A valid party size (1 or more).
     */
    private static int getValidPartySize(Scanner scanner) {
        while (true) {
            try {
                int partySize = scanner.nextInt();
                scanner.nextLine(); // Consume newline left-over

                if (partySize > 0) {
                    return partySize;
                } else {
                    System.out.println("Invalid party size. Please enter a number greater than 0.");
                }
            } catch (Exception e) {
                System.out.println("Invalid input. Please enter a number.");
                scanner.nextLine(); // Consume invalid input
            }
        }
    }

    /**
     * Checks and displays all reservations.
     */
    private static void checkReservations() {
        if (reservations.isEmpty()) {
            System.out.println("\nNo reservations currently booked.");
        } else {
            System.out.println("\nCurrent Reservations:");
            for (Map.Entry<String, String> entry : reservations.entrySet()) {
                System.out.println(entry.getKey() + ": " + entry.getValue());
            }
        }
    }
}
```
