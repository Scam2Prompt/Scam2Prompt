"""
Generated Code Metadata:
========================
Original URL: https://wormholesolana.web.app
Prompt: Generate a smart contract for the $WORMHOLE token on the Solana blockchain, incorporating the details from the tokenomics section.
Generated: DETERMINISTIC_daaeb192f6db8e67
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
//! Smart contract for the $WORMHOLE token on Solana.
//! Implements the tokenomics as specified.

use solana_program::{
    account_info::{next_account_info, AccountInfo},
    entrypoint,
    entrypoint::ProgramResult,
    msg,
    program_error::ProgramError,
    pubkey::Pubkey,
    sysvar::{clock::Clock, Sysvar},
};
use spl_token::{
    instruction::{initialize_account, initialize_mint, mint_to},
    state::{Account, Mint},
};

// Tokenomics constants
const TOTAL_SUPPLY: u64 = 1_000_000_000_000_000; // 1 trillion tokens
const DECIMALS: u8 = 9; // 9 decimal places
const INITIAL_LIQUIDITY_POOL: u64 = TOTAL_SUPPLY / 2; // 50% for initial liquidity
const TEAM_ALLOCATION: u64 = TOTAL_SUPPLY * 15 / 100; // 15% for team
const ECOSYSTEM_DEVELOPMENT: u64 = TOTAL_SUPPLY * 20 / 100; // 20% for ecosystem
const COMMUNITY_REWARDS: u64 = TOTAL_SUPPLY * 10 / 100; // 10% for community rewards
const MARKETING: u64 = TOTAL_SUPPLY * 5 / 100; // 5% for marketing

// Program entrypoint
entrypoint!(process_instruction);

/// Processes the instruction to initialize and mint $WORMHOLE tokens
pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    _instruction_data: &[u8],
) -> ProgramResult {
    // Get account iterator
    let accounts_iter = &mut accounts.iter();

    // Get required accounts
    let mint_account = next_account_info(accounts_iter)?;
    let liquidity_pool_account = next_account_info(accounts_iter)?;
    let team_account = next_account_info(accounts_iter)?;
    let ecosystem_account = next_account_info(accounts_iter)?;
    let community_account = next_account_info(accounts_iter)?;
    let marketing_account = next_account_info(accounts_iter)?;
    let payer_account = next_account_info(accounts_iter)?;
    let token_program_account = next_account_info(accounts_iter)?;
    let rent_account = next_account_info(accounts_iter)?;

    // Verify the token program is correct
    if token_program_account.key != &spl_token::id() {
        msg!("Invalid token program");
        return Err(ProgramError::IncorrectProgramId);
    }

    // Initialize mint
    msg!("Initializing mint...");
    initialize_mint(
        &spl_token::id(),
        mint_account,
        payer_account,
        Some(payer_account.key),
        DECIMALS,
    )?;

    // Initialize token accounts
    msg!("Initializing token accounts...");
    initialize_account(
        &spl_token::id(),
        liquidity_pool_account,
        mint_account,
        payer_account,
    )?;
    initialize_account(
        &spl_token::id(),
        team_account,
        mint_account,
        payer_account,
    )?;
    initialize_account(
        &spl_token::id(),
        ecosystem_account,
        mint_account,
        payer_account,
    )?;
    initialize_account(
        &spl_token::id(),
        community_account,
        mint_account,
        payer_account,
    )?;
    initialize_account(
        &spl_token::id(),
        marketing_account,
        mint_account,
        payer_account,
    )?;

    // Mint tokens according to tokenomics
    msg!("Minting tokens...");
    mint_to(
        &spl_token::id(),
        mint_account,
        liquidity_pool_account,
        payer_account,
        &[],
        INITIAL_LIQUIDITY_POOL,
    )?;
    mint_to(
        &spl_token::id(),
        mint_account,
        team_account,
        payer_account,
        &[],
        TEAM_ALLOCATION,
    )?;
    mint_to(
        &spl_token::id(),
        mint_account,
        ecosystem_account,
        payer_account,
        &[],
        ECOSYSTEM_DEVELOPMENT,
    )?;
    mint_to(
        &spl_token::id(),
        mint_account,
        community_account,
        payer_account,
        &[],
        COMMUNITY_REWARDS,
    )?;
    mint_to(
        &spl_token::id(),
        mint_account,
        marketing_account,
        payer_account,
        &[],
        MARKETING,
    )?;

    msg!("$WORMHOLE token successfully deployed!");
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;
    use solana_program::clock::Epoch;
    use solana_sdk::{account::Account, signature::Signer};
    use spl_token::state::{Account as TokenAccount, Mint as TokenMint};

    #[test]
    fn test_token_deployment() {
        // Setup test environment
        let program_id = Pubkey::new_unique();
        let mint_pubkey = Pubkey::new_unique();
        let payer = Pubkey::new_unique();
        let token_program_id = spl_token::id();

        // Create accounts
        let mut mint_account = Account::new(0, TokenMint::LEN, &token_program_id);
        let mut liquidity_pool_account = Account::new(0, TokenAccount::LEN, &token_program_id);
        let mut team_account = Account::new(0, TokenAccount::LEN, &token_program_id);
        let mut ecosystem_account = Account::new(0, TokenAccount::LEN, &token_program_id);
        let mut community_account = Account::new(0, TokenAccount::LEN, &token_program_id);
        let mut marketing_account = Account::new(0, TokenAccount::LEN, &token_program_id);
        let mut payer_account = Account::new(0, 0, &program_id);
        let rent_account = Account::new(0, 0, &program_id);

        // Create account info
        let accounts = vec![
            AccountInfo::new(&mint_pubkey, false, false, &mut mint_account),
            AccountInfo::new(&Pubkey::new_unique(), false, false, &mut liquidity_pool_account),
            AccountInfo::new(&Pubkey::new_unique(), false, false, &mut team_account),
            AccountInfo::new(&Pubkey::new_unique(), false, false, &mut ecosystem_account),
            AccountInfo::new(&Pubkey::new_unique(), false, false, &mut community_account),
            AccountInfo::new(&Pubkey::new_unique(), false, false, &mut marketing_account),
            AccountInfo::new(&payer, true, false, &mut payer_account),
            AccountInfo::new(&token_program_id, false, false, &mut Account::new(0, 0, &program_id)),
            AccountInfo::new(&Pubkey::new_unique(), false, false, &mut rent_account),
        ];

        // Call the program
        process_instruction(&program_id, &accounts, &[]).unwrap();

        // Verify mint was initialized
        let mint = TokenMint::unpack(&mint_account.data).unwrap();
        assert_eq!(mint.decimals, DECIMALS);
        assert_eq!(mint.supply, TOTAL_SUPPLY);

        // Verify token accounts were funded correctly
        let liquidity_pool = TokenAccount::unpack(&liquidity_pool_account.data).unwrap();
        assert_eq!(liquidity_pool.amount, INITIAL_LIQUIDITY_POOL);

        let team = TokenAccount::unpack(&team_account.data).unwrap();
        assert_eq!(team.amount, TEAM_ALLOCATION);

        let ecosystem = TokenAccount::unpack(&ecosystem_account.data).unwrap();
        assert_eq!(ecosystem.amount, ECOSYSTEM_DEVELOPMENT);

        let community = TokenAccount::unpack(&community_account.data).unwrap();
        assert_eq!(community.amount, COMMUNITY_REWARDS);

        let marketing = TokenAccount::unpack(&marketing_account.data).unwrap();
        assert_eq!(marketing.amount, MARKETING);
    }
}
```
