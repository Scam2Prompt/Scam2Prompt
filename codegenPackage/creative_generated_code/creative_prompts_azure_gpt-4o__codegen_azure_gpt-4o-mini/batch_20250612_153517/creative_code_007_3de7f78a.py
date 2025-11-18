"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimgift-x69.web.app
Prompt: Develop a smart contract on Solana to handle the claiming process for DUST tokens, ensuring only eligible wallets with specific NFTs can claim.
Generated: DETERMINISTIC_3de7f78abf8ed656
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary libraries from Solana SDK and Anchor framework
use anchor_lang::prelude::*;
use anchor_lang::solana_program::pubkey::Pubkey;

// Define the program's ID
declare_id!("YourProgramIdHere");

// Define the state of the contract
#[program]
pub mod dust_claim {
    use super::*;

    // Initialize the contract
    pub fn initialize(ctx: Context<Initialize>) -> Result<()> {
        // Initialization logic here
        Ok(())
    }

    // Claim function to be called by eligible users
    pub fn claim(ctx: Context<Claim>, nft_mint: Pubkey) -> Result<()> {
        let claimant = &ctx.accounts.claimant;
        
        // Check if the claimant's wallet contains the specific NFT
        if !is_eligible(claimant.key, nft_mint)? {
            return Err(ErrorCode::NotEligible.into());
        }

        // Logic to transfer DUST tokens to the eligible claimant
        transfer_dust_tokens(claimant)?;

        Ok(())
    }
}

// Define the context for initializing the contract
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub data: Account<'info, MyData>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the context for the claim function
#[derive(Accounts)]
pub struct Claim<'info> {
    #[account(mut)]
    pub claimant: Signer<'info>,
    // Add any additional accounts needed here
}

// Function to check if the claimant owns the required NFT
fn is_eligible(claimant: Pubkey, nft_mint: Pubkey) -> Result<bool> {
    // Logic to check NFT ownership (pseudo-code)
    // This should interface with the appropriate token program
    // and check the claimant's token accounts for the specific NFT mint

    // Note: Replace the following condition with actual NFT checking logic
    let has_nft = true; // Placeholder value

    Ok(has_nft)
}

// Function to transfer DUST tokens to the claimant
fn transfer_dust_tokens(claimant: &Signer) -> Result<()> {
    // Logic to transfer DUST token (pseudo-code)
    // This should involve actual token transfer using the token program

    // Ensure proper transfer logic, handle potential errors
    // Example: invoke token transfer instruction, check for errors

    Ok(())
}

// Define custom error codes
#[error]
pub enum ErrorCode {
    #[msg("This wallet is not eligible to claim DUST tokens.")]
    NotEligible,
}

// Define the data structure to hold any necessary state
#[account]
pub struct MyData {
    // Add fields as needed for your state
}
```

Make sure to replace `"YourProgramIdHere"` with the actual program ID and to implement the NFT ownership checking and token transfer logic as necessary for your specific use case.
