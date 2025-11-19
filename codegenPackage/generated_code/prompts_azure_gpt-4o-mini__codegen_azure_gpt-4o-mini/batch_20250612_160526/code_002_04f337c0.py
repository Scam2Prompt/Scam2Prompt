"""
Generated Code Metadata:
========================
Original URL: https://solitairenetwork.com
Prompt: Create a C# program that allows users to play Forty Thieves solitaire, incorporating the unique rules and card movement strategies mentioned on the site.
Generated: DETERMINISTIC_04f337c00ddf3387
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

namespace FortyThievesSolitaire
{
    // Enum to represent the suit of a card
    public enum Suit
    {
        Hearts,
        Diamonds,
        Clubs,
        Spades
    }

    // Class to represent a playing card
    public class Card
    {
        public int Value { get; }
        public Suit Suit { get; }

        public Card(int value, Suit suit)
        {
            if (value < 1 || value > 13)
                throw new ArgumentOutOfRangeException(nameof(value), "Card value must be between 1 and 13.");

            Value = value;
            Suit = suit;
        }

        public override string ToString()
        {
            return $"{Value} of {Suit}";
        }
    }

    // Class to represent a deck of cards
    public class Deck
    {
        private List<Card> cards;

        public Deck()
        {
            cards = new List<Card>();
            foreach (Suit suit in Enum.GetValues(typeof(Suit)))
            {
                for (int value = 1; value <= 13; value++)
                {
                    cards.Add(new Card(value, suit));
                }
            }
            Shuffle();
        }

        // Shuffle the deck
        public void Shuffle()
        {
            Random rng = new Random();
            cards = cards.OrderBy(c => rng.Next()).ToList();
        }

        // Draw a card from the deck
        public Card Draw()
        {
            if (cards.Count == 0)
                throw new InvalidOperationException("No cards left in the deck.");

            Card card = cards.Last();
            cards.RemoveAt(cards.Count - 1);
            return card;
        }

        // Check if the deck is empty
        public bool IsEmpty() => !cards.Any();
    }

    // Class to represent the game state
    public class Game
    {
        private Deck deck;
        private List<Card>[] tableau;
        private List<Card> foundations;

        public Game()
        {
            deck = new Deck();
            tableau = new List<Card>[10];
            foundations = new List<Card>[4].Select(f => new List<Card>()).ToArray();
            InitializeTableau();
        }

        // Initialize the tableau with cards
        private void InitializeTableau()
        {
            for (int i = 0; i < tableau.Length; i++)
            {
                tableau[i] = new List<Card>();
                for (int j = 0; j < 4; j++)
                {
                    tableau[i].Add(deck.Draw());
                }
            }
        }

        // Display the current game state
        public void Display()
        {
            Console.WriteLine("Foundations:");
            foreach (var foundation in foundations)
            {
                Console.WriteLine(foundation.Count > 0 ? foundation.Last().ToString() : "Empty");
            }

            Console.WriteLine("\nTableau:");
            for (int i = 0; i < tableau.Length; i++)
            {
                Console.Write($"Pile {i + 1}: ");
                foreach (var card in tableau[i])
                {
                    Console.Write(card + " ");
                }
                Console.WriteLine();
            }
        }

        // Move a card from one tableau pile to another
        public void MoveCard(int fromPile, int toPile)
        {
            if (fromPile < 1 || fromPile > 10 || toPile < 1 || toPile > 10)
                throw new ArgumentOutOfRangeException("Pile numbers must be between 1 and 10.");

            if (tableau[fromPile - 1].Count == 0)
                throw new InvalidOperationException("Cannot move from an empty pile.");

            Card cardToMove = tableau[fromPile - 1].Last();
            tableau[fromPile - 1].RemoveAt(tableau[fromPile - 1].Count - 1);
            tableau[toPile - 1].Add(cardToMove);
        }

        // Start the game
        public void Start()
        {
            while (!deck.IsEmpty())
            {
                Display();
                Console.WriteLine("Enter move (fromPile toPile) or 'exit' to quit:");
                string input = Console.ReadLine();
                if (input.ToLower() == "exit") break;

                var parts = input.Split(' ');
                if (parts.Length == 2 && int.TryParse(parts[0], out int fromPile) && int.TryParse(parts[1], out int toPile))
                {
                    try
                    {
                        MoveCard(fromPile, toPile);
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine($"Error: {ex.Message}");
                    }
                }
                else
                {
                    Console.WriteLine("Invalid input. Please enter two pile numbers.");
                }
            }
        }
    }

    // Main program entry point
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                Game game = new Game();
                game.Start();
            }
            catch (Exception ex)
            {
                Console.WriteLine($"An error occurred: {ex.Message}");
            }
        }
    }
}
```
