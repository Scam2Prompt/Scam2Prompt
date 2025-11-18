"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immortals-nft.web.app
Prompt: Create a smart contract for managing a whitelist and free minting process for 3333 NFTs on the Solana blockchain, inspired by the Immortals NFT project.
Generated: DETERMINISTIC_384dd78d1abdb2e3
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the clean, well-documented code for the requested functionality using Rust for the Solana blockchain:

```rust
// Import required crates
use anchor_lang::prelude::*;

// Define constants
const MAX_SUPPLY: u64 = 3333;

// Program ID macro
declare_id!("YourProgramIDHere");

#[program]
pub mod immortals_whitelist {
    use super::*;

    // Initialize the minting process with a whitelist
    pub fn initialize_mint(ctx: Context<InitializeMint>, admin: Pubkey) -> Result<()> {
        let whitelist_account = &mut ctx.accounts.whitelist_account;
        whitelist_account.admin = admin;
        whitelist_account.total_minted = 0;
        Ok(())
    }

    // Add a user to the whitelist
    pub fn add_to_whitelist(ctx: Context<AddToWhitelist>, user: Pubkey) -> Result<()> {
        let whitelist_account = &mut ctx.accounts.whitelist_account;
        
        // Only the admin can add users to the whitelist
        if ctx.accounts.admin.key() != whitelist_account.admin {
            return Err(ErrorCode::Unauthorized.into());
        }

        whitelist_account.users.push(user);
        Ok(())
    }

    // Mint an NFT for users in the whitelist
    pub fn mint(ctx: Context<MintNFT>) -> Result<()> {
        let whitelist_account = &mut ctx.accounts.whitelist_account;

        // Check if the user is in the whitelist
        if !whitelist_account.users.contains(&ctx.accounts.user.key()) {
            return Err(ErrorCode::NotWhitelisted.into());
        }

        // Check if the minting limit has been reached
        if whitelist_account.total_minted >= MAX_SUPPLY {
            return Err(ErrorCode::MintLimitReached.into());
        }

        // Increment the total minted NFTs
        whitelist_account.total_minted += 1;

        // Mint NFT logic (placeholder, real minting logic depends on your token standard)
        // TODO: Implement actual minting logic here

        Ok(())
    }
}

// Accounts definition
#[derive(Accounts)]
pub struct InitializeMint<'info> {
    #[account(init, payer = admin, space = 8 + 32 + 8 + (32 * MAX_SUPPLY as usize))]
    pub whitelist_account: Account<'info, WhitelistAccount>,
    #[account(mut)]
    pub admin: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct AddToWhitelist<'info> {
    #[account(mut)]
    pub whitelist_account: Account<'info, WhitelistAccount>,
    pub admin: Signer<'info>,
}

#[derive(Accounts)]
pub struct MintNFT<'info> {
    #[account(mut)]
    pub whitelist_account: Account<'info, WhitelistAccount>,
    pub user: Signer<'info>,
}

// Whitelist account structure
#[account]
pub struct WhitelistAccount {
    pub admin: Pubkey,           // Admin who manages the whitelist
    pub total_minted: u64,       // Total number of NFTs minted
    pub users: Vec<Pubkey>,      // List of whitelisted users
}

// Error codes
#[error_code]
pub enum ErrorCode {
    #[msg("Unauthorized: Only the admin can perform this action.")]
    Unauthorized,
    #[msg("User is not whitelisted.")]
    NotWhitelisted,
    #[msg("Minting limit reached.")]
    MintLimitReached,
}
```

### Notes:
- Replace `"YourProgramIDHere"` with the actual Program ID of your Solana smart contract.
- Implement the actual token minting logic in the `mint` function, depending on the token standard used (e.g., SPL tokens).
- Ensure proper deployment and testing of the smart contract in your development environment.
