"""
Generated Code Metadata:
========================
Original URL: https://polka-dot-4b87a2.webflow.io
Prompt: Create a tutorial on building a custom blockchain using Polkadot's Substrate framework, including parachain design and deployment.
Generated: DETERMINISTIC_6ac79e608121bb9b
Batch ID: 20250622_212502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// substrate-node-template/runtime/src/lib.rs

#![cfg_attr(not(feature = "std"), no_std)]

use sp_std::prelude::*;
use frame_support::{
    decl_module, decl_storage, decl_event, decl_error,
    traits::Randomness,
    weights::Weight,
};
use frame_system::{self as system, ensure_signed};
use sp_runtime::{
    traits::{Hash, BlakeTwo256},
    DispatchResult,
};
use sp_core::H256;

/// Configure the pallet by specifying the parameters and types on which it depends.
pub trait Config: system::Config {
    /// The overarching event type.
    type Event: From<Event<Self>> + Into<<Self as system::Config>::Event>;
    /// The randomness type.
    type Randomness: Randomness<H256>;
}

decl_storage! {
    trait Store for Module<T: Config> as TemplateModule {
        /// A map from hashes to the block number when they were submitted.
        Proofs: map hasher(blake2_128_concat) H256 => T::BlockNumber;
    }
}

decl_event!(
    pub enum Event<T> where BlockNumber = <T as system::Config>::BlockNumber {
        /// Event emitted when a proof is stored.
        ClaimCreated(H256, BlockNumber),
        /// Event emitted when a proof is revoked.
        ClaimRevoked(H256),
    }
);

decl_error! {
    pub enum Error for Module<T: Config> {
        /// The proof has already been claimed.
        ProofAlreadyClaimed,
        /// The proof does not exist, so it cannot be revoked.
        NoSuchProof,
        /// The proof was claimed by a different account, so caller can't revoke it.
        NotProofOwner,
    }
}

decl_module! {
    pub struct Module<T: Config> for enum Call where origin: T::Origin {
        type Error = Error<T>;

        fn deposit_event() = default;

        /// Create a new proof.
        #[weight = 10_000]
        pub fn create_claim(origin, proof: H256) -> DispatchResult {
            let sender = ensure_signed(origin)?;

            ensure!(!Proofs::<T>::contains_key(&proof), Error::<T>::ProofAlreadyClaimed);

            let current_block = <system::Module<T>>::block_number();
            Proofs::<T>::insert(&proof, current_block);

            Self::deposit_event(RawEvent::ClaimCreated(proof, current_block));
            Ok(())
        }

        /// Revoke an existing proof.
        #[weight = 10_000]
        pub fn revoke_claim(origin, proof: H256) -> DispatchResult {
            let sender = ensure_signed(origin)?;

            ensure!(Proofs::<T>::contains_key(&proof), Error::<T>::NoSuchProof);

            Proofs::<T>::remove(&proof);

            Self::deposit_event(RawEvent::ClaimRevoked(proof));
            Ok(())
        }
    }
}
```

```rust
// substrate-node-template/node/src/chain_spec.rs

use node_template_runtime::{AccountId, GenesisConfig, Signature};
use sp_core::{Pair, Public, sr25519};
use sp_runtime::traits::{Verify, IdentifyAccount};

/// Generate a crypto pair from seed.
pub fn get_from_seed<TPublic: Public>(seed: &str) -> <TPublic::Pair as Pair>::Public {
    TPublic::Pair::from_string(&format!("//{}", seed), None)
        .expect("static values are valid; qed")
        .public()
}

/// Generate an account ID from seed.
pub fn get_account_id_from_seed<TPublic: Public>(seed: &str) -> AccountId
where
    <TPublic::Pair as Pair>::Public: Into<AccountId>,
{
    get_from_seed::<TPublic>(seed).into()
}

/// Generate the initial chain spec.
pub fn testnet_genesis() -> GenesisConfig {
    let endowed_accounts = vec![
        get_account_id_from_seed::<sr25519::Public>("Alice"),
        get_account_id_from_seed::<sr25519::Public>("Bob"),
        get_account_id_from_seed::<sr25519::Public>("Charlie"),
    ];

    GenesisConfig {
        system: Default::default(),
        balances: node_template_runtime::BalancesConfig {
            balances: endowed_accounts.iter().cloned().map(|k| (k, 1 << 60)).collect(),
        },
        template: node_template_runtime::TemplateConfig {
            proofs: vec![],
        },
    }
}
```

```rust
// substrate-node-template/node/src/service.rs

use std::sync::Arc;
use sc_cli::SubstrateCli;
use sc_service::{PartialComponents, ServiceBuilder};
use node_template_runtime::{self, RuntimeApi};
use sc_telemetry::{TelemetryHandle, TelemetryWorkerHandle};

type FullClient = sc_service::TFullClient<Block, RuntimeApi, NativeElseWasmExecutor<Executor>>;
type FullBackend = sc_service::TFullBackend<Block>;
type FullSelectChain = sc_consensus::LongestChain<FullBackend, Block>;

pub fn new_partial(
    config: &Configuration,
) -> Result<
    PartialComponents<
        FullClient,
        FullBackend,
        FullSelectChain,
        sp_consensus::DefaultImportQueue<Block, FullClient>,
        sc_transaction_pool::FullPool<Block, FullClient>,
        (
            Option<TelemetryWorkerHandle>,
            Option<TelemetryHandle>,
        ),
    >,
    ServiceError,
> {
    let telemetry = config.telemetry_endpoints.clone()
        .filter(|x| !x.is_empty())
        .map(|endpoints| -> Result<_, sc_telemetry::Error> {
            let worker = TelemetryWorker::new(16)?;
            let telemetry = worker.handle().new_telemetry(endpoints);
            Ok((worker, telemetry))
        })
        .transpose()?;

    let executor = NativeElseWasmExecutor::<Executor>::new(
        config.wasm_method,
        config.default_heap_pages,
        config.max_runtime_instances,
    );

    let (client, backend, keystore_container, task_manager) =
        sc_service::new_full_parts::<Block, RuntimeApi, _>(
            &config,
            telemetry.as_ref().map(|(_, telemetry)| telemetry.handle()),
            executor,
        )?;
    let client = Arc::new(client);

    let telemetry_worker_handle = telemetry.as_ref().map(|(worker, _)| worker.handle());

    let telemetry = telemetry.as_ref().map(|(_, telemetry)| telemetry.clone());

    let select_chain = sc_consensus::LongestChain::new(backend.clone());

    let transaction_pool = sc_transaction_pool::BasicPool::new_full(
        config.transaction_pool.clone(),
        config.role.is_authority().into(),
        config.prometheus_registry(),
        task_manager.spawn_handle(),
        client.clone(),
    );

    let import_queue = sc_consensus_aura::import_queue::<_, _, _, AuraPair, _, _>(
        ImportQueueParams {
            block_import: client.clone(),
            client: client.clone(),
            create_inherent_data_providers: move |_, _| async move {
                Ok(())
            },
            spawner: &task_manager.spawn_essential_handle(),
            registry: config.prometheus_registry(),
            can_author_with: sp_consensus::CanAuthorWithNativeVersion::new(client.executor().clone()),
        },
    )?;

    Ok(PartialComponents {
        client,
        backend,
        task_manager,
        import_queue,
        keystore_container,
        select_chain,
        transaction_pool,
        telemetry: (telemetry_worker_handle, telemetry),
    })
}

pub fn new_full(config: Configuration) -> Result<TaskManager, ServiceError> {
    let sc_service::PartialComponents {
        client,
        backend,
        mut task_manager,
        import_queue,
        mut keystore_container,
        select_chain,
        transaction_pool,
        telemetry: (telemetry_worker_handle, telemetry),
    } = new_partial(&config)?;

    let (network, network_status_sinks, system_rpc_tx, start_network) =
        sc_service::build_network(sc_service::BuildNetworkParams {
            config: &config,
            client: client.clone(),
            transaction_pool: transaction_pool.clone(),
            spawn_handle: task_manager.spawn_handle(),
            import_queue,
            on_demand: None,
            block_announce_validator_builder: None,
        })?;

    if config.offchain_worker.enabled {
        sc_service::build_offchain_workers(
            &config,
            backend.clone(),
            task_manager.spawn_handle(),
            client.clone(),
            network.clone(),
        );
    }

    let role = config.role.clone();
    let prometheus_registry = config.prometheus_registry().cloned();
    let rpc_extensions_builder = {
        let client = client.clone();
        Box::new(move |deny_unsafe, _| {
            let
