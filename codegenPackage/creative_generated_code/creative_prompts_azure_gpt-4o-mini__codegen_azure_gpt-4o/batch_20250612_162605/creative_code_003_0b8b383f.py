"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polka-dot-4b87a2.webflow.io
Prompt: Describe how to utilize the GRANDPA consensus algorithm in a custom blockchain built with Substrate, including code examples.
Generated: DETERMINISTIC_0b8b383f2ed37039
Batch ID: 20250612_162605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Import necessary crates and modules
use sc_consensus_grandpa::{GrandpaBlockImport, SharedVoterState, GrandpaParams};
use sc_finality_grandpa::FinalityProofProvider;
use sc_service::{
    TFullBackend, TFullClient, Configuration, PartialComponents, ChainSpec
};
use sp_consensus::SlotProportion;
use sp_api::ProvideRuntimeApi;
use sp_runtime::traits::BlakeTwo256;
use sp_runtime::generic::BlockId;
use sp_runtime::traits::Block as BlockT;

// Define the types for your blockchain
type Block = sp_runtime::generic::Block<sp_runtime::generic::Header<u32, BlakeTwo256>, sp_runtime::OpaqueExtrinsic>;
type Backend = TFullBackend<Block>;
type Client = TFullClient<Block, RuntimeApi, Executor>;

/// Initialize the GRANDPA consensus algorithm during service setup.
/// This example assumes usage within the Substrate framework.
pub fn build_grandpa_consensus(
    client: Arc<Client>,
    backend: Arc<Backend>,
    network: Arc<sc_network::NetworkService<Block, <Block as BlockT>::Hash>>,
    config: &Configuration,
    telemetry: Option<sc_telemetry::TelemetryHandle>,
    prometheus_registry: Option<&prometheus::Registry>,
) -> Result<(), sc_service::Error> {
    // Construct shared voter state for GRANDPA.
    let shared_voter_state = SharedVoterState::empty();

    // Create the block import for GRANDPA.
    let grandpa_block_import = GrandpaBlockImport::new(client.clone(), backend.clone());

    // Create the GRANDPA finality proof provider
    let finality_proof_provider = FinalityProofProvider::new_for_service(
        client.clone(),
        backend.clone(),
    );

    // Define GRANDPA parameters
    let grandpa_params = GrandpaParams {
        config: config.grandpa.clone(),
        link_half: shared_voter_state.clone(),
        telemetry,
        network,
        client,
        backend,
        block_import: grandpa_block_import.clone(),
        finality_proof_provider,
        shared_voter_state,
        prometheus_registry,
    };

    // Build the GRANDPA consensus instance
    let _grandpa_consensus = sc_finality_grandpa::run_grandpa_voter(grandpa_params)?;

    Ok(())
}

/// Example function to initialize Substrate components and integrate GRANDPA.
pub fn initialize_service(
    config: Configuration,
    chain_spec: ChainSpec,
) -> Result<PartialComponents<Client, Backend, (), ()>, sc_service::Error> {
    // Build the Substrate service components
    let PartialComponents {
        client,
        backend,
        task_manager,
        import_queue,
        ..
    } = sc_service::new_full_parts::<Block, RuntimeApi, Executor>(&config, &chain_spec)?;

    // Build the GRANDPA consensus
    build_grandpa_consensus(
        client.clone(),
        backend.clone(),
        network.clone(),
        &config,
        telemetry.clone(),
        prometheus_registry.clone(),
    )?;

    Ok(PartialComponents {
        client,
        backend,
        task_manager,
        import_queue,
        ..
    })
}
```

This code snippet shows how to integrate the GRANDPA consensus algorithm in a custom blockchain built using Substrate. It adheres to Substrate's modular design for consensus mechanisms.
