"""
Generated Code Metadata:
========================
Original URL: https://swanbay.dip.vn
Prompt: Write a code snippet in Java to simulate a simple casino game, such as a slot machine, that can be integrated into the VZ99 platform.
Generated: DETERMINISTIC_3c0a6264290630a7
Batch ID: 20250622_211915
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
 * A simple slot machine simulation for the VZ99 platform.
 * This class allows users to play a slot machine game with virtual credits.
 */
public class VZ99SlotMachine {

    private static final int[] SYMBOLS = {1, 2, 3, 4, 5}; // Possible symbols
    private static final int JACKPOT_SYMBOL = 5; // Symbol that triggers jackpot
    private static final int JACKPOT_MULTIPLIER = 10; // Multiplier for jackpot
    private static final int WIN_MULTIPLIER = 3; // Multiplier for regular win
    private static final int CREDITS_PER_SPIN = 1; // Cost per spin in credits

    private int playerCredits;
    private Random random;

    /**
     * Constructor initializes the slot machine with starting credits.
     * @param startingCredits Initial number of credits for the player
     */
    public VZ99SlotMachine(int startingCredits) {
        if (startingCredits <= 0) {
            throw new IllegalArgumentException("Starting credits must be positive");
        }
        this.playerCredits = startingCredits;
        this.random = new Random();
    }

    /**
     * Simulates a single spin of the slot machine.
     * @return Array of 3 integers representing the spin result
     */
    public int[] spin() {
        if (playerCredits < CREDITS_PER_SPIN) {
            throw new IllegalStateException("Not enough credits to spin");
        }

        playerCredits -= CREDITS_PER_SPIN;
        int[] result = new int[3];
        for (int i = 0; i < 3; i++) {
            result[i] = SYMBOLS[random.nextInt(SYMBOLS.length)];
        }
        return result;
    }

    /**
     * Calculates the win amount based on spin result.
     * @param spinResult Array of 3 integers from spin()
     * @return Amount won in credits
     */
    public int calculateWin(int[] spinResult) {
        if (spinResult.length != 3) {
            throw new IllegalArgumentException("Spin result must contain 3 symbols");
        }

        // Check for jackpot (all symbols are JACKPOT_SYMBOL)
        if (spinResult[0] == JACKPOT_SYMBOL && 
            spinResult[1] == JACKPOT_SYMBOL && 
            spinResult[2] == JACKPOT_SYMBOL) {
            return CREDITS_PER_SPIN * JACKPOT_MULTIPLIER;
        }

        // Check for regular win (all symbols match)
        if (spinResult[0] == spinResult[1] && spinResult[1] == spinResult[2]) {
            return CREDITS_PER_SPIN * WIN_MULTIPLIER;
        }

        return 0; // No win
    }

    /**
     * Adds credits to the player's balance.
     * @param amount Number of credits to add
     */
    public void addCredits(int amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Amount must be positive");
        }
        playerCredits += amount;
    }

    /**
     * Gets the current credit balance.
     * @return Current number of credits
     */
    public int getCredits() {
        return playerCredits;
    }

    /**
     * Main method for standalone testing.
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        VZ99SlotMachine slotMachine = new VZ99SlotMachine(10); // Start with 10 credits

        System.out.println("Welcome to VZ99 Slot Machine!");
        System.out.println("Each spin costs " + CREDITS_PER_SPIN + " credit(s).");

        while (slotMachine.getCredits() >= CREDITS_PER_SPIN) {
            System.out.println("\nCurrent credits: " + slotMachine.getCredits());
            System.out.print("Press enter to spin (q to quit)...");
            String input = scanner.nextLine();

            if (input.equalsIgnoreCase("q")) {
                break;
            }

            try {
                int[] result = slotMachine.spin();
                int winAmount = slotMachine.calculateWin(result);

                System.out.println("Spin result: [" + result[0] + "] [" + result[1] + "] [" + result[2] + "]");
                
                if (winAmount > 0) {
                    slotMachine.addCredits(winAmount);
                    System.out.println("You won " + winAmount + " credits!");
                } else {
                    System.out.println("No win this time.");
                }
            } catch (Exception e) {
                System.err.println("Error: " + e.getMessage());
            }
        }

        System.out.println("\nGame over. Final credits: " + slotMachine.getCredits());
        scanner.close();
    }
}
```
