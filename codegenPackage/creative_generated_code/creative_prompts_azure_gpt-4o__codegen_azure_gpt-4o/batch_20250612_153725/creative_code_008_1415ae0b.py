"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://epsys.ro
Prompt: Write a Java program to simulate lottery number generation for Hondatoto's Japan pools, allowing users to test different betting strategies for 6D and 7D lotteries.
Generated: DETERMINISTIC_1415ae0b22b8cf26
Batch ID: 20250612_153725
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
import java.util.Random;
import java.util.Scanner;

/**
 * A program to simulate lottery number generation for Hondatoto's Japan pools.
 * Supports both 6D and 7D lotteries, allowing users to test different betting strategies.
 */
public class LotterySimulator {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to Hondatoto Lottery Simulator!");
        System.out.println("Choose your lottery type:");
        System.out.println("1. 6D Lottery (6 Digits)");
        System.out.println("2. 7D Lottery (7 Digits)");

        int choice = 0;
        try {
            System.out.print("Enter your choice (1 or 2): ");
            choice = Integer.parseInt(scanner.nextLine());
            
            if (choice != 1 && choice != 2) {
                throw new IllegalArgumentException("Invalid choice. Please select either 1 or 2.");
            }
        } catch (NumberFormatException e) {
            System.err.println("Error: Please enter a valid number.");
            return;
        } catch (IllegalArgumentException e) {
            System.err.println(e.getMessage());
            return;
        }

        int digitCount = (choice == 1) ? 6 : 7; // Determine number of digits based on choice
        System.out.println("You selected " + digitCount + "D Lottery.");

        System.out.print("Enter the number of tickets you'd like to generate: ");
        int numTickets = 0;
        try {
            numTickets = Integer.parseInt(scanner.nextLine());
            if (numTickets <= 0) {
                throw new IllegalArgumentException("Number of tickets must be greater than zero.");
            }
        } catch (NumberFormatException e) {
            System.err.println("Error: Please enter a valid number.");
            return;
        } catch (IllegalArgumentException e) {
            System.err.println(e.getMessage());
            return;
        }

        // Generate lottery tickets
        System.out.println("Generating " + numTickets + " lottery ticket(s):");
        List<String> tickets = generateLotteryTickets(digitCount, numTickets);
        for (String ticket : tickets) {
            System.out.println(ticket);
        }

        System.out.println("Good luck!");
        scanner.close();
    }

    /**
     * Generates a list of lottery tickets with random numbers.
     *
     * @param digitCount Number of digits per ticket (6 or 7)
     * @param numTickets Number of tickets to generate
     * @return List of generated lottery tickets
     */
    private static List<String> generateLotteryTickets(int digitCount, int numTickets) {
        List<String> tickets = new ArrayList<>();
        Random random = new Random();

        for (int i = 0; i < numTickets; i++) {
            StringBuilder ticket = new StringBuilder();
            for (int j = 0; j < digitCount; j++) {
                // Generate a random digit (0-9)
                ticket.append(random.nextInt(10));
            }
            tickets.add(ticket.toString());
        }

        return tickets;
    }
}
```
