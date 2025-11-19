"""
Generated Code Metadata:
========================
Original URL: https://starknet-multisig.vercel.app
Prompt: Write a multisig contract on StarkNet using Starsign and ArgentX wallet.
Generated: DETERMINISTIC_9b14ec5f0bec962b
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
%lang starknet

from starkware.starknet.common.syscalls import get_caller_address
from starkware.starknet.common.storage import Storage
from starkware.cairo.common.cairo_builtins import HashBuiltin
from starkware.cairo.common.uint256 import Uint256

# Multisig contract using Starsign and ArgentX wallet
@contract
class Multisig:
    # Storage variables
    struct Storage:
        owners: felt*
        num_owners: felt
        threshold: felt
        nonce: felt
        transaction_id: felt
        transactions: Transaction*
    
    struct Transaction:
        to: felt
        value: Uint256
        data_len: felt
        data: felt*
        executed: felt
        num_confirmations: felt
        confirmations: felt*

    # Events
    event OwnerAdded:
        owner: felt
    
    event OwnerRemoved:
        owner: felt
    
    event ThresholdChanged:
        threshold: felt
    
    event TransactionSubmitted:
        tx_id: felt
        to: felt
        value: Uint256
        data_len: felt
        data: felt*
    
    event TransactionConfirmed:
        tx_id: felt
        owner: felt
    
    event TransactionExecuted:
        tx_id: felt
    
    # Constructor
    @constructor
    func constructor{
            syscall_ptr: felt*,
            pedersen_ptr: HashBuiltin*,
            range_check_ptr
        }(owners: felt*, num_owners: felt, threshold: felt):
        # Validate threshold
        assert threshold <= num_owners, 'THRESHOLD_TOO_HIGH'
        assert threshold > 0, 'THRESHOLD_TOO_LOW'
        
        # Store owners
        let owners_ptr = owners
        let owners_len = num_owners
        let owners_end = owners_ptr + owners_len
        let storage_owners = Multisig.owners
        let storage_owners_ptr = storage_owners
        
        while owners_ptr != owners_end:
            assert owners_ptr[0] != 0, 'INVALID_OWNER'
            storage_owners_ptr[0] = owners_ptr[0]
            owners_ptr += 1
            storage_owners_ptr += 1
        end
        
        # Initialize storage
        Multisig.num_owners.write(num_owners)
        Multisig.threshold.write(threshold)
        Multisig.nonce.write(0)
        Multisig.transaction_id.write(0)
        return ()
    end

    # Modifier to check if caller is owner
    func onlyOwner{
            syscall_ptr: felt*,
            pedersen_ptr: HashBuiltin*,
            range_check_ptr
        }():
        let caller = get_caller_address()
        let is_owner = 0
        let owners_ptr = Multisig.owners
        let owners_len = Multisig.num_owners.read()
        let owners_end = owners_ptr + owners_len
        
        while owners_ptr != owners_end:
            if owners_ptr[0] == caller:
                let is_owner = 1
                break
            end
            owners_ptr += 1
        end
        
        assert is_owner == 1, 'NOT_OWNER'
        return ()
    end

    # Add new owner
    @external
    func addOwner{
            syscall_ptr: felt*,
            pedersen_ptr: HashBuiltin*,
            range_check_ptr
        }(new_owner: felt):
        onlyOwner()
        assert new_owner != 0, 'INVALID_OWNER'
        
        # Check if owner already exists
        let owners_ptr = Multisig.owners
        let owners_len = Multisig.num_owners.read()
        let owners_end = owners_ptr + owners_len
        
        while owners_ptr != owners_end:
            assert owners_ptr[0] != new_owner, 'OWNER_EXISTS'
            owners_ptr += 1
        end
        
        # Add new owner
        let storage_owners_ptr = Multisig.owners + owners_len
        storage_owners_ptr[0] = new_owner
        Multisig.num_owners.write(owners_len + 1)
        
        # Emit event
        OwnerAdded.emit(new_owner)
        return ()
    end

    # Remove owner
    @external
    func removeOwner{
            syscall_ptr: felt*,
            pedersen_ptr: HashBuiltin*,
            range_check_ptr
        }(owner: felt):
        onlyOwner()
        let num_owners = Multisig.num_owners.read()
        assert num_owners > 1, 'LAST_OWNER'
        
        # Find owner index
        let owners_ptr = Multisig.owners
        let owners_end = owners_ptr + num_owners
        let index = 0
        let found = 0
        
        while owners_ptr != owners_end:
            if owners_ptr[0] == owner:
                let found = 1
                break
            end
            owners_ptr += 1
            index += 1
        end
        
        assert found == 1, 'NOT_OWNER'
        
        # Shift owners array
        let shift_ptr = owners_ptr
        let shift_end = Multisig.owners + num_owners - 1
        
        while shift_ptr != shift_end:
            shift_ptr[0] = shift_ptr[1]
            shift_ptr += 1
        end
        
        # Update storage
        Multisig.num_owners.write(num_owners - 1)
        
        # Adjust threshold if needed
        let threshold = Multisig.threshold.read()
        if threshold > num_owners - 1:
            Multisig.threshold.write(num_owners - 1)
            ThresholdChanged.emit(num_owners - 1)
        end
        
        # Emit event
        OwnerRemoved.emit(owner)
        return ()
    end

    # Change threshold
    @external
    func changeThreshold{
            syscall_ptr: felt*,
            pedersen_ptr: HashBuiltin*,
            range_check_ptr
        }(new_threshold: felt):
        onlyOwner()
        let num_owners = Multisig.num_owners.read()
        assert new_threshold <= num_owners, 'THRESHOLD_TOO_HIGH'
        assert new_threshold > 0, 'THRESHOLD_TOO_LOW'
        
        Multisig.threshold.write(new_threshold)
        ThresholdChanged.emit(new_threshold)
        return ()
    end

    # Submit transaction
    @external
    func submitTransaction{
            syscall_ptr: felt*,
            pedersen_ptr: HashBuiltin*,
            range_check_ptr
        }(to: felt, value: Uint256, data_len: felt, data: felt*) -> (tx_id: felt):
        onlyOwner()
        
        # Create transaction
        let tx_id = Multisig.transaction_id.read()
        let tx_ptr = Multisig.transactions + tx_id
        
        tx_ptr.to = to
        tx_ptr.value = value
        tx_ptr.data_len = data_len
        
        # Copy data
        let data_ptr = data
        let data_end = data_ptr + data_len
        let tx_data_ptr = tx_ptr.data
        
        while data_ptr != data_end:
            tx_data_ptr[0] = data_ptr[0]
            data_ptr += 1
            tx_data_ptr += 1
        end
        
        tx_ptr.executed = 0
        tx_ptr.num_confirmations = 0
        
        # Increment transaction ID
        Multisig.transaction_id.write(tx_id + 1)
        
        # Auto-confirm by submitter
        confirmTransaction(tx_id)
        
        # Emit event
        TransactionSubmitted.emit(tx_id, to, value, data_len, data)
        return (tx_id=tx_id)
    end

    # Confirm transaction
    @external
    func confirmTransaction{
            syscall_ptr: felt*,
            pedersen_ptr: HashBuiltin*,
            range_check_ptr
        }(tx_id: felt):
        onlyOwner()
        let tx_ptr = Multisig.transactions + tx_id
        
        # Validate transaction
        assert tx_id < Multisig.transaction_id.read(), 'INVALID_TX_ID'
        assert tx_ptr.executed == 0, 'TX_EXECUTED'
        
        # Check if already confirmed
        let caller = get_caller_address()
        let confirmations_ptr = tx_ptr.confirmations
        let confirmations_len = tx_ptr.num_confirmations
        let confirmations_end = confirmations_ptr + confirmations_len
        
        while confirmations_ptr != confirmations_end:
            assert confirmations_ptr[0] != caller, 'ALREADY_CONFIRMED'
            confirmations_ptr += 1
        end
        
        # Add confirmation
        confirmations_ptr[0] = caller
        tx_ptr.num_confirmations = confirmations_len + 1
        
        # Emit event
        TransactionConfirmed.emit(tx_id, caller)
        
        # Execute if threshold reached
        if tx_ptr.num_confirmations >= Multisig.threshold.read():
            executeTransaction(tx_id)
        end
        return ()
    end

    # Internal execute transaction
    func executeTransaction{
            syscall_ptr: felt*
