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
 * FishShootingGame simulates a fish shooting game where players can shoot fish
 * to earn rewards. It includes basic game mechanics, such as shooting and scoring.
 */
public class FishShootingGame {
    // List to hold all fish in the game
    private List<Fish> fishList;
    // Player score
    private int score;
    // Random number generator for fish movements
    private Random random;

    /**
     * Constructor to initialize the game
     */
    public FishShootingGame() {
        this.fishList = new ArrayList<>();
        this.score = 0;
        this.random = new Random();
        initializeFish();
    }

    /**
     * Initializes the list of fish with random properties
     */
    private void initializeFish() {
        for (int i = 0; i < 10; i++) {
            fishList.add(new Fish("Fish-" + (i + 1), random.nextInt(20) + 1));
        }
    }

    /**
     * Simulates shooting a fish by its index
     * 
     * @param index Index of the fish to be shot
     * @return True if the fish was successfully shot; false otherwise
     */
    public boolean shootFish(int index) {
        if (index < 0 || index >= fishList.size()) {
            System.out.println("Invalid fish index! Please try again.");
            return false;
        }
        Fish fish = fishList.get(index);
        if (fish.isAlive()) {
            fish.setAlive(false);
            score += fish.getReward();
            System.out.println("You shot " + fish.getName() + "! You earned " + fish.getReward() + " points.");
            return true;
        } else {
            System.out.println("This fish has already been shot!");
            return false;
        }
    }

    /**
     * Displays the current score and the list of fish
     */
    public void displayStatus() {
        System.out.println("Current Score: " + score);
        for (int i = 0; i < fishList.size(); i++) {
            Fish fish = fishList.get(i);
            System.out.println((i + 1) + ": " + fish.getName() + " (Reward: " + fish.getReward() + ", Alive: " + fish.isAlive() + ")");
        }
    }

    /**
     * Main method to run the game
     * 
     * @param args Command line arguments
     */
    public static void main(String[] args) {
        FishShootingGame game = new FishShootingGame();
        Scanner scanner = new Scanner(System.in);
        String input;

        while (true) {
            game.displayStatus();
            System.out.println("Enter the fish number to shoot (or 'exit' to quit): ");
            input = scanner.nextLine();

            if (input.equalsIgnoreCase("exit")) {
                System.out.println("Exiting the game. Final Score: " + game.score);
                break;
            }

            try {
                int fishIndex = Integer.parseInt(input) - 1; // Convert to zero-based index
                game.shootFish(fishIndex);
            } catch (NumberFormatException e) {
                System.out.println("Please enter a valid integer or 'exit' to quit.");
            }
        }
        scanner.close();
    }
}

/**
 * Represents a fish in the game with a name, reward, and status of being alive
 */
class Fish {
    private String name;
    private int reward;
    private boolean alive;

    /**
     * Constructs a Fish object
     * 
     * @param name   The name of the fish
     * @param reward The reward points for shooting the fish
     */
    public Fish(String name, int reward) {
        this.name = name;
        this.reward = reward;
        this.alive = true; // Fish starts off alive
    }

    public String getName() {
        return name;
    }

    public int getReward() {
        return reward;
    }

    public boolean isAlive() {
        return alive;
    }

    public void setAlive(boolean alive) {
        this.alive = alive;
    }
}
```
