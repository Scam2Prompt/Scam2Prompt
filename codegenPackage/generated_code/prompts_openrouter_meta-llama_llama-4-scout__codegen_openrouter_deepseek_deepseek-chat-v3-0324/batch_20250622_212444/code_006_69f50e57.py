"""
Generated Code Metadata:
========================
Original URL: https://trumpchest.com
Prompt: "Design a basic NFT marketplace smart contract on Solana that allows users to mint, buy, and sell NFTs representing Trump Memes, using $TRUMP tokens for transactions."
Generated: DETERMINISTIC_69f50e57d2542793
Batch ID: 20250622_212444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount, Transfer};
use mpl_token_metadata::{
    instruction::create_metadata_accounts_v3,
    state::{Collection, DataV2, Creator, Metadata, TokenStandard},
};
use solana_program::program::invoke_signed;

declare_id!("Fg6PaFpoGXkYsidMpWTK6W2BeZ7FEfcYkg476zPFsLnS");

#[program]
pub mod trump_meme_marketplace {
    use super::*;

    // Initialize the marketplace
    pub fn initialize_marketplace(ctx: Context<InitializeMarketplace>) -> Result<()> {
        let marketplace = &mut ctx.accounts.marketplace;
        marketplace.admin = *ctx.accounts.admin.key;
        marketplace.fee_basis_points = 200; // 2% fee
        Ok(())
    }

    // Mint a new Trump Meme NFT
    pub fn mint_nft(
        ctx: Context<MintNft>,
        metadata_url: String,
        metadata_name: String,
        metadata_symbol: String,
    ) -> Result<()> {
        let cpi_program = ctx.accounts.token_metadata_program.to_account_info();
        let cpi_accounts = mpl_token_metadata::instruction::CreateMetadataAccountV3 {
            metadata: ctx.accounts.metadata_account.to_account_info(),
            mint: ctx.accounts.mint_account.to_account_info(),
            mint_authority: ctx.accounts.mint_authority.to_account_info(),
            update_authority: ctx.accounts.mint_authority.to_account_info(),
            payer: ctx.accounts.payer.to_account_info(),
            system_program: ctx.accounts.system_program.to_account_info(),
            rent: ctx.accounts.rent.to_account_info(),
        };

        let creator = Creator {
            address: *ctx.accounts.payer.key,
            verified: false,
            share: 100,
        };

        let data_v2 = DataV2 {
            name: metadata_name,
            symbol: metadata_symbol,
            uri: metadata_url,
            seller_fee_basis_points: 0,
            creators: Some(vec![creator]),
            collection: None,
            uses: None,
        };

        let ix = create_metadata_accounts_v3(
            cpi_program.key(),
            cpi_accounts.metadata.key(),
            cpi_accounts.mint.key(),
            cpi_accounts.mint_authority.key(),
            cpi_accounts.payer.key(),
            cpi_accounts.update_authority.key(),
            data_v2,
            TokenStandard::NonFungible,
            false,
            false,
            None,
            None,
        );

        invoke_signed(
            &ix,
            &[
                cpi_accounts.metadata,
                cpi_accounts.mint,
                cpi_accounts.mint_authority,
                cpi_accounts.payer,
                cpi_accounts.update_authority,
                cpi_accounts.system_program,
                cpi_accounts.rent,
            ],
            &[],
        )?;

        // Transfer NFT to owner
        token::transfer(
            CpiContext::new(
                ctx.accounts.token_program.to_account_info(),
                Transfer {
                    from: ctx.accounts.mint_token_account.to_account_info(),
                    to: ctx.accounts.owner_token_account.to_account_info(),
                    authority: ctx.accounts.mint_authority.to_account_info(),
                },
            ),
            1,
        )?;

        Ok(())
    }

    // List an NFT for sale
    pub fn list_nft(ctx: Context<ListNft>, price: u64) -> Result<()> {
        let listing = &mut ctx.accounts.listing;
        listing.mint = ctx.accounts.mint_account.key();
        listing.seller = *ctx.accounts.seller.key;
        listing.price = price;
        listing.bump = *ctx.bumps.get("listing").unwrap();
        Ok(())
    }

    // Buy an NFT
    pub fn buy_nft(ctx: Context<BuyNft>) -> Result<()> {
        // Transfer TRUMP tokens from buyer to seller
        let fee = ctx.accounts.listing.price * ctx.accounts.marketplace.fee_basis_points / 10000;
        let seller_amount = ctx.accounts.listing.price - fee;

        token::transfer(
            CpiContext::new(
                ctx.accounts.token_program.to_account_info(),
                Transfer {
                    from: ctx.accounts.buyer_token_account.to_account_info(),
                    to: ctx.accounts.seller_token_account.to_account_info(),
                    authority: ctx.accounts.buyer.to_account_info(),
                },
            ),
            seller_amount,
        )?;

        // Transfer fee to marketplace
        token::transfer(
            CpiContext::new(
                ctx.accounts.token_program.to_account_info(),
                Transfer {
                    from: ctx.accounts.buyer_token_account.to_account_info(),
                    to: ctx.accounts.marketplace_fee_account.to_account_info(),
                    authority: ctx.accounts.buyer.to_account_info(),
                },
            ),
            fee,
        )?;

        // Transfer NFT to buyer
        token::transfer(
            CpiContext::new(
                ctx.accounts.token_program.to_account_info(),
                Transfer {
                    from: ctx.accounts.seller_nft_account.to_account_info(),
                    to: ctx.accounts.buyer_nft_account.to_account_info(),
                    authority: ctx.accounts.seller.to_account_info(),
                },
            ),
            1,
        )?;

        // Close listing account
        Ok(())
    }

    // Update marketplace fee
    pub fn update_fee(ctx: Context<UpdateFee>, fee_basis_points: u16) -> Result<()> {
        require!(
            *ctx.accounts.admin.key == ctx.accounts.marketplace.admin,
            ErrorCode::Unauthorized
        );
        ctx.accounts.marketplace.fee_basis_points = fee_basis_points;
        Ok(())
    }
}

#[derive(Accounts)]
pub struct InitializeMarketplace<'info> {
    #[account(init, payer = admin, space = 8 + 32 + 2)]
    pub marketplace: Account<'info, Marketplace>,
    #[account(mut)]
    pub admin: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct MintNft<'info> {
    #[account(mut)]
    pub mint_account: Account<'info, token::Mint>,
    #[account(mut)]
    pub mint_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub owner_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub mint_authority: Signer<'info>,
    #[account(mut)]
    pub payer: Signer<'info>,
    /// CHECK: This is not dangerous because we don't read or write from this account
    #[account(mut)]
    pub metadata_account: UncheckedAccount<'info>,
    pub token_program: Program<'info, Token>,
    pub token_metadata_program: Program<'info, Metadata>,
    pub system_program: Program<'info, System>,
    pub rent: Sysvar<'info, Rent>,
}

#[derive(Accounts)]
pub struct ListNft<'info> {
    #[account(init, payer = seller, space = 8 + 32 + 32 + 8 + 1, seeds = [b"listing", mint_account.key().as_ref()], bump)]
    pub listing: Account<'info, Listing>,
    pub mint_account: Account<'info, token::Mint>,
    #[account(mut)]
    pub seller: Signer<'info>,
    #[account(mut)]
    pub seller_token_account: Account<'info, TokenAccount>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct BuyNft<'info> {
    #[account(mut, has_one = mint, has_one = seller)]
    pub listing: Account<'info, Listing>,
    pub mint: Account<'info, token::Mint>,
    #[account(mut)]
    pub seller: SystemAccount<'info>,
    #[account(mut)]
    pub buyer: Signer<'info>,
    #[account(mut)]
    pub seller_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub buyer_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub seller_nft_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub buyer_nft_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub marketplace_fee_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub marketplace: Account<'info, Marketplace>,
    pub token_program: Program<'info, Token>,
}

#[derive(Accounts)]
pub struct UpdateFee<'info> {
    #[account(mut)]
    pub marketplace: Account<'info, Marketplace>,
    pub admin: Signer<'info>,
}

#[account]
pub struct Marketplace {
    pub admin: Pubkey,
    pub fee_basis_points: u16,
}

#[account]
pub struct Listing {
    pub mint: Pubkey,
    pub seller: Pubkey,
    pub price: u64,
    pub bump: u8,
}

#[error_code
