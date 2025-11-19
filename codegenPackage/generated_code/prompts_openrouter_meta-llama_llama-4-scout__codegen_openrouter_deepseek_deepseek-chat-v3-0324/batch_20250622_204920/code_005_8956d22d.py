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
use std::net::{IpAddr, Ipv4Addr, SocketAddr};
use std::sync::Arc;
use std::time::Duration;
use monero_rpc::{
    DaemonRpcClient,
    RpcClient,
    WalletRpcClient,
};
use tokio::sync::Mutex;
use tokio::time;
use anyhow::{Context, Result};
use log::{info, error};

#[derive(Debug, Clone)]
pub struct MoneroNodeConfig {
    pub rpc_bind_ip: IpAddr,
    pub rpc_bind_port: u16,
    pub restricted_rpc: bool,
    pub data_dir: String,
    pub log_level: String,
}

impl Default for MoneroNodeConfig {
    fn default() -> Self {
        Self {
            rpc_bind_ip: IpAddr::V4(Ipv4Addr::new(127, 0, 0, 1)),
            rpc_bind_port: 18081,
            restricted_rpc: true,
            data_dir: "./monero_data".to_string(),
            log_level: "info".to_string(),
        }
    }
}

pub struct MoneroNode {
    config: MoneroNodeConfig,
    daemon_client: Arc<Mutex<Option<DaemonRpcClient>>>,
    wallet_client: Arc<Mutex<Option<WalletRpcClient>>>,
}

impl MoneroNode {
    pub fn new(config: MoneroNodeConfig) -> Self {
        Self {
            config,
            daemon_client: Arc::new(Mutex::new(None)),
            wallet_client: Arc::new(Mutex::new(None)),
        }
    }

    pub async fn start(&self) -> Result<()> {
        self.initialize_logging()?;
        self.start_daemon().await?;
        self.start_wallet_rpc().await?;
        self.monitor_services().await?;
        Ok(())
    }

    fn initialize_logging(&self) -> Result<()> {
        env_logger::Builder::from_default_env()
            .filter_level(self.config.log_level.parse().unwrap_or(log::LevelFilter::Info))
            .init();
        Ok(())
    }

    async fn start_daemon(&self) -> Result<()> {
        let socket = SocketAddr::new(self.config.rpc_bind_ip, self.config.rpc_bind_port);
        let client = DaemonRpcClient::new(socket)
            .with_context(|| format!("Failed to connect to Monero daemon at {}", socket))?;

        let mut guard = self.daemon_client.lock().await;
        *guard = Some(client);
        info!("Monero daemon RPC client initialized");
        Ok(())
    }

    async fn start_wallet_rpc(&self) -> Result<()> {
        let socket = SocketAddr::new(self.config.rpc_bind_ip, self.config.rpc_bind_port + 1);
        let client = WalletRpcClient::new(socket)
            .with_context(|| format!("Failed to connect to Monero wallet RPC at {}", socket))?;

        let mut guard = self.wallet_client.lock().await;
        *guard = Some(client);
        info!("Monero wallet RPC client initialized");
        Ok(())
    }

    async fn monitor_services(&self) -> Result<()> {
        let mut interval = time::interval(Duration::from_secs(30));
        loop {
            interval.tick().await;
            
            // Check daemon connection
            {
                let guard = self.daemon_client.lock().await;
                if let Some(client) = &*guard {
                    if let Err(e) = client.get_block_count().await {
                        error!("Daemon connection error: {}", e);
                    }
                }
            }
            
            // Check wallet connection
            {
                let guard = self.wallet_client.lock().await;
                if let Some(client) = &*guard {
                    if let Err(e) = client.get_balance().await {
                        error!("Wallet connection error: {}", e);
                    }
                }
            }
        }
    }

    pub async fn get_daemon_client(&self) -> Option<DaemonRpcClient> {
        let guard = self.daemon_client.lock().await;
        guard.clone()
    }

    pub async fn get_wallet_client(&self) -> Option<WalletRpcClient> {
        let guard = self.wallet_client.lock().await;
        guard.clone()
    }
}

#[tokio::main]
async fn main() -> Result<()> {
    let config = MoneroNodeConfig::default();
    let node = MoneroNode::new(config);
    node.start().await?;
    Ok(())
}
```
