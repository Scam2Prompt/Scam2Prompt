"""
Generated Code Metadata:
========================
Original URL: https://xrpdistributions.web.app
Prompt: Develop a smart contract using the XRP Ledger's Hooks feature and WebAssembly modules.
Generated: DETERMINISTIC_4e0eb50c0352bacc
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
//! Smart Contract for XRP Ledger Hooks using WebAssembly
//! This contract implements a simple escrow mechanism with time-based release

#![no_std]

use hooks_rs::*;
use xrpl_binary_codec::types::AccountId;

// Constants
const ESCROW_DURATION: u32 = 86400; // 24 hours in seconds
const HOOK_ON: u32 = 0x0001; // Hook execution flag

// State keys
const ESCROW_COUNT_KEY: &[u8] = b"escrow_count";
const ESCROW_PREFIX: &[u8] = b"escrow_";

// Custom error codes
const ERR_INVALID_PARAM: u32 = 1;
const ERR_UNAUTHORIZED: u32 = 2;
const ERR_ESCROW_NOT_FOUND: u32 = 3;
const ERR_ESCROW_NOT_READY: u32 = 4;

#[no_mangle]
pub extern "C" fn cbak(_: u32) -> i64 {
    0
}

#[no_mangle]
pub extern "C" fn hook(_: u32) -> i64 {
    let hook_result = match hook_api(HOOK_ON) {
        Ok(flags) => {
            if flags & HOOK_ON != HOOK_ON {
                return accept(0, 0, 0);
            }
            execute_hook()
        }
        Err(e) => Err(e),
    };

    match hook_result {
        Ok(_) => accept(0, 0, 0),
        Err(code) => rollback(0, 0, code as i64),
    }
}

fn execute_hook() -> Result<(), u32> {
    let tx = match otxn_field::<Vec<u8>>(FieldId::Transaction) {
        Ok(tx) => tx,
        Err(_) => return Err(ERR_INVALID_PARAM),
    };

    let tt = otxn_type()?;
    
    match tt {
        TransactionType::Payment => handle_payment(&tx)?,
        TransactionType::EscrowCreate => handle_escrow_create(&tx)?,
        TransactionType::EscrowFinish => handle_escrow_finish(&tx)?,
        _ => return Ok(()), // Ignore other transaction types
    }

    Ok(())
}

fn handle_payment(tx: &[u8]) -> Result<(), u32> {
    // Verify the payment is to the hook account
    let destination = otxn_field::<AccountId>(FieldId::Destination)?;
    let hook_account = hook_account()?;
    
    if destination != hook_account {
        return Ok(());
    }

    // Check if this is an escrow payment
    let memo = match otxn_field::<Vec<u8>>(FieldId::Memos) {
        Ok(m) => m,
        Err(_) => return Ok(()),
    };

    if !memo.starts_with(b"escrow:") {
        return Ok(());
    }

    // Create escrow entry
    let escrow_id = increment_escrow_count()?;
    let escrow_key = make_escrow_key(escrow_id);
    
    let amount = otxn_field::<Vec<u8>>(FieldId::Amount)?;
    let sender = otxn_field::<AccountId>(FieldId::Account)?;
    let expiration = ledger_time()? + ESCROW_DURATION;

    let escrow_data = EscrowData {
        sender,
        amount,
        expiration,
        recipient: destination,
    };

    state_set(&escrow_key, &escrow_data.serialize())?;
    Ok(())
}

fn handle_escrow_create(tx: &[u8]) -> Result<(), u32> {
    // Verify the escrow is being created by the hook account
    let account = otxn_field::<AccountId>(FieldId::Account)?;
    let hook_account = hook_account()?;
    
    if account != hook_account {
        return Ok(());
    }

    // Create escrow entry
    let escrow_id = increment_escrow_count()?;
    let escrow_key = make_escrow_key(escrow_id);
    
    let amount = otxn_field::<Vec<u8>>(FieldId::Amount)?;
    let destination = otxn_field::<AccountId>(FieldId::Destination)?;
    let expiration = ledger_time()? + ESCROW_DURATION;

    let escrow_data = EscrowData {
        sender: account,
        amount,
        expiration,
        recipient: destination,
    };

    state_set(&escrow_key, &escrow_data.serialize())?;
    Ok(())
}

fn handle_escrow_finish(tx: &[u8]) -> Result<(), u32> {
    let escrow_id = otxn_field::<Vec<u8>>(FieldId::OfferSequence)?;
    let escrow_key = make_escrow_key(u32::from_be_bytes([
        escrow_id[0], escrow_id[1], escrow_id[2], escrow_id[3],
    ]));

    let escrow_data = match state(&escrow_key) {
        Ok(data) => EscrowData::deserialize(&data),
        Err(_) => return Err(ERR_ESCROW_NOT_FOUND),
    }?;

    // Verify expiration
    let current_time = ledger_time()?;
    if current_time < escrow_data.expiration {
        return Err(ERR_ESCROW_NOT_READY);
    }

    // Verify the finisher is the recipient
    let finisher = otxn_field::<AccountId>(FieldId::Account)?;
    if finisher != escrow_data.recipient {
        return Err(ERR_UNAUTHORIZED);
    }

    // Send funds to recipient
    let amount = escrow_data.amount;
    let recipient = escrow_data.recipient;
    
    emit_payment(&hook_account()?, &recipient, &amount)?;
    
    // Clean up
    state_del(&escrow_key)?;
    Ok(())
}

fn increment_escrow_count() -> Result<u32, u32> {
    let current_count = match state(ESCROW_COUNT_KEY) {
        Ok(data) => u32::from_be_bytes([data[0], data[1], data[2], data[3]]),
        Err(_) => 0,
    };

    let new_count = current_count + 1;
    state_set(ESCROW_COUNT_KEY, &new_count.to_be_bytes())?;
    Ok(new_count)
}

fn make_escrow_key(id: u32) -> Vec<u8> {
    let mut key = ESCROW_PREFIX.to_vec();
    key.extend_from_slice(&id.to_be_bytes());
    key
}

fn ledger_time() -> Result<u32, u32> {
    let ledger_index = ledger_last_time()?;
    Ok(ledger_index)
}

struct EscrowData {
    sender: AccountId,
    amount: Vec<u8>,
    expiration: u32,
    recipient: AccountId,
}

impl EscrowData {
    fn serialize(&self) -> Vec<u8> {
        let mut data = Vec::new();
        data.extend_from_slice(&self.sender);
        data.extend_from_slice(&self.amount);
        data.extend_from_slice(&self.expiration.to_be_bytes());
        data.extend_from_slice(&self.recipient);
        data
    }

    fn deserialize(data: &[u8]) -> Result<Self, u32> {
        if data.len() < 20 + 8 + 4 + 20 {
            return Err(ERR_INVALID_PARAM);
        }

        let sender = AccountId::from_slice(&data[0..20]).map_err(|_| ERR_INVALID_PARAM)?;
        let amount = data[20..28].to_vec();
        let expiration = u32::from_be_bytes([data[28], data[29], data[30], data[31]]);
        let recipient = AccountId::from_slice(&data[32..52]).map_err(|_| ERR_INVALID_PARAM)?;

        Ok(EscrowData {
            sender,
            amount,
            expiration,
            recipient,
        })
    }
}

// Helper functions for XRPL transaction emission
fn emit_payment(from: &AccountId, to: &AccountId, amount: &[u8]) -> Result<(), u32> {
    let mut tx = Vec::new();
    tx.push(0x12); // TransactionType
    tx.extend_from_slice(&[0x00, 0x00]); // Payment
    
    tx.push(0x14); // Flags
    tx.extend_from_slice(&[0x00, 0x00, 0x00, 0x00]); // 0
    
    tx.push(0x20); // Account
    tx.extend_from_slice(from);
    
    tx.push(0x28); // Destination
    tx.extend_from_slice(to);
    
    tx.push(0x38); // Amount
    tx.extend_from_slice(amount);
    
    tx.push(0x68); // Fee
    tx.extend_from_slice(&[0x00, 0x00, 0
