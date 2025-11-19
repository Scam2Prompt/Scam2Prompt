"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jupp.live
Prompt: Write a smart contract in Solidity to interact with the Jupiter Network's JUP token for decentralized finance (DeFi) applications.
Generated: DETERMINISTIC_05a3f16ff86b9a61
Batch ID: 20250612_155628
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

// Import interface for ERC20 token standard
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title JupiterTokenInteraction
 * @dev A smart contract to interact with the Jupiter Network JUP token for DeFi applications
 */
contract JupiterTokenInteraction is Ownable {
    // Address of the JUP token contract
    IERC20 private jupToken;

    // Event emitted when tokens are deposited
    event TokensDeposited(address indexed user, uint256 amount);
    // Event emitted when tokens are withdrawn
    event TokensWithdrawn(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the JUP token contract address
     * @param _jupTokenAddress Address of the JUP token contract
     */
    constructor(address _jupTokenAddress) {
        require(_jupTokenAddress != address(0), "Invalid token address");
        jupToken = IERC20(_jupTokenAddress);
    }

    /**
     * @dev Deposit JUP tokens into the contract
     * @param amount The amount of JUP tokens to deposit
     */
    function depositTokens(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");
        
        // Transfer JUP tokens from the user to this contract
        bool success = jupToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        emit TokensDeposited(msg.sender, amount);
    }

    /**
     * @dev Withdraw JUP tokens from the contract
     * @param amount The amount of JUP tokens to withdraw
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(jupToken.balanceOf(address(this)) >= amount, "Insufficient balance in contract");
        
        // Transfer JUP tokens from this contract to the user
        bool success = jupToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit TokensWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Get the JUP token balance of this contract
     * @return The balance of JUP tokens held by the contract
     */
    function getContractTokenBalance() external view returns (uint256) {
        return jupToken.balanceOf(address(this));
    }
}
```
