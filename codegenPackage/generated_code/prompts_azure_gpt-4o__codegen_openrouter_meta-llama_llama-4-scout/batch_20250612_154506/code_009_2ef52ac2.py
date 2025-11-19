"""
Generated Code Metadata:
========================
Original URL: https://swanbay.dip.vn
Prompt: Write a Java program to simulate a fish shooting game with rewards, inspired by the VZ99 fish shooting game features.
Generated: DETERMINISTIC_2ef52ac25f2de415
Batch ID: 20250612_154506
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
 * Simulates a fish shooting game with rewards.
 */
public class FishShootingGame {

    // Game constants
    private static final int MAX_FISH = 10;
    private static final int MAX_BULLETS = 20;
    private static final int GAME_ROUNDS = 5;

    // Fish types with their respective rewards and difficulties
    private enum Fish {
        GOLDFISH(10, 1),
        SILVERFISH(20, 2),
        SHARK(50, 5);

        private final int reward;
        private final int difficulty;

        Fish(int reward, int difficulty) {
            this.reward = reward;
            this.difficulty = difficulty;
        }

        public int getReward() {
            return reward;
        }

        public int getDifficulty() {
            return difficulty;
        }
    }

    public static void main(String[] args) {
        // Initialize game
        FishShootingGame game = new FishShootingGame();
        game.startGame();
    }

    /**
     * Starts a new game.
     */
    public void startGame() {
        // Initialize player score and bullets
        int playerScore = 0;
        int bullets = MAX_BULLETS;

        // Game loop
        for (int round = 1; round <= GAME_ROUNDS; round++) {
            System.out.println("\nRound " + round + ":");
            System.out.println("Score: " + playerScore);
            System.out.println("Bullets: " + bullets);

            // Spawn random fish
            Fish[] fishArray = spawnFish(MAX_FISH);

            // Display fish
            displayFish(fishArray);

            // Player shoots fish
            bullets = shootFish(fishArray, bullets, playerScore);

            // Update player score
            playerScore = updateScore(fishArray, playerScore);

            // Check game over
            if (bullets <= 0) {
                System.out.println("\nGame Over! You ran out of bullets.");
                break;
            }
        }

        // Display final score
        System.out.println("\nFinal Score: " + playerScore);
    }

    /**
     * Spawns an array of random fish.
     *
     * @param count The number of fish to spawn.
     * @return An array of Fish.
     */
    private Fish[] spawnFish(int count) {
        Fish[] fishArray = new Fish[count];
        Random random = new Random();

        for (int i = 0; i < count; i++) {
            Fish[] values = Fish.values();
            fishArray[i] = values[random.nextInt(values.length)];
        }

        return fishArray;
    }

    /**
     * Displays the fish array.
     *
     * @param fishArray The array of Fish to display.
     */
    private void displayFish(Fish[] fishArray) {
        for (int i = 0; i < fishArray.length; i++) {
            System.out.println((i + 1) + ". " + fishArray[i].name() + " (Reward: " + fishArray[i].getReward() + ", Difficulty: " + fishArray[i].getDifficulty() + ")");
        }
    }

    /**
     * Allows the player to shoot fish and updates the bullet count.
     *
     * @param fishArray The array of Fish to shoot.
     * @param bullets   The current number of bullets.
     * @param playerScore The current player score.
     * @return The updated bullet count.
     */
    private int shootFish(Fish[] fishArray, int bullets, int playerScore) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.print("Enter the number of the fish to shoot (or -1 to skip): ");
            int choice = scanner.nextInt();

            if (choice == -1) {
                break;
            }

            if (choice < 1 || choice > fishArray.length) {
                System.out.println("Invalid choice. Please try again.");
                continue;
            }

            if (bullets <= 0) {
                System.out.println("You have no bullets left!");
                break;
            }

            // Simulate shooting
            Fish fish = fishArray[choice - 1];
            System.out.println("You shot a " + fish.name() + "!");

            // Decrease bullets
            bullets--;

            // Check if fish is hit
            if (hitFish(fish)) {
                System.out.println("You hit the " + fish.name() + "!");
            } else {
                System.out.println("You missed the " + fish.name() + "!");
            }
        }

        return bullets;
    }

    /**
     * Updates the player score based on the fish array.
     *
     * @param fishArray   The array of Fish.
     * @param playerScore The current player score.
     * @return The updated player score.
     */
    private int updateScore(Fish[] fishArray, int playerScore) {
        // For simplicity, assume all fish are hit and add their rewards
        for (Fish fish : fishArray) {
            playerScore += fish.getReward();
        }

        return playerScore;
    }

    /**
     * Simulates hitting a fish.
     *
     * @param fish The Fish to hit.
     * @return True if the fish is hit, false otherwise.
     */
    private boolean hitFish(Fish fish) {
        // For simplicity, assume a 50% chance of hitting the fish
        Random random = new Random();
        return random.nextDouble() < 0.5;
    }
}
```
