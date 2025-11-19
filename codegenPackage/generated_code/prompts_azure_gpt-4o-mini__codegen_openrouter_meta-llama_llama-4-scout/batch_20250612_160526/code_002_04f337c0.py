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

namespace FortyThievesSolitaire
{
    /// <summary>
    /// Represents a card in the deck.
    /// </summary>
    public class Card
    {
        public string Suit { get; set; }
        public string Value { get; set; }

        public Card(string suit, string value)
        {
            Suit = suit;
            Value = value;
        }

        public override string ToString()
        {
            return $"{Value} of {Suit}";
        }
    }

    /// <summary>
    /// Represents a deck of cards.
    /// </summary>
    public class Deck
    {
        private List<Card> cards;
        private Random random;

        public Deck()
        {
            cards = new List<Card>();
            random = new Random();

            string[] suits = { "Hearts", "Diamonds", "Clubs", "Spades" };
            string[] values = { "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King" };

            foreach (string suit in suits)
            {
                foreach (string value in values)
                {
                    cards.Add(new Card(suit, value));
                }
            }
        }

        public void Shuffle()
        {
            for (int i = cards.Count - 1; i > 0; i--)
            {
                int j = random.Next(i + 1);
                Card temp = cards[i];
                cards[i] = cards[j];
                cards[j] = temp;
            }
        }

        public Card DrawCard()
        {
            if (cards.Count == 0)
            {
                return null;
            }
            Card card = cards[0];
            cards.RemoveAt(0);
            return card;
        }
    }

    /// <summary>
    /// Represents a pile of cards in the game.
    /// </summary>
    public class Pile
    {
        public List<Card> Cards { get; set; }

        public Pile()
        {
            Cards = new List<Card>();
        }

        public void AddCard(Card card)
        {
            Cards.Add(card);
        }

        public Card RemoveCard()
        {
            if (Cards.Count == 0)
            {
                return null;
            }
            Card card = Cards[Cards.Count - 1];
            Cards.RemoveAt(Cards.Count - 1);
            return card;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Deck deck = new Deck();
            deck.Shuffle();

            // Initialize 10 piles with 4 cards each
            Pile[] piles = new Pile[10];
            for (int i = 0; i < 10; i++)
            {
                piles[i] = new Pile();
                for (int j = 0; j < 4; j++)
                {
                    piles[i].AddCard(deck.DrawCard());
                }
            }

            // Initialize foundation piles
            Pile[] foundationPiles = new Pile[4];
            for (int i = 0; i < 4; i++)
            {
                foundationPiles[i] = new Pile();
            }

            Console.WriteLine("Welcome to Forty Thieves Solitaire!");

            while (true)
            {
                Console.WriteLine("\nCurrent state of the game:");
                PrintPiles(piles);
                PrintFoundationPiles(foundationPiles);

                Console.WriteLine("\nOptions:");
                Console.WriteLine("1. Draw a card from the deck");
                Console.WriteLine("2. Move a card from a pile to another pile");
                Console.WriteLine("3. Move a card from a pile to a foundation pile");
                Console.WriteLine("4. Quit");

                Console.Write("Choose an option: ");
                string option = Console.ReadLine();

                switch (option)
                {
                    case "1":
                        DrawCard(deck, piles);
                        break;
                    case "2":
                        MoveCardBetweenPiles(piles);
                        break;
                    case "3":
                        MoveCardToFoundation(piles, foundationPiles);
                        break;
                    case "4":
                        return;
                    default:
                        Console.WriteLine("Invalid option. Please choose again.");
                        break;
                }

                if (HasWon(foundationPiles))
                {
                    Console.WriteLine("\nCongratulations, you have won!");
                    return;
                }
            }
        }

        static void PrintPiles(Pile[] piles)
        {
            for (int i = 0; i < 10; i++)
            {
                Console.WriteLine($"Pile {i + 1}:");
                foreach (Card card in piles[i].Cards)
                {
                    Console.WriteLine(card);
                }
            }
        }

