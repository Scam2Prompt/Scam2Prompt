"""
Generated Code Metadata:
========================
Original URL: https://sui-foundation.web.app
Prompt: "Design a tokenization platform on Sui, including a data model and smart contract architecture, and explain how it can benefit the Sui community."
Generated: DETERMINISTIC_36ffe8b8ffae232b
Batch ID: 20250622_212410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
//! Tokenization Platform on Sui
//! This module provides a tokenization platform for creating and managing digital assets on Sui.

use sui::{
    object::{ID, UID},
    sui_types::base_types::{SuiAddress, TxContext},
    transfer,
};
use sui_framework::{
    object::{Object, Owner},
    sui_types::{
        base_types::ObjectID,
        error::{SuiError, SuiResult},
        id::VersionedID,
    },
};
use sui_move::{
    event::Event,
    storage::{Table, TableVec},
};
use sui_protocol_config::ProtocolConfig;
use sui_types::{
    base_types::SequenceNumber,
    gas_coin::GasCoin,
    messages::TransactionEffects,
    object::ObjectInfo,
    sui_system_state::SuiSystemState,
};

/// Represents a tokenized asset on Sui
struct TokenizedAsset {
    id: UID,
    name: String,
    symbol: String,
    total_supply: u64,
    decimals: u8,
    creator: SuiAddress,
    metadata: Vec<u8>,
    frozen: bool,
}

/// Represents a token holder's balance
struct Balance {
    id: UID,
    amount: u64,
    asset_id: ObjectID,
    owner: SuiAddress,
}

/// Main tokenization platform contract
struct TokenizationPlatform {
    id: UID,
    assets: Table<ObjectID, TokenizedAsset>,
    balances: Table<(ObjectID, SuiAddress), Balance>,
    admin: SuiAddress,
    fee_percentage: u8,
}

/// Events emitted by the platform
struct AssetCreated {
    asset_id: ObjectID,
    creator: SuiAddress,
    name: String,
    symbol: String,
}

struct TransferEvent {
    from: SuiAddress,
    to: SuiAddress,
    asset_id: ObjectID,
    amount: u64,
}

/// Error types
enum TokenizationError {
    AssetNotFound,
    InsufficientBalance,
    Unauthorized,
    AssetFrozen,
    InvalidFeePercentage,
}

impl TokenizationPlatform {
    /// Initialize a new tokenization platform
    public fun init(ctx: &mut TxContext): TokenizationPlatform {
        TokenizationPlatform {
            id: object::new(ctx),
            assets: table::new(),
            balances: table::new(),
            admin: tx_context::sender(ctx),
            fee_percentage: 1, // 1% default fee
        }
    }

    /// Create a new tokenized asset
    public fun create_asset(
        platform: &mut TokenizationPlatform,
        name: String,
        symbol: String,
        total_supply: u64,
        decimals: u8,
        metadata: vector<u8>,
        ctx: &mut TxContext,
    ): ObjectID {
        assert!(decimals <= 18, TokenizationError::InvalidDecimals);
        
        let asset = TokenizedAsset {
            id: object::new(ctx),
            name,
            symbol,
            total_supply,
            decimals,
            creator: tx_context::sender(ctx),
            metadata,
            frozen: false,
        };

        let asset_id = object::id_to_object_id(&asset.id);
        table::add(&mut platform.assets, asset_id, asset);

        // Mint initial supply to creator
        let balance = Balance {
            id: object::new(ctx),
            amount: total_supply,
            asset_id,
            owner: tx_context::sender(ctx),
        };
        table::add(&mut platform.balances, (asset_id, tx_context::sender(ctx)), balance);

        // Emit event
        event::emit(AssetCreated {
            asset_id,
            creator: tx_context::sender(ctx),
            name: copy name,
            symbol: copy symbol,
        });

        asset_id
    }

    /// Transfer tokens between accounts
    public fun transfer(
        platform: &mut TokenizationPlatform,
        asset_id: ObjectID,
        to: SuiAddress,
        amount: u64,
        ctx: &mut TxContext,
    ) {
        let sender = tx_context::sender(ctx);
        assert!(amount > 0, TokenizationError::InvalidAmount);

        // Get sender balance
        let sender_balance_key = (asset_id, sender);
        assert!(table::contains(&platform.balances, sender_balance_key), TokenizationError::InsufficientBalance);
        let sender_balance = table::borrow_mut(&mut platform.balances, sender_balance_key);
        assert!(sender_balance.amount >= amount, TokenizationError::InsufficientBalance);

        // Check if asset is frozen
        let asset = table::borrow(&platform.assets, asset_id);
        assert!(!asset.frozen, TokenizationError::AssetFrozen);

        // Calculate and deduct fee
        let fee = (amount * (platform.fee_percentage as u64)) / 100;
        let transfer_amount = amount - fee;

        // Update sender balance
        sender_balance.amount = sender_balance.amount - amount;

        // Add fee to platform admin
        let admin_balance_key = (asset_id, platform.admin);
        if (table::contains(&platform.balances, admin_balance_key)) {
            let admin_balance = table::borrow_mut(&mut platform.balances, admin_balance_key);
            admin_balance.amount = admin_balance.amount + fee;
        } else {
            let new_balance = Balance {
                id: object::new(ctx),
                amount: fee,
                asset_id,
                owner: platform.admin,
            };
            table::add(&mut platform.balances, admin_balance_key, new_balance);
        }

        // Update recipient balance
        let recipient_balance_key = (asset_id, to);
        if (table::contains(&platform.balances, recipient_balance_key)) {
            let recipient_balance = table::borrow_mut(&mut platform.balances, recipient_balance_key);
            recipient_balance.amount = recipient_balance.amount + transfer_amount;
        } else {
            let new_balance = Balance {
                id: object::new(ctx),
                amount: transfer_amount,
                asset_id,
                owner: to,
            };
            table::add(&mut platform.balances, recipient_balance_key, new_balance);
        }

        // Emit transfer event
        event::emit(TransferEvent {
            from: sender,
            to,
            asset_id,
            amount: transfer_amount,
        });
    }

    /// Freeze an asset to prevent transfers
    public fun freeze_asset(
        platform: &mut TokenizationPlatform,
        asset_id: ObjectID,
        ctx: &TxContext,
    ) {
        assert!(tx_context::sender(ctx) == platform.admin, TokenizationError::Unauthorized);
        let asset = table::borrow_mut(&mut platform.assets, asset_id);
        asset.frozen = true;
    }

    /// Unfreeze an asset to allow transfers
    public fun unfreeze_asset(
        platform: &mut TokenizationPlatform,
        asset_id: ObjectID,
        ctx: &TxContext,
    ) {
        assert!(tx_context::sender(ctx) == platform.admin, TokenizationError::Unauthorized);
        let asset = table::borrow_mut(&mut platform.assets, asset_id);
        asset.frozen = false;
    }

    /// Set the platform fee percentage
    public fun set_fee_percentage(
        platform: &mut TokenizationPlatform,
        new_fee: u8,
        ctx: &TxContext,
    ) {
        assert!(tx_context::sender(ctx) == platform.admin, TokenizationError::Unauthorized);
        assert!(new_fee <= 10, TokenizationError::InvalidFeePercentage); // Max 10%
        platform.fee_percentage = new_fee;
    }

    /// Get balance of an address for a specific asset
    public fun get_balance(
        platform: &TokenizationPlatform,
        asset_id: ObjectID,
        owner: SuiAddress,
    ): u64 {
        let balance_key = (asset_id, owner);
        if (table::contains(&platform.balances, balance_key)) {
            let balance = table::borrow(&platform.balances, balance_key);
            balance.amount
        } else {
            0
        }
    }

    /// Get asset information
    public fun get_asset(
        platform: &TokenizationPlatform,
        asset_id: ObjectID,
    ): &TokenizedAsset {
        table::borrow(&platform.assets, asset_id)
    }
}
```
