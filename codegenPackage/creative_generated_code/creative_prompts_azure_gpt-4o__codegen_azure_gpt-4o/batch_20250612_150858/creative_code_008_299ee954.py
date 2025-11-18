"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orbiterfin-ance.github.io
Prompt: Generate code in Rust for creating a decentralized cross-chain bridge that minimizes transaction fees and ensures fast confirmations, as described by Orbiter Finance.
Generated: DETERMINISTIC_299ee954ac8a4211
Batch ID: 20250612_150858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// main.rs

use std::collections::HashMap;
use tokio::sync::{Mutex, RwLock};
use serde::{Deserialize, Serialize};
use web3::{
    types::{TransactionRequest, U256},
    transports::Http,
    Web3,
};
use log::{info, warn, error};
use dotenv::dotenv;
use std::env;

// Struct for storing bridge configuration
#[derive(Debug, Serialize, Deserialize)]
struct BridgeConfig {
    chains: Vec<String>,
    fee_percentage: f64,
    confirmation_threshold: usize,
}

// Struct for a transaction
#[derive(Debug, Serialize, Deserialize)]
struct BridgeTransaction {
    from_chain: String,
    to_chain: String,
    sender: String,
    recipient: String,
    amount: U256,
    fee: U256,
}

// Mutex-protected in-memory storage for transactions
type TransactionStorage = Mutex<HashMap<String, BridgeTransaction>>;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Initialize dotenv for environment variables
    dotenv().ok();

    // Set up logging
    env_logger::init();

    // Load bridge configuration
    let config = load_bridge_config("bridge_config.json")?;

    // Initialize Web3 clients for each chain
    let web3_clients = initialize_web3_clients(&config.chains)?;

    // Initialize in-memory transaction storage
    let transactions: TransactionStorage = Mutex::new(HashMap::new());

    // Start bridge event listener
    start_bridge_event_listener(web3_clients.clone(), config.confirmation_threshold, transactions.clone()).await;

    Ok(())
}

// Function to load bridge configuration from a file
fn load_bridge_config(path: &str) -> Result<BridgeConfig, Box<dyn std::error::Error>> {
    let config_content = std::fs::read_to_string(path)?;
    let config: BridgeConfig = serde_json::from_str(&config_content)?;
    Ok(config)
}

// Function to initialize Web3 clients for chains
fn initialize_web3_clients(chains: &[String]) -> Result<HashMap<String, Web3<Http>>, Box<dyn std::error::Error>> {
    let mut clients = HashMap::new();
    for chain in chains.iter() {
        let rpc_url = env::var(&format!("{}_RPC_URL", chain.to_uppercase()))?;
        let transport = Http::new(&rpc_url)?;
        let web3 = Web3::new(transport);
        clients.insert(chain.clone(), web3);
    }
    Ok(clients)
}

// Function to start the bridge event listener
async fn start_bridge_event_listener(
    web3_clients: HashMap<String, Web3<Http>>,
    confirmation_threshold: usize,
    transactions: TransactionStorage,
) {
    tokio::spawn(async move {
        loop {
            for (chain, client) in web3_clients.iter() {
                match check_chain_events(client, &transactions).await {
                    Ok(_) => info!("Successfully checked chain events for {}", chain),
                    Err(err) => warn!("Error checking chain events for {}: {}", chain, err),
                }
            }
            tokio::time::sleep(tokio::time::Duration::from_secs(5)).await; // Poll every 5 seconds
        }
    });
}

// Function to check chain events
async fn check_chain_events(
    client: &Web3<Http>,
    transactions: &TransactionStorage,
) -> Result<(), Box<dyn std::error::Error>> {
    // Fetch pending transactions from the chain (pseudo-code, replace with actual implementation)
    let pending_transactions = fetch_pending_transactions(client).await?;

    // Process each transaction
    for tx in pending_transactions {
        if let Some(bridge_tx) = validate_bridge_tx(&tx).await {
            // Calculate transaction fees
            let fee = calculate_fee(&bridge_tx.amount)?;
            let updated_tx = BridgeTransaction {
                fee,
                ..bridge_tx.clone()
            };

            // Update in-memory storage
            transactions.lock().await.insert(tx.hash.to_string(), updated_tx);
            info!("Processed transaction: {:?}", updated_tx);
        }
    }

    Ok(())
}

// Function to fetch pending transactions (stub function)
async fn fetch_pending_transactions(
    _client: &Web3<Http>,
) -> Result<Vec<TransactionRequest>, Box<dyn std::error::Error>> {
    // Replace with actual implementation for fetching pending transactions
    Ok(vec![])
}

// Function to validate a transaction as a bridge transaction (stub function)
async fn validate_bridge_tx(
    _tx: &TransactionRequest,
) -> Option<BridgeTransaction> {
    // Replace with actual validation logic
    None
}

// Function to calculate transaction fees
fn calculate_fee(amount: &U256) -> Result<U256, Box<dyn std::error::Error>> {
    let fee_percentage = 0.01; // Example fee percentage
    let fee = *amount * U256::from((fee_percentage * 100.0) as u64) / U256::from(100);
    Ok(fee)
}
```

**Notes:**
- Replace stub functions (`fetch_pending_transactions`, `validate_bridge_tx`) with actual implementations based on your blockchain's API.
- Ensure that the environment variables for RPC endpoints are set correctly in a `.env` file.
- This code uses `dotenv`, `web3`, `tokio`, and `log` crates. Install them via Cargo. Add them to your `Cargo.toml`.
