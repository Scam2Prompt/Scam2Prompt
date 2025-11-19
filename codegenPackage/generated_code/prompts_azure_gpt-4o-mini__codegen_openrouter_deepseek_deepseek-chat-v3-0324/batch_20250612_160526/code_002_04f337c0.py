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
    public class Card
    {
        public enum Suit { Hearts, Diamonds, Clubs, Spades }
        public enum Rank { Ace = 1, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King }

        public Suit CardSuit { get; }
        public Rank CardRank { get; }
        public bool FaceUp { get; set; }

        public Card(Suit suit, Rank rank)
        {
            CardSuit = suit;
            CardRank = rank;
            FaceUp = false;
        }

        public override string ToString()
        {
            return $"{CardRank} of {CardSuit}";
        }

        public bool IsRed()
        {
            return CardSuit == Suit.Hearts || CardSuit == Suit.Diamonds;
        }

        public bool IsBlack()
        {
            return CardSuit == Suit.Clubs || CardSuit == Suit.Spades;
        }

        public bool IsOppositeColor(Card other)
        {
            return (IsRed() && other.IsBlack()) || (IsBlack() && other.IsRed());
        }

        public bool IsSameSuit(Card other)
        {
            return CardSuit == other.CardSuit;
        }

        public bool IsOneLessThan(Card other)
        {
            return (int)CardRank == (int)other.CardRank - 1;
        }
    }

    public class Deck
    {
        private List<Card> cards;
        private Random random = new Random();

        public Deck()
        {
            cards = new List<Card>();
            Initialize();
        }

        private void Initialize()
        {
            foreach (Card.Suit suit in Enum.GetValues(typeof(Card.Suit)))
            {
                foreach (Card.Rank rank in Enum.GetValues(typeof(Card.Rank)))
                {
                    cards.Add(new Card(suit, rank));
                }
            }
        }

        public void Shuffle()
        {
            int n = cards.Count;
            while (n > 1)
            {
                n--;
                int k = random.Next(n + 1);
                Card value = cards[k];
                cards[k] = cards[n];
                cards[n] = value;
            }
        }

        public Card Draw()
        {
            if (cards.Count == 0)
                throw new InvalidOperationException("Deck is empty");

            Card card = cards[0];
            cards.RemoveAt(0);
            return card;
        }

        public bool IsEmpty()
        {
            return cards.Count == 0;
        }

        public int Count()
        {
            return cards.Count;
        }
    }

    public class FortyThievesGame
    {
        private const int TableauPiles = 10;
        private const int FoundationPiles = 8;
        private const int StockPiles = 2;

        private List<List<Card>> tableau;
        private List<List<Card>> foundation;
        private List<Card>[] stock;
        private List<Card> waste;

        public FortyThievesGame()
        {
            InitializeGame();
        }

        private void InitializeGame()
        {
            // Initialize tableau (10 piles)
            tableau = new List<List<Card>>();
            for (int i = 0; i < TableauPiles; i++)
            {
                tableau.Add(new List<Card>());
            }

            // Initialize foundation (8 piles)
            foundation = new List<List<Card>>();
            for (int i = 0; i < FoundationPiles; i++)
            {
                foundation.Add(new List<Card>());
            }

            // Initialize stock (2 piles)
            stock = new List<Card>[StockPiles];
            for (int i = 0; i < StockPiles; i++)
            {
                stock[i] = new List<Card>();
            }

            waste = new List<Card>();

            // Create and shuffle two decks
            Deck deck1 = new Deck();
            Deck deck2 = new Deck();
            deck1.Shuffle();
            deck2.Shuffle();

            // Deal cards to tableau (4 face-up cards in each pile)
            for (int i = 0; i < 4; i++)
            {
                for (int j = 0; j < TableauPiles; j++)
                {
                    if (!deck1.IsEmpty())
                    {
                        Card card = deck1.Draw();
                        card.FaceUp = true;
                        tableau[j].Add(card);
                    }
                }
            }

            // Deal remaining cards to stock piles
            int stockIndex = 0;
            while (!deck1.IsEmpty())
            {
                stock[stockIndex].Add(deck1.Draw());
                stockIndex = (stockIndex + 1) % StockPiles;
            }

            while (!deck2.IsEmpty())
            {
                stock[stockIndex].Add(deck2.Draw());
                stockIndex = (stockIndex + 1) % StockPiles;
            }
        }

        public bool MoveFromTableauToFoundation(int tableauIndex, int foundationIndex)
        {
            if (tableauIndex < 0 || tableauIndex >= TableauPiles)
                return false;
            if (foundationIndex < 0 || foundationIndex >= FoundationPiles)
                return false;

            List<Card> tableauPile = tableau[tableauIndex];
            if (tableauPile.Count == 0)
                return false;

            Card cardToMove = tableauPile.Last();
            if (!cardToMove.FaceUp)
                return false;

            List<Card> foundationPile = foundation[foundationIndex];

            if (foundationPile.Count == 0)
            {
                if (cardToMove.CardRank == Card.Rank.Ace)
                {
                    tableauPile.RemoveAt(tableauPile.Count - 1);
                    foundationPile.Add(cardToMove);
                    return true;
                }
                return false;
            }

            Card topFoundationCard = foundationPile.Last();
            if (cardToMove.IsSameSuit(topFoundationCard) && cardToMove.IsOneLessThan(topFoundationCard))
            {
                tableauPile.RemoveAt(tableauPile.Count - 1);
                foundationPile.Add(cardToMove);
                return true;
            }

            return false;
        }

        public bool MoveFromTableauToTableau(int sourceIndex, int destinationIndex, int cardCount)
        {
            if (sourceIndex < 0 || sourceIndex >= TableauPiles)
                return false;
            if (destinationIndex < 0 || destinationIndex >= TableauPiles)
                return false;
            if (sourceIndex == destinationIndex)
                return false;

            List<Card> sourcePile = tableau[sourceIndex];
            List<Card> destinationPile = tableau[destinationIndex];

            if (sourcePile.Count < cardCount)
                return false;

            // Check if all cards to move are face up
            for (int i = sourcePile.Count - cardCount; i < sourcePile.Count; i++)
            {
                if (!sourcePile[i].FaceUp)
                    return false;
            }

            Card bottomCardToMove = sourcePile[sourcePile.Count - cardCount];
            if (destinationPile.Count == 0)
            {
                // Can move any sequence to empty pile
                MoveCards(sourcePile, destinationPile, cardCount);
                return true;
            }

            Card topDestinationCard = destinationPile.Last();
            if (bottomCardToMove.IsOppositeColor(topDestinationCard) && 
                topDestinationCard.IsOneLessThan(bottomCardToMove))
            {
                MoveCards(sourcePile, destinationPile, cardCount);
                return true;
            }

            return false;
        }

        private void MoveCards(List<Card> source, List<Card> destination, int count)
        {
            int startIndex = source.Count - count;
            List<Card> cardsToMove = source.GetRange(startIndex, count);
            source.RemoveRange(startIndex, count);
            destination.AddRange(cardsToMove);
        }

        public bool MoveFromWasteToFoundation(int foundationIndex)
        {
            if (foundationIndex < 0 || foundationIndex >= FoundationPiles)
                return false;
            if (waste.Count == 0)
                return false;

            Card cardToMove = waste.Last();
            List<Card> foundationPile = foundation[foundationIndex];

            if (foundationPile.Count == 0)
            {
                if (cardToMove.CardRank == Card.Rank.Ace)
                {
                    waste.RemoveAt(waste.Count - 1);
                    foundationPile.Add(cardToMove);
                    return true;
                }
                return false;
            }

            Card topFoundationCard = foundationPile.Last();
            if (cardToMove.IsSameSuit(topFoundationCard) && cardToMove.IsOneLessThan(topFoundationCard))
            {
                waste.RemoveAt(waste.Count - 1);
                foundationPile.Add(cardToMove);
                return true;
            }

            return false;
        }

        public bool MoveFromWasteToTableau(int tableauIndex)
        {
            if (tableauIndex < 0 || tableauIndex >= TableauPiles)
                return false;
            if (waste.Count == 0)
                return false;

            Card cardToMove = waste.Last();
