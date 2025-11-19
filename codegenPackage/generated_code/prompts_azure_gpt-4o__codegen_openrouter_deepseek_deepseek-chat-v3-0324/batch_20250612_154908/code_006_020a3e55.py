"""
Generated Code Metadata:
========================
Original URL: https://zkdrops.xyz
Prompt: Write a smart contract on Solana that utilizes zkdrops for proof of participation in a blockchain-based voting system.
Generated: DETERMINISTIC_020a3e554de229a1
Batch ID: 20250612_154908
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
use anchor_lang::prelude::*;
use anchor_lang::solana_program::entrypoint::ProgramResult;
use anchor_lang::solana_program::program_error::ProgramError;
use std::str::FromStr;

declare_id!("Fg6PaFpoGXkYsidMpWTK6W2BeZ7FEfcYkg476zPFsLnS");

#[program]
pub mod voting_system {
    use super::*;

    #[derive(Accounts)]
    pub struct InitializeVoting<'info> {
        #[account(init, payer = authority, space = 8 + 32 + 8 + 8)]
        pub voting_account: Account<'info, VotingAccount>,
        #[account(mut)]
        pub authority: Signer<'info>,
        pub system_program: Program<'info, System>,
    }

    #[derive(Accounts)]
    pub struct CastVote<'info> {
        #[account(mut)]
        pub voting_account: Account<'info, VotingAccount>,
        pub voter: Signer<'info>,
        #[account(init_if_needed, payer = voter, space = 8 + 32 + 1)]
        pub proof_account: Account<'info, ProofAccount>,
        pub system_program: Program<'info, System>,
    }

    #[account]
    pub struct VotingAccount {
        pub authority: Pubkey,
        pub yes_votes: u64,
        pub no_votes: u64,
    }

    #[account]
    pub struct ProofAccount {
        pub voter: Pubkey,
        pub has_voted: bool,
    }

    pub fn initialize_voting(ctx: Context<InitializeVoting>) -> ProgramResult {
        let voting_account = &mut ctx.accounts.voting_account;
        voting_account.authority = *ctx.accounts.authority.key;
        voting_account.yes_votes = 0;
        voting_account.no_votes = 0;
        Ok(())
    }

    pub fn cast_vote(ctx: Context<CastVote>, vote: bool) -> ProgramResult {
        let voting_account = &mut ctx.accounts.voting_account;
        let proof_account = &mut ctx.accounts.proof_account;

        // Check if voter has already voted
        if proof_account.has_voted {
            return Err(ProgramError::InvalidAccountData);
        }

        // Update vote count
        if vote {
            voting_account.yes_votes += 1;
        } else {
            voting_account.no_votes += 1;
        }

        // Mark as voted
        proof_account.voter = *ctx.accounts.voter.key;
        proof_account.has_voted = true;

        Ok(())
    }

    // Zero-knowledge proof verification (simplified for demonstration)
    pub fn verify_zk_proof(proof: &[u8], public_inputs: &[u8]) -> bool {
        // In a real implementation, this would verify a zk-SNARK proof
        // For demo purposes, we just return true
        true
    }

    #[derive(Accounts)]
    pub struct ZkCastVote<'info> {
        #[account(mut)]
        pub voting_account: Account<'info, VotingAccount>,
        #[account(init_if_needed, payer = anonymous, space = 8 + 32 + 1)]
        pub proof_account: Account<'info, ProofAccount>,
        #[account(mut)]
        pub anonymous: Signer<'info>,
        pub system_program: Program<'info, System>,
    }

    pub fn zk_cast_vote(
        ctx: Context<ZkCastVote>,
        vote: bool,
        proof: Vec<u8>,
        public_inputs: Vec<u8>,
    ) -> ProgramResult {
        // Verify the zero-knowledge proof
        if !verify_zk_proof(&proof, &public_inputs) {
            return Err(ProgramError::InvalidInstructionData);
        }

        let voting_account = &mut ctx.accounts.voting_account;
        let proof_account = &mut ctx.accounts.proof_account;

        // Update vote count
        if vote {
            voting_account.yes_votes += 1;
        } else {
            voting_account.no_votes += 1;
        }

        // Mark as voted (without revealing voter identity)
        proof_account.voter = Pubkey::from_str("11111111111111111111111111111111").unwrap();
        proof_account.has_voted = true;

        Ok(())
    }
}
```
