"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://promo-ws108.github.io
Prompt: Develop a Solana-based program that tracks and displays the winning chances for specific tokens like BONK, NANA, BOOTY, and COCO from the Degen Toy Machine.
Generated: DETERMINISTIC_ef3d38d00a9f5d2e
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
use solana_program::{
    account_info::AccountInfo, entrypoint, entrypoint::ProgramResult, msg, pubkey::Pubkey,
};
use std::collections::HashMap;

// Entry point for the program
entrypoint!(process_instruction);

/// Program to track and display the winning chances of tokens.
pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    msg!("Degen Toy Machine winning chances tracker.");

    let token_odds = get_token_odds();

    // Display the odds of winning for the tokens
    for (token, odds) in &token_odds {
        msg!("Token: {}, Winning Chances: {}%", token, odds);
    }

    Ok(())
}

/// Function to return the odds of winning for specific tokens.
/// This simulates static odds for demonstration purposes.
fn get_token_odds() -> HashMap<&'static str, f32> {
    let mut odds_map = HashMap::new();

    // Add tokens and their respective winning chances
    odds_map.insert("BONK", 25.0);  // BONK token has a 25% chance of winning
    odds_map.insert("NANA", 15.0);  // NANA token has a 15% chance of winning
    odds_map.insert("BOOTY", 35.0); // BOOTY token has a 35% chance of winning
    odds_map.insert("COCO", 25.0);  // COCO token has a 25% chance of winning

    odds_map
}
```
