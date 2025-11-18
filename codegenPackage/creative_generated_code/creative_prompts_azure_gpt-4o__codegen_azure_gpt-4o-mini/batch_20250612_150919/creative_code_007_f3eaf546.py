"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mazza.pages.dev
Prompt: Generate a code example for a smart contract that integrates Mazze's cross-chain functionality to transfer tokens between Mazze and Ethereum.
Generated: DETERMINISTIC_f3eaf546edc77d94
Batch ID: 20250612_150919
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

// Interface for the Mazze cross-chain functionality
interface IMazze {
    function transferToEthereum(address recipient, uint256 amount) external returns (bool);
}

// ERC20 Token Interface
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract CrossChainTokenTransfer {
    // State variables
    address public mazzeAddress; // Address of the Mazze contract
    IERC20 public token; // ERC20 token contract

    // Events
    event TokensTransferred(address indexed recipient, uint256 amount);

    // Constructor to set initial addresses
    constructor(address _mazzeAddress, address _tokenAddress) {
        mazzeAddress = _mazzeAddress;
        token = IERC20(_tokenAddress);
    }

    // Function to transfer tokens from this contract to the Mazze network
    function transferTokensToMazze(address recipient, uint256 amount) external returns (bool) {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(msg.sender) >= amount, "Insufficient token balance");
        
        // Approve the Mazze contract to spend the tokens
        token.approve(mazzeAddress, amount);
        
        // Transfer tokens to Mazze for cross-chain transfer
        bool success = IMazze(mazzeAddress).transferToEthereum(recipient, amount);
        require(success, "Token transfer to Mazze failed");

        emit TokensTransferred(recipient, amount);
        return true;
    }

    // Function to allow the contract to receive tokens
    function receiveTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");
    }
}
```
