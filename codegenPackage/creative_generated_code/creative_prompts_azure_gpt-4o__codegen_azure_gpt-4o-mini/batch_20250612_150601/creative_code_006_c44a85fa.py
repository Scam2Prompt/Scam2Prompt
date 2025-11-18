"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atlasorng.web.app
Prompt: Create a smart contract on Solana to facilitate secure transactions for buying and selling allowlists in an allowlist marketplace like the one on Atlas3.
Generated: DETERMINISTIC_c44a85fa1c1bc2ad
Batch ID: 20250612_150601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary libraries and modules
use anchor_lang::prelude::*;
use anchor_lang::solana_program::pubkey::Pubkey;

// Define the program ID
declare_id!("YOUR_PROGRAM_ID_HERE");

// Define the main program struct
#[program]
pub mod allowlist_marketplace {
    use super::*;

    // Initializes the marketplace
    pub fn initialize(ctx: Context<Initialize>) -> Result<()> {
        let marketplace = &mut ctx.accounts.marketplace;
        marketplace.owner = ctx.accounts.owner.key();
        marketplace.allowlist_count = 0;
        Ok(())
    }

    // Adds a new allowlist to the marketplace
    pub fn add_allowlist(ctx: Context<AddAllowlist>, allowlist_address: Pubkey) -> Result<()> {
        let marketplace = &mut ctx.accounts.marketplace;

        // Ensure that the allowlist does not already exist
        if marketplace.allowlists.contains(&allowlist_address) {
            return Err(ErrorCode::AllowlistAlreadyExists.into());
        }

        // Add the allowlist to the marketplace
        marketplace.allowlists.push(allowlist_address);
        marketplace.allowlist_count += 1;
        Ok(())
    }

    // Facilitates the purchase of an allowlist
    pub fn buy_allowlist(ctx: Context<BuyAllowlist>, allowlist_address: Pubkey) -> Result<()> {
        let marketplace = &mut ctx.accounts.marketplace;

        // Ensure that the allowlist exists
        if !marketplace.allowlists.contains(&allowlist_address) {
            return Err(ErrorCode::AllowlistNotFound.into());
        }

        // Transfer the payment from buyer to seller
        let payment_amount = marketplace.allowlist_price;
        let cpi_accounts = anchor_lang::solana_program::system_instruction::Transfer {
            from: ctx.accounts.buyer.to_account_info(),
            to: ctx.accounts.seller.to_account_info(),
            lamports: payment_amount,
        };
        let cpi_program = ctx.accounts.system_program.to_account_info();
        let _result = anchor_lang::solana_program::program::invoke(&cpi_accounts, &[
            ctx.accounts.buyer.to_account_info(),
            ctx.accounts.seller.to_account_info(),
            cpi_program
        ])?;

        Ok(())
    }
}

// Define the marketplace state
#[account]
pub struct Marketplace {
    pub owner: Pubkey,
    pub allowlists: Vec<Pubkey>,
    pub allowlist_count: u64,
    pub allowlist_price: u64, // Price in lamports
}

// Define the context for initializing the marketplace
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = owner, space = 8 + std::mem::size_of::<Marketplace>())]
    pub marketplace: Account<'info, Marketplace>,
    #[account(mut)]
    pub owner: Signer<'info>,
    pub system_program: Program<'info, System>,
}

// Define the context for adding an allowlist
#[derive(Accounts)]
pub struct AddAllowlist<'info> {
    #[account(mut)]
    pub marketplace: Account<'info, Marketplace>,
}

// Define the context for buying an allowlist
#[derive(Accounts)]
pub struct BuyAllowlist<'info> {
    #[account(mut)]
    pub marketplace: Account<'info, Marketplace>,
    #[account(mut)]
    pub buyer: Signer<'info>,
    #[account(mut)]
    pub seller: AccountInfo<'info>,
    pub system_program: Program<'info, System>,
}

// Define error codes for the smart contract
#[error_code]
pub enum ErrorCode {
    #[msg("This allowlist already exists.")]
    AllowlistAlreadyExists,
    #[msg("Allowlist not found.")]
    AllowlistNotFound,
}
```

**Replace `YOUR_PROGRAM_ID_HERE` with your actual program ID.**
