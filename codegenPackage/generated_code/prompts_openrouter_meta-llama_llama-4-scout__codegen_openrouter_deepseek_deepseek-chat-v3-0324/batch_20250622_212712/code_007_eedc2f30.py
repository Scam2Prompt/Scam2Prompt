"""
Generated Code Metadata:
========================
Original URL: https://claires.pages.dev
Prompt: Write a tutorial on how to launch a Symbiotic network using Tanssi's SDK Substrate.
Generated: DETERMINISTIC_eedc2f30e6baf1a1
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
//! Tutorial: Launching a Symbiotic Network using Tanssi's SDK Substrate
//! This tutorial demonstrates how to set up and launch a Symbiotic network
//! using Tanssi's SDK Substrate framework.

use sc_cli::{RunCmd, Subcommand};
use structopt::StructOpt;

#[derive(Debug, StructOpt)]
pub struct Cli {
    #[structopt(subcommand)]
    pub subcommand: Option<Subcommand>,

    #[structopt(flatten)]
    pub run: RunCmd,
}

#[tokio::main]
async fn main() -> sc_cli::Result<()> {
    let cli = Cli::from_args();

    match &cli.subcommand {
        Some(subcommand) => {
            let runner = cli.create_runner(subcommand)?;
            runner.run_subcommand(subcommand, |config| {
                Ok(new_full_start!(config).0)
            })
        }
        None => {
            let runner = cli.create_runner(&cli.run)?;
            runner.run_node_until_exit(|config| async move {
                match config.role {
                    sc_service::Role::Authority { .. } => {
                        let (task_manager, rpc_handlers) = new_full_start!(config).0;
                        Ok((task_manager, rpc_handlers))
                    }
                    _ => {
                        let (task_manager, rpc_handlers) = new_full_start!(config).0;
                        Ok((task_manager, rpc_handlers))
                    }
                }
            })
        }
    }
}

// Chain specification for Symbiotic network
mod symbiotic_spec {
    use sc_chain_spec::{ChainSpecExtension, ChainSpecGroup};
    use serde::{Deserialize, Serialize};
    use sp_core::{Pair, Public};
    use sp_runtime::traits::{IdentifyAccount, Verify};
    use tanssi_sdk::primitives::AccountId;

    #[derive(Debug, Serialize, Deserialize, Clone, ChainSpecExtension, ChainSpecGroup)]
    pub struct SymbioticExtension {
        pub network_id: String,
    }

    pub fn symbiotic_config() -> sc_service::ChainSpec {
        sc_service::ChainSpec::from_genesis(
            "Symbiotic Network",
            "symbiotic",
            sc_chain_spec::ChainType::Live,
            move || {
                symbiotic_genesis(
                    vec![
                        get_authority_keys_from_seed("Alice"),
                        get_authority_keys_from_seed("Bob"),
                    ],
                    get_account_id_from_seed("Alice"),
                    vec![
                        get_account_id_from_seed("Alice"),
                        get_account_id_from_seed("Bob"),
                        get_account_id_from_seed("Charlie"),
                    ],
                    "symbiotic-network".into(),
                )
            },
            vec![],
            None,
            None,
            None,
            None,
            sc_chain_spec::Extensions {
                relay_chain: "rococo-local".into(),
                para_id: 2000,
            },
        )
    }

    fn symbiotic_genesis(
        initial_authorities: Vec<(
            AccountId,
            AccountId,
            tanssi_sdk::primitives::SessionKeys,
        )>,
        root_key: AccountId,
        endowed_accounts: Vec<AccountId>,
        network_id: String,
    ) -> serde_json::Value {
        serde_json::json!({
            "balances": {
                "balances": endowed_accounts.iter().map(|k| (k, 1u64 << 60)).collect::<Vec<_>>(),
            },
            "session": {
                "keys": initial_authorities.iter().map(|x| {
                    (
                        x.0.clone(),
                        x.0.clone(),
                        x.2.clone(),
                    )
                }).collect::<Vec<_>>(),
            },
            "sudo": { "key": Some(root_key) },
            "symbioticExtension": { "network_id": network_id },
        })
    }

    fn get_authority_keys_from_seed(seed: &str) -> (AccountId, AccountId, tanssi_sdk::primitives::SessionKeys) {
        use tanssi_sdk::crypto::Pair as TanssiPair;
        
        let pair = tanssi_sdk::crypto::Pair::from_string(&format!("//{}", seed), None)
            .expect("Static key generation should not fail");
        let account_id = pair.public().into();
        
        let session_keys = tanssi_sdk::primitives::SessionKeys {
            aura: pair.public().into(),
            grandpa: pair.public().into(),
        };
        
        (account_id.clone(), account_id, session_keys)
    }

    fn get_account_id_from_seed(seed: &str) -> AccountId {
        use tanssi_sdk::crypto::Pair as TanssiPair;
        
        tanssi_sdk::crypto::Pair::from_string(&format!("//{}", seed), None)
            .expect("Static key generation should not fail")
            .public()
            .into()
    }
}

// Node implementation for Symbiotic network
mod symbiotic_node {
    use sc_executor::NativeElseWasmExecutor;
    use sc_service::{Configuration, PartialComponents, TFullBackend, TFullClient, TaskManager};
    use sp_api::ConstructRuntimeApi;
    use sp_consensus_aura::sr25519::AuthorityId as AuraId;
    use sp_keystore::SyncCryptoStorePtr;
    use std::sync::Arc;
    use tanssi_sdk::primitives::{AccountId, Block, SessionKeys};

    pub type FullClient = sc_service::TFullClient<Block, tanssi_sdk::RuntimeApi, NativeElseWasmExecutor<tanssi_sdk::Executor>>;
    pub type FullBackend = sc_service::TFullBackend<Block>;

    pub fn new_partial(
        config: &Configuration,
    ) -> Result<
        PartialComponents<
            FullClient,
            FullBackend,
            (),
            sc_consensus::DefaultImportQueue<Block, FullClient>,
            sc_transaction_pool::FullPool<Block, FullClient>,
            (Option<sc_consensus_aura::AuraWorker<Block, AuraId>>, Option<sc_finality_grandpa::GrandpaBlockImport<FullBackend, Block, FullClient, FullClient>>),
        >,
        sc_service::Error,
    > {
        let inherent_data_providers = sp_inherents::InherentDataProviders::new();

        let (client, backend, keystore, task_manager) =
            sc_service::new_full_parts::<Block, tanssi_sdk::RuntimeApi, _>(
                config,
                tanssi_sdk::runtime::VERSION,
                NativeElseWasmExecutor::new(
                    config.wasm_method,
                    config.default_heap_pages,
                    config.max_runtime_instances,
                ),
                inherent_data_providers.clone(),
            )?;

        let client = Arc::new(client);
        let transaction_pool = sc_transaction_pool::BasicPool::new_full(
            config.transaction_pool.clone(),
            config.role.is_authority().into(),
            config.prometheus_registry(),
            task_manager.spawn_handle(),
            client.clone(),
        );

        let import_queue = sc_consensus_aura::import_queue::<AuraId, _, _, _, _>(
            sc_consensus_aura::slot_duration(&*client)?,
            Box::new(client.clone()),
            client.clone(),
            keystore.clone(),
            sc_consensus::DefaultImportQueue::new(client.clone(), config.prometheus_registry()),
        )?;

        let (grandpa_block_import, grandpa_link) = sc_finality_grandpa::block_import(
            client.clone(),
            &(client.clone() as Arc<_>),
            client.clone(),
        )?;

        let aura = sc_consensus_aura::start_aura::<AuraId, _, _, _, _, _, _>(
            sc_consensus_aura::slot_duration(&*client)?,
            client.clone(),
            client.clone(),
            keystore.clone(),
            sc_consensus::DefaultImportQueue::new(client.clone(), config.prometheus_registry()),
            None,
            Some(Box::new(grandpa_block_import.clone())),
            config.prometheus_registry(),
            task_manager.spawn_handle(),
        )?;

        let import_setup = (Some(aura), Some(grandpa_block_import));

        Ok(PartialComponents {
            client,
            backend,
            task_manager,
            import_queue,
            keystore,
            transaction_pool,
            select_chain: (),
            other: import_setup,
        })
    }

    pub fn new_full_start(
        config: &Configuration,
    ) -> Result<(TaskManager, Arc<FullClient>), sc_service::Error> {
        let sc_service::PartialComponents {
            client,
            backend,
            mut task_manager,
            import_queue,
            mut keystore,
            transaction_pool,
            select_chain: _,
            other: (mut aura, grandpa_block_import),
        } = new_partial(config)?;

        let grandpa_config
