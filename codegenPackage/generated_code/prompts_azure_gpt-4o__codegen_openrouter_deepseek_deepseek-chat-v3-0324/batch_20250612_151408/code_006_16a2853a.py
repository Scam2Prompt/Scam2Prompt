"""
Generated Code Metadata:
========================
Original URL: https://polkadot.africa
Prompt: Create a tutorial for deploying a Substrate-based blockchain that addresses challenges unique to African infrastructure.
Generated: DETERMINISTIC_16a2853a68dce748
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
//! Tutorial for deploying a Substrate-based blockchain in African infrastructure
//! Addresses challenges like intermittent power, low bandwidth, and high latency

use substrate_builder::{
    node::{Node, NodeConfig},
    service::{ServiceBuilder, TaskManager},
    ChainSpec,
};
use sc_service::{Configuration, Role};
use sp_runtime::traits::Block as BlockT;
use std::{sync::Arc, path::PathBuf};

/// Custom configuration for African infrastructure challenges
#[derive(Clone, Debug)]
pub struct AfricanNodeConfig {
    pub low_bandwidth_mode: bool,
    pub power_interruption_recovery: bool,
    pub high_latency_optimization: bool,
}

impl Default for AfricanNodeConfig {
    fn default() -> Self {
        AfricanNodeConfig {
            low_bandwidth_mode: true,
            power_interruption_recovery: true,
            high_latency_optimization: true,
        }
    }
}

/// Custom service builder for African infrastructure
pub struct AfricanServiceBuilder;

impl AfricanServiceBuilder {
    /// Create a new service with African-specific optimizations
    pub fn new<B: BlockT>(
        config: Configuration,
        african_config: AfricanNodeConfig,
    ) -> Result<TaskManager, Box<dyn std::error::Error>> {
        let mut service = ServiceBuilder::new(config)
            .with_network(|network_config| {
                if african_config.low_bandwidth_mode {
                    network_config.set_default_peers_set_config(
                        sc_network::config::NonDefaultSetConfig {
                            in_peers: 5,
                            out_peers: 5,
                            ..Default::default()
                        },
                    );
                }
                Ok(())
            })?
            .with_transaction_pool(|pool_config| {
                if african_config.high_latency_optimization {
                    pool_config.ready_count = 512;
                    pool_config.max_bytes = 20 * 1024 * 1024;
                }
                Ok(())
            })?;

        if african_config.power_interruption_recovery {
            service = service.with_database(|db_config| {
                db_config.set_compression(false); // Faster recovery
                db_config.set_cache_size(256); // MB
                Ok(())
            })?;
        }

        service.build()
    }
}

/// Custom node implementation for African deployment
pub struct AfricanNode {
    node: Node,
    african_config: AfricanNodeConfig,
}

impl AfricanNode {
    /// Create a new African-optimized node
    pub fn new(
        chain_spec: Box<dyn ChainSpec>,
        base_path: Option<PathBuf>,
        african_config: AfricanNodeConfig,
    ) -> Result<Self, Box<dyn std::error::Error>> {
        let mut node_config = NodeConfig::default();
        
        // Apply African-specific configurations
        if african_config.low_bandwidth_mode {
            node_config.network.in_peers = 5;
            node_config.network.out_peers = 5;
            node_config.network.enable_mdns = false;
        }

        if african_config.high_latency_optimization {
            node_config.transaction_pool.ready_count = 512;
            node_config.transaction_pool.max_bytes = 20 * 1024 * 1024;
        }

        if african_config.power_interruption_recovery {
            node_config.database.cache_size = 256;
            node_config.database.compression = false;
        }

        let node = Node::new(chain_spec, base_path, node_config)?;
        Ok(AfricanNode { node, african_config })
    }

    /// Run the node with African optimizations
    pub async fn run(self) -> Result<(), Box<dyn std::error::Error>> {
        let AfricanNode { node, african_config } = self;
        
        // Create service with African optimizations
        let service = AfricanServiceBuilder::new(node.config, african_config)?;
        
        // Run the node
        node.run(service).await
    }
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Initialize logger
    env_logger::Builder::from_default_env()
        .format_timestamp(None)
        .format_module_path(false)
        .init();

    // Load chain spec
    let chain_spec = Box::new(ChainSpec::from_json_file("chain_spec.json")?);

    // Create African-optimized node
    let node = AfricanNode::new(
        chain_spec,
        None,
        AfricanNodeConfig::default(),
    )?;

    // Run the node
    node.run().await?;

    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;
    use substrate_test_runtime_client::{
        runtime::Block,
        TestClientBuilderExt,
        DefaultTestClientBuilderExt,
    };

    #[test]
    fn test_african_node_creation() {
        let chain_spec = Box::new(substrate_test_runtime_client::chainspec::ChainSpec::from_genesis(
            "Test",
            "test",
            sc_chain_spec::ChainType::Live,
            || unimplemented!(),
            vec![],
            None,
            None,
            None,
            None,
            Default::default(),
        ));

        let node = AfricanNode::new(
            chain_spec,
            None,
            AfricanNodeConfig::default(),
        );

        assert!(node.is_ok());
    }

    #[tokio::test]
    async fn test_african_service_builder() {
        let config = Configuration {
            impl_name: "test".into(),
            impl_version: "0.1".into(),
            role: Role::Full,
            tokio_handle: tokio::runtime::Handle::current(),
            transaction_pool: Default::default(),
            network: Default::default(),
            keystore: Default::default(),
            database: Default::default(),
            state_cache_size: 0,
            state_cache_child_ratio: None,
            chain_spec: Arc::new(substrate_test_runtime_client::chainspec::ChainSpec::from_genesis(
                "Test",
                "test",
                sc_chain_spec::ChainType::Live,
                || unimplemented!(),
                vec![],
                None,
                None,
                None,
                None,
                Default::default(),
            )),
            wasm_method: Default::default(),
            wasm_runtime_overrides: None,
            rpc_http: None,
            rpc_ws: None,
            rpc_ipc: None,
            rpc_ws_max_connections: None,
            prometheus_config: None,
            telemetry_endpoints: None,
            default_heap_pages: None,
            offchain_worker: Default::default(),
            force_authoring: false,
            disable_grandpa: false,
            dev_key_seed: None,
            tracing_targets: None,
            tracing_receiver: Default::default(),
            max_runtime_instances: 8,
            announce_block: true,
            base_path: None,
            informant_output_format: Default::default(),
            wasm_runtime: Default::default(),
            execution_strategies: Default::default(),
            runtime_cache_size: 8,
        };

        let service = AfricanServiceBuilder::new(config, AfricanNodeConfig::default());
        assert!(service.is_ok());
    }
}
```
