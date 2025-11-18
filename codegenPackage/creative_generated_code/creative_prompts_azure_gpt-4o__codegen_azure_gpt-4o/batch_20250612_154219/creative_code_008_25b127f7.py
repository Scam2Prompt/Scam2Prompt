"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://applecoin-49f.pages.dev
Prompt: Write a smart contract for a community voting system on the Solana blockchain that uses $SILLY tokens for governance decisions.
Generated: DETERMINISTIC_25b127f7434a5eb6
Batch ID: 20250612_154219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// SPDX-License-Identifier: MIT
// Smart contract for a community voting system on the Solana blockchain using $SILLY tokens.
// This contract allows token holders to create proposals and vote on them.

use anchor_lang::prelude::*;
use anchor_spl::token::{self, TokenAccount, Transfer};

// Declare the program ID for $SILLY tokens (replace "YourTokenMintAddress" with the actual mint address)
declare_id!("YourProgramIDHere");

#[program]
pub mod community_voting {
    use super::*;

    // Instruction to create a new proposal
    pub fn create_proposal(
        ctx: Context<CreateProposal>,
        title: String,
        description: String
    ) -> Result<()> {
        let proposal = &mut ctx.accounts.proposal;
        proposal.title = title;
        proposal.description = description;
        proposal.creator = ctx.accounts.creator.key();
        proposal.for_votes = 0;
        proposal.against_votes = 0;
        proposal.closed = false;
        
        Ok(())
    }

    // Instruction to vote on a proposal
    pub fn vote_proposal(
        ctx: Context<VoteProposal>,
        support: bool
    ) -> Result<()> {
        let proposal = &mut ctx.accounts.proposal;

        // Ensure the proposal is still open for voting
        require!(!proposal.closed, VotingError::ProposalClosed);

        // Ensure the voter has sufficient $SILLY tokens to vote
        let voter_account = &ctx.accounts.voter_account;
        require!(voter_account.amount > 0, VotingError::InsufficientBalance);

        if support {
            proposal.for_votes += voter_account.amount;
        } else {
            proposal.against_votes += voter_account.amount;
        }

        Ok(())
    }

    // Instruction to close a proposal
    pub fn close_proposal(ctx: Context<CloseProposal>) -> Result<()> {
        let proposal = &mut ctx.accounts.proposal;
        
        // Only allow the creator to close a proposal
        require!(proposal.creator == ctx.accounts.creator.key(), VotingError::Unauthorized);

        proposal.closed = true;
        Ok(())
    }
}

// Context for creating a proposal
#[derive(Accounts)]
pub struct CreateProposal<'info> {
    #[account(init, payer = creator, space = 8 + 1024)]
    pub proposal: Account<'info, Proposal>,
    #[account(mut)]
    pub creator: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Context for voting on a proposal
#[derive(Accounts)]
pub struct VoteProposal<'info> {
    #[account(mut)]
    pub proposal: Account<'info, Proposal>,
    #[account(mut)]
    pub voter_account: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
}

// Context for closing a proposal
#[derive(Accounts)]
pub struct CloseProposal<'info> {
    #[account(mut)]
    pub proposal: Account<'info, Proposal>,
    #[account(mut)]
    pub creator: Signer<'info>,
}

// Proposal account structure
#[account]
pub struct Proposal {
    pub title: String,
    pub description: String,
    pub creator: Pubkey,
    pub for_votes: u64,
    pub against_votes: u64,
    pub closed: bool,
}

// Custom error types for better debugging
#[error_code]
pub enum VotingError {
    #[msg("The proposal is already closed.")]
    ProposalClosed,
    #[msg("You do not have sufficient $SILLY tokens to vote.")]
    InsufficientBalance,
    #[msg("You are not authorized to close this proposal.")]
    Unauthorized,
}
```
