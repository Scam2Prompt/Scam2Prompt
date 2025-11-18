"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pecinosol.com
Prompt: Create a Solana-based smart contract that integrates the Pecino ($PCNO) token and allows users to participate in meme contests by submitting their entries.
Generated: DETERMINISTIC_d0d22671024c2192
Batch ID: 20250612_153547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code written in Rust for a Solana-based smart contract (`program` in Solana language) that fulfills the requirements.

```rust
// File: src/lib.rs

use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, TokenAccount, Transfer};

declare_id!("YourProgramPublicKeyHere");

#[program]
pub mod meme_contest {
    use super::*;

    /// Initializes the contest account
    pub fn initialize_contest(ctx: Context<InitializeContest>, _contest_name: String) -> Result<()> {
        let contest = &mut ctx.accounts.contest;
        contest.name = _contest_name;
        contest.owner = ctx.accounts.owner.key();
        contest.entries = Vec::new();
        Ok(())
    }

    /// Submit a meme entry to the contest
    pub fn submit_entry(ctx: Context<SubmitEntry>, image_url: String) -> Result<()> {
        let contest = &mut ctx.accounts.contest;

        // Add the new entry to the contest
        contest.entries.push(MemeEntry {
            submitter: ctx.accounts.submitter.key(),
            image_url,
            votes: 0,
        });

        Ok(())
    }

    /// Vote for an entry in the contest
    pub fn vote_entry(ctx: Context<VoteEntry>, entry_index: u64) -> Result<()> {
        let contest = &mut ctx.accounts.contest;

        // Ensure the entry index is valid
        require!(
            entry_index < contest.entries.len() as u64,
            ContestError::InvalidEntryIndex
        );

        // Increase the vote count for the specified entry
        contest.entries[entry_index as usize].votes += 1;

        Ok(())
    }
}

// Define the MemeEntry struct
#[derive(AnchorSerialize, AnchorDeserialize, Clone)]
pub struct MemeEntry {
    pub submitter: Pubkey,
    pub image_url: String,
    pub votes: u64,
}

// Define the Contest account structure
#[account]
pub struct Contest {
    pub name: String,
    pub owner: Pubkey,
    pub entries: Vec<MemeEntry>,
}

// Error types for better error handling
#[error_code]
pub enum ContestError {
    #[msg("Invalid entry index.")]
    InvalidEntryIndex,
}

// Context for initializing the contest
#[derive(Accounts)]
pub struct InitializeContest<'info> {
    #[account(init, payer = owner, space = 8 + 32 + (4 + 100) + (4 + 1000 * (32 + 4 + 100)))]
    pub contest: Account<'info, Contest>,
    #[account(mut)]
    pub owner: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Context for submitting an entry to the contest
#[derive(Accounts)]
pub struct SubmitEntry<'info> {
    #[account(mut)]
    pub contest: Account<'info, Contest>,
    pub submitter: Signer<'info>,
}

// Context for voting on a contest entry
#[derive(Accounts)]
pub struct VoteEntry<'info> {
    #[account(mut)]
    pub contest: Account<'info, Contest>,
    pub voter: Signer<'info>,
}

```

### Notes:
1. Replace `YourProgramPublicKeyHere` with the actual public key of your deployed program.
2. This code is structured using the Anchor framework for Solana smart contracts.
3. The `Contest` account stores all meme entries and other metadata about the contest.
4. Error handling is included for invalid entry indexes.
5. For production, ensure you perform gas/cost analysis and optimize the design based on expected usage patterns.
