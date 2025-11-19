"""
Generated Code Metadata:
========================
Original URL: https://raydiumnodes.com
Prompt: Generate Java code for implementing a spin-based game mechanic with instant cash rewards and jackpot opportunities, inspired by LUCKSVIP's gameplay.
Generated: DETERMINISTIC_c086f3313b0add10
Batch ID: 20250622_204650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.Random;
import java.util.Scanner;

/**
 * SpinGame class implements a simple spin-based game mechanic
 * with instant cash rewards and jackpot opportunities.
 */
public class SpinGame {
    private static final int JACKPOT_THRESHOLD = 100; // Threshold for jackpot
    private static final int SPIN_COST = 10; // Cost to spin
    private static final int MAX_REWARD = 50; // Maximum cash reward
    private static final int MIN_REWARD = 5; // Minimum cash reward
    private int playerBalance; // Player's current balance
    private Random random; // Random number generator

    /**
     * Constructor to initialize the game with a starting balance.
     *
     * @param startingBalance Initial balance for the player.
     */
    public SpinGame(int startingBalance) {
        this.playerBalance = startingBalance;
        this.random = new Random();
    }

    /**
     * Spins the wheel and returns the reward.
     *
     * @return The cash reward from the spin.
     */
    public int spin() {
        if (playerBalance < SPIN_COST) {
            throw new IllegalStateException("Insufficient balance to spin.");
        }

        // Deduct the cost of spinning
        playerBalance -= SPIN_COST;

        // Generate a random reward
        int reward = random.nextInt(MAX_REWARD - MIN_REWARD + 1) + MIN_REWARD;

        // Check for jackpot
        if (reward >= JACKPOT_THRESHOLD) {
            reward *= 2; // Double the reward for jackpot
            System.out.println("Jackpot! You won a double reward!");
        }

        // Add the reward to the player's balance
        playerBalance += reward;
        return reward;
    }

    /**
     * Returns the current balance of the player.
     *
     * @return The player's current balance.
     */
    public int getBalance() {
        return playerBalance;
    }

    /**
     * Main method to run the SpinGame.
     *
     * @param args Command line arguments.
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your starting balance: ");
        
        // Validate input for starting balance
        int startingBalance;
        try {
            startingBalance = Integer.parseInt(scanner.nextLine());
            if (startingBalance < 0) {
                throw new NumberFormatException("Balance cannot be negative.");
            }
        } catch (NumberFormatException e) {
            System.out.println("Invalid input. Please enter a valid starting balance.");
            return;
        }

        SpinGame game = new SpinGame(startingBalance);
        String command;

        // Game loop
        do {
            System.out.println("Current balance: " + game.getBalance());
            System.out.print("Type 'spin' to spin the wheel or 'exit' to quit: ");
            command = scanner.nextLine().trim().toLowerCase();

            if ("spin".equals(command)) {
                try {
                    int reward = game.spin();
                    System.out.println("You won: " + reward + "!");
                } catch (IllegalStateException e) {
                    System.out.println(e.getMessage());
                }
            } else if (!"exit".equals(command)) {
                System.out.println("Invalid command. Please type 'spin' or 'exit'.");
            }
        } while (!"exit".equals(command));

        System.out.println("Thank you for playing! Your final balance is: " + game.getBalance());
        scanner.close();
    }
}
```
