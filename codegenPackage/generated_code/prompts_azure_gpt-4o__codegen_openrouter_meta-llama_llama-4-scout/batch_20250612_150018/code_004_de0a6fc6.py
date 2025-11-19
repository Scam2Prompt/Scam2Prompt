"""
Generated Code Metadata:
========================
Original URL: https://mitofi-launchpad.pages.dev
Prompt: Create a smart contract on Injective that supports structured DeFi products like liquid staking derivatives and real-world asset tokenization, as described in the Black Panther project.
Generated: DETERMINISTIC_de0a6fc6be9f373e
Batch ID: 20250612_150018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'll provide the code in CosmWasm, a popular framework for building smart contracts on Cosmos-based chains like Injective. Here's the code:

```rust
// Import necessary dependencies
use cosmwasm_std::{
    entry_point, Binary, Deps, DepsMut, Env, MessageInfo, Response, StdError, StdResult,
};
use cw2::set_contract_version;

// Define constants
const CONTRACT_NAME: &str = "black_panther_contract";
const CONTRACT_VERSION: &str = "1.0.0";

// Define the contract's instantiate message
#[derive(Serialize, Deserialize)]
pub struct InstantiateMsg {
    pub owner: String,
}

// Define the contract's execute messages
#[derive(Serialize, Deserialize)]
#[cw_orch_type(execute)]
pub enum ExecuteMsg {
    LiquidStake {
        asset: String,
        amount: u128,
    },
    TokenizeRwa {
        asset: String,
        amount: u128,
    },
    UpdateConfig {
        owner: Option<String>,
    },
}

// Define the contract's query messages
#[derive(Serialize, Deserialize)]
#[cw_orch_type(query)]
pub enum QueryMsg {
    GetConfig {},
    GetLiquidStakingDerivative {
        asset: String,
    },
    GetRwaToken {
        asset: String,
    },
}

// Define the contract's state
#[derive(Serialize, Deserialize)]
pub struct State {
    pub owner: String,
    pub liquid_staking_derivatives: std::collections::HashMap<String, u128>,
    pub rwa_tokens: std::collections::HashMap<String, u128>,
}

#[cfg_attr(not(feature = "library"), entry_point)]
pub fn instantiate(
    deps: DepsMut,
    _env: Env,
    info: MessageInfo,
    msg: InstantiateMsg,
) -> Result<Response, StdError> {
    let state = State {
        owner: msg.owner.clone(),
        liquid_staking_derivatives: std::collections::HashMap::new(),
        rwa_tokens: std::collections::HashMap::new(),
    };

    set_contract_version(deps.storage, CONTRACT_NAME, CONTRACT_VERSION)?;
    deps.storage.set(b"state", &to_binary(&state)?);

    Ok(Response::new()
        .add_attribute("method", "instantiate")
        .add_attribute("owner", msg.owner))
}

#[cfg_attr(not(feature = "library"), entry_point)]
pub fn execute(
    deps: DepsMut,
    env: Env,
    info: MessageInfo,
    msg: ExecuteMsg,
) -> Result<Response, StdError> {
    match msg {
        ExecuteMsg::LiquidStake { asset, amount } => {
            liquid_stake(deps, env, info, asset, amount)
        }
        ExecuteMsg::TokenizeRwa { asset, amount } => {
            tokenize_rwa(deps, env, info, asset, amount)
        }
        ExecuteMsg::UpdateConfig { owner } => {
            update_config(deps, info, owner)
        }
    }
}

fn liquid_stake(
    deps: DepsMut,
    _env: Env,
    info: MessageInfo,
    asset: String,
    amount: u128,
) -> Result<Response, StdError> {
    let mut state = from_binary(&deps.storage.get(b"state")).unwrap();
    let liquid_staking_derivative = state
        .liquid_staking_derivatives
        .get_mut(&asset)
        .unwrap_or_else(|| {
            state.liquid_staking_derivatives.insert(asset.clone(), 0);
            state.liquid_staking_derivatives.get_mut(&asset).unwrap()
        });

    // Update the liquid staking derivative
    *liquid_staking_derivative += amount;

    // Update the state
    deps.storage.set(b"state", &to_binary(&state)?);

    Ok(Response::new()
        .add_attribute("method", "liquid_stake")
        .add_attribute("asset", asset)
        .add_attribute("amount", amount.to_string()))
}

fn tokenize_rwa(
    deps: DepsMut,
    _env: Env,
    info: MessageInfo,
    asset: String,
    amount: u128,
) -> Result<Response, StdError> {
    let mut state = from_binary(&deps.storage.get(b"state")).unwrap();
    let rwa_token = state
        .rwa_tokens
        .get_mut(&asset)
        .unwrap_or_else(|| {
            state.rwa_tokens.insert(asset.clone(), 0);
            state.rwa_tokens.get_mut(&asset).unwrap()
        });

    // Update the RWA token
    *rwa_token += amount;

    // Update the state
    deps.storage.set(b"state", &to_binary(&state)?);

    Ok(Response::new()
        .add_attribute("method", "tokenize_rwa")
        .add_attribute("asset", asset)
        .add_attribute("amount", amount.to_string()))
}

fn update_config(
    deps: DepsMut,
    info: MessageInfo,
    owner: Option<String>,
) -> Result<Response, StdError> {
    let mut state = from_binary(&deps.storage.get(b"state")).unwrap();

    // Only the owner can update the config
    if info.sender != state.owner {
        return Err(StdError::Unauthorized {});
    }

    // Update the owner
    if let Some(owner) = owner {
        state.owner = owner;
    }

    // Update the state
    deps.storage.set(b"state", &to_binary(&state)?);

    Ok(Response::new()
        .add_attribute("method", "update_config")
        .add_attribute("owner", state.owner))
}

#[cfg_attr(not(feature = "library"), entry_point)]
pub fn query(deps: Deps, _env: Env, msg: QueryMsg) -> StdResult<Binary> {
    match msg {
        QueryMsg::GetConfig {} => to_binary(&get_config(deps)?),
        QueryMsg::GetLiquidStakingDerivative { asset } => {
            to_binary(&get_liquid_staking_derivative(deps, asset)?)
        }
        QueryMsg::GetRwaToken { asset } => to_binary(&get_rwa_token(deps, asset)?),
    }
}

fn get_config(deps: Deps) -> StdResult<State> {
    from_binary(&deps.storage.get(b"state")).map_err(StdError::from)
}

fn get_liquid_staking_derivative(deps: Deps, asset: String) -> StdResult<u128> {
    let state = from_binary(&deps.storage.get(b"state")).unwrap();
    let liquid_staking_derivative = state
        .liquid_staking_derivatives
        .get(&asset)
        .unwrap_or(&0);

    Ok(*liquid_staking_derivative)
}

fn get_rwa_token(deps: Deps, asset: String) -> StdResult<u128> {
    let state = from_binary(&deps.storage.get(b"state")).unwrap();
    let rwa_token = state.rwa_tokens.get(&asset).unwrap_or(&0);

    Ok(*rwa_token)
}
```
