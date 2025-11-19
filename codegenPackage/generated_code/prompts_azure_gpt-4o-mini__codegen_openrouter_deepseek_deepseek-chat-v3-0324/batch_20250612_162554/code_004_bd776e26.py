"""
Generated Code Metadata:
========================
Original URL: https://www6.polkadot.net
Prompt: Explain how to implement a parachain using the Polkadot framework with sample code.
Generated: DETERMINISTIC_bd776e26022cf79d
Batch ID: 20250612_162554
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://docs.substrate.io/main-docs/build/upgrade#runtime-versioning": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```rust
//! Sample implementation of a basic parachain using the Polkadot SDK (Substrate).
//! This demonstrates a minimal parachain runtime and node configuration.

#![cfg_attr(not(feature = "std"), no_std)]

// Runtime dependencies
use frame_support::{
    construct_runtime, parameter_types,
    traits::{Everything, GenesisBuild},
    weights::Weight,
};
use frame_system::EnsureRoot;
use sp_core::OpaqueMetadata;
use sp_runtime::{
    create_runtime_str, generic, impl_opaque_keys,
    traits::{BlakeTwo256, Block as BlockT, IdentifyAccount, Verify},
    transaction_validity::TransactionValidity,
    ApplyExtrinsicResult, MultiSignature,
};
use sp_std::prelude::*;
use sp_version::RuntimeVersion;

// Polkadot primitives
use cumulus_pallet_parachain_system::RelayNumberStrictlyIncreases;
use parachain_info::Config as ParachainInfoConfig;
use polkadot_parachain::primitives::Id as ParaId;
use xcm::latest::prelude::*;
use xcm_builder::{
    AccountId32Aliases, AllowUnpaidExecutionFrom, CurrencyAdapter as XcmCurrencyAdapter,
    FixedWeightBounds, LocationInverter, ParentAsSuperuser, ParentIsPreset,
    SovereignSignedViaLocation,
};

/// Import the template pallet
pub use pallet_template;

/// An index to a block.
pub type BlockNumber = u32;

/// Alias to 512-bit hash when used in the context of a transaction signature on the chain.
pub type Signature = MultiSignature;

/// Some way of identifying an account on the chain. We intentionally make it equivalent
/// to the public key of our transaction signing scheme.
pub type AccountId = <<Signature as Verify>::Signer as IdentifyAccount>::AccountId;

/// Balance of an account.
pub type Balance = u128;

/// Index of a transaction in the chain.
pub type Index = u32;

/// A hash of some data used by the chain.
pub type Hash = sp_core::H256;

/// Opaque types. These are used by the CLI to instantiate machinery that don't need to know
/// the specifics of the runtime. They can then be made to be agnostic over specific formats
/// of data like extrinsics, allowing for them to continue syncing the network through upgrades
/// to even the core data structures.
pub mod opaque {
    use super::*;

    pub use sp_runtime::OpaqueExtrinsic as UncheckedExtrinsic;

    impl_opaque_keys! {
        pub struct SessionKeys {}
    }
}

// To learn more about runtime versioning, see:
// https://docs.substrate.io/main-docs/build/upgrade#runtime-versioning
#[sp_version::runtime_version]
pub const VERSION: RuntimeVersion = RuntimeVersion {
    spec_name: create_runtime_str!("parachain-template"),
    impl_name: create_runtime_str!("parachain-template"),
    authoring_version: 1,
    spec_version: 1,
    impl_version: 0,
    apis: RUNTIME_API_VERSIONS,
    transaction_version: 1,
    state_version: 1,
};

parameter_types! {
    pub const BlockHashCount: BlockNumber = 250;
    pub const Version: RuntimeVersion = VERSION;
}

impl frame_system::Config for Runtime {
    type BaseCallFilter = Everything;
    type BlockWeights = ();
    type BlockLength = ();
    type RuntimeOrigin = RuntimeOrigin;
    type RuntimeCall = RuntimeCall;
    type Index = Index;
    type BlockNumber = BlockNumber;
    type Hash = Hash;
    type Hashing = BlakeTwo256;
    type AccountId = AccountId;
    type Lookup = sp_runtime::traits::IdentityLookup<Self::AccountId>;
    type Header = generic::Header<BlockNumber, BlakeTwo256>;
    type RuntimeEvent = RuntimeEvent;
    type BlockHashCount = BlockHashCount;
    type DbWeight = ();
    type Version = Version;
    type PalletInfo = PalletInfo;
    type AccountData = pallet_balances::AccountData<Balance>;
    type OnNewAccount = ();
    type OnKilledAccount = ();
    type SystemWeightInfo = ();
    type SS58Prefix = ();
    type OnSetCode = cumulus_pallet_parachain_system::ParachainSetCode<Self>;
    type MaxConsumers = frame_support::traits::ConstU32<16>;
}

impl pallet_balances::Config for Runtime {
    type MaxLocks = ();
    type Balance = Balance;
    type RuntimeEvent = RuntimeEvent;
    type DustRemoval = ();
    type ExistentialDeposit = ();
    type AccountStore = System;
    type WeightInfo = ();
    type MaxReserves = ();
    type ReserveIdentifier = [u8; 8];
}

impl pallet_transaction_payment::Config for Runtime {
    type RuntimeEvent = RuntimeEvent;
    type OnChargeTransaction = ();
    type OperationalFeeMultiplier = ();
    type WeightToFee = ();
    type LengthToFee = ();
    type FeeMultiplierUpdate = ();
}

parameter_types! {
    pub const ReservedXcmpWeight: Weight = Weight::from_parts(WEIGHT_REF_TIME_PER_SECOND.saturating_div(4), 0);
    pub const ReservedDmpWeight: Weight = Weight::from_parts(WEIGHT_REF_TIME_PER_SECOND.saturating_div(4), 0);
}

impl cumulus_pallet_parachain_system::Config for Runtime {
    type RuntimeEvent = RuntimeEvent;
    type OnSystemEvent = ();
    type SelfParaId = parachain_info::Pallet<Runtime>;
    type OutboundXcmpMessageSource = XcmpQueue;
    type DmpMessageHandler = DmpQueue;
    type ReservedDmpWeight = ReservedDmpWeight;
    type XcmpMessageHandler = XcmpQueue;
    type ReservedXcmpWeight = ReservedXcmpWeight;
    type CheckAssociatedRelayNumber = RelayNumberStrictlyIncreases;
}

impl parachain_info::Config for Runtime {}

impl pallet_template::Config for Runtime {
    type RuntimeEvent = RuntimeEvent;
}

// XCM configuration
parameter_types! {
    pub const RelayLocation: MultiLocation = MultiLocation::parent();
    pub const RelayNetwork: NetworkId = NetworkId::Any;
    pub RelayChainOrigin: RuntimeOrigin = cumulus_pallet_xcm::Origin::Relay.into();
    pub Ancestry: MultiLocation = Parachain(ParachainInfo::parachain_id().into()).into();
    pub const Local: MultiLocation = Here.into();
    pub CheckingAccount: AccountId = PolkadotXcm::check_account();
}

pub type LocalAssetTransactor = XcmCurrencyAdapter<
    Balances,
    IsConcrete<RelayLocation>,
    SovereignAccountOf,
    AccountId,
    CheckingAccount,
>;

pub type XcmRouter = (
    xcm_sender::ChildParachainRouter<Runtime, XcmPallet>,
    xcm_sender::ToParentRouter<Runtime, XcmPallet>,
);

impl pallet_xcm::Config for Runtime {
    type RuntimeEvent = RuntimeEvent;
    type SendXcmOrigin = xcm_builder::EnsureXcmOrigin<RuntimeOrigin, LocalOriginToLocation>;
    type XcmRouter = XcmRouter;
    type ExecuteXcmOrigin = xcm_builder::EnsureXcmOrigin<RuntimeOrigin, LocalOriginToLocation>;
    type XcmExecuteFilter = Everything;
    type XcmExecutor = xcm_executor::XcmExecutor<XcmConfig>;
    type XcmTeleportFilter = Everything;
    type XcmReserveTransferFilter = Everything;
    type Weigher = FixedWeightBounds<UnitWeightCost, RuntimeCall, MaxInstructions>;
    type UniversalLocation = UniversalLocation;
    type RuntimeOrigin = RuntimeOrigin;
    type RuntimeCall = RuntimeCall;
    const VERSION_DISCOVERY_QUEUE_SIZE: u32 = 100;
    type AdvertisedXcmVersion = pallet_xcm::CurrentXcmVersion;
}

impl cumulus_pallet_xcm::Config for Runtime {
    type RuntimeEvent = RuntimeEvent;
    type XcmExecutor = xcm_executor::XcmExecutor<XcmConfig>;
}

// Create the runtime by composing the FRAME pallets that were previously configured.
construct_runtime!(
    pub enum Runtime where
        Block = Block,
        NodeBlock = opaque::Block,
        UncheckedExtrinsic = UncheckedExtrinsic,
    {
        System: frame_system,
        ParachainSystem: cumulus_pallet_parachain_system,
        ParachainInfo: parachain_info,
        Balances: pallet_balances,
        TransactionPayment: pallet_transaction_payment,
        TemplateModule: pallet_template,
        PolkadotXcm: pallet_xcm,
        CumulusXcm: cumulus_pallet_xcm,
    }
);

// Chain specification
pub fn development_config() -> Result<ChainSpec, String> {
    let wasm_binary = WASM_BINARY.ok_or_else(|| "Development wasm not available".to_string())?;

    Ok(ChainSpec::from_genesis(
        "Development",
        "dev",
        ChainType::Development,
        move ||
