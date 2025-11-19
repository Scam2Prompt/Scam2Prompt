"""
Generated Code Metadata:
========================
Original URL: https://polka-dot-4b87a2.webflow.io
Prompt: Write a code snippet that demonstrates how to implement a parachain using the Substrate SDK in Polkadot.
Generated: DETERMINISTIC_083d36efb79faafa
Batch ID: 20250612_162605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
//! A minimal Substrate parachain implementation using the Substrate SDK.

#![cfg_attr(not(feature = "std"), no_std)]

use frame_support::{
    construct_runtime, parameter_types,
    traits::{Everything, Nothing},
    weights::Weight,
};
use frame_system::EnsureRoot;
use sp_api::impl_runtime_apis;
use sp_core::OpaqueMetadata;
use sp_runtime::{
    create_runtime_str, generic, impl_opaque_keys,
    traits::{BlakeTwo256, Block as BlockT, IdentifyAccount, Verify},
    transaction_validity::{TransactionSource, TransactionValidity},
    ApplyExtrinsicResult, MultiSignature,
};
use sp_std::prelude::*;
use sp_version::RuntimeVersion;
use xcm::latest::prelude::*;
use xcm_builder::{
    AccountId32Aliases, AllowUnpaidExecutionFrom, CurrencyAdapter as XcmCurrencyAdapter,
    FixedWeightBounds, LocationInverter, NativeAsset, ParentIsPreset, SiblingParachainConvertsVia,
    SignedAccountId32AsNative, SignedToAccountId32, SovereignSignedViaLocation,
};
use xcm_executor::{Config, XcmExecutor};

pub use parachains_common::{AccountId, Balance, BlockNumber, Hash, Header, Index, Signature};
use parachains_common::{AuraId, SLOT_DURATION};

/// The address format for describing accounts.
pub type Address = sp_runtime::MultiAddress<AccountId, ()>;
/// Block type as expected by this runtime.
pub type Block = generic::Block<Header, UncheckedExtrinsic>;
/// A Block signed with a Justification
pub type SignedBlock = generic::SignedBlock<Block>;
/// BlockId type as expected by this runtime.
pub type BlockId = generic::BlockId<Block>;
/// The SignedExtension to the basic transaction logic.
pub type SignedExtra = (
    frame_system::CheckSpecVersion<Runtime>,
    frame_system::CheckTxVersion<Runtime>,
    frame_system::CheckGenesis<Runtime>,
    frame_system::CheckEra<Runtime>,
    frame_system::CheckNonce<Runtime>,
    frame_system::CheckWeight<Runtime>,
    pallet_transaction_payment::ChargeTransactionPayment<Runtime>,
);
/// Unchecked extrinsic type as expected by this runtime.
pub type UncheckedExtrinsic = generic::UncheckedExtrinsic<Address, Call, Signature, SignedExtra>;
/// Extrinsic type that has already been checked.
pub type CheckedExtrinsic = generic::CheckedExtrinsic<AccountId, Call, SignedExtra>;
/// Executive: handles dispatch to the various modules.
pub type Executive = frame_executive::Executive<
    Runtime,
    Block,
    frame_system::ChainContext<Runtime>,
    Runtime,
    AllPalletsWithSystem,
>;

/// Opaque types. These are used by the CLI to instantiate machinery that don't need to know
/// the specifics of the runtime. They can then be made to be agnostic over specific formats
/// of data like extrinsics, allowing for them to continue syncing the network through upgrades
/// to even the core data structures.
pub mod opaque {
    use super::*;

    pub use sp_runtime::OpaqueExtrinsic as UncheckedExtrinsic;

    impl_opaque_keys! {
        pub struct SessionKeys {
            pub aura: Aura,
        }
    }
}

parameter_types! {
    pub const Version: RuntimeVersion = RuntimeVersion {
        spec_name: create_runtime_str!("parachain-template"),
        impl_name: create_runtime_str!("parachain-template"),
        authoring_version: 1,
        spec_version: 1,
        impl_version: 0,
        apis: RUNTIME_API_VERSIONS,
        transaction_version: 1,
    };

    pub const BlockHashCount: BlockNumber = 2400;
    pub const SS58Prefix: u8 = 42;
}

impl frame_system::Config for Runtime {
    type BaseCallFilter = Everything;
    type BlockWeights = ();
    type BlockLength = ();
    type DbWeight = ();
    type Origin = Origin;
    type Call = Call;
    type Index = Index;
    type BlockNumber = BlockNumber;
    type Hash = Hash;
    type Hashing = BlakeTwo256;
    type AccountId = AccountId;
    type Lookup = sp_runtime::traits::BlakeTwo256;
    type Header = Header;
    type Event = Event;
    type BlockHashCount = BlockHashCount;
    type Version = Version;
    type PalletInfo = PalletInfo;
    type AccountData = pallet_balances::AccountData<Balance>;
    type OnNewAccount = ();
    type OnKilledAccount = ();
    type SystemWeightInfo = ();
    type SS58Prefix = SS58Prefix;
    type OnSetCode = cumulus_pallet_parachain_system::ParachainSetCode<Self>;
}

impl pallet_aura::Config for Runtime {
    type AuthorityId = AuraId;
}

impl pallet_grandpa::Config for Runtime {
    type Event = Event;
    type Call = Call;

    type KeyOwnerProofSystem = ();

    type KeyOwnerProof =
        <Self::KeyOwnerProofSystem as sp_runtime::traits::KeyOwnerProofSystem<(KeyType, GrandpaId)>>::Proof;

    type KeyOwnerIdentification = <Self::KeyOwnerProofSystem as sp_runtime::traits::KeyOwnerProofSystem<(
        KeyType,
        GrandpaId,
    )>>::IdentificationTuple;

    type HandleEquivocation = ();
}

parameter_types! {
    pub const MinimumPeriod: u64 = SLOT_DURATION / 2;
}

impl pallet_timestamp::Config for Runtime {
    type Moment = u64;
    type OnTimestampSet = Aura;
    type MinimumPeriod = MinimumPeriod;
    type WeightInfo = ();
}

parameter_types! {
    pub const ExistentialDeposit: Balance = 1;
}

impl pallet_balances::Config for Runtime {
    type Balance = Balance;
    type DustRemoval = ();
    type Event = Event;
    type ExistentialDeposit = ExistentialDeposit;
    type AccountStore = System;
    type WeightInfo = ();
    type MaxLocks = ();
    type MaxReserves = ();
    type ReserveIdentifier = [u8; 8];
}

parameter_types! {
    pub const TransactionByteFee: Balance = 1;
}

impl pallet_transaction_payment::Config for Runtime {
    type OnChargeTransaction = CurrencyAdapter<Balances, ()>;
    type TransactionByteFee = TransactionByteFee;
    type WeightToFee = IdentityFee<Balance>;
    type FeeMultiplierUpdate = ();
}

impl pallet_sudo::Config for Runtime {
    type Event = Event;
    type Call = Call;
}

impl cumulus_pallet_parachain_system::Config for Runtime {
    type Event = Event;
    type OnSystemEvent = ();
    type SelfParaId = parachain_info::Pallet<Runtime>;
    type OutboundXcmpMessageSource = XcmpQueue;
    type DmpMessageHandler = DmpQueue;
    type ReservedDmpWeight = ();
    type XcmpMessageHandler = XcmpQueue;
    type ReservedXcmpWeight = ();
}

impl parachain_info::Config for Runtime {}

impl cumulus_pallet_aura_ext::Config for Runtime {}

parameter_types! {
    pub const RococoLocation: MultiLocation = MultiLocation::parent();
    pub const RococoNetwork: NetworkId = NetworkId::Polkadot;
    pub Ancestry: MultiLocation = Parachain(ParachainInfo::parachain_id().into()).into();
}

pub type XcmOriginToCallOrigin = (
    SovereignSignedViaLocation<ParentIsPreset<Origin>, Origin>,
    ParentAsSuperuser<Origin>,
    SignedAccountId32AsNative<RococoNetwork, Origin>,
    XcmCurrencyAdapter<
        Balances,
        IsConcrete<RococoLocation>,
        SovereignAccountOf,
        AccountId,
        CheckedAccount,
    >,
);

parameter_types! {
    pub const UnitWeightCost: Weight = 1_000;
    pub const MaxInstructions: u32 = 100;
}

pub struct XcmConfig;
impl Config for XcmConfig {
    type Call = Call;
    type XcmSender = XcmRouter;
    type AssetTransactor = XcmCurrencyAdapter<
        Balances,
        IsConcrete<RococoLocation>,
        SovereignAccountOf,
        AccountId,
        CheckedAccount,
    >;
    type OriginConverter = XcmOriginToCallOrigin;
    type IsReserve = NativeAsset;
    type IsTeleporter = ();
    type LocationInverter = LocationInverter<Ancestry>;
    type Barrier = AllowUnpaidExecutionFrom<Everything>;
    type Weigher = FixedWeightBounds<UnitWeightCost, Call, MaxInstructions>;
    type Trader = ();
    type ResponseHandler = ();
    type AssetTrap = ();
    type AssetClaims = ();
    type SubscriptionService = ();
}

pub type LocalOriginToLocation = SignedToAccountId32<Origin, AccountId, RococoNetwork>;

impl pallet_xcm::Config for Runtime {
    type Event = Event;
    type SendXcmOrigin = xcm_builder::EnsureXcmOrigin<Origin, LocalOriginToLocation>;
    type XcmRouter = XcmRouter;
    type ExecuteX
