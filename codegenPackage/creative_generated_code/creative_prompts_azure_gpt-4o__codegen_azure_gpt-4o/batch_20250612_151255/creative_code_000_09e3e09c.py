"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solananpcs.pages.dev
Prompt: Write a Solana-based smart contract for the $NPCS token that includes governance voting functionality for token holders, referencing the contract address `5ToDNkiBAK6k697RRyngTburU7yZNFZFx7jzsD1Uc7pK`.
Generated: DETERMINISTIC_09e3e09ca51f0b64
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the Solana-based smart contract written in Rust using the Anchor framework for the $NPCS token. It includes governance voting functionality for token holders.

```rust
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, TokenAccount};
use std::collections::HashMap;

declare_id!("5ToDNkiBAK6k697RRyngTburU7yZNFZFx7jzsD1Uc7pK");

#[program]
pub mod npcs_token_governance {
    use super::*;

    pub fn create_proposal(ctx: Context<CreateProposal>, title: String, description: String) -> Result<()> {
        let proposal = &mut ctx.accounts.proposal;
        proposal.title = title;
        proposal.description = description;
        proposal.vote_count_yes = 0;
        proposal.vote_count_no = 0;
        proposal.token_holder_votes = HashMap::new();
        proposal.is_finalized = false;

        Ok(())
    }

    pub fn vote(ctx: Context<Vote>, proposal_id: u64, vote: bool) -> Result<()> {
        let signer = &ctx.accounts.signer;
        let proposal = &mut ctx.accounts.proposal;

        require!(!proposal.is_finalized, GovernanceError::ProposalFinalized);
        require!(proposal.token_holder_votes.get(&signer.key()).is_none(), GovernanceError::AlreadyVoted);

        let token_account = &ctx.accounts.token_account;
        require!(token_account.amount > 0, GovernanceError::NoTokens);

        if vote {
            proposal.vote_count_yes += token_account.amount;
        } else {
            proposal.vote_count_no += token_account.amount;
        }

        proposal.token_holder_votes.insert(signer.key(), vote);
        Ok(())
    }

    pub fn finalize_proposal(ctx: Context<FinalizeProposal>) -> Result<()> {
        let proposal = &mut ctx.accounts.proposal;

        require!(!proposal.is_finalized, GovernanceError::ProposalFinalized);

        proposal.is_finalized = true;
        Ok(())
    }
}

#[derive(Accounts)]
pub struct CreateProposal<'info> {
    #[account(init, payer = signer, space = 8 + Proposal::MAX_SIZE)]
    pub proposal: Account<'info, Proposal>,
    #[account(mut)]
    pub signer: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Vote<'info> {
    #[account(mut)]
    pub proposal: Account<'info, Proposal>,
    #[account(mut)]
    pub token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub signer: Signer<'info>,
    pub token_program: Program<'info, token::Token>,
}

#[derive(Accounts)]
pub struct FinalizeProposal<'info> {
    #[account(mut)]
    pub proposal: Account<'info, Proposal>,
    #[account(mut)]
    pub signer: Signer<'info>,
}

#[account]
pub struct Proposal {
    pub title: String,
    pub description: String,
    pub vote_count_yes: u64,
    pub vote_count_no: u64,
    pub token_holder_votes: HashMap<Pubkey, bool>,
    pub is_finalized: bool,
}

impl Proposal {
    const MAX_SIZE: usize = 4 + 100 // title (max 100 chars)
        + 4 + 300 // description (max 300 chars)
        + 8 // vote_count_yes
        + 8 // vote_count_no
        + 4 + 1024 // token_holder_votes (max 1024 entries)
        + 1; // is_finalized
}

#[error_code]
pub enum GovernanceError {
    #[msg("The proposal has already been finalized.")]
    ProposalFinalized,
    #[msg("The signer has already voted on this proposal.")]
    AlreadyVoted,
    #[msg("The signer does not hold any tokens.")]
    NoTokens,
}
```

Make sure you have installed the Anchor framework to use this code. It implements functions for creating proposals, voting, and finalizing proposals in the governance system.
