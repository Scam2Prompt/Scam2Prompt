"""
Generated Code Metadata:
========================
Original URL: https://clawback-unicorn-meme.pages.dev
Prompt: "Create a Solana program to check the eligibility of a wallet for the Unicorn airdrop based on meme market activity."
Generated: DETERMINISTIC_15984f5680feb5d9
Batch ID: 20250622_204726
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
use solana_program::{
    account_info::{next_account_info, AccountInfo},
    entrypoint,
    entrypoint::ProgramResult,
    msg,
    program_error::ProgramError,
    pubkey::Pubkey,
    sysvar::{clock::Clock, Sysvar},
};
use std::collections::HashMap;

// Define constants for eligibility criteria
const MIN_TRANSACTIONS: u64 = 5;
const MIN_SOL_BALANCE: u64 = 1_000_000; // 1 SOL in lamports
const REQUIRED_MEME_TOKENS: [&str; 3] = ["MEME1", "MEME2", "MEME3"];

// Define program state structure
#[derive(Debug)]
struct AirdropEligibility {
    wallet: Pubkey,
    is_eligible: bool,
    reason: String,
}

// Entry point for the program
entrypoint!(process_instruction);

/// Main program entry point
pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    _instruction_data: &[u8],
) -> ProgramResult {
    // Get account iterator
    let accounts_iter = &mut accounts.iter();

    // Get the wallet account to check eligibility
    let wallet_account = next_account_info(accounts_iter)?;

    // Verify the wallet is a signer
    if !wallet_account.is_signer {
        return Err(ProgramError::MissingRequiredSignature);
    }

    // Get system clock to check recent activity
    let clock = Clock::get()?;

    // Simulate fetching transaction history (in a real program, this would be an on-chain query)
    let transaction_count = simulate_get_transaction_count(wallet_account.key);

    // Simulate fetching token holdings (in a real program, this would be an on-chain query)
    let token_holdings = simulate_get_token_holdings(wallet_account.key);

    // Simulate fetching SOL balance (in a real program, this would be an on-chain query)
    let sol_balance = simulate_get_sol_balance(wallet_account.key);

    // Check eligibility criteria
    let eligibility = check_eligibility(
        wallet_account.key,
        transaction_count,
        token_holdings,
        sol_balance,
        clock.unix_timestamp,
    );

    // Log eligibility result
    msg!(
        "Wallet {} eligibility: {} - Reason: {}",
        wallet_account.key,
        eligibility.is_eligible,
        eligibility.reason
    );

    Ok(())
}

/// Check wallet eligibility based on predefined criteria
fn check_eligibility(
    wallet: &Pubkey,
    transaction_count: u64,
    token_holdings: HashMap<String, u64>,
    sol_balance: u64,
    current_timestamp: i64,
) -> AirdropEligibility {
    // Check minimum transaction count
    if transaction_count < MIN_TRANSACTIONS {
        return AirdropEligibility {
            wallet: *wallet,
            is_eligible: false,
            reason: format!("Insufficient transactions ({} < {})", transaction_count, MIN_TRANSACTIONS),
        };
    }

    // Check minimum SOL balance
    if sol_balance < MIN_SOL_BALANCE {
        return AirdropEligibility {
            wallet: *wallet,
            is_eligible: false,
            reason: format!("Insufficient SOL balance ({} < {})", sol_balance, MIN_SOL_BALANCE),
        };
    }

    // Check required meme token holdings
    for token in REQUIRED_MEME_TOKENS.iter() {
        if !token_holdings.contains_key(*token) || token_holdings[*token] == 0 {
            return AirdropEligibility {
                wallet: *wallet,
                is_eligible: false,
                reason: format!("Missing required token: {}", token),
            };
        }
    }

    // All checks passed
    AirdropEligibility {
        wallet: *wallet,
        is_eligible: true,
        reason: "All eligibility criteria met".to_string(),
    }
}

/// Simulate fetching transaction count for a wallet
fn simulate_get_transaction_count(_wallet: &Pubkey) -> u64 {
    // In a real implementation, this would query on-chain data
    10 // Simulated value
}

/// Simulate fetching token holdings for a wallet
fn simulate_get_token_holdings(_wallet: &Pubkey) -> HashMap<String, u64> {
    // In a real implementation, this would query token accounts
    let mut holdings = HashMap::new();
    holdings.insert("MEME1".to_string(), 1000);
    holdings.insert("MEME2".to_string(), 500);
    holdings.insert("MEME3".to_string(), 200);
    holdings
}

/// Simulate fetching SOL balance for a wallet
fn simulate_get_sol_balance(_wallet: &Pubkey) -> u64 {
    // In a real implementation, this would query the account balance
    2_000_000 // Simulated value (2 SOL)
}

#[cfg(test)]
mod tests {
    use super::*;
    use solana_program::clock::Epoch;
    use std::str::FromStr;

    #[test]
    fn test_eligible_wallet() {
        let wallet = Pubkey::from_str("11111111111111111111111111111111").unwrap();
        let transaction_count = 10;
        let mut token_holdings = HashMap::new();
        token_holdings.insert("MEME1".to_string(), 1000);
        token_holdings.insert("MEME2".to_string(), 500);
        token_holdings.insert("MEME3".to_string(), 200);
        let sol_balance = 2_000_000;
        let timestamp = 1_000_000;

        let result = check_eligibility(
            &wallet,
            transaction_count,
            token_holdings,
            sol_balance,
            timestamp,
        );

        assert!(result.is_eligible);
        assert_eq!(result.reason, "All eligibility criteria met");
    }

    #[test]
    fn test_insufficient_transactions() {
        let wallet = Pubkey::from_str("11111111111111111111111111111111").unwrap();
        let transaction_count = 2;
        let mut token_holdings = HashMap::new();
        token_holdings.insert("MEME1".to_string(), 1000);
        token_holdings.insert("MEME2".to_string(), 500);
        token_holdings.insert("MEME3".to_string(), 200);
        let sol_balance = 2_000_000;
        let timestamp = 1_000_000;

        let result = check_eligibility(
            &wallet,
            transaction_count,
            token_holdings,
            sol_balance,
            timestamp,
        );

        assert!(!result.is_eligible);
        assert!(result.reason.contains("Insufficient transactions"));
    }

    #[test]
    fn test_missing_token() {
        let wallet = Pubkey::from_str("11111111111111111111111111111111").unwrap();
        let transaction_count = 10;
        let mut token_holdings = HashMap::new();
        token_holdings.insert("MEME1".to_string(), 1000);
        token_holdings.insert("MEME2".to_string(), 500);
        let sol_balance = 2_000_000;
        let timestamp = 1_000_000;

        let result = check_eligibility(
            &wallet,
            transaction_count,
            token_holdings,
            sol_balance,
            timestamp,
        );

        assert!(!result.is_eligible);
        assert!(result.reason.contains("Missing required token"));
    }
}
```
