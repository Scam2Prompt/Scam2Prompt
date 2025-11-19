"""
Generated Code Metadata:
========================
Original URL: https://wallet-lto-network.pages.dev
Prompt: Create an example of a smart contract using CosmWasm widgets on the LTO Network for dynamic digital collectibles.
Generated: DETERMINISTIC_fb94d60a2a571735
Batch ID: 20250612_161130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import necessary CosmWasm libraries
use cosmwasm_std::{entry_point, to_binary, Binary, Deps, DepsMut, Env, MessageInfo, Response, StdResult};
use cw_storage_plus::Map;
use serde::{Deserialize, Serialize};

// Define the structure for a collectible
#[derive(Serialize, Deserialize, Clone, Debug, PartialEq)]
pub struct Collectible {
    pub id: String,
    pub owner: String,
    pub metadata: String,
}

// Define the state storage for collectibles
const COLLECTIBLES: Map<&str, Collectible> = Map::new("collectibles");

// Define the instantiate message
#[derive(Serialize, Deserialize, Clone, Debug, PartialEq)]
pub struct InstantiateMsg {
    pub owner: String,
}

// Define the execute messages
#[derive(Serialize, Deserialize, Clone, Debug, PartialEq)]
pub enum ExecuteMsg {
    CreateCollectible { id: String, metadata: String },
    TransferCollectible { id: String, new_owner: String },
}

// Define the query messages
#[derive(Serialize, Deserialize, Clone, Debug, PartialEq)]
pub enum QueryMsg {
    GetCollectible { id: String },
}

// Entry point for contract instantiation
#[entry_point]
pub fn instantiate(
    deps: DepsMut,
    _env: Env,
    info: MessageInfo,
    msg: InstantiateMsg,
) -> StdResult<Response> {
    // Ensure the owner is set correctly
    if msg.owner.is_empty() {
        return Err(cosmwasm_std::StdError::generic_err("Owner cannot be empty"));
    }

    // Store the owner in the contract state
    COLLECTIBLES.save(deps.storage, &msg.owner, &Collectible {
        id: msg.owner.clone(),
        owner: msg.owner.clone(),
        metadata: String::new(),
    })?;

    Ok(Response::default())
}

// Entry point for executing messages
#[entry_point]
pub fn execute(
    deps: DepsMut,
    env: Env,
    info: MessageInfo,
    msg: ExecuteMsg,
) -> StdResult<Response> {
    match msg {
        ExecuteMsg::CreateCollectible { id, metadata } => create_collectible(deps, info, id, metadata),
        ExecuteMsg::TransferCollectible { id, new_owner } => transfer_collectible(deps, info, id, new_owner),
    }
}

// Function to create a new collectible
fn create_collectible(
    deps: DepsMut,
    info: MessageInfo,
    id: String,
    metadata: String,
) -> StdResult<Response> {
    // Check if the collectible already exists
    if COLLECTIBLES.has(deps.storage, &id) {
        return Err(cosmwasm_std::StdError::generic_err("Collectible already exists"));
    }

    // Create and store the new collectible
    let collectible = Collectible {
        id: id.clone(),
        owner: info.sender.to_string(),
        metadata,
    };
    COLLECTIBLES.save(deps.storage, &id, &collectible)?;

    Ok(Response::new().add_attribute("action", "create_collectible").add_attribute("id", id))
}

// Function to transfer ownership of a collectible
fn transfer_collectible(
    deps: DepsMut,
    info: MessageInfo,
    id: String,
    new_owner: String,
) -> StdResult<Response> {
    // Load the collectible
    let mut collectible = COLLECTIBLES.load(deps.storage, &id)?;

    // Ensure the sender is the current owner
    if collectible.owner != info.sender.to_string() {
        return Err(cosmwasm_std::StdError::generic_err("Unauthorized: not the owner"));
    }

    // Update the owner and save the collectible
    collectible.owner = new_owner.clone();
    COLLECTIBLES.save(deps.storage, &id, &collectible)?;

    Ok(Response::new().add_attribute("action", "transfer_collectible").add_attribute("id", id).add_attribute("new_owner", new_owner))
}

// Entry point for querying messages
#[entry_point]
pub fn query(deps: Deps, _env: Env, msg: QueryMsg) -> StdResult<Binary> {
    match msg {
        QueryMsg::GetCollectible { id } => to_binary(&query_collectible(deps, id)?),
    }
}

// Function to query a collectible by ID
fn query_collectible(deps: Deps, id: String) -> StdResult<Collectible> {
    COLLECTIBLES.load(deps.storage, &id)
}
```
