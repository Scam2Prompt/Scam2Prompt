"""
Generated Code Metadata:
========================
Original URL: https://matmo-ccdashboard.pages.dev
Prompt: Develop a smart contract for a horizontally scalable network of chains, incorporating shared security and communication layers, similar to Matmo's Superchain architecture.
Generated: DETERMINISTIC_0ffab1c5091c819d
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/// @title Smart Contract for a Horizontally Scalable Network of Chains
/// @notice This contract implements a basic structure for a Superchain architecture
///         with shared security and communication layers.
contract Superchain {
    // Event emitted when a new chain is registered
    event ChainRegistered(address indexed chainAddress, string chainName);

    // Event emitted when a message is sent between chains
    event MessageSent(address indexed fromChain, address indexed toChain, string message);

    // Struct to represent a registered chain
    struct Chain {
        string name; // Name of the chain
        address chainAddress; // Address of the chain contract
        bool isActive; // Status of the chain
    }

    // Mapping to store registered chains
    mapping(address => Chain) public chains;

    // Array to keep track of all registered chains
    address[] public chainAddresses;

    // Modifier to check if the caller is a registered chain
    modifier onlyRegisteredChain() {
        require(chains[msg.sender].isActive, "Caller is not a registered chain");
        _;
    }

    /// @notice Registers a new chain in the Superchain network
    /// @param _chainAddress The address of the chain contract
    /// @param _chainName The name of the chain
    function registerChain(address _chainAddress, string memory _chainName) external {
        require(_chainAddress != address(0), "Invalid chain address");
        require(bytes(_chainName).length > 0, "Chain name cannot be empty");
        require(!chains[_chainAddress].isActive, "Chain is already registered");

        // Register the new chain
        chains[_chainAddress] = Chain({
            name: _chainName,
            chainAddress: _chainAddress,
            isActive: true
        });

        chainAddresses.push(_chainAddress);
        emit ChainRegistered(_chainAddress, _chainName);
    }

    /// @notice Sends a message from one chain to another
    /// @param _toChain The address of the destination chain
    /// @param _message The message to be sent
    function sendMessage(address _toChain, string memory _message) external onlyRegisteredChain {
        require(chains[_toChain].isActive, "Destination chain is not registered");

        // Emit the message sent event
        emit MessageSent(msg.sender, _toChain, _message);
    }

    /// @notice Deactivates a registered chain
    /// @param _chainAddress The address of the chain to deactivate
    function deactivateChain(address _chainAddress) external {
        require(chains[_chainAddress].isActive, "Chain is not active");
        
        // Deactivate the chain
        chains[_chainAddress].isActive = false;
    }

    /// @notice Returns the details of a registered chain
    /// @param _chainAddress The address of the chain
    /// @return name The name of the chain
    /// @return isActive The active status of the chain
    function getChainDetails(address _chainAddress) external view returns (string memory name, bool isActive) {
        require(chains[_chainAddress].isActive || !chains[_chainAddress].isActive, "Chain not found");
        Chain memory chain = chains[_chainAddress];
        return (chain.name, chain.isActive);
    }

    /// @notice Returns the list of all registered chains
    /// @return addresses The array of registered chain addresses
    function getAllChains() external view returns (address[] memory addresses) {
        return chainAddresses;
    }
}
```
