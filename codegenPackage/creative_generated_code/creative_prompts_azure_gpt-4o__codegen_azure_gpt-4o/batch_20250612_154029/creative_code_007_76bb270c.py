"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectsflrsync.online
Prompt: Generate a smart contract that allows dApps to serve multiple chains through a single deployment on Flare Network.
Generated: DETERMINISTIC_76bb270ce112df97
Batch ID: 20250612_154029
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
 * @title MultiChainGateway
 * @dev Smart contract to enable dApps to serve multiple chains via a single deployment on the Flare Network.
 * This contract facilitates cross-chain communication by leveraging Flare's interoperability features.
 */
contract MultiChainGateway {
    // Owner of the contract
    address public owner;

    // Mapping to store supported chain IDs
    mapping(uint256 => bool) public supportedChains;

    // Event emitted when a chain is added or removed
    event ChainStatusUpdated(uint256 indexed chainId, bool isSupported);

    // Event emitted when a cross-chain message is relayed
    event CrossChainMessage(
        address indexed sender,
        uint256 indexed targetChainId,
        address indexed targetContract,
        bytes payload
    );

    /**
     * @dev Modifier to restrict function calls to the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor that sets the deployer as the owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Add or remove support for a specific chain ID.
     * @param chainId The ID of the chain.
     * @param isSupported Boolean indicating whether the chain is supported.
     */
    function updateChainSupport(uint256 chainId, bool isSupported) external onlyOwner {
        supportedChains[chainId] = isSupported;
        emit ChainStatusUpdated(chainId, isSupported);
    }

    /**
     * @dev Relay a message to a target contract on a supported chain.
     * @param targetChainId The ID of the target chain.
     * @param targetContract The address of the target contract on the destination chain.
     * @param payload The message payload to be sent.
     */
    function relayMessage(
        uint256 targetChainId,
        address targetContract,
        bytes memory payload
    ) external {
        // Ensure the target chain is supported
        require(supportedChains[targetChainId], "Target chain is not supported");

        // Emit an event for the relay operation (this can be picked up by off-chain relayers)
        emit CrossChainMessage(msg.sender, targetChainId, targetContract, payload);
    }

    /**
     * @dev Transfer ownership of the contract to a new owner.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        owner = newOwner;
    }
}
```
