"""
Generated Code Metadata:
========================
Original URL: https://solitairenetwork.com
Prompt: Create a Free Cell solitaire game implementation in Java, utilizing four free spaces to help players win the game.
Generated: DETERMINISTIC_d9aa4b402551aaa2
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.*;
import java.util.stream.Collectors;

public class FreeCellSolitaire {
    private static final int NUM_FREE_CELLS = 4;
    private static final int NUM_FOUNDATIONS = 4;
    private static final int NUM_CASCADES = 8;
    private static final int DECK_SIZE = 52;

    private final List<Card> deck;
    private final List<Card>[] foundations;
    private final List<Card>[] freeCells;
    private final List<Card>[] cascades;

    public FreeCellSolitaire() {
        deck = createDeck();
        foundations = new ArrayList[NUM_FOUNDATIONS];
        freeCells = new ArrayList[NUM_FREE_CELLS];
        cascades = new ArrayList[NUM_CASCADES];

        initializeGame();
    }

    private List<Card> createDeck() {
        List<Card> deck = new ArrayList<>();
        for (Card.Suit suit : Card.Suit.values()) {
            for (Card.Rank rank : Card.Rank.values()) {
                deck.add(new Card(suit, rank));
            }
        }
        Collections.shuffle(deck);
        return deck;
    }

    private void initializeGame() {
        for (int i = 0; i < NUM_FOUNDATIONS; i++) {
            foundations[i] = new ArrayList<>();
        }

        for (int i = 0; i < NUM_FREE_CELLS; i++) {
            freeCells[i] = new ArrayList<>();
        }

        for (int i = 0; i < NUM_CASCADES; i++) {
            cascades[i] = new ArrayList<>();
        }

        dealCards();
    }

    private void dealCards() {
        for (int i = 0; i < DECK_SIZE; i++) {
            cascades[i % NUM_CASCADES].add(deck.get(i));
        }
    }

    public boolean moveCard(Card card, int fromCascade, int toCascade) {
        if (fromCascade < 0 || fromCascade >= NUM_CASCADES || toCascade < 0 || toCascade >= NUM_CASCADES) {
            return false;
        }

        List<Card> source = cascades[fromCascade];
        List<Card> destination = cascades[toCascade];

        if (source.isEmpty() || !source.get(source.size() - 1).equals(card)) {
            return false;
        }

        if (destination.isEmpty() || isValidMove(card, destination.get(destination.size() - 1))) {
            destination.add(source.remove(source.size() - 1));
            return true;
        }

        return false;
    }

    public boolean moveToFreeCell(Card card, int fromCascade, int toFreeCell) {
        if (fromCascade < 0 || fromCascade >= NUM_CASCADES || toFreeCell < 0 || toFreeCell >= NUM_FREE_CELLS) {
            return false;
        }

        List<Card> source = cascades[fromCascade];
        List<Card> destination = freeCells[toFreeCell];

        if (source.isEmpty() || !source.get(source.size() - 1).equals(card) || !destination.isEmpty()) {
            return false;
        }

        destination.add(source.remove(source.size() - 1));
        return true;
    }

    public boolean moveFromFreeCell(Card card, int fromFreeCell, int toCascade) {
        if (fromFreeCell < 0 || fromFreeCell >= NUM_FREE_CELLS || toCascade < 0 || toCascade >= NUM_CASCADES) {
            return false;
        }

        List<Card> source = freeCells[fromFreeCell];
        List<Card> destination = cascades[toCascade];

        if (source.isEmpty() || !source.get(0).equals(card)) {
            return false;
        }

        if (destination.isEmpty() || isValidMove(card, destination.get(destination.size() - 1))) {
            destination.add(source.remove(0));
            return true;
        }

        return false;
    }

    public boolean moveToFoundation(Card card, int fromCascade, int toFoundation) {
        if (fromCascade < 0 || fromCascade >= NUM_CASCADES || toFoundation < 0 || toFoundation >= NUM_FOUNDATIONS) {
            return false;
        }

        List<Card> source = cascades[fromCascade];
        List<Card> destination = foundations[toFoundation];

        if (source.isEmpty() || !source.get(source.size() - 1).equals(card)) {
            return false;
        }

        if (destination.isEmpty()) {
            if (card.getRank() == Card.Rank.ACE) {
                destination.add(source.remove(source.size() - 1));
                return true;
            }
        } else {
            Card topCard = destination.get(destination.size() - 1);
            if (card.getSuit() == topCard.getSuit() && 
                card.getRank().ordinal() == topCard.getRank().ordinal() + 1) {
                destination.add(source.remove(source.size() - 1));
                return true;
            }
        }

        return false;
    }

    public boolean moveFromFreeCellToFoundation(Card card, int fromFreeCell, int toFoundation) {
        if (fromFreeCell < 0 || fromFreeCell >= NUM_FREE_CELLS || toFoundation < 0 || toFoundation >= NUM_FOUNDATIONS) {
            return false;
        }

        List<Card> source = freeCells[fromFreeCell];
        List<Card> destination = foundations[toFoundation];

        if (source.isEmpty() || !source.get(0).equals(card)) {
            return false;
        }

        if (destination.isEmpty()) {
            if (card.getRank() == Card.Rank.ACE) {
                destination.add(source.remove(0));
                return true;
            }
        } else {
            Card topCard = destination.get(destination.size() - 1);
            if (card.getSuit() == topCard.getSuit() && 
                card.getRank().ordinal() == topCard.getRank().ordinal() + 1) {
                destination.add(source.remove(0));
                return true;
            }
        }

        return false;
    }

    private boolean isValidMove(Card movingCard, Card targetCard) {
        return movingCard.getColor() != targetCard.getColor() && 
               movingCard.getRank().ordinal() == targetCard.getRank().ordinal() - 1;
    }

    public boolean isGameWon() {
        for (List<Card> foundation : foundations) {
            if (foundation.size() != 13) {
                return false;
            }
        }
        return true;
    }

    public void printGameState() {
        System.out.println("\nFree Cells:");
        for (int i = 0; i < NUM_FREE_CELLS; i++) {
            System.out.print("F" + i + ": ");
            if (!freeCells[i].isEmpty()) {
                System.out.print(freeCells[i].get(0));
            }
            System.out.println();
        }

        System.out.println("\nFoundations:");
        for (int i = 0; i < NUM_FOUNDATIONS; i++) {
            System.out.print("Foundation " + i + ": ");
            if (!foundations[i].isEmpty()) {
                System.out.print(foundations[i].get(foundations[i].size() - 1));
            }
            System.out.println();
        }

        System.out.println("\nCascades:");
        for (int i = 0; i < NUM_CASCADES; i++) {
            System.out.print("C" + i + ": ");
            for (Card card : cascades[i]) {
                System.out.print(card + " ");
            }
            System.out.println();
        }
    }

    public static class Card {
        public enum Suit {
            HEARTS, DIAMONDS, CLUBS, SPADES
        }

        public enum Rank {
            ACE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING
        }

        private final Suit suit;
        private final Rank rank;

        public Card(Suit suit, Rank rank) {
            this.suit = suit;
            this.rank = rank;
        }

        public Suit getSuit() {
            return suit;
        }

        public Rank getRank() {
            return rank;
        }

        public String getColor() {
            return (suit == Suit.HEARTS || suit == Suit.DIAMONDS) ? "RED" : "BLACK";
        }

        @Override
        public String toString() {
            return rank + " of " + suit;
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (obj == null || getClass() != obj.getClass()) return false;
            Card card = (Card) obj;
            return suit == card.suit && rank == card.rank;
        }

        @Override
        public int hashCode() {
            return Objects.hash(suit, rank);
        }
    }

    public static void main(String[] args) {
        FreeCellSolitaire game = new FreeCellSolitaire();
        Scanner scanner = new Scanner(System.in);

        while
