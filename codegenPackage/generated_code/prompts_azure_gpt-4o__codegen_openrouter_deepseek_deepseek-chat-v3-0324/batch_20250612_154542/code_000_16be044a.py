"""
Generated Code Metadata:
========================
Original URL: https://mansorytoken.xyz
Prompt: Write a Solana smart contract to implement a token similar to Mansory Token (MN$RY) with a total supply of 1,000,000,000 and features for governance voting by token holders.
Generated: DETERMINISTIC_16be044a5cdc410e
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, Token, TokenAccount, Transfer};
use std::str::FromStr;

declare_id!("Fg6PaFpoGXkYsidMpWTK6W2BeZ7FEfcYkg476zPFsLnS");

#[program]
pub mod mnsry_token {
    use super::*;

    // Initialize the token with total supply and governance parameters
    pub fn initialize(
        ctx: Context<Initialize>,
        _decimals: u8,
        governance_params: GovernanceParams,
    ) -> Result<()> {
        let mint = &mut ctx.accounts.mint;
        mint.decimals = _decimals;
        mint.supply = governance_params.total_supply;

        let governance = &mut ctx.accounts.governance;
        governance.params = governance_params;
        governance.total_votes = 0;
        governance.proposal_count = 0;

        Ok(())
    }

    // Create a new proposal
    pub fn create_proposal(
        ctx: Context<CreateProposal>,
        title: String,
        description: String,
        options: Vec<String>,
    ) -> Result<()> {
        let governance = &mut ctx.accounts.governance;
        let proposal = &mut ctx.accounts.proposal;

        proposal.id = governance.proposal_count;
        proposal.title = title;
        proposal.description = description;
        proposal.options = options;
        proposal.votes = vec![0; options.len()];
        proposal.creator = *ctx.accounts.creator.key;
        proposal.created_at = Clock::get()?.unix_timestamp;
        proposal.is_active = true;

        governance.proposal_count += 1;

        Ok(())
    }

    // Vote on a proposal
    pub fn vote(ctx: Context<Vote>, proposal_id: u64, option_index: u8, amount: u64) -> Result<()> {
        let proposal = &mut ctx.accounts.proposal;
        let governance = &mut ctx.accounts.governance;
        let voter = &mut ctx.accounts.voter;

        require!(proposal.is_active, ErrorCode::ProposalNotActive);
        require!(
            option_index < proposal.options.len() as u8,
            ErrorCode::InvalidOption
        );

        // Check voter has enough tokens
        require!(
            voter.amount >= amount,
            ErrorCode::InsufficientTokensForVote
        );

        // Record the vote
        proposal.votes[option_index as usize] += amount;
        governance.total_votes += amount;

        // Lock tokens during voting period
        voter.locked_amount += amount;
        voter.amount -= amount;

        Ok(())
    }

    // Finalize a proposal and unlock tokens
    pub fn finalize_proposal(ctx: Context<FinalizeProposal>) -> Result<()> {
        let proposal = &mut ctx.accounts.proposal;
        let governance = &mut ctx.accounts.governance;

        require!(proposal.is_active, ErrorCode::ProposalNotActive);
        require!(
            Clock::get()?.unix_timestamp > proposal.created_at + governance.params.voting_period,
            ErrorCode::VotingPeriodNotEnded
        );

        proposal.is_active = false;

        // Unlock all tokens locked for this proposal
        for voter in &mut ctx.remaining_accounts {
            let mut voter_account = Account::<Voter>::try_from(voter)?;
            voter_account.amount += voter_account.locked_amount;
            voter_account.locked_amount = 0;
        }

        Ok(())
    }

    // Transfer tokens between accounts
    pub fn transfer(ctx: Context<TransferTokens>, amount: u64) -> Result<()> {
        let transfer_instruction = Transfer {
            from: ctx.accounts.from.to_account_info(),
            to: ctx.accounts.to.to_account_info(),
            authority: ctx.accounts.authority.to_account_info(),
        };

        let cpi_ctx = CpiContext::new(
            ctx.accounts.token_program.to_account_info(),
            transfer_instruction,
        );

        token::transfer(cpi_ctx, amount)?;

        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = payer, space = 8 + 32 + 8 + 8 + 8)]
    pub mint: Account<'info, Mint>,
    #[account(init, payer = payer, space = 8 + GovernanceParams::LEN + 8 + 8)]
    pub governance: Account<'info, Governance>,
    #[account(mut)]
    pub payer: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct CreateProposal<'info> {
    #[account(mut)]
    pub governance: Account<'info, Governance>,
    #[account(init, payer = creator, space = 8 + Proposal::MAX_SIZE)]
    pub proposal: Account<'info, Proposal>,
    #[account(mut)]
    pub creator: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Vote<'info> {
    #[account(mut)]
    pub governance: Account<'info, Governance>,
    #[account(mut)]
    pub proposal: Account<'info, Proposal>,
    #[account(mut)]
    pub voter: Account<'info, Voter>,
    pub voter_authority: Signer<'info>,
}

#[derive(Accounts)]
pub struct FinalizeProposal<'info> {
    #[account(mut)]
    pub governance: Account<'info, Governance>,
    #[account(mut)]
    pub proposal: Account<'info, Proposal>,
}

#[derive(Accounts)]
pub struct TransferTokens<'info> {
    #[account(mut)]
    pub from: Account<'info, TokenAccount>,
    #[account(mut)]
    pub to: Account<'info, TokenAccount>,
    pub authority: Signer<'info>,
    pub token_program: Program<'info, Token>,
}

#[account]
pub struct Mint {
    pub decimals: u8,
    pub supply: u64,
}

#[account]
pub struct Governance {
    pub params: GovernanceParams,
    pub total_votes: u64,
    pub proposal_count: u64,
}

#[derive(AnchorSerialize, AnchorDeserialize, Clone)]
pub struct GovernanceParams {
    pub total_supply: u64,          // 1,000,000,000 tokens
    pub voting_period: i64,         // seconds
    pub min_proposal_duration: i64, // seconds
    pub quorum_percentage: u8,      // percentage required
}

impl GovernanceParams {
    pub const LEN: usize = 8 + 8 + 8 + 1;
}

#[account]
pub struct Proposal {
    pub id: u64,
    pub title: String,
    pub description: String,
    pub options: Vec<String>,
    pub votes: Vec<u64>,
    pub creator: Pubkey,
    pub created_at: i64,
    pub is_active: bool,
}

impl Proposal {
    pub const MAX_SIZE: usize = 8 + 100 + 500 + (10 * 50) + (10 * 8) + 32 + 8 + 1;
}

#[account]
pub struct Voter {
    pub amount: u64,
    pub locked_amount: u64,
}

#[error_code]
pub enum ErrorCode {
    #[msg("Proposal is not active")]
    ProposalNotActive,
    #[msg("Invalid option index")]
    InvalidOption,
    #[msg("Insufficient tokens for vote")]
    InsufficientTokensForVote,
    #[msg("Voting period has not ended")]
    VotingPeriodNotEnded,
}
```
