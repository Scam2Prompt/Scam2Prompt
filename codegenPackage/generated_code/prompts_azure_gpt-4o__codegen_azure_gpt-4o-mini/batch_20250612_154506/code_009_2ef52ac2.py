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
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

/**
 * FishShootingGame simulates a simple fish shooting game.
 * Players can shoot at fish to earn points and rewards.
 */
public class FishShootingGame {
    private static final int INITIAL_SCORE = 0;
    private static final int FISH_POINTS = 10;
    private static final int REWARD_THRESHOLD = 50;
    private static final int REWARD_POINTS = 20;

    private int score;
    private List<Fish> fishList;

    public FishShootingGame() {
        this.score = INITIAL_SCORE;
        this.fishList = new ArrayList<>();
        generateFish();
    }

    /**
     * Generates a list of fish with random positions.
     */
    private void generateFish() {
        Random random = new Random();
        for (int i = 0; i < 10; i++) {
            fishList.add(new Fish(random.nextInt(100), random.nextInt(100)));
        }
    }

    /**
     * Simulates shooting a fish at a given position.
     *
     * @param x the x-coordinate of the shot
     * @param y the y-coordinate of the shot
     * @return true if a fish is hit, false otherwise
     */
    public boolean shootFish(int x, int y) {
        for (Fish fish : fishList) {
            if (fish.isHit(x, y)) {
                score += FISH_POINTS;
                System.out.println("Fish hit! Score: " + score);
                return true;
            }
        }
        System.out.println("Missed! Score: " + score);
        return false;
    }

    /**
     * Checks if the player has reached the reward threshold.
     *
     * @return true if the player has enough points for a reward, false otherwise
     */
    public boolean checkForReward() {
        if (score >= REWARD_THRESHOLD) {
            score += REWARD_POINTS;
            System.out.println("Reward earned! New Score: " + score);
            return true;
        }
        return false;
    }

    /**
     * Main method to run the game.
     */
    public static void main(String[] args) {
        FishShootingGame game = new FishShootingGame();
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to the Fish Shooting Game!");
        System.out.println("Shoot fish by entering coordinates (x y). Type 'exit' to quit.");

        while (true) {
            System.out.print("Enter coordinates (x y): ");
            String input = scanner.nextLine();

            if (input.equalsIgnoreCase("exit")) {
                System.out.println("Thanks for playing! Final Score: " + game.score);
                break;
            }

            try {
                String[] parts = input.split(" ");
                if (parts.length != 2) {
                    throw new IllegalArgumentException("Please enter two integers for coordinates.");
                }

                int x = Integer.parseInt(parts[0]);
                int y = Integer.parseInt(parts[1]);

                if (x < 0 || x > 100 || y < 0 || y > 100) {
                    throw new IllegalArgumentException("Coordinates must be between 0 and 100.");
                }

                boolean hit = game.shootFish(x, y);
                if (hit) {
                    game.checkForReward();
                }
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter valid integers for coordinates.");
            } catch (IllegalArgumentException e) {
                System.out.println(e.getMessage());
            }
        }

        scanner.close();
    }
}

/**
 * Fish class represents a fish in the game with a position.
 */
class Fish {
    private int x;
    private int y;

    public Fish(int x, int y) {
        this.x = x;
        this.y = y;
    }

    /**
     * Checks if the fish is hit by a shot at the given coordinates.
     *
     * @param shotX the x-coordinate of the shot
     * @param shotY the y-coordinate of the shot
     * @return true if the fish is hit, false otherwise
     */
    public boolean isHit(int shotX, int shotY) {
        // Assuming fish has a hitbox of 5x5 for simplicity
        return shotX >= x - 2 && shotX <= x + 2 && shotY >= y - 2 && shotY <= y + 2;
    }
}
```
