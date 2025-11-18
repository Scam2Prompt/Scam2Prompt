"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metarebelz-rust.vercel.app
Prompt: Provide Rust-based code for creating a community wallet and charity wallet system, ensuring secure transactions and transparency, as mentioned in the Meta Rebelz roadmap.
Generated: DETERMINISTIC_ace697613dfcbd1b
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
use std::collections::HashMap;
use std::sync::{Mutex, Arc};
use uuid::Uuid;

// Define the Wallet struct to represent a wallet with balance and transaction history
#[derive(Debug)]
struct Wallet {
    id: Uuid,                  // Unique identifier for the wallet
    balance: f64,              // Wallet balance
    transaction_history: Vec<Transaction>, // List of transactions
}

// Define the Transaction struct to represent a wallet transaction
#[derive(Debug, Clone)]
struct Transaction {
    id: Uuid,                  // Unique transaction ID
    amount: f64,               // Amount involved in the transaction
    transaction_type: String,  // Type of transaction (e.g., "deposit", "withdraw", "donate")
    timestamp: String,         // Timestamp of the transaction
}

// Define the WalletSystem struct to manage multiple wallets
struct WalletSystem {
    community_wallet: Arc<Mutex<Wallet>>,  // Shared community wallet
    charity_wallet: Arc<Mutex<Wallet>>,    // Shared charity wallet
}

impl WalletSystem {
    // Creates a new WalletSystem with initialized wallets
    fn new() -> WalletSystem {
        WalletSystem {
            community_wallet: Arc::new(Mutex::new(Wallet {
                id: Uuid::new_v4(),
                balance: 0.0,
                transaction_history: vec![],
            })),
            charity_wallet: Arc::new(Mutex::new(Wallet {
                id: Uuid::new_v4(),
                balance: 0.0,
                transaction_history: vec![],
            })),
        }
    }

    // Deposit funds into a wallet
    fn deposit(&self, wallet_type: &str, amount: f64) -> Result<(), String> {
        if amount <= 0.0 {
            return Err("Deposit amount must be greater than zero.".to_string());
        }

        let wallet = match wallet_type {
            "community" => &self.community_wallet,
            "charity" => &self.charity_wallet,
            _ => return Err("Invalid wallet type. Use 'community' or 'charity'.".to_string()),
        };

        let mut wallet = wallet.lock().unwrap();
        wallet.balance += amount;
        wallet.transaction_history.push(Transaction {
            id: Uuid::new_v4(),
            amount,
            transaction_type: "deposit".to_string(),
            timestamp: chrono::Utc::now().to_string(),
        });

        Ok(())
    }

    // Withdraw funds from a wallet
    fn withdraw(&self, wallet_type: &str, amount: f64) -> Result<(), String> {
        if amount <= 0.0 {
            return Err("Withdrawal amount must be greater than zero.".to_string());
        }

        let wallet = match wallet_type {
            "community" => &self.community_wallet,
            "charity" => &self.charity_wallet,
            _ => return Err("Invalid wallet type. Use 'community' or 'charity'.".to_string()),
        };

        let mut wallet = wallet.lock().unwrap();
        if wallet.balance < amount {
            return Err("Insufficient funds.".to_string());
        }

        wallet.balance -= amount;
        wallet.transaction_history.push(Transaction {
            id: Uuid::new_v4(),
            amount,
            transaction_type: "withdraw".to_string(),
            timestamp: chrono::Utc::now().to_string(),
        });

        Ok(())
    }

    // Transfer funds between community wallet and charity wallet
    fn transfer(&self, from_wallet_type: &str, to_wallet_type: &str, amount: f64) -> Result<(), String> {
        if amount <= 0.0 {
            return Err("Transfer amount must be greater than zero.".to_string());
        }

        if from_wallet_type == to_wallet_type {
            return Err("Cannot transfer between the same wallet.".to_string());
        }

        let from_wallet = match from_wallet_type {
            "community" => &self.community_wallet,
            "charity" => &self.charity_wallet,
            _ => return Err("Invalid 'from' wallet type. Use 'community' or 'charity'.".to_string()),
        };

        let to_wallet = match to_wallet_type {
            "community" => &self.community_wallet,
            "charity" => &self.charity_wallet,
            _ => return Err("Invalid 'to' wallet type. Use 'community' or 'charity'.".to_string()),
        };

        let mut from_wallet = from_wallet.lock().unwrap();
        let mut to_wallet = to_wallet.lock().unwrap();

        if from_wallet.balance < amount {
            return Err("Insufficient funds for transfer.".to_string());
        }

        from_wallet.balance -= amount;
        to_wallet.balance += amount;

        let transaction = Transaction {
            id: Uuid::new_v4(),
            amount,
            transaction_type: "transfer".to_string(),
            timestamp: chrono::Utc::now().to_string(),
        };

        from_wallet.transaction_history.push(transaction.clone());
        to_wallet.transaction_history.push(transaction);

        Ok(())
    }

    // Get wallet information
    fn get_wallet_info(&self, wallet_type: &str) -> Result<Wallet, String> {
        let wallet = match wallet_type {
            "community" => &self.community_wallet,
            "charity" => &self.charity_wallet,
            _ => return Err("Invalid wallet type. Use 'community' or 'charity'.".to_string()),
        };

        let wallet = wallet.lock().unwrap();
        Ok(wallet.clone())
    }
}

fn main() {
    // Initialize the wallet system
    let wallet_system = WalletSystem::new();

    // Example usage
    wallet_system.deposit("community", 1000.0).unwrap();
    wallet_system.deposit("charity", 500.0).unwrap();

    wallet_system.transfer("community", "charity", 200.0).unwrap();

    let community_wallet_info = wallet_system.get_wallet_info("community").unwrap();
    println!("Community Wallet Info: {:?}", community_wallet_info);

    let charity_wallet_info = wallet_system.get_wallet_info("charity").unwrap();
    println!("Charity Wallet Info: {:?}", charity_wallet_info);
}
```
