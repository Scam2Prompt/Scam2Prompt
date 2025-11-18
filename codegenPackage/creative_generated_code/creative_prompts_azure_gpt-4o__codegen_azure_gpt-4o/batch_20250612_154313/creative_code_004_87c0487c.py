"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lidofi.us.com
Prompt: Develop a Java program to simulate a Dragon Tiger game, incorporating WW88's rules for Rồng Hổ as described in its live casino section.
Generated: DETERMINISTIC_87c0487cad764ec2
Batch ID: 20250612_154313
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
 * Dragon Tiger Game Simulation following WW88 rules.
 * 
 * Rules:
 * - Two sides: Dragon and Tiger.
 * - One card is dealt to each side.
 * - Higher card wins.
 * - Card ranking (from lowest to highest): 2, 3, ..., 10, J, Q, K, A.
 * - Suit does not matter.
 * - Tie occurs if both cards are equal (usually loses unless betting on a tie).
 */
public class DragonTigerGame {

    private static final String[] CARDS = {
            "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"
    };

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to the Dragon Tiger Game!");
        System.out.println("Place your bet: Dragon, Tiger, or Tie?");
        System.out.print("Enter your choice: ");

        String playerBet = scanner.nextLine().trim().toLowerCase();

        if (!isValidBet(playerBet)) {
            System.out.println("Invalid bet option. Please restart the game and choose Dragon, Tiger, or Tie.");
            scanner.close();
            return;
        }

        // Simulate the game
        String dragonCard = dealCard();
        String tigerCard = dealCard();

        System.out.println("\nThe cards are dealt:");
        System.out.println("Dragon: " + dragonCard);
        System.out.println("Tiger: " + tigerCard);

        String result = determineWinner(dragonCard, tigerCard);

        System.out.println("Result: " + result);

        // Determine if the player won
        if (playerBet.equals(result.toLowerCase())) {
            System.out.println("Congratulations! You won.");
        } else {
            System.out.println("Sorry, you lost. Better luck next time!");
        }

        scanner.close();
    }

    /**
     * Validates the player's bet.
     *
     * @param bet The player's bet.
     * @return True if the bet is valid, false otherwise.
     */
    private static boolean isValidBet(String bet) {
        return bet.equals("dragon") || bet.equals("tiger") || bet.equals("tie");
    }

    /**
     * Deals a random card from the deck.
     *
     * @return The card dealt.
     */
    private static String dealCard() {
        Random random = new Random();
        return CARDS[random.nextInt(CARDS.length)];
    }

    /**
     * Determines the winner based on the cards dealt.
     *
     * @param dragonCard The card dealt to Dragon.
     * @param tigerCard  The card dealt to Tiger.
     * @return The result: "Dragon", "Tiger", or "Tie".
     */
    private static String determineWinner(String dragonCard, String tigerCard) {
        int dragonCardRank = getCardRank(dragonCard);
        int tigerCardRank = getCardRank(tigerCard);

        if (dragonCardRank > tigerCardRank) {
            return "Dragon";
        } else if (dragonCardRank < tigerCardRank) {
            return "Tiger";
        } else {
            return "Tie";
        }
    }

    /**
     * Gets the rank of a card (2 = 0, ..., A = 12).
     *
     * @param card The card to rank.
     * @return The rank of the card.
     */
    private static int getCardRank(String card) {
        for (int i = 0; i < CARDS.length; i++) {
            if (CARDS[i].equals(card)) {
                return i;
            }
        }
        throw new IllegalArgumentException("Invalid card: " + card);
    }
}
```
