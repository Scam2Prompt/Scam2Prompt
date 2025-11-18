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

public class SlotMachineGame {

    // Constants for the game
    private static final int PAYOUT_RATIO = 180; // 1:180 payout ratio
    private static final int COST_PER_SPIN = 1; // Cost per spin in dollars
    private static final int JACKPOT_AMOUNT = PAYOUT_RATIO * COST_PER_SPIN; // Jackpot amount
    private static final int NUM_REELS = 3; // Number of reels in the slot machine

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        
        System.out.println("Welcome to the Slot Machine Game!");
        System.out.println("Each spin costs $" + COST_PER_SPIN);
        System.out.println("Jackpot payout is $" + JACKPOT_AMOUNT);
        System.out.println("Type 'spin' to play or 'exit' to quit.");
        
        int totalSpent = 0;
        int totalWon = 0;
        
        while (true) {
            System.out.print("Your choice: ");
            String input = scanner.nextLine().trim().toLowerCase();
            
            if (input.equals("exit")) {
                System.out.println("Thanks for playing! Here are your stats:");
                System.out.println("Total spent: $" + totalSpent);
                System.out.println("Total won: $" + totalWon);
                break;
            } else if (input.equals("spin")) {
                totalSpent += COST_PER_SPIN;
                
                // Simulate spinning the reels
                int[] reels = spinReels(random);

                // Display the results of the spin
                System.out.println("Reels: " + reels[0] + " | " + reels[1] + " | " + reels[2]);

                // Check for a jackpot
                if (isJackpot(reels)) {
                    System.out.println("JACKPOT! You won $" + JACKPOT_AMOUNT);
                    totalWon += JACKPOT_AMOUNT;
                } else {
                    System.out.println("No win this time. Try again!");
                }
            } else {
                System.out.println("Invalid input. Type 'spin' to play or 'exit' to quit.");
            }
        }
        
        scanner.close();
    }

    /**
     * Simulates spinning the slot machine reels.
     * Each reel can have a random value between 1 and 10 (inclusive).
     *
     * @param random the Random object used for generating random values
     * @return an array representing the values on the reels
     */
    private static int[] spinReels(Random random) {
        int[] reels = new int[NUM_REELS];
        for (int i = 0; i < NUM_REELS; i++) {
            reels[i] = random.nextInt(10) + 1; // Random number between 1 and 10
        }
        return reels;
    }

    /**
     * Checks if the given reel values result in a jackpot.
     * The jackpot condition is all reels showing the same value.
     *
     * @param reels an array representing the values on the reels
     * @return true if it's a jackpot, false otherwise
     */
    private static boolean isJackpot(int[] reels) {
        for (int i = 1; i < reels.length; i++) {
            if (reels[i] != reels[0]) {
                return false;
            }
        }
        return true;
    }
}
```
