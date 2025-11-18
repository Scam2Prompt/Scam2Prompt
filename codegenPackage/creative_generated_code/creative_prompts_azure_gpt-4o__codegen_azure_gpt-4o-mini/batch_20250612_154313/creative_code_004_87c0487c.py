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
 * A simple simulation of the Dragon Tiger game following the WW88 rules.
 * The game consists of two hands: Dragon and Tiger. Each hand is dealt one card,
 * and the hand with the higher card wins. The Ace is the lowest card and the King is the highest.
 */
public class DragonTigerGame {

    private static final String[] SUITS = {"Hearts", "Diamonds", "Clubs", "Spades"};
    private static final String[] RANKS = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"};
    private static final int NUM_CARDS = RANKS.length;

    private static class Card {
        private final String rank;
        private final String suit;

        public Card(String rank, String suit) {
            this.rank = rank;
            this.suit = suit;
        }

        public int getValue() {
            return getRankValue(rank);
        }

        @Override
        public String toString() {
            return rank + " of " + suit;
        }

        private int getRankValue(String rank) {
            switch (rank) {
                case "A": return 1;
                case "2": return 2;
                case "3": return 3;
                case "4": return 4;
                case "5": return 5;
                case "6": return 6;
                case "7": return 7;
                case "8": return 8;
                case "9": return 9;
                case "10": return 10;
                case "J": return 11;
                case "Q": return 12;
                case "K": return 13;
                default: throw new IllegalArgumentException("Invalid card rank: " + rank);
            }
        }
    }

    /**
     * Deals a random card from the deck.
     * @return a new Card object representing the dealt card.
     */
    private Card dealCard() {
        Random random = new Random();
        String rank = RANKS[random.nextInt(NUM_CARDS)];
        String suit = SUITS[random.nextInt(SUITS.length)];
        return new Card(rank, suit);
    }

    /**
     * Main method to run the game.
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        DragonTigerGame game = new DragonTigerGame();

        // Welcome message
        System.out.println("Welcome to Dragon Tiger!");
        System.out.println("Press Enter to deal the cards.");
        scanner.nextLine();

        try {
            // Deal cards for Dragon and Tiger
            Card dragonCard = game.dealCard();
            Card tigerCard = game.dealCard();

            // Display the cards
            System.out.println("Dragon's card: " + dragonCard);
            System.out.println("Tiger's card: " + tigerCard);

            // Determine the winner
            if (dragonCard.getValue() > tigerCard.getValue()) {
                System.out.println("Dragon wins!");
            } else if (dragonCard.getValue() < tigerCard.getValue()) {
                System.out.println("Tiger wins!");
            } else {
                System.out.println("It's a tie!");
            }
        } catch (Exception e) {
            System.err.println("An error occurred during the game: " + e.getMessage());
        } finally {
            // Clean up resources
            scanner.close();
        }
    }
}
```
