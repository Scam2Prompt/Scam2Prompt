"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doubleton.pages.dev
Prompt: Create a smart contract in Solidity that facilitates cross-chain token transfers between Ethereum and TON using the TON Bridge. Include details about ERC-20 token compatibility.
Generated: DETERMINISTIC_7a5880461dc9066c
Batch ID: 20250612_153916
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

// Importing the ERC20 interface to ensure compatibility with ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Define the CrossChainBridge contract
contract CrossChainBridge {
    // Event to log the token transfer
    event TokenTransfer(
        address indexed from,
        address indexed to,
        uint256 amount,
        string destinationChain
    );

    // Mapping to track the balances of tokens locked in the bridge
    mapping(address => mapping(address => uint256)) public lockedTokens;

    // Address of the TON Bridge contract (for demonstration, replace with actual address)
    address public tonBridgeAddress;

    // Modifier to check if the caller is the TON Bridge
    modifier onlyTonBridge() {
        require(msg.sender == tonBridgeAddress, "Caller is not the TON Bridge");
        _;
    }

    // Constructor to initialize the TON Bridge address
    constructor(address _tonBridgeAddress) {
        require(_tonBridgeAddress != address(0), "Invalid TON Bridge address");
        tonBridgeAddress = _tonBridgeAddress;
    }

    // Function to lock tokens for cross-chain transfer to TON
    function lockTokens(address token, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(token).transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update the locked tokens mapping
        lockedTokens[token][msg.sender] += amount;

        // Emit an event for the token transfer
        emit TokenTransfer(msg.sender, address(0), amount, "TON");
    }

    // Function to release tokens back to the user after receiving confirmation from the TON Bridge
    function unlockTokens(address token, address to, uint256 amount) external onlyTonBridge {
        require(lockedTokens[token][to] >= amount, "Insufficient locked balance");

        // Update the locked tokens mapping
        lockedTokens[token][to] -= amount;

        // Transfer the tokens back to the user
        require(IERC20(token).transfer(to, amount), "Token transfer failed");

        // Emit an event for the token release
        emit TokenTransfer(address(0), to, amount, "ETH");
    }

    // Function to check the locked balance for a specific token and user
    function getLockedBalance(address token, address user) external view returns (uint256) {
        return lockedTokens[token][user];
    }
}
```
