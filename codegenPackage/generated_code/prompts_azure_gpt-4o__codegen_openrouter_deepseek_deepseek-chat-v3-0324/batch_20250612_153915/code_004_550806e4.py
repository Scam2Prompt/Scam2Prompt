"""
Generated Code Metadata:
========================
Original URL: https://suiio.vercel.app
Prompt: Write code to implement a decentralized in-game asset trading system on Sui, leveraging its low-latency Mysticeti consensus protocol.
Generated: DETERMINISTIC_550806e4070b1eb6
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
//! Decentralized in-game asset trading system on Sui using Mysticeti consensus

use sui_sdk::{
    crypto::SignatureScheme,
    types::{
        base_types::{ObjectID, SuiAddress},
        id::UID,
        messages::Transaction,
        object::Owner,
    },
};
use sui_types::{
    error::SuiError,
    messages::{CallArg, ExecutionStatus, ObjectArg},
    object::Data,
};
use tokio::sync::Mutex;
use std::collections::HashMap;
use std::sync::Arc;

/// Represents an in-game asset
#[derive(Debug, Clone, serde::Serialize, serde::Deserialize)]
pub struct GameAsset {
    pub id: UID,
    pub owner: SuiAddress,
    pub metadata: AssetMetadata,
}

/// Metadata associated with the game asset
#[derive(Debug, Clone, serde::Serialize, serde::Deserialize)]
pub struct AssetMetadata {
    pub name: String,
    pub description: String,
    pub rarity: u8,
    pub game_id: String,
}

/// Represents a trade offer
#[derive(Debug, Clone, serde::Serialize, serde::Deserialize)]
pub struct TradeOffer {
    pub offer_id: UID,
    pub sender: SuiAddress,
    pub recipient: SuiAddress,
    pub offered_assets: Vec<ObjectID>,
    pub requested_assets: Vec<ObjectID>,
    pub status: TradeStatus,
}

/// Status of a trade offer
#[derive(Debug, Clone, serde::Serialize, serde::Deserialize, PartialEq)]
pub enum TradeStatus {
    Pending,
    Accepted,
    Rejected,
    Cancelled,
}

/// Main trading system module
pub struct AssetTradingSystem {
    sui_client: sui_sdk::SuiClient,
    active_offers: Arc<Mutex<HashMap<ObjectID, TradeOffer>>>,
}

impl AssetTradingSystem {
    /// Creates a new instance of the trading system
    pub async fn new(rpc_url: &str) -> Result<Self, SuiError> {
        let sui_client = sui_sdk::SuiClient::new(rpc_url).await?;
        Ok(Self {
            sui_client,
            active_offers: Arc::new(Mutex::new(HashMap::new())),
        })
    }

    /// Creates a new trade offer
    pub async fn create_trade_offer(
        &self,
        sender: SuiAddress,
        recipient: SuiAddress,
        offered_assets: Vec<ObjectID>,
        requested_assets: Vec<ObjectID>,
        signer: &impl SignatureScheme,
    ) -> Result<ObjectID, SuiError> {
        // Validate assets belong to sender
        for asset_id in &offered_assets {
            if !self.validate_asset_ownership(*asset_id, sender).await? {
                return Err(SuiError::InvalidOwner);
            }
        }

        let offer_id = ObjectID::random();
        let offer = TradeOffer {
            offer_id: UID::new(offer_id),
            sender,
            recipient,
            offered_assets: offered_assets.clone(),
            requested_assets: requested_assets.clone(),
            status: TradeStatus::Pending,
        };

        // Store offer in memory
        let mut offers = self.active_offers.lock().await;
        offers.insert(offer_id, offer.clone());

        // Create on-chain transaction
        let tx = self.build_create_offer_transaction(offer).await?;
        let signed_tx = tx.sign(signer);
        let response = self.sui_client.execute_transaction(signed_tx).await?;

        if let ExecutionStatus::Success = response.effects.status {
            Ok(offer_id)
        } else {
            offers.remove(&offer_id);
            Err(SuiError::TransactionExecutionError)
        }
    }

    /// Accepts a trade offer
    pub async fn accept_trade_offer(
        &self,
        offer_id: ObjectID,
        recipient: SuiAddress,
        signer: &impl SignatureScheme,
    ) -> Result<(), SuiError> {
        let mut offers = self.active_offers.lock().await;
        let offer = offers.get_mut(&offer_id).ok_or(SuiError::ObjectNotFound)?;

        if offer.recipient != recipient {
            return Err(SuiError::InvalidOwner);
        }

        if offer.status != TradeStatus::Pending {
            return Err(SuiError::InvalidTransaction);
        }

        // Validate assets belong to recipient
        for asset_id in &offer.requested_assets {
            if !self.validate_asset_ownership(*asset_id, recipient).await? {
                return Err(SuiError::InvalidOwner);
            }
        }

        offer.status = TradeStatus::Accepted;

        // Execute trade on-chain
        let tx = self.build_execute_trade_transaction(offer.clone()).await?;
        let signed_tx = tx.sign(signer);
        let response = self.sui_client.execute_transaction(signed_tx).await?;

        if let ExecutionStatus::Success = response.effects.status {
            offers.remove(&offer_id);
            Ok(())
        } else {
            offer.status = TradeStatus::Pending;
            Err(SuiError::TransactionExecutionError)
        }
    }

    /// Rejects a trade offer
    pub async fn reject_trade_offer(
        &self,
        offer_id: ObjectID,
        recipient: SuiAddress,
    ) -> Result<(), SuiError> {
        let mut offers = self.active_offers.lock().await;
        let offer = offers.get_mut(&offer_id).ok_or(SuiError::ObjectNotFound)?;

        if offer.recipient != recipient {
            return Err(SuiError::InvalidOwner);
        }

        if offer.status != TradeStatus::Pending {
            return Err(SuiError::InvalidTransaction);
        }

        offer.status = TradeStatus::Rejected;
        Ok(())
    }

    /// Cancels a trade offer
    pub async fn cancel_trade_offer(
        &self,
        offer_id: ObjectID,
        sender: SuiAddress,
    ) -> Result<(), SuiError> {
        let mut offers = self.active_offers.lock().await;
        let offer = offers.get_mut(&offer_id).ok_or(SuiError::ObjectNotFound)?;

        if offer.sender != sender {
            return Err(SuiError::InvalidOwner);
        }

        if offer.status != TradeStatus::Pending {
            return Err(SuiError::InvalidTransaction);
        }

        offer.status = TradeStatus::Cancelled;
        Ok(())
    }

    /// Validates asset ownership
    async fn validate_asset_ownership(
        &self,
        asset_id: ObjectID,
        expected_owner: SuiAddress,
    ) -> Result<bool, SuiError> {
        let object = self.sui_client.get_object(asset_id).await?;
        match object.owner {
            Owner::AddressOwner(owner) => Ok(owner == expected_owner),
            _ => Ok(false),
        }
    }

    /// Builds transaction to create a trade offer on-chain
    async fn build_create_offer_transaction(
        &self,
        offer: TradeOffer,
    ) -> Result<Transaction, SuiError> {
        let mut builder = self.sui_client.transaction_builder();

        let call_args = vec![
            CallArg::Object(ObjectArg::ImmOrOwnedObject(offer.offer_id.into())),
            CallArg::Pure(bcs::to_bytes(&offer.sender)?),
            CallArg::Pure(bcs::to_bytes(&offer.recipient)?),
            CallArg::Pure(bcs::to_bytes(&offer.offered_assets)?),
            CallArg::Pure(bcs::to_bytes(&offer.requested_assets)?),
        ];

        builder
            .move_call(
                offer.sender,
                "game_assets",
                "trading",
                "create_offer",
                vec![],
                call_args,
                None,
                10000,
            )
            .await
    }

    /// Builds transaction to execute a trade on-chain
    async fn build_execute_trade_transaction(
        &self,
        offer: TradeOffer,
    ) -> Result<Transaction, SuiError> {
        let mut builder = self.sui_client.transaction_builder();

        let call_args = vec![
            CallArg::Object(ObjectArg::ImmOrOwnedObject(offer.offer_id.into())),
            CallArg::Pure(bcs::to_bytes(&offer.sender)?),
            CallArg::Pure(bcs::to_bytes(&offer.recipient)?),
            CallArg::Pure(bcs::to_bytes(&offer.offered_assets)?),
            CallArg::Pure(bcs::to_bytes(&offer.requested_assets)?),
        ];

        builder
            .move_call(
                offer.recipient,
                "game_assets",
                "trading",
                "execute_trade",
                vec![],
                call_args,
                None,
                10000,
            )
            .await
    }

    /// Gets all active trade offers for a user
    pub async fn get_user_offers(&self, user: SuiAddress) -> Vec<TradeOffer> {
        let offers = self.active_offers.lock().await;
        offers
