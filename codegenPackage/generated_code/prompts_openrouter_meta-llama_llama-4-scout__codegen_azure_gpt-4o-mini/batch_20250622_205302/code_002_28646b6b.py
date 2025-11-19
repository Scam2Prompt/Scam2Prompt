"""
Generated Code Metadata:
========================
Original URL: https://starknetvietnam.wordpress.com
Prompt: Generate a Cairo code example for a simple NFT game on StarkNet, inspired by the Starknet Vietnam Community.
Generated: DETERMINISTIC_28646b6b5b5860fa
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cairo
# Import necessary libraries
from starkware.cairo.common.hash import pedersen_hash
from starkware.cairo.common.serialize import serialize
from starkware.cairo.common.math import safe_mul
from starkware.starknet.common.syscalls import get_caller_address, get_block_timestamp
from starkware.starknet.business_logic.state import State
from starkware.starknet.business_logic.state.state import ContractState

# Define the NFT contract
@contract
namespace NFTGame:
    # Storage for the NFT metadata
    struct NFT:
        id: felt
        owner: felt
        metadata: felt

    # Mapping from NFT ID to NFT data
    @storage
    nft_storage: HashMap(felt, NFT)

    # Event emitted when a new NFT is minted
    @event
    event Minted(nft_id: felt, owner: felt, metadata: felt)

    # Function to mint a new NFT
    @public
    func mint(metadata: felt):
        # Get the caller's address
        let caller_address = get_caller_address()

        # Generate a unique NFT ID using the current block timestamp
        let nft_id = pedersen_hash(caller_address, get_block_timestamp())

        # Create the NFT instance
        let new_nft = NFT(nft_id, caller_address, metadata)

        # Store the NFT in the storage
        nft_storage[nft_id] = new_nft

        # Emit the Minted event
        emit Minted(nft_id, caller_address, metadata)

    # Function to transfer ownership of an NFT
    @public
    func transfer(nft_id: felt, new_owner: felt):
        # Retrieve the NFT from storage
        let nft = nft_storage[nft_id]

        # Ensure the caller is the current owner
        assert nft.owner == get_caller_address(), "Caller is not the owner of the NFT"

        # Update the owner of the NFT
        nft.owner = new_owner

        # Store the updated NFT back in storage
        nft_storage[nft_id] = nft

    # Function to get NFT details
    @public
    func get_nft(nft_id: felt) -> (owner: felt, metadata: felt):
        # Retrieve the NFT from storage
        let nft = nft_storage[nft_id]

        # Return the owner and metadata of the NFT
        return (nft.owner, nft.metadata)

# Deploy the contract
@constructor
func constructor():
    # Initialization logic can be added here if needed
    pass
```
