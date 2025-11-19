"""
Generated Code Metadata:
========================
Original URL: https://fuel-dapp-implement.vercel.app
Prompt: Using the Fuels CLI, demonstrate how to enable type-safe hot-reloading for Sway programs in a Fuel-based application.
Generated: DETERMINISTIC_a475fc70fa64f3e3
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import required libraries
use std::env;
use std::path::PathBuf;
use fuels::{prelude::*, programs::sway::SwayProgram};
use anyhow::{Context, Result};

// Define a function to enable type-safe hot-reloading
async fn enable_hot_reloading(
    contract_path: &str,
    script_path: &str,
) -> Result<()> {
    // Initialize the Fuels provider
    let provider = Provider::default().await?;

    // Set up the wallet
    let wallet = WalletUnlocked::new_random();

    // Set up the contract
    let contract_id = Contract::load_from(
        contract_path,
        &provider,
        wallet.address(),
    )
    .await?
    .id();

    // Set up the script
    let script = Script::load_from(script_path, &provider, wallet.address()).await?;

    // Enable hot-reloading
    let hot_reload_config = HotReloadConfig::new(contract_id, script.id());

    // Start the hot-reloading watcher
    let watcher = HotReloadWatcher::new(hot_reload_config);

    // Run the watcher in a separate task
    tokio::spawn(async move {
        watcher.watch().await?;
        Ok(())
    });

    // Run indefinitely to keep the watcher running
    loop {
        tokio::time::sleep(tokio::time::Duration::from_secs(1)).await;
    }
}

// Define the main function
#[tokio::main]
async fn main() -> Result<()> {
    // Get the contract and script paths from environment variables
    let contract_path = env::var("CONTRACT_PATH")
        .context("CONTRACT_PATH environment variable not set")?;
    let script_path = env::var("SCRIPT_PATH")
        .context("SCRIPT_PATH environment variable not set")?;

    // Enable hot-reloading
    enable_hot_reloading(&contract_path, &script_path).await?;

    Ok(())
}
```

```toml
# Cargo.toml
[package]
name = "fuel_hot_reloading"
version = "0.1.0"
edition = "2021"

[dependencies]
fuels = "0.17.0"
anyhow = "1.0.64"
tokio = { version = "1", features = ["full"] }
```

```bash
# Run with
CONTRACT_PATH="/path/to/contract.sw" SCRIPT_PATH="/path/to/script.sw" cargo run
```
