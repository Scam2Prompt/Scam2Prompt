"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://treasury.casino
Prompt: Create a C# application that simulates a game of Blackjack as described on the Treasury Brisbane Casino website, allowing users to play against a dealer.
Generated: DETERMINISTIC_e35a981cf630aa84
Batch ID: 20250612_161231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```csharp
using System;
using System.Collections.Generic;

namespace BlackjackGame
{
    // Enum to represent card suits
    public enum Suit
    {
        Hearts,
        Diamonds,
        Clubs,
        Spades
    }

    // Enum to represent card values
    public enum Value
    {
        Two = 2,
        Three,
        Four,
        Five,
        Six,
        Seven,
        Eight,
        Nine,
        Ten,
        Jack = 10,
        Queen = 10,
        King = 10,
        Ace = 11
    }

    // Class to represent a card
    public class Card
    {
        public Suit Suit { get; set; }
        public Value Value { get; set; }

        public Card(Suit suit, Value value)
        {
            Suit = suit;
            Value = value;
        }

        // Method to return card representation
        public override string ToString()
        {
            return $"{Value} of {Suit}";
        }
    }

    // Class to represent a deck of cards
    public class Deck
    {
        private List<Card> cards;
        private Random random;

        public Deck()
        {
            random = new Random();
            cards = new List<Card>();
            InitializeDeck();
        }

        // Method to initialize the deck with 52 cards
        private void InitializeDeck()
        {
            foreach (Suit suit in Enum.GetValues(typeof(Suit)))
            {
                foreach (Value value in Enum.GetValues(typeof(Value)))
                {
                    cards.Add(new Card(suit, value));
                }
            }
        }

        // Method to shuffle the deck
        public void Shuffle()
        {
            for (int i = 0; i < cards.Count; i++)
            {
                int j = random.Next(i, cards.Count);
                Card temp = cards[i];
                cards[i] = cards[j];
                cards[j] = temp;
            }
        }

        // Method to draw a card from the deck
        public Card DrawCard()
        {
            if (cards.Count == 0)
                throw new InvalidOperationException("No cards left in the deck.");

            Card drawnCard = cards[0];
            cards.RemoveAt(0);
            return drawnCard;
        }
    }

    // Class to represent a player (both user and dealer)
    public class Player
    {
        public List<Card> Hand { get; private set; }
        public int Score { get; private set; }

        public Player()
        {
            Hand = new List<Card>();
            Score = 0;
        }

        // Method to add a card to the player's hand
        public void AddCard(Card card)
        {
            Hand.Add(card);
            UpdateScore();
        }

        // Method to update the player's score
        private void UpdateScore()
        {
            Score = 0;
            int acesCount = 0;

            foreach (var card in Hand)
            {
                Score += (int)card.Value;
                if (card.Value == Value.Ace) acesCount++;
            }

            // Adjust score for Aces
            while (Score > 21 && acesCount > 0)
            {
                Score -= 10; // Count Ace as 1 instead of 11
                acesCount--;
            }
        }

        // Method to reset the player's hand
        public void Reset()
        {
            Hand.Clear();
            Score = 0;
        }
    }

    // Main game class
    public class BlackjackGame
    {
        private Deck deck;
        private Player player;
        private Player dealer;

        public BlackjackGame()
        {
            deck = new Deck();
            player = new Player();
            dealer = new Player();
            deck.Shuffle();
        }

        // Method to start the game
        public void StartGame()
        {
            try
            {
                // Deal initial cards
                DealInitialCards();

                // Player's turn
                PlayerTurn();

                // Dealer's turn
                DealerTurn();

                // Determine winner
                DetermineWinner();
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }
        }

        // Method to deal initial cards to both player and dealer
        private void DealInitialCards()
        {
            player.AddCard(deck.DrawCard());
            dealer.AddCard(deck.DrawCard());
            player.AddCard(deck.DrawCard());
            dealer.AddCard(deck.DrawCard());
        }

        // Method to handle player's turn
        private void PlayerTurn()
        {
            while (true)
            {
                Console.WriteLine($"Your hand: {string.Join(", ", player.Hand)} (Score: {player.Score})");
                Console.WriteLine("Do you want to hit (h) or stand (s)?");
                string choice = Console.ReadLine().ToLower();

                if (choice == "h")
                {
                    player.AddCard(deck.DrawCard());
                    if (player.Score > 21)
                    {
                        Console.WriteLine($"Your hand: {string.Join(", ", player.Hand)} (Score: {player.Score}) - You busted!");
                        return;
                    }
                }
                else if (choice == "s")
                {
                    break;
                }
                else
                {
                    Console.WriteLine("Invalid choice. Please enter 'h' or 's'.");
                }
            }
        }

        // Method to handle dealer's turn
        private void DealerTurn()
        {
            while (dealer.Score < 17)
            {
                dealer.AddCard(deck.DrawCard());
            }
            Console.WriteLine($"Dealer's hand: {string.Join(", ", dealer.Hand)} (Score: {dealer.Score})");
        }

        // Method to determine the winner
        private void DetermineWinner()
        {
            if (player.Score > 21)
            {
                Console.WriteLine("Dealer wins!");
            }
            else if (dealer.Score > 21 || player.Score > dealer.Score)
            {
                Console.WriteLine("You win!");
            }
            else if (player.Score < dealer.Score)
            {
                Console.WriteLine("Dealer wins!");
            }
            else
            {
                Console.WriteLine("It's a tie!");
            }
        }

        // Entry point of the application
        public static void Main(string[] args)
        {
            BlackjackGame game = new BlackjackGame();
            game.StartGame();
        }
    }
}
```
