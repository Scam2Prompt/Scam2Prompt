"""
Generated Code Metadata:
========================
Original URL: https://pinet1.pages.dev
Prompt: Develop a smart contract for the Pi blockchain that supports token exchange functionality within the Pi Browser.
Generated: DETERMINISTIC_e29aa9d7ee6cf261
Batch ID: 20250612_145734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide the code for a smart contract that supports token exchange functionality on the Pi blockchain. However, I need to clarify that I'll be providing a sample code in Rust, as the Pi blockchain is built on the Stellar Consensus Protocol (SCP) and uses Rust for its smart contracts.

```rust
// Import necessary libraries
use std::collections::HashMap;
use pi_contract_sdk::contract::{Contract, ContractError};
use pi_contract_sdk::types::{Asset, Balance, BalanceResult};

// Define the contract
pub struct TokenExchangeContract {
    // Mapping of token symbols to their respective balances
    balances: HashMap<String, Balance>,
    // Mapping of token exchange rates
    exchange_rates: HashMap<(String, String), u64>,
}

impl TokenExchangeContract {
    // Initialize the contract
    pub fn new() -> Self {
        Self {
            balances: HashMap::new(),
            exchange_rates: HashMap::new(),
        }
    }

    // Add a new token to the contract
    pub fn add_token(&mut self, symbol: String, balance: Balance) -> Result<(), ContractError> {
        // Check if the token already exists
        if self.balances.contains_key(&symbol) {
            return Err(ContractError::TokenAlreadyExists);
        }
        // Add the token to the balances map
        self.balances.insert(symbol, balance);
        Ok(())
    }

    // Set the exchange rate for two tokens
    pub fn set_exchange_rate(&mut self, token1: String, token2: String, rate: u64) -> Result<(), ContractError> {
        // Check if both tokens exist
        if !self.balances.contains_key(&token1) || !self.balances.contains_key(&token2) {
            return Err(ContractError::TokenDoesNotExist);
        }
        // Add the exchange rate to the map
        self.exchange_rates.insert((token1, token2), rate);
        Ok(())
    }

    // Exchange tokens
    pub fn exchange(&mut self, from_token: String, to_token: String, amount: u64) -> Result<BalanceResult, ContractError> {
        // Check if both tokens exist
        if !self.balances.contains_key(&from_token) || !self.balances.contains_key(&to_token) {
            return Err(ContractError::TokenDoesNotExist);
        }
        // Check if the exchange rate is set
        if !self.exchange_rates.contains_key(&(from_token.clone(), to_token.clone())) {
            return Err(ContractError::ExchangeRateNotSet);
        }
        // Get the exchange rate
        let rate = self.exchange_rates[&(from_token.clone(), to_token.clone())];
        // Calculate the exchanged amount
        let exchanged_amount = amount * rate;
        // Update the balances
        *self.balances.get_mut(&from_token).unwrap() -= amount;
        *self.balances.get_mut(&to_token).unwrap() += exchanged_amount;
        Ok(BalanceResult {
            balance: *self.balances.get(&to_token).unwrap(),
        })
    }
}

impl Contract for TokenExchangeContract {
    // Execute a function on the contract
    fn execute(&mut self, func: String, args: Vec<String>) -> Result<String, ContractError> {
        match func.as_str() {
            "add_token" => {
                let symbol = args[0].clone();
                let balance = args[1].parse::<Balance>().unwrap();
                self.add_token(symbol, balance)?;
                Ok("Token added successfully".to_string())
            }
            "set_exchange_rate" => {
                let token1 = args[0].clone();
                let token2 = args[1].clone();
                let rate = args[2].parse::<u64>().unwrap();
                self.set_exchange_rate(token1, token2, rate)?;
                Ok("Exchange rate set successfully".to_string())
            }
            "exchange" => {
                let from_token = args[0].clone();
                let to_token = args[1].clone();
                let amount = args[2].parse::<u64>().unwrap();
                let result = self.exchange(from_token, to_token, amount)?;
                Ok(format!("Exchanged balance: {}", result.balance))
            }
            _ => Err(ContractError::FunctionNotFound),
        }
    }
}

// Define custom error types
#[derive(Debug)]
pub enum ContractError {
    TokenAlreadyExists,
    TokenDoesNotExist,
    ExchangeRateNotSet,
    FunctionNotFound,
}

// Implement From trait for ContractError
impl From<ContractError> for String {
    fn from(e: ContractError) -> Self {
        match e {
            ContractError::TokenAlreadyExists => "Token already exists".to_string(),
            ContractError::TokenDoesNotExist => "Token does not exist".to_string(),
            ContractError::ExchangeRateNotSet => "Exchange rate not set".to_string(),
            ContractError::FunctionNotFound => "Function not found".to_string(),
        }
    }
}
```
