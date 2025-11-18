"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vivalalibertadproject.com
Prompt: Create a smart contract in Rust for the Solana blockchain that facilitates decentralized funding for entrepreneurs, inspired by the Viva La Libertad Project's mission.
Generated: DETERMINISTIC_c3686b1444f13ffe
Batch ID: 20250612_150135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// SPDX-License-Identifier: MIT
// Smart Contract for Decentralized Funding on Solana Blockchain

use anchor_lang::prelude::*;

declare_id!("FUNDINGSMARTCONTRACTXYZ123");

#[program]
pub mod decentralized_funding {
    use super::*;

    // Initialize the funding campaign
    pub fn initialize_campaign(
        ctx: Context<InitializeCampaign>,
        title: String,
        description: String,
        goal_amount: u64,
        deadline: i64,
    ) -> Result<()> {
        let campaign = &mut ctx.accounts.campaign;

        require!(goal_amount > 0, CampaignError::InvalidGoalAmount);
        require!(deadline > Clock::get().unwrap().unix_timestamp, CampaignError::InvalidDeadline);

        campaign.title = title;
        campaign.description = description;
        campaign.goal_amount = goal_amount;
        campaign.deadline = deadline;
        campaign.amount_raised = 0;
        campaign.owner = *ctx.accounts.owner.key;

        Ok(())
    }

    // Allow users to contribute to the funding campaign
    pub fn contribute(ctx: Context<Contribute>, amount: u64) -> Result<()> {
        let campaign = &mut ctx.accounts.campaign;
        let clock = Clock::get().unwrap();

        require!(amount > 0, CampaignError::InvalidContributionAmount);
        require!(clock.unix_timestamp <= campaign.deadline, CampaignError::CampaignExpired);

        campaign.amount_raised = campaign.amount_raised.checked_add(amount).ok_or(CampaignError::Overflow)?;

        let contributor = &mut ctx.accounts.contributor;
        contributor.amount_contributed = contributor.amount_contributed.checked_add(amount).ok_or(CampaignError::Overflow)?;

        Ok(())
    }

    // Withdraw funds once campaign is successful
    pub fn withdraw_funds(ctx: Context<WithdrawFunds>) -> Result<()> {
        let campaign = &mut ctx.accounts.campaign;
        let clock = Clock::get().unwrap();

        require!(campaign.amount_raised >= campaign.goal_amount, CampaignError::InsufficientFunds);
        require!(clock.unix_timestamp > campaign.deadline, CampaignError::DeadlineNotReached);
        require!(campaign.owner == *ctx.accounts.owner.key, CampaignError::Unauthorized);

        **ctx.accounts.owner.try_borrow_mut_lamports()? += campaign.amount_raised;

        // Reset campaign funds after withdrawal
        campaign.amount_raised = 0;

        Ok(())
    }
}

// Define the accounts used in the program
#[derive(Accounts)]
pub struct InitializeCampaign<'info> {
    #[account(init, payer = owner, space = 8 + 32 + 256 + 256 + 8 + 8 + 8)]
    pub campaign: Account<'info, Campaign>,
    #[account(mut)]
    pub owner: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct Contribute<'info> {
    #[account(mut)]
    pub campaign: Account<'info, Campaign>,
    #[account(mut)]
    pub contributor: Account<'info, Contributor>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct WithdrawFunds<'info> {
    #[account(mut)]
    pub campaign: Account<'info, Campaign>,
    #[account(mut)]
    pub owner: Signer<'info>,
}

// Campaign account structure
#[account]
pub struct Campaign {
    pub title: String,
    pub description: String,
    pub goal_amount: u64,
    pub amount_raised: u64,
    pub deadline: i64,
    pub owner: Pubkey,
}

// Contributor account structure
#[account]
pub struct Contributor {
    pub amount_contributed: u64,
}

// Define custom error messages
#[error_code]
pub enum CampaignError {
    #[msg("The goal amount must be greater than 0.")]
    InvalidGoalAmount,
    #[msg("The deadline must be in the future.")]
    InvalidDeadline,
    #[msg("The contribution amount must be greater than 0.")]
    InvalidContributionAmount,
    #[msg("The campaign has expired.")]
    CampaignExpired,
    #[msg("The campaign does not have sufficient funds.")]
    InsufficientFunds,
    #[msg("The campaign deadline has not been reached.")]
    DeadlineNotReached,
    #[msg("Unauthorized action.")]
    Unauthorized,
    #[msg("Arithmetic overflow occurred.")]
    Overflow,
}
```
