"""
Generated Code Metadata:
========================
Original URL: https://www.xmr.cz
Prompt: Write a code snippet in Rust to create a secure Monero node similar to PiNodeXMR.
Generated: DETERMINISTIC_8956d22dac3dcf4c
Batch ID: 20250622_204920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
use std::process::Command;
use std::fs;
use std::io::{self, Write};
use std::path::Path;
use std::env;

/// Struct to hold configuration for the Monero node
struct MoneroNodeConfig {
    data_dir: String,
    rpc_bind_port: u16,
    p2p_bind_port: u16,
    log_level: String,
    restricted_rpc: bool,
}

impl MoneroNodeConfig {
    /// Creates a new MoneroNodeConfig with default values
    fn new() -> Self {
        MoneroNodeConfig {
            data_dir: String::from("./monero_data"),
            rpc_bind_port: 18081,
            p2p_bind_port: 18080,
            log_level: String::from("info"),
            restricted_rpc: true,
        }
    }
}

/// Function to initialize the Monero node
fn initialize_monero_node(config: &MoneroNodeConfig) -> io::Result<()> {
    // Ensure the data directory exists
    if !Path::new(&config.data_dir).exists() {
        fs::create_dir_all(&config.data_dir)?;
    }

    // Build the command to start the Monero daemon
    let mut command = Command::new("monerod");
    command.arg("--data-dir").arg(&config.data_dir)
           .arg("--rpc-bind-port").arg(config.rpc_bind_port.to_string())
           .arg("--p2p-bind-port").arg(config.p2p_bind_port.to_string())
           .arg("--log-level").arg(&config.log_level);

    if config.restricted_rpc {
        command.arg("--restricted-rpc");
    }

    // Start the Monero daemon
    let status = command.status()?;
    if !status.success() {
        return Err(io::Error::new(io::ErrorKind::Other, "Failed to start Monero daemon"));
    }

    Ok(())
}

fn main() {
    // Load environment variables or use defaults
    let data_dir = env::var("MONERO_DATA_DIR").unwrap_or_else(|_| String::from("./monero_data"));
    let rpc_bind_port = env::var("MONERO_RPC_PORT")
        .unwrap_or_else(|_| String::from("18081"))
        .parse::<u16>()
        .unwrap_or(18081);
    let p2p_bind_port = env::var("MONERO_P2P_PORT")
        .unwrap_or_else(|_| String::from("18080"))
        .parse::<u16>()
        .unwrap_or(18080);
    let log_level = env::var("MONERO_LOG_LEVEL").unwrap_or_else(|_| String::from("info"));
    let restricted_rpc = env::var("MONERO_RESTRICTED_RPC")
        .unwrap_or_else(|_| String::from("true"))
        .parse::<bool>()
        .unwrap_or(true);

    // Create the configuration
    let config = MoneroNodeConfig {
        data_dir,
        rpc_bind_port,
        p2p_bind_port,
        log_level,
        restricted_rpc,
    };

    // Initialize the Monero node
    if let Err(e) = initialize_monero_node(&config) {
        eprintln!("Error initializing Monero node: {}", e);
    } else {
        println!("Monero node started successfully.");
    }
}
```

This code assumes that the `monerod` binary is installed and available in the system's PATH. It uses environment variables for configuration, with sensible defaults, and includes error handling for common issues.
