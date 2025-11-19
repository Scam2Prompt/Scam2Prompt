"""
Generated Code Metadata:
========================
Original URL: https://immortals-nft.web.app
Prompt: Create a smart contract for managing a whitelist and free minting process for 3333 NFTs on the Solana blockchain, inspired by the Immortals NFT project.
Generated: DETERMINISTIC_384dd78d1abdb2e3
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
use anchor_lang::prelude::*;
use anchor_spl::token;
use std::collections::BTreeMap;

declare_id!("YourProgramIDHere");

#[program]
pub mod immortals_nft {
    use super::*;

    #[state]
    pub struct Immortals {
        pub admin: Pubkey,
        pub whitelist: BTreeMap<Pubkey, bool>,
        pub minted_count: u32,
        pub max_supply: u32,
        pub is_minting_active: bool,
        pub is_whitelist_active: bool,
    }

    impl Immortals {
        pub fn new(ctx: Context<Initialize>, max_supply: u32) -> Result<Self> {
            Ok(Self {
                admin: *ctx.accounts.admin.key,
                whitelist: BTreeMap::new(),
                minted_count: 0,
                max_supply,
                is_minting_active: false,
                is_whitelist_active: false,
            })
        }

        pub fn add_to_whitelist(ctx: Context<AdminOnly>, user: Pubkey) -> Result<()> {
            let state = &mut ctx.accounts.state;
            state.whitelist.insert(user, true);
            Ok(())
        }

        pub fn remove_from_whitelist(ctx: Context<AdminOnly>, user: Pubkey) -> Result<()> {
            let state = &mut ctx.accounts.state;
            state.whitelist.remove(&user);
            Ok(())
        }

        pub fn toggle_minting(ctx: Context<AdminOnly>) -> Result<()> {
            let state = &mut ctx.accounts.state;
            state.is_minting_active = !state.is_minting_active;
            Ok(())
        }

        pub fn toggle_whitelist(ctx: Context<AdminOnly>) -> Result<()> {
            let state = &mut ctx.accounts.state;
            state.is_whitelist_active = !state.is_whitelist_active;
            Ok(())
        }

        pub fn mint_nft(ctx: Context<MintNFT>) -> Result<()> {
            let state = &mut ctx.accounts.state;

            // Check if minting is active
            require!(state.is_minting_active, ErrorCode::MintingNotActive);

            // Check if supply is available
            require!(
                state.minted_count < state.max_supply,
                ErrorCode::MaxSupplyReached
            );

            // Check whitelist if whitelist is active
            if state.is_whitelist_active {
                require!(
                    state.whitelist.contains_key(ctx.accounts.user.key),
                    ErrorCode::NotWhitelisted
                );
            }

            // Mint NFT logic would go here
            // In a real implementation, you would:
            // 1. Create metadata account
            // 2. Create mint account
            // 3. Create token account
            // 4. Mint token to user

            state.minted_count += 1;
            Ok(())
        }

        pub fn update_admin(ctx: Context<AdminOnly>, new_admin: Pubkey) -> Result<()> {
            let state = &mut ctx.accounts.state;
            state.admin = new_admin;
            Ok(())
        }
    }

    #[derive(Accounts)]
    pub struct Initialize<'info> {
        #[account(init, payer = admin, space = 8 + 32 + 4 + 4 + 1 + 1 + 10000)]
        pub state: ProgramAccount<'info, Immortals>,
        pub admin: Signer<'info>,
        pub system_program: Program<'info, System>,
    }

    #[derive(Accounts)]
    pub struct AdminOnly<'info> {
        #[account(mut, has_one = admin)]
        pub state: ProgramAccount<'info, Immortals>,
        pub admin: Signer<'info>,
    }

    #[derive(Accounts)]
    pub struct MintNFT<'info> {
        #[account(mut)]
        pub state: ProgramAccount<'info, Immortals>,
        #[account(mut)]
        pub user: Signer<'info>,
        // Additional accounts needed for actual minting would go here
        // e.g., mint, metadata, token account, etc.
    }

    #[error]
    pub enum ErrorCode {
        #[msg("Minting is not currently active")]
        MintingNotActive,
        #[msg("Maximum supply has been reached")]
        MaxSupplyReached,
        #[msg("User is not whitelisted")]
        NotWhitelisted,
        #[msg("Unauthorized: only admin can perform this action")]
        Unauthorized,
    }
}
```
