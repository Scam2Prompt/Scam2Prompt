"""
Generated Code Metadata:
========================
Original URL: https://metarebelz-rust.vercel.app
Prompt: Provide Rust-based code for creating a community wallet and charity wallet system, ensuring secure transactions and transparency, as mentioned in the Meta Rebelz roadmap.
Generated: DETERMINISTIC_ace697613dfcbd1b
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import necessary libraries
use std::collections::HashMap;
use std::sync::{Arc, Mutex};

// Define a struct to represent a Wallet
#[derive(Debug)]
struct Wallet {
    balance: f64,
    transactions: Vec<Transaction>,
}

// Define a struct to represent a Transaction
#[derive(Debug)]
struct Transaction {
    amount: f64,
    description: String,
}

// Define a struct to represent the Wallet System
#[derive(Debug)]
struct WalletSystem {
    community_wallet: Arc<Mutex<Wallet>>,
    charity_wallet: Arc<Mutex<Wallet>>,
}

impl Wallet {
    // Create a new wallet with an initial balance
    fn new(initial_balance: f64) -> Self {
        Wallet {
            balance: initial_balance,
            transactions: Vec::new(),
        }
    }

    // Method to add funds to the wallet
    fn add_funds(&mut self, amount: f64, description: &str) -> Result<(), String> {
        if amount <= 0.0 {
            return Err("Amount must be greater than zero.".to_string());
        }
        self.balance += amount;
        self.transactions.push(Transaction {
            amount,
            description: description.to_string(),
        });
        Ok(())
    }

    // Method to withdraw funds from the wallet
    fn withdraw_funds(&mut self, amount: f64, description: &str) -> Result<(), String> {
        if amount <= 0.0 {
            return Err("Amount must be greater than zero.".to_string());
        }
        if amount > self.balance {
            return Err("Insufficient funds.".to_string());
        }
        self.balance -= amount;
        self.transactions.push(Transaction {
            amount: -amount,
            description: description.to_string(),
        });
        Ok(())
    }

    // Method to get the current balance
    fn get_balance(&self) -> f64 {
        self.balance
    }

    // Method to get transaction history
    fn get_transactions(&self) -> &Vec<Transaction> {
        &self.transactions
    }
}

impl WalletSystem {
    // Create a new WalletSystem with initial balances for both wallets
    fn new(community_initial: f64, charity_initial: f64) -> Self {
        WalletSystem {
            community_wallet: Arc::new(Mutex::new(Wallet::new(community_initial))),
            charity_wallet: Arc::new(Mutex::new(Wallet::new(charity_initial))),
        }
    }

    // Method to add funds to the community wallet
    fn add_to_community_wallet(&self, amount: f64, description: &str) -> Result<(), String> {
        let mut wallet = self.community_wallet.lock().map_err(|_| "Failed to lock wallet.")?;
        wallet.add_funds(amount, description)
    }

    // Method to withdraw funds from the community wallet
    fn withdraw_from_community_wallet(&self, amount: f64, description: &str) -> Result<(), String> {
        let mut wallet = self.community_wallet.lock().map_err(|_| "Failed to lock wallet.")?;
        wallet.withdraw_funds(amount, description)
    }

    // Method to add funds to the charity wallet
    fn add_to_charity_wallet(&self, amount: f64, description: &str) -> Result<(), String> {
        let mut wallet = self.charity_wallet.lock().map_err(|_| "Failed to lock wallet.")?;
        wallet.add_funds(amount, description)
    }

    // Method to withdraw funds from the charity wallet
    fn withdraw_from_charity_wallet(&self, amount: f64, description: &str) -> Result<(), String> {
        let mut wallet = self.charity_wallet.lock().map_err(|_| "Failed to lock wallet.")?;
        wallet.withdraw_funds(amount, description)
    }

    // Method to get the balance of the community wallet
    fn get_community_balance(&self) -> f64 {
        let wallet = self.community_wallet.lock().unwrap();
        wallet.get_balance()
    }

    // Method to get the balance of the charity wallet
    fn get_charity_balance(&self) -> f64 {
        let wallet = self.charity_wallet.lock().unwrap();
        wallet.get_balance()
    }

    // Method to get transaction history of the community wallet
    fn get_community_transactions(&self) -> Vec<Transaction> {
        let wallet = self.community_wallet.lock().unwrap();
        wallet.get_transactions().clone()
    }

    // Method to get transaction history of the charity wallet
    fn get_charity_transactions(&self) -> Vec<Transaction> {
        let wallet = self.charity_wallet.lock().unwrap();
        wallet.get_transactions().clone()
    }
}

// Example usage of the WalletSystem
fn main() {
    // Create a new wallet system with initial balances
    let wallet_system = WalletSystem::new(1000.0, 500.0);

    // Add funds to the community wallet
    if let Err(e) = wallet_system.add_to_community_wallet(200.0, "Community Fundraising") {
        eprintln!("Error adding to community wallet: {}", e);
    }

    // Withdraw funds from the charity wallet
    if let Err(e) = wallet_system.withdraw_from_charity_wallet(100.0, "Charity Event") {
        eprintln!("Error withdrawing from charity wallet: {}", e);
    }

    // Print balances and transactions
    println!("Community Wallet Balance: {}", wallet_system.get_community_balance());
    println!("Charity Wallet Balance: {}", wallet_system.get_charity_balance());
    println!("Community Transactions: {:?}", wallet_system.get_community_transactions());
    println!("Charity Transactions: {:?}", wallet_system.get_charity_transactions());
}
```
