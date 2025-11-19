"""
Generated Code Metadata:
========================
Original URL: https://solitairenetwork.com
Prompt: Design a simple game interface in React for playing the La Belle Lucie solitaire game, including the two redeals feature and the free move on the last deal.
Generated: DETERMINISTIC_fbb31848a410c3e5
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import './LaBelleLucie.css';

const LaBelleLucie = () => {
  const [deck, setDeck] = useState([]);
  const [tableau, setTableau] = useState([]);
  const [foundation, setFoundation] = useState([]);
  const [redealsLeft, setRedealsLeft] = useState(2);
  const [gameWon, setGameWon] = useState(false);
  const [gameLost, setGameLost] = useState(false);
  const [selectedCard, setSelectedCard] = useState(null);

  // Initialize the game
  useEffect(() => {
    initializeGame();
  }, []);

  // Check for win condition
  useEffect(() => {
    if (foundation.length === 52) {
      setGameWon(true);
    }
  }, [foundation]);

  // Initialize a new game
  const initializeGame = () => {
    // Create a standard deck of 52 cards
    const suits = ['hearts', 'diamonds', 'clubs', 'spades'];
    const values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'];
    const newDeck = [];

    for (let suit of suits) {
      for (let value of values) {
        newDeck.push({ suit, value, faceUp: false });
      }
    }

    // Shuffle the deck
    const shuffledDeck = shuffleDeck(newDeck);

    // Deal the cards into 17 piles (16 piles of 3 cards, 1 pile of 4 cards)
    const newTableau = [];
    for (let i = 0; i < 17; i++) {
      const pileSize = i === 16 ? 4 : 3;
      const pile = shuffledDeck.splice(0, pileSize);
      pile[pile.length - 1].faceUp = true; // Top card is face up
      newTableau.push(pile);
    }

    setDeck(shuffledDeck);
    setTableau(newTableau);
    setFoundation([]);
    setRedealsLeft(2);
    setGameWon(false);
    setGameLost(false);
    setSelectedCard(null);
  };

  // Shuffle the deck using Fisher-Yates algorithm
  const shuffleDeck = (deck) => {
    const shuffled = [...deck];
    for (let i = shuffled.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
    }
    return shuffled;
  };

  // Handle card selection
  const handleCardClick = (pileIndex, cardIndex) => {
    const pile = tableau[pileIndex];
    const card = pile[cardIndex];

    // Only allow selecting the top card of a pile
    if (!card.faceUp || cardIndex !== pile.length - 1) return;

    // If no card is selected, select this one
    if (!selectedCard) {
      setSelectedCard({ pileIndex, cardIndex });
      return;
    }

    // If same card is clicked again, deselect it
    if (
      selectedCard.pileIndex === pileIndex &&
      selectedCard.cardIndex === cardIndex
    ) {
      setSelectedCard(null);
      return;
    }

    // Try to move the selected card to the clicked pile
    moveCard(selectedCard.pileIndex, selectedCard.cardIndex, pileIndex);
    setSelectedCard(null);
  };

  // Move a card from one pile to another
  const moveCard = (fromPileIndex, fromCardIndex, toPileIndex) => {
    const newTableau = [...tableau];
    const fromPile = newTableau[fromPileIndex];
    const toPile = newTableau[toPileIndex];
    const card = fromPile[fromCardIndex];

    // Check if the move is valid (same suit and consecutive rank)
    if (toPile.length > 0) {
      const topCard = toPile[toPile.length - 1];
      if (
        card.suit !== topCard.suit ||
        !isConsecutiveRank(card.value, topCard.value)
      ) {
        return;
      }
    }

    // Move the card
    const movedCard = fromPile.splice(fromCardIndex, 1)[0];
    toPile.push(movedCard);

    // Flip the next card in the from pile if it exists
    if (fromPile.length > 0) {
      fromPile[fromPile.length - 1].faceUp = true;
    }

    setTableau(newTableau);
  };

  // Check if two card values are consecutive
  const isConsecutiveRank = (value1, value2) => {
    const values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'];
    const index1 = values.indexOf(value1);
    const index2 = values.indexOf(value2);
    return Math.abs(index1 - index2) === 1;
  };

  // Move a card to foundation
  const moveToFoundation = (pileIndex, cardIndex) => {
    const newTableau = [...tableau];
    const pile = newTableau[pileIndex];
    const card = pile[cardIndex];

    // Only allow moving the top card of a pile
    if (cardIndex !== pile.length - 1) return;

    // Check if the card can be moved to foundation
    const foundationSuit = foundation.find((f) => f.suit === card.suit);
    if (foundationSuit) {
      const lastCard = foundationSuit.cards[foundationSuit.cards.length - 1];
      if (!isConsecutiveRank(card.value, lastCard.value)) {
        return;
      }
    } else if (card.value !== 'A') {
      return;
    }

    // Remove the card from tableau
    const movedCard = pile.splice(cardIndex, 1)[0];

    // Add to foundation
    const newFoundation = [...foundation];
    const suitIndex = newFoundation.findIndex((f) => f.suit === movedCard.suit);

    if (suitIndex >= 0) {
      newFoundation[suitIndex].cards.push(movedCard);
    } else {
      newFoundation.push({ suit: movedCard.suit, cards: [movedCard] });
    }

    // Flip the next card in the pile if it exists
    if (pile.length > 0) {
      pile[pile.length - 1].faceUp = true;
    }

    setTableau(newTableau);
    setFoundation(newFoundation);
    setSelectedCard(null);
  };

  // Redeal the cards
  const redeal = () => {
    if (redealsLeft <= 0) return;

    // Collect all remaining cards
    const remainingCards = [];
    tableau.forEach((pile) => {
      pile.forEach((card) => {
        if (card.faceUp) remainingCards.push(card);
      });
    });

    // Shuffle the remaining cards
    const shuffledCards = shuffleDeck(remainingCards);

    // Redeal into new piles
    const newTableau = [];
    const piles = Math.ceil(shuffledCards.length / 3);
    for (let i = 0; i < piles; i++) {
      const pileSize = i === piles - 1 ? shuffledCards.length % 3 || 3 : 3;
      const pile = shuffledCards.splice(0, pileSize);
      pile[pile.length - 1].faceUp = true;
      newTableau.push(pile);
    }

    setTableau(newTableau);
    setRedealsLeft(redealsLeft - 1);

    // Check for game loss on last redeal
    if (redealsLeft === 1) {
      checkForGameLoss(newTableau);
    }
  };

  // Check if the game is lost (no more moves possible)
  const checkForGameLoss = (currentTableau) => {
    let hasValidMove = false;

    // Check all possible moves between piles
    for (let i = 0; i < currentTableau.length; i++) {
      const fromPile = currentTableau[i];
      if (fromPile.length === 0) continue;

      const fromCard = fromPile[fromPile.length - 1];

      for (let j = 0; j < currentTableau.length; j++) {
        if (i === j) continue;

        const toPile = currentTableau[j];
        if (toPile.length === 0) {
          hasValidMove = true;
          break;
        }

        const toCard = toPile[toPile.length - 1];
        if (fromCard.suit === toCard.suit && isConsecutiveRank(fromCard.value, toCard.value)) {
          hasValidMove = true;
          break;
        }
