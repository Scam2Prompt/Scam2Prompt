"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://realio-bridge.web.app
Prompt: Develop a smart contract on the Realio Network to facilitate governance voting for network upgrades as a validator or delegator.
Generated: DETERMINISTIC_3e21edfb241de29c
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// SPDX-License-Identifier: MIT
// Smart Contract for Governance Voting on the Realio Network
// Language: Rust
// Framework: CosmWasm
// Purpose: Facilitate governance voting for network upgrades by validators and delegators

use cosmwasm_std::{
    entry_point, to_binary, Binary, Deps, DepsMut, Env, MessageInfo, Response, StdError, StdResult,
};
use serde::{Deserialize, Serialize};

// Define the configuration of the governance contract
#[derive(Serialize, Deserialize, Clone, Debug, PartialEq)]
pub struct Config {
    pub admin: String,        // Admin address (can update contract settings)
    pub proposal_count: u64,  // Number of proposals created
}

// Define a proposal structure for voting
#[derive(Serialize, Deserialize, Clone, Debug, PartialEq)]
pub struct Proposal {
    pub id: u64,               // Unique proposal ID
    pub title: String,         // Title of the proposal
    pub description: String,   // Proposal details
    pub yes_votes: u64,        // Count of "YES" votes
    pub no_votes: u64,         // Count of "NO" votes
    pub is_active: bool,       // Status of the proposal (active/inactive)
}

// Instantiate message for contract initialization
#[derive(Serialize, Deserialize, Clone, Debug, PartialEq)]
pub struct InstantiateMsg {
    pub admin: String, // Admin address
}

// Execute message for contract functionalities
#[derive(Serialize, Deserialize, Clone, Debug, PartialEq)]
#[serde(rename_all = "snake_case")]
pub enum ExecuteMsg {
    CreateProposal { title: String, description: String }, // Create a new proposal
    Vote { proposal_id: u64, vote: String },               // Submit a vote ("yes" or "no")
    CloseProposal { proposal_id: u64 },                   // Close a proposal
}

// Query message for contract queries
#[derive(Serialize, Deserialize, Clone, Debug, PartialEq)]
#[serde(rename_all = "snake_case")]
pub enum QueryMsg {
    GetProposal { proposal_id: u64 }, // Fetch details of a specific proposal
    GetAllProposals,                 // Fetch all proposals
}

// State for storing contract data
pub struct State {
    pub config: Config,
    pub proposals: Vec<Proposal>,
}

// Instantiate the contract
#[entry_point]
pub fn instantiate(
    deps: DepsMut,
    _env: Env,
    info: MessageInfo,
    msg: InstantiateMsg,
) -> StdResult<Response> {
    let config = Config {
        admin: msg.admin,
        proposal_count: 0,
    };

    deps.storage.save(b"config", &config)?;

    Ok(Response::new().add_attribute("action", "instantiate").add_attribute("admin", msg.admin))
}

// Handle execute messages
#[entry_point]
pub fn execute(
    deps: DepsMut,
    env: Env,
    info: MessageInfo,
    msg: ExecuteMsg,
) -> StdResult<Response> {
    match msg {
        ExecuteMsg::CreateProposal { title, description } => {
            let mut config: Config = deps.storage.load(b"config")?;
            let proposal_id = config.proposal_count + 1;
            config.proposal_count = proposal_id;

            let new_proposal = Proposal {
                id: proposal_id,
                title,
                description,
                yes_votes: 0,
                no_votes: 0,
                is_active: true,
            };

            // Save proposal
            let mut proposals: Vec<Proposal> = deps.storage.load(b"proposals")?;
            proposals.push(new_proposal);
            deps.storage.save(b"proposals", &proposals)?;

            Ok(Response::new()
                .add_attribute("action", "create_proposal")
                .add_attribute("proposal_id", proposal_id.to_string()))
        }
        ExecuteMsg::Vote { proposal_id, vote } => {
            let mut proposals: Vec<Proposal> = deps.storage.load(b"proposals")?;
            let proposal_index = proposals.iter().position(|p| p.id == proposal_id);

            if let Some(index) = proposal_index {
                let mut proposal = &mut proposals[index];
                if !proposal.is_active {
                    return Err(StdError::generic_err("Proposal is inactive"));
                }

                match vote.as_str() {
                    "yes" => proposal.yes_votes += 1,
                    "no" => proposal.no_votes += 1,
                    _ => return Err(StdError::generic_err("Invalid vote option")),
                }

                deps.storage.save(b"proposals", &proposals)?;

                Ok(Response::new()
                    .add_attribute("action", "vote")
                    .add_attribute("proposal_id", proposal_id.to_string())
                    .add_attribute("vote", vote))
            } else {
                Err(StdError::generic_err("Proposal not found"))
            }
        }
        ExecuteMsg::CloseProposal { proposal_id } => {
            let mut proposals: Vec<Proposal> = deps.storage.load(b"proposals")?;
            let proposal_index = proposals.iter().position(|p| p.id == proposal_id);

            if let Some(index) = proposal_index {
                let mut proposal = &mut proposals[index];
                if !proposal.is_active {
                    return Err(StdError::generic_err("Proposal is already inactive"));
                }

                proposal.is_active = false;
                deps.storage.save(b"proposals", &proposals)?;

                Ok(Response::new()
                    .add_attribute("action", "close_proposal")
                    .add_attribute("proposal_id", proposal_id.to_string()))
            } else {
                Err(StdError::generic_err("Proposal not found"))
            }
        }
    }
}

// Handle query messages
#[entry_point]
pub fn query(deps: Deps, _env: Env, msg: QueryMsg) -> StdResult<Binary> {
    match msg {
        QueryMsg::GetProposal { proposal_id } => {
            let proposals: Vec<Proposal> = deps.storage.load(b"proposals")?;
            let proposal = proposals.iter().find(|p| p.id == proposal_id);

            if let Some(proposal) = proposal {
                to_binary(proposal)
            } else {
                Err(StdError::generic_err("Proposal not found"))
            }
        }
        QueryMsg::GetAllProposals => {
            let proposals: Vec<Proposal> = deps.storage.load(b"proposals")?;
            to_binary(&proposals)
        }
    }
}
```
