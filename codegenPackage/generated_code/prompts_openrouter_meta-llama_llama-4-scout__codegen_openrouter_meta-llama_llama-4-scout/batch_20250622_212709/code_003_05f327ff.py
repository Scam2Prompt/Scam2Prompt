"""
Generated Code Metadata:
========================
Original URL: https://sui.direct
Prompt: Generate an example of how to store code on-chain using sui.direct and the SUI blockchain.
Generated: DETERMINISTIC_05f327ffa890ba4c
Batch ID: 20250622_212709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import necessary dependencies
use sui::client::Client;
use sui::client::Error;
use sui::types::SuiAddress;
use sui::types::ObjectID;
use sui::types::ObjectRef;
use sui::types::TransactionEffects;
use sui_types::base64;
use sui_types::gas::GasCoin;
use sui_types::messages::ExecuteTransactionRequest;
use sui_types::messages::TransactionData;
use sui_types::object::Owner;
use std::env;

// Define a struct to hold the on-chain code
#[derive(Debug, Serialize, Deserialize)]
struct OnChainCode {
    code: String,
}

// Define a function to store code on-chain
async fn store_code_on_chain(
    client: &Client,
    sender: SuiAddress,
    code: String,
) -> Result<ObjectID, Error> {
    // Create a new object to store the code
    let gas_coin = GasCoin::default();
    let create_obj = client
        .transaction_builder()
        .create_object(
            sender,
            OnChainCode { code },
            gas_coin.object_ref(),
            1000000, // gas budget
        )
        .await?;

    // Execute the transaction
    let tx_response = client
        .execute_transaction(
            ExecuteTransactionRequest {
                transaction: create_obj,
                request_type: sui_types::messages::ExecuteTransactionRequestType::WaitForLocalExecution,
            },
        )
        .await?;

    // Get the object ID of the created object
    let obj_id = match tx_response.effects.status {
        sui_types::effects::TransactionStatus::Created(c) => c[0].0,
        _ => panic!("Failed to create object"),
    };

    Ok(obj_id)
}

// Define a function to get code from on-chain
async fn get_code_from_chain(
    client: &Client,
    obj_id: ObjectID,
) -> Result<String, Error> {
    // Get the object from the chain
    let obj = client.get_object(obj_id).await?;

    // Deserialize the object into OnChainCode
    let on_chain_code = bcs::from_bytes(obj.data.contents.as_slice())?;

    Ok(on_chain_code.code)
}

#[tokio::main]
async fn main() {
    // Initialize the SUI client
    let url = env::var("SUI_URL").expect("SUI_URL must be set");
    let client = Client::new(&url).await.expect("Failed to create client");

    // Define the sender's address
    let sender = SuiAddress::from_str("0x...").expect("Invalid SUI address");

    // Define the code to store on-chain
    let code = "example code".to_string();

    // Store the code on-chain
    let obj_id = store_code_on_chain(&client, sender, code)
        .await
        .expect("Failed to store code on-chain");

    println!("Stored code on-chain with object ID: {}", obj_id);

    // Get the code from on-chain
    let stored_code = get_code_from_chain(&client, obj_id)
        .await
        .expect("Failed to get code from on-chain");

    println!("Retrieved code from on-chain: {}", stored_code);
}
```
