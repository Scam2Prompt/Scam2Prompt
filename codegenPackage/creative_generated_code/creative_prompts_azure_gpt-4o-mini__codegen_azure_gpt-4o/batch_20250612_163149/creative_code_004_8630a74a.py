"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectsflrsync.online
Prompt: Create a simple dApp that demonstrates the use of Flare's EVM compatibility and its ability to serve multiple chains with a single deployment.
Generated: DETERMINISTIC_8630a74a6903191a
Batch ID: 20250612_163149
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
 * @title MultiChainStorage
 * @dev A simple decentralized application (dApp) that demonstrates Flare's EVM compatibility
 * and its ability to serve multiple chains with a single deployment. This contract allows users
 * to store and retrieve data while identifying the originating chain.
 */
contract MultiChainStorage {
    // Mapping to store data, keyed by chainID and sender address
    mapping(uint256 => mapping(address => string)) private storedData;

    // Event to notify data storage, including chainID and sender
    event DataStored(uint256 chainID, address indexed sender, string data);

    /**
     * @dev Stores data for the sender on the current chain.
     * @param data The string data to be stored.
     */
    function storeData(string memory data) external {
        // Get the current chain ID
        uint256 chainID = block.chainid;

        // Store the data in the mapping
        storedData[chainID][msg.sender] = data;

        // Emit event for transparency and tracking
        emit DataStored(chainID, msg.sender, data);
    }

    /**
     * @dev Retrieves stored data for the sender on the current chain.
     * @return The stored data as a string.
     */
    function retrieveData() external view returns (string memory) {
        // Get the current chain ID
        uint256 chainID = block.chainid;

        // Retrieve the data from the mapping
        return storedData[chainID][msg.sender];
    }

    /**
     * @dev Retrieves stored data for a specific chainID and sender address.
     * @param chainID The chain ID to query.
     * @param sender The address of the sender whose data needs to be retrieved.
     * @return The stored data as a string.
     */
    function retrieveDataByChain(uint256 chainID, address sender)
        external
        view
        returns (string memory)
    {
        // Retrieve data based on chainID and sender address
        return storedData[chainID][sender];
    }
}
```

This Solidity code is designed to be deployed to Flare's EVM-compatible blockchain and should work seamlessly across multiple chains. It leverages `block.chainid` to identify the chain on which it is executed, demonstrating Flare's ability to interact with multiple chains within the same deployment.
