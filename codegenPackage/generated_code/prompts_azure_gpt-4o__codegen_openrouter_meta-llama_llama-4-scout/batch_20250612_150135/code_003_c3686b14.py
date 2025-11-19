"""
Generated Code Metadata:
========================
Original URL: https://vivalalibertadproject.com
Prompt: Create a smart contract in Rust for the Solana blockchain that facilitates decentralized funding for entrepreneurs, inspired by the Viva La Libertad Project's mission.
Generated: DETERMINISTIC_c3686b1444f13ffe
Batch ID: 20250612_150135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import required libraries
use anchor_lang::prelude::*;

// Define the program ID
declare_id!("your-program-id");

// Define the program
#[program]
pub mod entrepreneur_funding {
    use super::*;

    // Initialize the program
    pub fn initialize(ctx: Context<Initialize>, name: String, description: String) -> Result<()> {
        // Get the program's account
        let funding_program = &mut ctx.accounts.funding_program;

        // Set the program's name and description
        funding_program.name = name;
        funding_program.description = description;

        // Set the program's authority
        funding_program.authority = ctx.accounts.authority.key();

        Ok(())
    }

    // Create a new funding campaign
    pub fn create_campaign(ctx: Context<CreateCampaign>, name: String, goal: u64, description: String) -> Result<()> {
        // Get the campaign account
        let campaign = &mut ctx.accounts.campaign;

        // Set the campaign's details
        campaign.name = name;
        campaign.goal = goal;
        campaign.description = description;
        campaign.funded_amount = 0;
        campaign.is_active = true;

        // Set the campaign's creator
        campaign.creator = ctx.accounts.creator.key();

        Ok(())
    }

    // Fund a campaign
    pub fn fund_campaign(ctx: Context<FundCampaign>, amount: u64) -> Result<()> {
        // Get the campaign account
        let campaign = &mut ctx.accounts.campaign;

        // Check if the campaign is active
        if !campaign.is_active {
            return Err(ProgramError::InvalidArgument);
        }

        // Check if the funding amount is valid
        if amount <= 0 {
            return Err(ProgramError::InvalidArgument);
        }

        // Update the campaign's funded amount
        campaign.funded_amount += amount;

        // Transfer funds from the funder to the campaign
        let funder = &ctx.accounts.funder;
        let campaign_escrow = &ctx.accounts.campaign_escrow;
        anchor_spl::token::transfer(
            CpiContext::new(
                ctx.accounts.token_program.key(),
                anchor_spl::token::Transfer {
                    from: funder.key(),
                    to: campaign_escrow.key(),
                    authority: funder.key(),
                },
                ctx.accounts.token_program.key(),
            ),
            amount,
        )?;

        Ok(())
    }

    // Withdraw funds from a campaign
    pub fn withdraw_funds(ctx: Context<WithdrawFunds>) -> Result<()> {
        // Get the campaign account
        let campaign = &ctx.accounts.campaign;

        // Check if the campaign has reached its goal
        if campaign.funded_amount < campaign.goal {
            return Err(ProgramError::InvalidArgument);
        }

        // Transfer funds from the campaign escrow to the creator
        let campaign_escrow = &ctx.accounts.campaign_escrow;
        let creator = &ctx.accounts.creator;
        anchor_spl::token::transfer(
            CpiContext::new(
                ctx.accounts.token_program.key(),
                anchor_spl::token::Transfer {
                    from: campaign_escrow.key(),
                    to: creator.key(),
                    authority: campaign_escrow.key(),
                },
                ctx.accounts.token_program.key(),
            ),
            campaign.funded_amount,
        )?;

        // Update the campaign's status
        let campaign = &mut ctx.accounts.campaign;
        campaign.is_active = false;

        Ok(())
    }
}

// Define the accounts for the program
#[account]
pub struct FundingProgram {
    pub name: String,
    pub description: String,
    pub authority: Pubkey,
}

#[account]
pub struct Campaign {
    pub name: String,
    pub goal: u64,
    pub description: String,
    pub funded_amount: u64,
    pub is_active: bool,
    pub creator: Pubkey,
}

// Define the instructions for the program
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = authority, space = 1000)]
    pub funding_program: Account<'info, FundingProgram>,
    #[account(mut)]
    pub authority: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct CreateCampaign<'info> {
    #[account(init, payer = creator, space = 1000)]
    pub campaign: Account<'info, Campaign>,
    #[account(mut)]
    pub creator: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct FundCampaign<'info> {
    #[account(mut)]
    pub campaign: Account<'info, Campaign>,
    #[account(mut)]
    pub funder: Signer<'info>,
    #[account(mut)]
    pub campaign_escrow: AccountInfo<'info>,
    pub token_program: Program<'info, anchor_spl::token::Token>,
}

#[derive(Accounts)]
pub struct WithdrawFunds<'info> {
    #[account(mut)]
    pub campaign: Account<'info, Campaign>,
    #[account(mut)]
    pub campaign_escrow: AccountInfo<'info>,
    #[account(mut)]
    pub creator: AccountInfo<'info>,
    pub token_program: Program<'info, anchor_spl::token::Token>,
}
```