        static void PrintFoundationPiles(Pile[] foundationPiles)
        {
            for (int i = 0; i < 4; i++)
            {
                Console.WriteLine($"Foundation Pile {i + 1}:");
                foreach (Card card in foundationPiles[i].Cards)
                {
                    Console.WriteLine(card);
                }
            }
        }

        static void DrawCard(Deck deck, Pile[] piles)
        {
            Card card = deck.DrawCard();
            if (card == null)
            {
                Console.WriteLine("No more cards in the deck.");
                return;
            }

            Console.WriteLine("Choose a pile to add the drawn card to:");
            for (int i = 0; i < 10; i++)
            {
                Console.WriteLine($"{i + 1}. Pile {i + 1}");
            }

            Console.Write("Enter the number of the pile: ");
            int pileNumber;
            if (int.TryParse(Console.ReadLine(), out pileNumber) && pileNumber > 0 && pileNumber <= 10)
            {
                piles[pileNumber - 1].AddCard(card);
            }
            else
            {
                Console.WriteLine("Invalid pile number.");
            }
        }

        static void MoveCardBetweenPiles(Pile[] piles)
        {
            Console.WriteLine("Choose a pile to move a card from:");
            for (int i = 0; i < 10; i++)
            {
                Console.WriteLine($"{i + 1}. Pile {i + 1}");
            }

            Console.Write("Enter the number of the pile: ");
            int fromPileNumber;
            if (!int.TryParse(Console.ReadLine(), out fromPileNumber) || fromPileNumber < 1 || fromPileNumber > 10)
            {
                Console.WriteLine("Invalid pile number.");
                return;
            }

            Pile fromPile = piles[fromPileNumber - 1];
            if (fromPile.Cards.Count == 0)
            {
                Console.WriteLine("Pile is empty.");
                return;
            }

            Card card = fromPile.RemoveCard();
            Console.WriteLine($"You have removed: {card}");

            Console.WriteLine("Choose a pile to move the card to:");
            for (int i = 0; i < 10; i++)
            {
                Console.WriteLine($"{i + 1}. Pile {i + 1}");
            }

            Console.Write("Enter the number of the pile: ");
            int toPileNumber;
            if (int.TryParse(Console.ReadLine(), out toPileNumber) && toPileNumber > 0 && toPileNumber <= 10)
            {
                piles[toPileNumber - 1].AddCard(card);
            }
            else
            {
                Console.WriteLine("Invalid pile number.");
                fromPile.AddCard(card);
            }
        }

        static void MoveCardToFoundation(Pile[] piles, Pile[] foundationPiles)
        {
            Console.WriteLine("Choose a pile to move a card from:");
            for (int i = 0; i < 10; i++)
            {
                Console.WriteLine($"{i + 1}. Pile {i + 1}");
            }

            Console.Write("Enter the number of the pile: ");
            int fromPileNumber;
            if (!int.TryParse(Console.ReadLine(), out fromPileNumber) || fromPileNumber < 1 || fromPileNumber > 10)
            {
                Console.WriteLine("Invalid pile number.");
                return;
            }

            Pile fromPile = piles[fromPileNumber - 1];
            if (fromPile.Cards.Count == 0)
            {
                Console.WriteLine("Pile is empty.");
                return;
            }

            Card card = fromPile.RemoveCard();

            Console.WriteLine("Choose a foundation pile to move the card to:");
            for (int i = 0; i < 4; i++)
            {
                Console.WriteLine($"{i + 1}. Foundation Pile {i + 1}");
            }

            Console.Write("Enter the number of the foundation pile: ");
            int toFoundationPileNumber;
            if (int.TryParse(Console.ReadLine(), out toFoundationPileNumber) && toFoundationPileNumber > 0 && toFoundationPileNumber <= 4)
            {
                foundationPiles[toFoundationPileNumber - 1].AddCard(card);
            }
            else
            {
                Console.WriteLine("Invalid foundation pile number.");
                fromPile.AddCard(card);
            }
        }

        static bool HasWon(Pile[] foundationPiles)
        {
            foreach (Pile pile in foundationPiles)
            {
                if (pile.Cards.Count != 13)
                {
                    return false;
                }
            }
            return true;
        }
    }
}
```
