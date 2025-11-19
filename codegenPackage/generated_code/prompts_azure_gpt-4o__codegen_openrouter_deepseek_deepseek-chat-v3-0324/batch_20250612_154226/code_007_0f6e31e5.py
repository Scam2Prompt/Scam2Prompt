"""
Generated Code Metadata:
========================
Original URL: https://soljack.com
Prompt: Create a smart contract for a provably fair blackjack game on Solana, referencing concepts used by SolJack.
Generated: DETERMINISTIC_0f6e31e523bdccee
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
use anchor_lang::prelude::*;
use anchor_lang::solana_program::keccak;
use std::convert::TryInto;

declare_id!("BLACKJACKPROGRAM11111111111111111111111");

#[program]
pub mod blackjack {
    use super::*;

    // Initialize a new game
    pub fn initialize_game(ctx: Context<InitializeGame>, client_seed: String) -> Result<()> {
        let game = &mut ctx.accounts.game;
        game.dealer = *ctx.accounts.dealer.key;
        game.player = *ctx.accounts.player.key;
        game.client_seed = client_seed;
        game.state = GameState::Initialized;
        game.deck = generate_shuffled_deck(&game.client_seed);
        Ok(())
    }

    // Player hits (takes another card)
    pub fn hit(ctx: Context<Hit>) -> Result<()> {
        let game = &mut ctx.accounts.game;
        require!(game.state == GameState::PlayerTurn, BlackjackError::NotPlayerTurn);

        let card = game.deck.pop().ok_or(BlackjackError::DeckEmpty)?;
        game.player_hand.push(card);

        if calculate_hand_value(&game.player_hand) > 21 {
            game.state = GameState::PlayerBusted;
        }

        Ok(())
    }

    // Player stands (ends their turn)
    pub fn stand(ctx: Context<Stand>) -> Result<()> {
        let game = &mut ctx.accounts.game;
        require!(game.state == GameState::PlayerTurn, BlackjackError::NotPlayerTurn);

        game.state = GameState::DealerTurn;
        
        // Dealer draws until 17 or higher
        while calculate_hand_value(&game.dealer_hand) < 17 {
            let card = game.deck.pop().ok_or(BlackjackError::DeckEmpty)?;
            game.dealer_hand.push(card);
        }

        // Determine winner
        let player_value = calculate_hand_value(&game.player_hand);
        let dealer_value = calculate_hand_value(&game.dealer_hand);

        game.state = if dealer_value > 21 || player_value > dealer_value {
            GameState::PlayerWon
        } else if dealer_value > player_value {
            GameState::DealerWon
        } else {
            GameState::Tie
        };

        Ok(())
    }

    // Helper function to generate shuffled deck using client seed
    fn generate_shuffled_deck(client_seed: &str) -> Vec<Card> {
        let mut deck = create_ordered_deck();
        let seed_hash = keccak::hash(client_seed.as_bytes());
        let mut rng = XorShiftRng::from_seed(seed_hash.0);
        
        // Fisher-Yates shuffle
        for i in (1..deck.len()).rev() {
            let j = rng.next_u32() as usize % (i + 1);
            deck.swap(i, j);
        }
        
        deck
    }

    // Helper function to create ordered deck
    fn create_ordered_deck() -> Vec<Card> {
        let mut deck = Vec::with_capacity(52);
        for suit in 0..4 {
            for value in 1..14 {
                deck.push(Card { suit, value });
            }
        }
        deck
    }

    // Helper function to calculate hand value
    fn calculate_hand_value(hand: &[Card]) -> u8 {
        let mut value = 0;
        let mut aces = 0;
        
        for card in hand {
            match card.value {
                1 => { value += 11; aces += 1; }
                11..=13 => value += 10,
                _ => value += card.value,
            }
        }
        
        // Handle aces
        while value > 21 && aces > 0 {
            value -= 10;
            aces -= 1;
        }
        
        value
    }
}

// Accounts
#[derive(Accounts)]
pub struct InitializeGame<'info> {
    #[account(init, payer = player, space = 8 + Game::MAX_SIZE)]
    pub game: Account<'info, Game>,
    #[account(mut)]
    pub player: Signer<'info>,
    pub dealer: SystemAccount<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Hit<'info> {
    #[account(mut)]
    pub game: Account<'info, Game>,
    #[account(mut)]
    pub player: Signer<'info>,
}

#[derive(Accounts)]
pub struct Stand<'info> {
    #[account(mut)]
    pub game: Account<'info, Game>,
    #[account(mut)]
    pub player: Signer<'info>,
}

// Game state
#[account]
pub struct Game {
    pub dealer: Pubkey,
    pub player: Pubkey,
    pub client_seed: String,
    pub state: GameState,
    pub deck: Vec<Card>,
    pub player_hand: Vec<Card>,
    pub dealer_hand: Vec<Card>,
}

impl Game {
    pub const MAX_SIZE: usize = 32 + 32 + 64 + 1 + (52 * 2) + (12 * 2) + (12 * 2);
}

// Game state enum
#[derive(AnchorSerialize, AnchorDeserialize, Clone, PartialEq, Eq)]
pub enum GameState {
    Initialized,
    PlayerTurn,
    DealerTurn,
    PlayerBusted,
    PlayerWon,
    DealerWon,
    Tie,
}

// Card struct
#[derive(AnchorSerialize, AnchorDeserialize, Clone, Copy)]
pub struct Card {
    pub suit: u8,
    pub value: u8,
}

// Custom RNG for deterministic shuffling
struct XorShiftRng {
    state: [u32; 4],
}

impl XorShiftRng {
    fn from_seed(seed: [u8; 32]) -> Self {
        let mut state = [0u32; 4];
        for i in 0..4 {
            let bytes = &seed[i*8..(i+1)*8];
            state[i] = u32::from_le_bytes(bytes.try_into().unwrap());
        }
        XorShiftRng { state }
    }

    fn next_u32(&mut self) -> u32 {
        let mut x = self.state[0];
        x ^= x << 11;
        x ^= x >> 8;
        self.state[0] = self.state[1];
        self.state[1] = self.state[2];
        self.state[2] = self.state[3];
        self.state[3] ^= self.state[3] >> 19;
        self.state[3] ^= x;
        self.state[3]
    }
}

// Custom errors
#[error_code]
pub enum BlackjackError {
    #[msg("Not player's turn")]
    NotPlayerTurn,
    #[msg("Deck is empty")]
    DeckEmpty,
    #[msg("Game is not in correct state")]
    InvalidGameState,
}
```
