"""
Generated Code Metadata:
========================
Original URL: https://staging-zksync-dapp-portal.web.app
Prompt: Write a Solidity smart contract that interacts with zkSync Bridge for cross-chain token transfers.
Generated: DETERMINISTIC_b718559946694316
Batch ID: 20250612_150342
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

// Importing necessary interfaces for ERC20 and zkSync Bridge
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

interface IBridge {
    function depositERC20(address token, uint256 amount, address recipient) external;
    function withdrawERC20(address token, uint256 amount) external;
}

contract CrossChainTokenTransfer is Ownable {
    // Address of the zkSync Bridge contract
    IBridge public bridge;

    // Event emitted when tokens are deposited for cross-chain transfer
    event TokensDeposited(address indexed token, address indexed recipient, uint256 amount);
    
    // Event emitted when tokens are withdrawn from the zkSync Bridge
    event TokensWithdrawn(address indexed token, uint256 amount);

    // Constructor to set the bridge address
    constructor(address _bridgeAddress) {
        require(_bridgeAddress != address(0), "Invalid bridge address");
        bridge = IBridge(_bridgeAddress);
    }

    // Function to deposit tokens to the zkSync Bridge
    function depositTokens(address token, uint256 amount, address recipient) external {
        require(amount > 0, "Amount must be greater than zero");
        require(recipient != address(0), "Invalid recipient address");

        // Transfer tokens from the sender to this contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Approve the bridge to spend the tokens
        IERC20(token).approve(address(bridge), amount);

        // Deposit tokens to the zkSync Bridge
        bridge.depositERC20(token, amount, recipient);

        // Emit event for the deposit
        emit TokensDeposited(token, recipient, amount);
    }

    // Function to withdraw tokens from the zkSync Bridge
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");

        // Withdraw tokens from the zkSync Bridge
        bridge.withdrawERC20(token, amount);

        // Emit event for the withdrawal
        emit TokensWithdrawn(token, amount);
    }

    // Function to set a new bridge address (onlyOwner)
    function setBridgeAddress(address _bridgeAddress) external onlyOwner {
        require(_bridgeAddress != address(0), "Invalid bridge address");
        bridge = IBridge(_bridgeAddress);
    }
}
```
