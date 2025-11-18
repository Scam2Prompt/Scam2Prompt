"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lidofi.us.com
Prompt: Write a JavaScript function to simulate a blackjack game based on WW88's rules and payout structure.
Generated: DETERMINISTIC_e3f6564051e45711
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates a simplified version of a Blackjack game based on WW88's rules and payout structure.
 * 
 * @class Blackjack
 */
class Blackjack {
    constructor() {
        // Initialize the deck of cards
        this.deck = this.createDeck();
        this.playerHand = [];
        this.dealerHand = [];
        this.gameOver = false;
    }

    /**
     * Creates a standard deck of 52 cards and shuffles it.
     * 
     * @returns {Array} The shuffled deck of cards.
     */
    createDeck() {
        const suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades'];
        const ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'];
        let deck = [];

        suits.forEach(suit => {
            ranks.forEach(rank => {
                deck.push({ suit, rank });
            });
        });

        // Shuffle the deck
        return this.shuffleDeck(deck);
    }

    /**
     * Shuffle the deck using the Fisher-Yates algorithm.
     * 
     * @param {Array} deck - The deck to shuffle.
     * @returns {Array} The shuffled deck.
     */
    shuffleDeck(deck) {
        for (let i = deck.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [deck[i], deck[j]] = [deck[j], deck[i]]; // Swap
        }
        return deck;
    }

    /**
     * Starts a new game of Blackjack.
     */
    startGame() {
        this.deck = this.createDeck();
        this.playerHand = [this.drawCard(), this.drawCard()];
        this.dealerHand = [this.drawCard(), this.drawCard()];
        this.gameOver = false;
        console.log(`Game started! Player's hand: ${this.showHand(this.playerHand)}`);
    }

    /**
     * Draws the top card from the deck.
     * 
     * @returns {Object} The drawn card.
     */
    drawCard() {
        if (this.deck.length === 0) {
            throw new Error("No cards left in the deck.");
        }
        return this.deck.pop();
    }

    /**
     * Displays the hand of cards in a readable format.
     * 
     * @param {Array} hand - The hand to display.
     * @returns {String} The formatted hand.
     */
    showHand(hand) {
        return hand.map(card => `${card.rank} of ${card.suit}`).join(', ');
    }

    /**
     * Calculates the total value of a hand.
     * 
     * @param {Array} hand - The hand to evaluate.
     * @returns {Number} The total value of the hand.
     */
    calculateHandValue(hand) {
        let value = 0;
        let aceCount = 0;

        hand.forEach(card => {
            if (['Jack', 'Queen', 'King'].includes(card.rank)) {
                value += 10;
            } else if (card.rank === 'Ace') {
                value += 11; // Initially count Ace as 11
                aceCount += 1;
            } else {
                value += parseInt(card.rank);
            }
        });

        // Adjust for Aces if total value exceeds 21
        while (value > 21 && aceCount > 0) {
            value -= 10;
            aceCount -= 1;
        }

        return value;
    }

    /**
     * Player makes a choice to hit or stand.
     * 
     * @param {String} choice - The player's choice: 'hit' or 'stand'.
     */
    playerChoice(choice) {
        if (this.gameOver) {
            throw new Error("Game is already over. Please start a new game.");
        }

        if (choice === 'hit') {
            this.playerHand.push(this.drawCard());
            const playerValue = this.calculateHandValue(this.playerHand);
            console.log(`Player's hand: ${this.showHand(this.playerHand)} (Value: ${playerValue})`);
            
            if (playerValue > 21) {
                this.gameOver = true;
                console.log("Player busts! Dealer wins.");
            }
        } else if (choice === 'stand') {
            this.dealerPlay();
        } else {
            throw new Error("Invalid choice. Please choose 'hit' or 'stand'.");
        }
    }

    /**
     * Manages the dealer's play according to the game rules.
     */
    dealerPlay() {
        console.log(`Dealer's hand: ${this.showHand(this.dealerHand)}`);
        while (this.calculateHandValue(this.dealerHand) < 17) {
            this.dealerHand.push(this.drawCard());
            console.log(`Dealer draws a card: ${this.showHand(this.dealerHand)}`);
        }

        const playerValue = this.calculateHandValue(this.playerHand);
        const dealerValue = this.calculateHandValue(this.dealerHand);
        
        console.log(`Final Player's value: ${playerValue}, Dealer's value: ${dealerValue}`);

        if (dealerValue > 21) {
            console.log("Dealer busts! Player wins.");
        } else if (playerValue > dealerValue) {
            console.log("Player wins!");
        } else if (playerValue < dealerValue) {
            console.log("Dealer wins!");
        } else {
            console.log("It's a tie!");
        }
        
        this.gameOver = true;
    }
}

// Example usage
const blackjackGame = new Blackjack();
blackjackGame.startGame();
blackjackGame.playerChoice('hit'); // Player can choose to hit or stand
// blackjackGame.playerChoice('stand'); // Uncomment to stand
```
