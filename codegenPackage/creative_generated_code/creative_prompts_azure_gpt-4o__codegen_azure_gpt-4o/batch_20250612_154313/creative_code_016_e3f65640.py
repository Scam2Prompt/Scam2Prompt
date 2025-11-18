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
 * Simulates a simplified blackjack game based on specified rules and payout structure.
 * - The player and dealer are dealt cards randomly from a standard 52-card deck.
 * - The player can choose to 'hit' (draw a card) or 'stand' (end their turn).
 * - The dealer must follow a specific rule: hit if their total is below 17, stand otherwise.
 * - Payouts are determined based on the player's outcome (win, loss, or tie).
 * 
 * @returns {void} Prints the result of the game and payouts.
 */
function simulateBlackjack() {
  // Helper functions and constants
  const suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades'];
  const values = [
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'
  ];

  const deck = [];
  const payouts = { win: 2, blackjack: 2.5, tie: 1, loss: 0 };

  // Create and shuffle the deck
  function initializeDeck() {
    values.forEach(value => {
      suits.forEach(suit => {
        deck.push({ value, suit });
      });
    });
    shuffle(deck);
  }

  // Shuffle the deck
  function shuffle(cards) {
    for (let i = cards.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [cards[i], cards[j]] = [cards[j], cards[i]];
    }
  }

  // Draws a card from the deck
  function drawCard() {
    if (deck.length === 0) {
      throw new Error('Deck is empty. Cannot draw card.');
    }
    return deck.pop();
  }

  // Calculate hand value
  function calculateHandValue(hand) {
    let total = 0;
    let aceCount = 0;

    hand.forEach(card => {
      if (['J', 'Q', 'K'].includes(card.value)) {
        total += 10;
      } else if (card.value === 'A') {
        total += 11;
        aceCount++;
      } else {
        total += parseInt(card.value, 10);
      }
    });

    // Adjust for aces if total exceeds 21
    while (total > 21 && aceCount > 0) {
      total -= 10;
      aceCount--;
    }

    return total;
  }

  // Dealer logic: hits until total is 17 or higher
  function dealerPlay(hand) {
    let value = calculateHandValue(hand);
    while (value < 17) {
      hand.push(drawCard());
      value = calculateHandValue(hand);
    }
  }

  // Player logic: simplified to always stand after two cards
  function playerPlay(hand) {
    return calculateHandValue(hand);
  }

  // Initialize the game
  initializeDeck();

  const playerHand = [drawCard(), drawCard()];
  const dealerHand = [drawCard(), drawCard()];

  console.log('Player Hand:', playerHand);
  console.log('Dealer Hand:', dealerHand);

  const playerTotal = playerPlay(playerHand);
  dealerPlay(dealerHand);
  const dealerTotal = calculateHandValue(dealerHand);

  console.log(`Player Total: ${playerTotal}`);
  console.log(`Dealer Total: ${dealerTotal}`);

  // Determine the result and payout
  let result, payout;
  if (playerTotal > 21) {
    result = 'Player busts! Dealer wins.';
    payout = payouts.loss;
  } else if (dealerTotal > 21) {
    result = 'Dealer busts! Player wins.';
    payout = payouts.win;
  } else if (playerTotal > dealerTotal) {
    result = 'Player wins!';
    payout = payouts.win;
  } else if (playerTotal === 21 && playerHand.length === 2) {
    result = 'Blackjack! Player wins with a higher payout.';
    payout = payouts.blackjack;
  } else if (playerTotal === dealerTotal) {
    result = 'It\'s a tie.';
    payout = payouts.tie;
  } else {
    result = 'Dealer wins.';
    payout = payouts.loss;
  }

  console.log(result);
  console.log(`Payout: ${payout}x`);
}

// Run the simulation
simulateBlackjack();
```
