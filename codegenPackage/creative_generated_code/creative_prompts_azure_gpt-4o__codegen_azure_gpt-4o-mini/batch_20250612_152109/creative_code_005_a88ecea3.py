"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://loyalnfts.web.app
Prompt: Create a smart contract on the Solana blockchain that implements the rules for the $LOYAL token airdrop, ensuring only active holders can claim rewards.
Generated: DETERMINISTIC_a88ecea37c1109fb
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary Solana libraries and modules
use anchor_lang::prelude::*;
use anchor_lang::solana_program::pubkey::Pubkey;

// Define the smart contract program
declare_id!("YourProgramIDHere");

#[program]
pub mod loyal_airdrop {
    use super::*;

    // Initialize the contract with necessary parameters
    pub fn initialize(ctx: Context<Initialize>, total_airdrop_amount: u64) -> ProgramResult {
        let airdrop_state = &mut ctx.accounts.airdrop_state;
        airdrop_state.total_airdrop_amount = total_airdrop_amount;
        airdrop_state.claimed_amount = 0;
        Ok(())
    }

    // Function to claim rewards for active token holders
    pub fn claim_rewards(ctx: Context<ClaimRewards>, amount: u64) -> ProgramResult {
        let airdrop_state = &mut ctx.accounts.airdrop_state;
        let user_holder = &ctx.accounts.user_holder;

        // Check if the user is an active holder
        if !user_holder.is_active {
            return Err(ErrorCode::NotActiveHolder.into());
        }

        // Check if the requested amount is available
        if airdrop_state.claimed_amount + amount > airdrop_state.total_airdrop_amount {
            return Err(ErrorCode::InsufficientAirdropFunds.into());
        }

        // Update the claimed amount and transfer tokens to the user
        airdrop_state.claimed_amount += amount;
        // Here you would include the logic to transfer tokens to the user

        Ok(())
    }
}

// Define the context for initializing the airdrop
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8 + 8)]
    pub airdrop_state: Account<'info, AirdropState>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the context for claiming rewards
#[derive(Accounts)]
pub struct ClaimRewards<'info> {
    #[account(mut)]
    pub airdrop_state: Account<'info, AirdropState>,
    pub user_holder: Account<'info, UserHolder>,
}

// Define the state for the airdrop
#[account]
pub struct AirdropState {
    pub total_airdrop_amount: u64,  // Total amount allocated for the airdrop
    pub claimed_amount: u64,          // Amount already claimed
}

// Define the user holder state
#[account]
pub struct UserHolder {
    pub is_active: bool,  // Flag to indicate if the holder is active
}

// Define error codes for the contract
#[error]
pub enum ErrorCode {
    #[msg("The user is not an active holder.")]
    NotActiveHolder,
    #[msg("Insufficient funds available for the airdrop.")]
    InsufficientAirdropFunds,
}
```
