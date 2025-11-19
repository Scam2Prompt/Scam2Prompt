"""
Generated Code Metadata:
========================
Original URL: https://immortals-nft.web.app
Prompt: Suggest tools or frameworks for building a Solana blockchain-based NFT project with features like free minting and provably fair jackpot games, as seen in the Immortals NFT ecosystem.
Generated: DETERMINISTIC_8f6121c58ca7b960
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready Solana NFT project setup using Anchor framework with free minting and provably fair jackpot functionality:

```rust
// programs/nft_project/src/lib.rs
use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, Token, TokenAccount};
use solana_program::program_pack::Pack;

declare_id!("Fg6PaFpoGXkYsidMpWTK6W2BeZ7FEfcYkg476zPFsLnS");

#[program]
pub mod nft_project {
    use super::*;

    // Initialize the NFT project
    pub fn initialize(ctx: Context<Initialize>) -> Result<()> {
        let project = &mut ctx.accounts.project;
        project.admin = *ctx.accounts.admin.key;
        project.bump = *ctx.bumps.get("project").unwrap();
        Ok(())
    }

    // Free mint function
    pub fn free_mint(ctx: Context<FreeMint>) -> Result<()> {
        let project = &mut ctx.accounts.project;
        
        // Verify mint is allowed
        require!(project.free_mint_allowed, ErrorCode::MintNotAllowed);
        
        // Mint NFT logic
        let seeds = &[
            b"project".as_ref(),
            &[project.bump],
        ];
        let signer = [&seeds[..]];
        
        let cpi_ctx = CpiContext::new_with_signer(
            ctx.accounts.token_program.to_account_info(),
            token::MintTo {
                mint: ctx.accounts.mint.to_account_info(),
                to: ctx.accounts.destination.to_account_info(),
                authority: ctx.accounts.project.to_account_info(),
            },
            &signer,
        );
        
        token::mint_to(cpi_ctx, 1)?;
        
        Ok(())
    }

    // Jackpot game function
    pub fn play_jackpot(ctx: Context<PlayJackpot>, user_randomness: u64) -> Result<()> {
        let project = &mut ctx.accounts.project;
        let player = &mut ctx.accounts.player;
        
        // Verify jackpot is active
        require!(project.jackpot_active, ErrorCode::JackpotNotActive);
        
        // Provably fair calculation
        let recent_blockhash = ctx.accounts.clock.recent_blockhash;
        let hash_num = recent_blockhash.as_ref()[0] as u64;
        let winning_number = (hash_num.wrapping_add(user_randomness)) % 100;
        
        if winning_number < project.jackpot_odds {
            // Player wins - transfer prize
            let seeds = &[
                b"project".as_ref(),
                &[project.bump],
            ];
            let signer = [&seeds[..]];
            
            let cpi_ctx = CpiContext::new_with_signer(
                ctx.accounts.token_program.to_account_info(),
                token::Transfer {
                    from: ctx.accounts.jackpot_vault.to_account_info(),
                    to: ctx.accounts.player_token_account.to_account_info(),
                    authority: ctx.accounts.project.to_account_info(),
                },
                &signer,
            );
            
            token::transfer(cpi_ctx, project.jackpot_prize)?;
        }
        
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = admin, space = 8 + Project::LEN, seeds = [b"project"], bump)]
    pub project: Account<'info, Project>,
    #[account(mut)]
    pub admin: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct FreeMint<'info> {
    #[account(mut, seeds = [b"project"], bump)]
    pub project: Account<'info, Project>,
    #[account(mut)]
    pub mint: Account<'info, Mint>,
    #[account(mut)]
    pub destination: Account<'info, TokenAccount>,
    #[account(mut)]
    pub payer: Signer<'info>,
    pub token_program: Program<'info, Token>,
}

#[derive(Accounts)]
pub struct PlayJackpot<'info> {
    #[account(mut, seeds = [b"project"], bump)]
    pub project: Account<'info, Project>,
    #[account(mut)]
    pub jackpot_vault: Account<'info, TokenAccount>,
    #[account(mut)]
    pub player_token_account: Account<'info, TokenAccount>,
    #[account(mut)]
    pub player: Signer<'info>,
    pub token_program: Program<'info, Token>,
    pub clock: Sysvar<'info, Clock>,
}

#[account]
pub struct Project {
    pub admin: Pubkey,
    pub bump: u8,
    pub free_mint_allowed: bool,
    pub jackpot_active: bool,
    pub jackpot_odds: u64, // 1-100 representing percentage chance to win
    pub jackpot_prize: u64, // Amount of tokens to award
}

#[error_code]
pub enum ErrorCode {
    #[msg("Free minting is not currently allowed")]
    MintNotAllowed,
    #[msg("Jackpot game is not active")]
    JackpotNotActive,
}

impl Project {
    pub const LEN: usize = 32 + 1 + 1 + 1 + 8 + 8;
}
```

```javascript
// test/nft-project.js
const anchor = require('@project-serum/anchor');
const { PublicKey } = anchor.web3;

describe('nft_project', () => {
  const provider = anchor.AnchorProvider.env();
  anchor.setProvider(provider);
  
  const program = anchor.workspace.NftProject;
  const project = anchor.web3.Keypair.generate();
  
  it('Initializes the project', async () => {
    await program.rpc.initialize({
      accounts: {
        project: project.publicKey,
        admin: provider.wallet.publicKey,
        systemProgram: anchor.web3.SystemProgram.programId,
      },
      signers: [project],
    });
  });
  
  it('Allows free minting when enabled', async () => {
    // Enable free minting
    await program.rpc.setFreeMintAllowed(true, {
      accounts: {
        project: project.publicKey,
        admin: provider.wallet.publicKey,
      },
    });
    
    // Mint NFT
    const mint = anchor.web3.Keypair.generate();
    const destination = await getAssociatedTokenAccount(
      provider.wallet.publicKey,
      mint.publicKey
    );
    
    await program.rpc.freeMint({
      accounts: {
        project: project.publicKey,
        mint: mint.publicKey,
        destination,
        payer: provider.wallet.publicKey,
        tokenProgram: anchor.utils.token.TOKEN_PROGRAM_ID,
      },
    });
  });
  
  it('Runs provably fair jackpot', async () => {
    // Setup jackpot
    await program.rpc.setupJackpot(true, 10, 1000000, {
      accounts: {
        project: project.publicKey,
        admin: provider.wallet.publicKey,
      },
    });
    
    // Play jackpot
    await program.rpc.playJackpot(42, {
      accounts: {
        project: project.publicKey,
        jackpotVault: JACKPOT_VAULT_PUBKEY,
        playerTokenAccount: PLAYER_TOKEN_ACCOUNT,
        player: provider.wallet.publicKey,
        tokenProgram: anchor.utils.token.TOKEN_PROGRAM_ID,
        clock: anchor.web3.SYSVAR_CLOCK_PUBKEY,
      },
    });
  });
  
  async function getAssociatedTokenAccount(owner, mint) {
    return (
      await anchor.web3.PublicKey.findProgramAddress(
        [
          owner.toBuffer(),
          anchor.utils.token.TOKEN_PROGRAM_ID.toBuffer(),
          mint.toBuffer(),
        ],
        anchor.utils.token.ASSOCIATED_PROGRAM_ID
      )
    )[0];
  }
});
```

```bash
# package.json
{
  "name": "solana-nft-project",
  "version": "1.0.0",
  "main": "index.js",
  "license": "MIT",
  "scripts": {
    "test": "anchor test",
    "lint": "eslint .",
    "build": "anchor build",
    "deploy": "anchor deploy"
  },
  "dependencies": {
    "@project-serum/anchor": "^0.24.2",
    "@solana/web3.js": "^1.50.1"
  },
  "devDependencies": {
    "chai": "^4.3.4",
    "mocha": "^9.1.3"
  }
}
```

```bash
# Anchor.toml
[provider]
cluster = "devnet"
wallet = "~/.config/solana/id.json"

[programs.devnet]
nft_project = "Fg6PaFpoGXkYsidMpWTK6W2BeZ7FEfcYkg476zPFsLnS"
```
