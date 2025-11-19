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
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Welcome to Blackjack!");
            BlackjackGame game = new BlackjackGame();
            game.Start();
        }
    }

    public class Card
    {
        public string Suit { get; }
        public string Rank { get; }
        public int Value { get; }

        public Card(string suit, string rank, int value)
        {
            Suit = suit;
            Rank = rank;
            Value = value;
        }

        public override string ToString()
        {
            return $"{Rank} of {Suit}";
        }
    }

    public class Deck
    {
        private List<Card> cards;
        private Random rand = new Random();

        public Deck()
        {
            cards = new List<Card>();
            string[] suits = { "Hearts", "Diamonds", "Clubs", "Spades" };
            string[] ranks = { "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace" };
            int[] values = { 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11 };

            foreach (var suit in suits)
            {
                for (int i = 0; i < ranks.Length; i++)
                {
                    cards.Add(new Card(suit, ranks[i], values[i]));
                }
            }
        }

        public void Shuffle()
        {
            for (int i = cards.Count - 1; i > 0; i--)
            {
                int swapIndex = rand.Next(i + 1);
                Card temp = cards[i];
                cards[i] = cards[swapIndex];
                cards[swapIndex] = temp;
            }
        }

        public Card DrawCard()
        {
            if (cards.Count > 0)
            {
                Card topCard = cards[0];
                cards.RemoveAt(0);
                return topCard;
            }
            throw new InvalidOperationException("Deck is empty. Cannot draw a card.");
        }
    }

    public class Player
    {
        public List<Card> Hand { get; } = new List<Card>();

        public int GetHandValue()
        {
            int value = 0;
            int aceCount = 0;

            foreach (var card in Hand)
            {
                value += card.Value;
                if (card.Rank == "Ace")
                {
                    aceCount++;
                }
            }

            // Adjust for Aces if value exceeds 21
            while (value > 21 && aceCount > 0)
            {
                value -= 10;
                aceCount--;
            }

            return value;
        }

        public void AddCard(Card card)
        {
            Hand.Add(card);
        }

        public void DisplayHand(string name)
        {
            Console.WriteLine($"{name}'s Hand:");
            foreach (var card in Hand)
            {
                Console.WriteLine(card);
            }
            Console.WriteLine($"Total Value: {GetHandValue()}\n");
        }
    }

    public class BlackjackGame
    {
        private Deck deck;
        private Player player;
        private Player dealer;

        public void Start()
        {
            deck = new Deck();
            deck.Shuffle();

            player = new Player();
            dealer = new Player();

            // Initial deal
            player.AddCard(deck.DrawCard());
            player.AddCard(deck.DrawCard());
            dealer.AddCard(deck.DrawCard());
            dealer.AddCard(deck.DrawCard());

            // Display hands
            player.DisplayHand("Player");
            dealer.DisplayHand("Dealer");

            // Player's turn
            PlayerTurn();

            // Dealer's turn
            DealerTurn();

            // Determine winner
            DetermineWinner();
        }

        private void PlayerTurn()
        {
            while (true)
            {
                Console.WriteLine("Do you want to [H]it or [S]tand?");
                string choice = Console.ReadLine().Trim().ToUpper();

                if (choice == "H")
                {
                    player.AddCard(deck.DrawCard());
                    player.DisplayHand("Player");

                    if (player.GetHandValue() > 21)
                    {
                        Console.WriteLine("Player busted! Dealer wins.");
                        Environment.Exit(0);
                    }
                }
                else if (choice == "S")
                {
                    break;
                }
                else
                {
                    Console.WriteLine("Invalid choice. Please enter H or S.");
                }
            }
        }

        private void DealerTurn()
        {
            while (dealer.GetHandValue() < 17)
            {
                Console.WriteLine("Dealer hits.");
                dealer.AddCard(deck.DrawCard());
                dealer.DisplayHand("Dealer");
            }

            if (dealer.GetHandValue() > 21)
            {
                Console.WriteLine("Dealer busted! Player wins.");
                Environment.Exit(0);
            }
        }

        private void DetermineWinner()
        {
            int playerValue = player.GetHandValue();
            int dealerValue = dealer.GetHandValue();

            Console.WriteLine("Final Results:");
            player.DisplayHand("Player");
            dealer.DisplayHand("Dealer");

            if (playerValue > dealerValue)
            {
                Console.WriteLine("Player wins!");
            }
            else if (playerValue < dealerValue)
            {
                Console.WriteLine("Dealer wins!");
            }
            else
            {
                Console.WriteLine("It's a tie!");
            }
        }
    }
}
```
