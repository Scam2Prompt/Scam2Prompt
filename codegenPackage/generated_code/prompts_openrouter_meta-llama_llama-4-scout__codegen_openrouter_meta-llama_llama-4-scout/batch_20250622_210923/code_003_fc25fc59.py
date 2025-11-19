"""
Generated Code Metadata:
========================
Original URL: https://pecinosol.com
Prompt: Generate a smart contract code snippet in Rust for a new token on the Solana blockchain that adopts similar tokenomics to Pecino ($PCNO), including no private sale and presale.
Generated: DETERMINISTIC_fc25fc59f02f1a64
Batch ID: 20250622_210923
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import necessary libraries
use anchor_lang::prelude::*;

// Define the program ID
declare_id!("");

// Define the tokenomics constants
const TOTAL_SUPPLY: u64 = 100_000_000; // 100 million tokens
const PRESALE_SUPPLY: u64 = 0; // No presale
const PRIVATE_SALE_SUPPLY: u64 = 0; // No private sale
const COMMUNITY_SUPPLY: u64 = 40_000_000; // 40% for community
const TEAM_SUPPLY: u64 = 20_000_000; // 20% for team
const ADVISORS_SUPPLY: u64 = 5_000_000; // 5% for advisors
const RESERVE_SUPPLY: u64 = 35_000_000; // 35% for reserve

// Define the token name and symbol
const TOKEN_NAME: &str = "Pecino Token";
const TOKEN_SYMBOL: &str = "$PCNO";

// Define the token program
#[program]
pub mod pecino_token {
    use super::*;

    // Initialize the token program
    pub fn initialize(ctx: Context<Initialize>, 
                      name: String, 
                      symbol: String, 
                      total_supply: u64) -> Result<()> {
        // Check if the total supply matches the predefined tokenomics
        require!(total_supply == TOTAL_SUPPLY, TokenError::InvalidSupply);

        // Create the token
        let token_account = &mut ctx.accounts.token_account;
        token_account.authority = ctx.accounts.authority.key();
        token_account.name = name;
        token_account.symbol = symbol;
        token_account.total_supply = total_supply;

        // Mint initial tokens to community, team, advisors, and reserve
        mint_tokens(ctx, COMMUNITY_SUPPLY, ctx.accounts.community)?;
        mint_tokens(ctx, TEAM_SUPPLY, ctx.accounts.team)?;
        mint_tokens(ctx, ADVISORS_SUPPLY, ctx.accounts.advisors)?;
        mint_tokens(ctx, RESERVE_SUPPLY, ctx.accounts.reserve)?;

        Ok(())
    }

    // Mint tokens to a specified account
    fn mint_tokens(ctx: Context<Initialize>, amount: u64, to: AccountInfo) -> Result<()> {
        let token_account = &mut ctx.accounts.token_account;
        token_account.total_supply += amount;

        // Mint tokens using Solana's token program
        let mint_authority = ctx.accounts.authority.key();
        let token_program = ctx.accounts.token_program.key();
        let mint = ctx.accounts.token_account.key();
        let to_account = to.key();

        let cpi_accounts = anchor_spl::token::MintTo {
            mint,
            to: to_account,
            authority: mint_authority,
        };
        let cpi_program = token_program;
        let cpi_ctx = CpiContext::new(cpi_program, cpi_accounts);

        anchor_spl::token::mint_to(cpi_ctx, amount)?;

        Ok(())
    }
}

// Define accounts for the token program
#[account]
pub struct TokenAccount {
    pub authority: Pubkey,
    pub name: String,
    pub symbol: String,
    pub total_supply: u64,
}

// Define error types for the token program
#[error]
pub enum TokenError {
    #[msg("Invalid supply")]
    InvalidSupply,
}

// Define the initialize context
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = authority, space = 100)]
    pub token_account: Account<'info, TokenAccount>,

    #[account(mut)]
    pub authority: Signer<'info>,

    pub community: AccountInfo<'info>,
    pub team: AccountInfo<'info>,
    pub advisors: AccountInfo<'info>,
    pub reserve: AccountInfo<'info>,

    pub token_program: Program<'info, anchor_spl::token::Token>,
    pub system_program: Program<'info, anchor_lang::solana_program::system_program::System>,
}
```
