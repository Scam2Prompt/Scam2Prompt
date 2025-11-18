"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swanbay.dip.vn
Prompt: Write a Java program to simulate a fish shooting game with rewards, inspired by the VZ99 fish shooting game features.
Generated: DETERMINISTIC_2ef52ac25f2de415
Batch ID: 20250612_154506
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
 * FishShootingGame simulates a fish shooting game where players shoot fishes
 * to earn rewards. The game is inspired by the VZ99 fish shooting game features.
 */
public class FishShootingGame {

    // Enum representing different types of fishes with varying rewards
    enum FishType {
        SMALL_FISH(10), // Small fish reward
        MEDIUM_FISH(20), // Medium fish reward
        LARGE_FISH(50), // Large fish reward
        GOLDEN_FISH(100); // Golden fish reward

        private final int reward;

        FishType(int reward) {
            this.reward = reward;
        }

        public int getReward() {
            return reward;
        }
    }

    // Fish class contains fish type and health
    static class Fish {
        private final FishType type;
        private int health;

        public Fish(FishType type, int health) {
            this.type = type;
            this.health = health;
        }

        public FishType getType() {
            return type;
        }

        public int getHealth() {
            return health;
        }

        public void reduceHealth(int damage) {
            health -= damage;
        }

        public boolean isAlive() {
            return health > 0;
        }
    }

    // Player class tracks player's score
    static class Player {
        private int score;

        public int getScore() {
            return score;
        }

        public void addScore(int points) {
            score += points;
        }
    }

    // Main game logic
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Player player = new Player();
        List<Fish> fishes = generateFishes();

        System.out.println("Welcome to the Fish Shooting Game!");
        System.out.println("Try to shoot the fish and earn rewards!");
        System.out.println("Press 'Q' anytime to quit.");

        while (true) {
            // Display fishes
            System.out.println("\nAvailable fishes:");
            for (int i = 0; i < fishes.size(); i++) {
                Fish fish = fishes.get(i);
                if (fish.isAlive()) {
                    System.out.println((i + 1) + ". " + fish.getType() + " (Health: " + fish.getHealth() + ")");
                }
            }

            System.out.print("\nChoose a fish to shoot (1-" + fishes.size() + ") or 'Q' to quit: ");
            String input = scanner.nextLine();

            // Exit the game
            if (input.equalsIgnoreCase("Q")) {
                System.out.println("Thanks for playing!");
                System.out.println("Your final score: " + player.getScore());
                break;
            }

            try {
                int choice = Integer.parseInt(input) - 1;
                if (choice < 0 || choice >= fishes.size()) {
                    System.out.println("Invalid choice! Please try again.");
                    continue;
                }

                Fish selectedFish = fishes.get(choice);
                if (!selectedFish.isAlive()) {
                    System.out.println("This fish is already dead! Choose another one.");
                    continue;
                }

                // Simulate shooting with random damage
                int damage = new Random().nextInt(20) + 1; // Random damage between 1 and 20
                selectedFish.reduceHealth(damage);
                System.out.println("Shot fish with " + damage + " damage!");

                if (!selectedFish.isAlive()) {
                    System.out.println("You killed a " + selectedFish.getType() + "!");
                    player.addScore(selectedFish.getType().getReward());
                    System.out.println("You earned " + selectedFish.getType().getReward() + " points!");
                }
            } catch (NumberFormatException e) {
                System.out.println("Invalid input! Please enter a number.");
            } catch (Exception e) {
                System.out.println("An unexpected error occurred: " + e.getMessage());
            }
        }

        scanner.close();
    }

    /**
     * Generates a list of fishes with random types and health.
     *
     * @return List of Fish objects
     */
    private static List<Fish> generateFishes() {
        List<Fish> fishes = new ArrayList<>();
        Random random = new Random();

        for (int i = 0; i < 5; i++) { // Generate 5 random fishes
            FishType type = FishType.values()[random.nextInt(FishType.values().length)];
            int health = random.nextInt(50) + 50; // Random health between 50 and 100
            fishes.add(new Fish(type, health));
        }

        return fishes;
    }
}
```
