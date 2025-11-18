"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swanbay.dip.vn
Prompt: Write Java code to simulate a slot machine game using the payout ratio of 1:180 as described on the VZ99 website.
Generated: DETERMINISTIC_5d9d051b44ebc8f2
Batch ID: 20250612_154506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.util.Random;
import java.util.Scanner;

/**
 * A simple simulation of a slot machine game.
 * The game has a payout ratio of 1:180.
 */
public class SlotMachineGame {

    private static final int PAYOUT_RATIO = 180; // Payout ratio
    private static final int MAX_SPINS = 100; // Maximum number of spins
    private static final Random RANDOM = new Random(); // Random number generator

    /**
     * Main method to run the slot machine game.
     * @param args Command line arguments
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int totalBalance = 1000; // Starting balance
        int spins = 0; // Count of spins

        System.out.println("Welcome to the Slot Machine Game!");
        System.out.println("Your starting balance is: $" + totalBalance);

        while (totalBalance > 0 && spins < MAX_SPINS) {
            System.out.print("Press Enter to spin or type 'exit' to quit: ");
            String input = scanner.nextLine();

            if (input.equalsIgnoreCase("exit")) {
                break;
            }

            totalBalance = spinSlotMachine(totalBalance);
            spins++;

            if (totalBalance <= 0) {
                System.out.println("You have run out of money! Game Over.");
            } else {
                System.out.println("Your current balance is: $" + totalBalance);
            }
        }

        System.out.println("Thank you for playing! Your final balance is: $" + totalBalance);
        scanner.close();
    }

    /**
     * Simulates a spin of the slot machine.
     * @param balance Current balance of the player
     * @return Updated balance after the spin
     */
    private static int spinSlotMachine(int balance) {
        // Define possible outcomes (simple representation)
        String[] outcomes = { "Cherry", "Lemon", "Orange", "Plum", "Bell", "Bar", "Seven" };
        
        // Generate random outcomes for three slots
        String slot1 = outcomes[RANDOM.nextInt(outcomes.length)];
        String slot2 = outcomes[RANDOM.nextInt(outcomes.length)];
        String slot3 = outcomes[RANDOM.nextInt(outcomes.length)];

        System.out.println("Spinning... " + slot1 + " | " + slot2 + " | " + slot3);

        // Check for win condition (all three slots match)
        if (slot1.equals(slot2) && slot2.equals(slot3)) {
            int payout = calculatePayout(balance);
            balance += payout; // Add payout to balance
            System.out.println("Congratulations! You win: $" + payout);
        } else {
            balance -= 10; // Deduct cost of spin
            System.out.println("Sorry, you lost $10.");
        }

        return balance;
    }

    /**
     * Calculates the payout based on the current balance.
     * @param balance Current balance of the player
     * @return Payout amount
     */
    private static int calculatePayout(int balance) {
        // Ensure that the payout does not exceed the total balance
        return Math.min(balance / PAYOUT_RATIO, 100); // Cap payout to a maximum of $100
    }
}
```
