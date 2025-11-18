"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multidappsresolver.pages.dev
Prompt: Write a smart contract that utilizes Resolver String's protocol for token bridge operations, ensuring secure cross-chain transfers.
Generated: DETERMINISTIC_156acfee84ba88b1
Batch ID: 20250612_152235
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Context.sol";

// Interface for the Resolver String protocol
interface IResolverString {
    function resolve(string calldata identifier) external view returns (address);
}

// Smart contract for cross-chain token bridge
contract TokenBridge is Ownable {
    // Events for logging operations
    event TokensBridged(address indexed sender, address indexed token, uint256 amount, string targetChain);
    event TokensReceived(address indexed receiver, address indexed token, uint256 amount, string sourceChain);

    // Mapping to keep track of bridged tokens
    mapping(address => mapping(string => bool)) public bridgedTokens;

    // Resolver String contract address
    IResolverString public resolver;

    // Constructor to set the Resolver String address
    constructor(address _resolver) {
        resolver = IResolverString(_resolver);
    }

    // Function to bridge tokens to another chain
    function bridgeTokens(address token, uint256 amount, string calldata targetChain) external {
        // Ensure the token contract is valid
        require(resolver.resolve(token) != address(0), "Invalid token");

        // Transfer tokens from sender to the bridge contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Mark the token as bridged to prevent re-entrance
        bridgedTokens[token][targetChain] = true;

        // Emit an event for the bridging operation
        emit TokensBridged(msg.sender, token, amount, targetChain);
    }

    // Function to receive bridged tokens from another chain
    function receiveTokens(address token, uint256 amount, string calldata sourceChain) external onlyOwner {
        // Ensure the token is recognized for receiving
        require(bridgedTokens[token][sourceChain], "Token not bridged");

        // Reset the bridged status for the token
        bridgedTokens[token][sourceChain] = false;

        // Transfer tokens to the receiver (owner)
        IERC20(token).transfer(msg.sender, amount);

        // Emit an event for the received operation
        emit TokensReceived(msg.sender, token, amount, sourceChain);
    }

    // Function to withdraw tokens stuck in the contract
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        // Transfer the specified amount of tokens to the owner
        IERC20(token).transfer(msg.sender, amount);
    }

    // Function to update the Resolver String address
    function updateResolver(address _resolver) external onlyOwner {
        resolver = IResolverString(_resolver);
    }
}
```
