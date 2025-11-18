"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bobukineko.pages.dev
Prompt: Create a smart contract on Solana to support the $BOBUKI token presale, including functionality for swapping SOL and handling slippage settings.
Generated: DETERMINISTIC_6e638675963b5b10
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary libraries from the Solana SDK and other dependencies
use anchor_lang::prelude::*;
use anchor_lang::solana_program::pubkey::Pubkey;
use anchor_lang::solana_program::program::invoke;
use anchor_lang::solana_program::system_instruction;
use spl_token::state::Mint;

declare_id!("YourProgramIdHere"); // Replace with your program ID

#[program]
pub mod bobuki_presale {
    use super::*;

    // Initialize the presale with the necessary parameters
    pub fn initialize_presale(
        ctx: Context<InitializePresale>,
        total_supply: u64,
        sale_price: u64,
        slippage: u64,
    ) -> Result<()> {
        let presale = &mut ctx.accounts.presale;
        presale.total_supply = total_supply;
        presale.sale_price = sale_price;
        presale.slippage = slippage;
        presale.vendor = *ctx.accounts.vendor.key;
        presale.sold_tokens = 0;

        Ok(())
    }

    // Function to handle the token purchase during the presale
    pub fn purchase_tokens(ctx: Context<PurchaseTokens>, amount: u64) -> Result<()> {
        let presale = &mut ctx.accounts.presale;

        // Calculate total cost with respect to slippage
        let total_cost = presale.sale_price.checked_mul(amount).ok_or(ProgramError::InvalidArgument)?;

        // Ensure that SOL received covers the purchase
        let sol_received = ctx.accounts.user.to_account_info().lamports();
        if sol_received < total_cost {
            return Err(ProgramError::InsufficientFunds);
        }

        // Transfer SOL to the vendor
        let transfer_instruction = system_instruction::transfer(
            ctx.accounts.user.key,
            ctx.accounts.vendor.key,
            total_cost,
        );
        invoke(
            &transfer_instruction,
            &[
                ctx.accounts.user.to_account_info(),
                ctx.accounts.vendor.to_account_info(),
                ctx.accounts.system_program.to_account_info(),
            ],
        )?;

        // Update the state of tokens sold
        presale.sold_tokens = presale.sold_tokens.checked_add(amount).ok_or(ProgramError::InvalidArgument)?;

        Ok(())
    }

    // Function to withdraw the funds after the presale ends
    pub fn withdraw_funds(ctx: Context<WithdrawFunds>) -> Result<()> {
        let presale = &ctx.accounts.presale;

        // Ensure only the vendor can withdraw
        if *ctx.accounts.vendor.key != presale.vendor {
            return Err(ProgramError::Unauthorized);
        }

        // Transfer SOL to vendor
        let total_funds = presale.sold_tokens.checked_mul(presale.sale_price).ok_or(ProgramError::InvalidArgument)?;

        **ctx.accounts.vendor.try_borrow_mut_lamports()? += total_funds;
        **ctx.accounts.presale.to_account_info().try_borrow_mut_lamports()? -= total_funds;

        Ok(())
    }
}

// Define the context for initializing the presale
#[derive(Accounts)]
pub struct InitializePresale<'info> {
    #[account(init, payer = vendor, space = Presale::SIZE)]
    pub presale: Account<'info, Presale>,
    #[account(mut)]
    pub vendor: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the context for purchasing tokens
#[derive(Accounts)]
pub struct PurchaseTokens<'info> {
    #[account(mut)]
    pub presale: Account<'info, Presale>,
    #[account(mut)]
    pub user: Signer<'info>,
    #[account(mut)]
    pub vendor: AccountInfo<'info>,
    pub system_program: Program<'info, System>,
}

// Define the context for withdrawing funds
#[derive(Accounts)]
pub struct WithdrawFunds<'info> {
    #[account(mut)]
    pub presale: Account<'info, Presale>,
    #[account(mut)]
    pub vendor: Signer<'info>,
}

// Presale structure to hold relevant data
#[account]
pub struct Presale {
    pub total_supply: u64,
    pub sale_price: u64,
    pub slippage: u64,
    pub vendor: Pubkey,
    pub sold_tokens: u64,
}

// Size of the Presale structure
impl Presale {
    const SIZE: usize = 8 + 8 + 8 + 32 + 8; // Account size in bytes
}
```
