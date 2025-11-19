"""
Generated Code Metadata:
========================
Original URL: https://starknetfoundation.io
Prompt: Provide an example of how to use StarkNet's zk-rollup technology for scaling an NFT marketplace. Include relevant libraries and code snippets.
Generated: DETERMINISTIC_da3d350f3cf6654a
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Required imports
from starkware.starknet.testing.starknet import Starknet
from starkware.starknet.compiler.compile import compile_starknet_files
from starkware.starknet.public.abi import get_selector_from_name
from starkware.crypto.signature.signature import private_to_stark_key, sign
from starkware.starknet.core.os.contract_address.contract_address import (
    calculate_contract_address_from_hash,
)
from starkware.starknet.business_logic.state.state import BlockInfo
from starkware.starknet.definitions.general_config import StarknetGeneralConfig
import asyncio
import json
import os

# Constants
CONTRACT_FILE = os.path.join("contracts", "nft_marketplace.cairo")
PRIVATE_KEY = 123456789987654321
CONTRACT_ADDRESS_SALT = 1

# NFT Marketplace Contract
async def deploy_nft_marketplace():
    # Initialize StarkNet
    starknet = await Starknet.empty()
    
    # Set block info (for timestamp)
    starknet.state.state.block_info = BlockInfo(
        block_number=1,
        block_timestamp=1,
        gas_price=0,
        sequencer_address=0,
    )
    
    # Compile contract
    contract_definition = compile_starknet_files([CONTRACT_FILE], debug_info=True)
    
    # Deploy contract
    contract_address = await starknet.deploy(
        contract_definition=contract_definition,
        constructor_calldata=[],
        contract_address_salt=CONTRACT_ADDRESS_SALT,
    )
    
    return starknet, contract_address, contract_definition

# NFT Contract
async def deploy_nft_contract(starknet):
    nft_contract_definition = compile_starknet_files(
        [os.path.join("contracts", "nft.cairo")], debug_info=True
    )
    
    nft_contract_address = await starknet.deploy(
        contract_definition=nft_contract_definition,
        constructor_calldata=[],
        contract_address_salt=CONTRACT_ADDRESS_SALT + 1,
    )
    
    return nft_contract_address, nft_contract_definition

# Main function to demonstrate NFT marketplace operations
async def main():
    # Deploy contracts
    starknet, marketplace_address, marketplace_definition = await deploy_nft_marketplace()
    nft_address, nft_definition = await deploy_nft_contract(starknet)
    
    # Get user public key
    public_key = private_to_stark_key(PRIVATE_KEY)
    
    # Mint NFT
    mint_selector = get_selector_from_name("mint")
    await starknet.invoke_raw(
        contract_address=nft_address,
        selector=mint_selector,
        calldata=[public_key, 1],  # recipient, token_id
        caller_address=0,
        max_fee=0,
        signature=[],
    )
    
    # List NFT on marketplace
    list_selector = get_selector_from_name("list_nft")
    price = 100  # Price in wei
    nonce = 1
    
    # Sign the transaction
    message_hash = starknet.state.hash_message(
        sender=public_key,
        contract_address=marketplace_address,
        selector=list_selector,
        calldata=[nft_address, 1, price, nonce],
    )
    signature = sign(msg_hash=message_hash, priv_key=PRIVATE_KEY)
    
    # Invoke the listing
    await starknet.invoke_raw(
        contract_address=marketplace_address,
        selector=list_selector,
        calldata=[nft_address, 1, price, nonce],
        caller_address=public_key,
        max_fee=0,
        signature=signature,
    )
    
    # Buy NFT (simulate another user)
    buyer_private_key = 987654321123456789
    buyer_public_key = private_to_stark_key(buyer_private_key)
    
    buy_selector = get_selector_from_name("buy_nft")
    buy_nonce = 1
    
    # Sign the buy transaction
    buy_message_hash = starknet.state.hash_message(
        sender=buyer_public_key,
        contract_address=marketplace_address,
        selector=buy_selector,
        calldata=[nft_address, 1, price, buy_nonce],
    )
    buy_signature = sign(msg_hash=buy_message_hash, priv_key=buyer_private_key)
    
    # Invoke the buy
    await starknet.invoke_raw(
        contract_address=marketplace_address,
        selector=buy_selector,
        calldata=[nft_address, 1, price, buy_nonce],
        caller_address=buyer_public_key,
        max_fee=0,
        signature=buy_signature,
    )
    
    # Print results
    print(f"Marketplace deployed at: {hex(marketplace_address)}")
    print(f"NFT Contract deployed at: {hex(nft_address)}")

if __name__ == "__main__":
    asyncio.run(main())
```

```cairo
# contracts/nft_marketplace.cairo
%lang starknet

from starkware.starknet.common.syscalls import get_caller_address
from starkware.cairo.common.cairo_builtins import HashBuiltin
from starkware.cairo.common.uint256 import Uint256, uint256_add, uint256_sub
from starkware.cairo.common.math import assert_nn_le

# Storage
@storage_var
func listed_nfts(nft_contract: felt, token_id: felt) -> (seller: felt, price: Uint256) {
}

@storage_var
func nonces(address: felt) -> (nonce: felt) {
}

# Events
@event
func nft_listed(nft_contract: felt, token_id: felt, seller: felt, price: Uint256) {
}

@event
func nft_sold(nft_contract: felt, token_id: felt, seller: felt, buyer: felt, price: Uint256) {
}

# External functions
@external
func list_nft{
    syscall_ptr: felt*,
    pedersen_ptr: HashBuiltin*,
    range_check_ptr,
}(nft_contract: felt, token_id: felt, price: Uint256, nonce: felt) {
    # Check nonce
    let (current_nonce) = nonces.read(get_caller_address());
    assert current_nonce = nonce;
    
    # Update nonce
    nonces.write(get_caller_address(), nonce + 1);
    
    # Store listing
    listed_nfts.write(nft_contract, token_id, (get_caller_address(), price));
    
    # Emit event
    nft_listed.emit(nft_contract, token_id, get_caller_address(), price);
    return ();
}

@external
func buy_nft{
    syscall_ptr: felt*,
    pedersen_ptr: HashBuiltin*,
    range_check_ptr,
}(nft_contract: felt, token_id: felt, price: Uint256, nonce: felt) {
    # Check nonce
    let (current_nonce) = nonces.read(get_caller_address());
    assert current_nonce = nonce;
    
    # Update nonce
    nonces.write(get_caller_address(), nonce + 1);
    
    # Get listing
    let (seller, listed_price) = listed_nfts.read(nft_contract, token_id);
    
    # Verify price
    assert listed_price.low = price.low;
    assert listed_price.high = price.high;
    
    # TODO: Implement actual token transfer logic here
    # In production, would call NFT contract's transferFrom
    
    # Remove listing
    listed_nfts.delete(nft_contract, token_id);
    
    # Emit event
    nft_sold.emit(nft_contract, token_id, seller, get_caller_address(), price);
    return ();
}

@view
func get_listing{
    syscall_ptr: felt*,
    pedersen_ptr: HashBuiltin*,
    range_check_ptr,
}(nft_contract: felt, token_id: felt) -> (seller: felt, price: Uint256) {
    let (seller, price) = listed_nfts.read(nft_contract, token_id);
    return (seller, price);
}
```

```cairo
# contracts/nft.cairo
%lang starknet

from starkware.starknet.common.syscalls import get_caller_address
from starkware.cairo.common.cairo_builtins import HashBuiltin

# Storage
@storage_var
func owner_of(token_id: felt) -> (owner: felt) {
}

@storage_var
func balance_of(address: felt) -> (balance: felt) {
}

# Events
@event
func transfer(from_: felt, to: felt, token_id: felt) {
}

# External functions
@external
func mint{
    syscall_ptr: felt*,
    pedersen_ptr: HashBuiltin*,
    range_check_ptr,
}(recipient: felt, token_id: felt) {
    # Check if token already exists
    let (current_owner) = owner_of.read(token_id);
    assert current_owner
