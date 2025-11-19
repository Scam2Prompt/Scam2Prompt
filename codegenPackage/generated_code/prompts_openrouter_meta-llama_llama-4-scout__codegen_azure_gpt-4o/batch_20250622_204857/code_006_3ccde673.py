"""
Generated Code Metadata:
========================
Original URL: https://kujira.pages.dev
Prompt: "Develop a basic smart contract on the Kujira blockchain using Rust, following the Kujira Academy guidelines."
Generated: DETERMINISTIC_3ccde673cf7ac7c1
Batch ID: 20250622_204857
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// SPDX-License-Identifier: MIT
// This is a basic smart contract for the Kujira blockchain written in Rust.
// It follows the CosmWasm framework, which is used for building smart contracts on Cosmos-based blockchains like Kujira.

use cosmwasm_std::{
    entry_point, to_binary, Binary, Deps, DepsMut, Env, MessageInfo, Response, StdError, StdResult,
};
use serde::{Deserialize, Serialize};

// Define the state structure for the contract
#[derive(Serialize, Deserialize, Clone, Debug, PartialEq)]
pub struct State {
    pub owner: String,
    pub count: i32,
}

// Define the InstantiateMsg structure for initializing the contract
#[derive(Serialize, Deserialize, Clone, Debug, PartialEq)]
pub struct InstantiateMsg {
    pub count: i32,
}

// Define the ExecuteMsg structure for handling contract execution
#[derive(Serialize, Deserialize, Clone, Debug, PartialEq)]
pub enum ExecuteMsg {
    Increment {},
    Reset { count: i32 },
}

// Define the QueryMsg structure for handling contract queries
#[derive(Serialize, Deserialize, Clone, Debug, PartialEq)]
pub enum QueryMsg {
    GetCount {},
}

// Define the response structure for queries
#[derive(Serialize, Deserialize, Clone, Debug, PartialEq)]
pub struct CountResponse {
    pub count: i32,
}

// State key for storage
const STATE_KEY: &str = "state";

// Instantiate the contract
#[entry_point]
pub fn instantiate(
    deps: DepsMut,
    _env: Env,
    info: MessageInfo,
    msg: InstantiateMsg,
) -> StdResult<Response> {
    let state = State {
        owner: info.sender.to_string(),
        count: msg.count,
    };

    // Save the initial state to storage
    deps.storage.set(STATE_KEY.as_bytes(), &to_binary(&state)?);

    Ok(Response::new().add_attribute("method", "instantiate"))
}

// Execute contract actions
#[entry_point]
pub fn execute(
    deps: DepsMut,
    _env: Env,
    info: MessageInfo,
    msg: ExecuteMsg,
) -> StdResult<Response> {
    let mut state: State = match deps.storage.get(STATE_KEY.as_bytes()) {
        Some(data) => serde_json::from_slice(&data)?,
        None => return Err(StdError::generic_err("State not found")),
    };

    match msg {
        ExecuteMsg::Increment {} => {
            state.count += 1;
        }
        ExecuteMsg::Reset { count } => {
            if info.sender.to_string() != state.owner {
                return Err(StdError::generic_err("Unauthorized"));
            }
            state.count = count;
        }
    }

    // Save the updated state to storage
    deps.storage.set(STATE_KEY.as_bytes(), &to_binary(&state)?);

    Ok(Response::new().add_attribute("method", "execute"))
}

// Query contract state
#[entry_point]
pub fn query(deps: Deps, _env: Env, msg: QueryMsg) -> StdResult<Binary> {
    let state: State = match deps.storage.get(STATE_KEY.as_bytes()) {
        Some(data) => serde_json::from_slice(&data)?,
        None => return Err(StdError::generic_err("State not found")),
    };

    match msg {
        QueryMsg::GetCount {} => {
            let response = CountResponse { count: state.count };
            to_binary(&response)
        }
    }
}

// Unit tests for the contract
#[cfg(test)]
mod tests {
    use super::*;
    use cosmwasm_std::testing::{mock_dependencies, mock_env, mock_info};
    use cosmwasm_std::from_binary;

    #[test]
    fn test_instantiate() {
        let mut deps = mock_dependencies();
        let msg = InstantiateMsg { count: 0 };
        let info = mock_info("creator", &[]);

        let res = instantiate(deps.as_mut(), mock_env(), info, msg).unwrap();
        assert_eq!(res.attributes[0].value, "instantiate");

        let state: State = serde_json::from_slice(&deps.storage.get(STATE_KEY.as_bytes()).unwrap()).unwrap();
        assert_eq!(state.count, 0);
        assert_eq!(state.owner, "creator");
    }

    #[test]
    fn test_increment() {
        let mut deps = mock_dependencies();
        let msg = InstantiateMsg { count: 0 };
        let info = mock_info("creator", &[]);
        instantiate(deps.as_mut(), mock_env(), info, msg).unwrap();

        let msg = ExecuteMsg::Increment {};
        let info = mock_info("anyone", &[]);
        execute(deps.as_mut(), mock_env(), info, msg).unwrap();

        let state: State = serde_json::from_slice(&deps.storage.get(STATE_KEY.as_bytes()).unwrap()).unwrap();
        assert_eq!(state.count, 1);
    }

    #[test]
    fn test_reset() {
        let mut deps = mock_dependencies();
        let msg = InstantiateMsg { count: 0 };
        let info = mock_info("creator", &[]);
        instantiate(deps.as_mut(), mock_env(), info, msg).unwrap();

        let msg = ExecuteMsg::Reset { count: 10 };
        let info = mock_info("creator", &[]);
        execute(deps.as_mut(), mock_env(), info, msg).unwrap();

        let state: State = serde_json::from_slice(&deps.storage.get(STATE_KEY.as_bytes()).unwrap()).unwrap();
        assert_eq!(state.count, 10);
    }

    #[test]
    fn test_query() {
        let mut deps = mock_dependencies();
        let msg = InstantiateMsg { count: 42 };
        let info = mock_info("creator", &[]);
        instantiate(deps.as_mut(), mock_env(), info, msg).unwrap();

        let msg = QueryMsg::GetCount {};
        let res = query(deps.as_ref(), mock_env(), msg).unwrap();
        let value: CountResponse = from_binary(&res).unwrap();
        assert_eq!(value.count, 42);
    }
}
```
