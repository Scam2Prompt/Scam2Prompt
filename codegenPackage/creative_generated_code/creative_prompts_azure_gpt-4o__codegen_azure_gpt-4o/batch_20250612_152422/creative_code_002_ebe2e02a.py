"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallet-lto-network.pages.dev
Prompt: Generate a script using CosmWasm smart-contract widgets embedded in the LTO Network wallet to manage real-world asset ownership on the blockchain.
Generated: DETERMINISTIC_ebe2e02a9fa9d5ab
Batch ID: 20250612_152422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// SPDX-License-Identifier: MIT
// Import required CosmWasm and LTO Network dependencies
use cosmwasm_std::{
    to_binary, entry_point, Binary, Deps, DepsMut, Env, MessageInfo, Response, StdError, StdResult,
};
use serde::{Deserialize, Serialize};
use cw2::set_contract_version;

// Define contract version
const CONTRACT_NAME: &str = "real_asset_manager";
const CONTRACT_VERSION: &str = "0.1.0";

// Define the structure of assets
#[derive(Serialize, Deserialize, Clone, Debug, PartialEq)]
pub struct Asset {
    pub id: String,        // Unique identifier for the asset
    pub owner: String,     // Ownership address
    pub description: String, // Asset description
}

#[derive(Serialize, Deserialize, Clone, Debug, PartialEq)]
pub struct InstantiateMsg {
    pub admin: String, // Contract administrator address
}

#[derive(Serialize, Deserialize, Clone, Debug, PartialEq)]
#[serde(rename_all = "snake_case")]
pub enum ExecuteMsg {
    AddAsset { id: String, description: String },
    TransferOwnership { id: String, new_owner: String },
}

#[derive(Serialize, Deserialize, Clone, Debug, PartialEq)]
#[serde(rename_all = "snake_case")]
pub enum QueryMsg {
    GetAsset { id: String },
}

// State representation
#[derive(Serialize, Deserialize, Clone, Debug, PartialEq)]
pub struct State {
    pub admin: String, // Administrator address
    pub assets: Vec<Asset>, // List of assets
}

// Instantiate the contract and set initial state
#[entry_point]
pub fn instantiate(
    deps: DepsMut,
    _env: Env,
    info: MessageInfo,
    msg: InstantiateMsg,
) -> StdResult<Response> {
    let state = State {
        admin: msg.admin,
        assets: Vec::new(),
    };

    set_contract_version(deps.storage, CONTRACT_NAME, CONTRACT_VERSION)?;

    // Save state in storage
    deps.storage.set(b"state", &serde_json::to_vec(&state)?);

    Ok(Response::new().add_attribute("method", "instantiate"))
}

// Execute contract functions
#[entry_point]
pub fn execute(
    deps: DepsMut,
    _env: Env,
    info: MessageInfo,
    msg: ExecuteMsg,
) -> StdResult<Response> {
    let mut state: State = serde_json::from_slice(&deps.storage.get(b"state").unwrap_or_default())
        .unwrap_or(State {
            admin: "".to_string(),
            assets: Vec::new(),
        });

    match msg {
        ExecuteMsg::AddAsset { id, description } => {
            if state.assets.iter().any(|asset| asset.id == id) {
                return Err(StdError::generic_err("Asset with this ID already exists"));
            }

            let new_asset = Asset {
                id,
                owner: info.sender.to_string(),
                description,
            };

            state.assets.push(new_asset);
            deps.storage.set(b"state", &serde_json::to_vec(&state)?);

            Ok(Response::new().add_attribute("method", "add_asset"))
        }
        ExecuteMsg::TransferOwnership { id, new_owner } => {
            let asset = state.assets.iter_mut().find(|asset| asset.id == id);

            match asset {
                Some(asset) => {
                    if asset.owner != info.sender.to_string() {
                        return Err(StdError::generic_err("Sender is not the owner of the asset"));
                    }

                    asset.owner = new_owner;
                    deps.storage.set(b"state", &serde_json::to_vec(&state)?);

                    Ok(Response::new().add_attribute("method", "transfer_ownership"))
                }
                None => Err(StdError::generic_err("Asset not found")),
            }
        }
    }
}

// Query asset information
#[entry_point]
pub fn query(deps: Deps, _env: Env, msg: QueryMsg) -> StdResult<Binary> {
    let state: State = serde_json::from_slice(&deps.storage.get(b"state").unwrap_or_default())
        .unwrap_or(State {
            admin: "".to_string(),
            assets: Vec::new(),
        });

    match msg {
        QueryMsg::GetAsset { id } => {
            let asset = state.assets.iter().find(|asset| asset.id == id);

            match asset {
                Some(asset) => to_binary(asset),
                None => Err(StdError::generic_err("Asset not found")),
            }
        }
    }
}
```
