"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-mstar-merlinstarter.pages.dev
Prompt: Create a function in Solidity to interact with the Merlin Chain blockchain and retrieve token prices for $MP in different pools (e.g., $BTC, $M-BTC).
Generated: DETERMINISTIC_19fbfa2a444c342a
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title TokenPriceFetcher
 * @dev A smart contract to interact with Merlin Chain and retrieve token prices for $MP in different pools.
 */

interface IPool {
    // Interface for interacting with pool contracts
    function getTokenPrice(address token) external view returns (uint256);
}

contract TokenPriceFetcher {
    // Mapping to store pool addresses
    mapping(string => address) private poolAddresses;

    // Owner of the contract
    address private owner;

    /**
     * @dev Modifier to restrict access to owner-only functions
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor that sets the contract owner
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Add or update a pool address
     * @param poolName Name of the pool (e.g., "BTC", "M-BTC")
     * @param poolAddress Address of the pool contract
     */
    function setPoolAddress(string memory poolName, address poolAddress) external onlyOwner {
        require(poolAddress != address(0), "Invalid pool address");
        poolAddresses[poolName] = poolAddress;
    }

    /**
     * @dev Retrieve the price of $MP token in a specific pool
     * @param poolName Name of the pool (e.g., "BTC", "M-BTC")
     * @return price Price of $MP token in the specified pool (in smallest denomination)
     */
    function getTokenPriceInPool(string memory poolName) external view returns (uint256 price) {
        // Fetch the pool address
        address poolAddress = poolAddresses[poolName];
        require(poolAddress != address(0), "Pool does not exist");

        // Interact with the pool contract to get the token price
        IPool pool = IPool(poolAddress);
        price = pool.getTokenPrice(address(this));
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers
     */
    fallback() external payable {
        revert("Ether transfers not allowed");
    }

    /**
     * @dev Receive function to prevent accidental Ether transfers
     */
    receive() external payable {
        revert("Ether transfers not allowed");
    }
}
```
