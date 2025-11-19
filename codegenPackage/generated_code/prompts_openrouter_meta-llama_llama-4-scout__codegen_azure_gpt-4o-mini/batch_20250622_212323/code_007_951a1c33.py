"""
Generated Code Metadata:
========================
Original URL: https://usual-portal.web.app
Prompt: Write a Solidity code to implement a 4-year cash flow scarcity advantage for a token, similar to Usual's mechanism.
Generated: DETERMINISTIC_951a1c335e597d77
Batch ID: 20250622_212323
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CashFlowScarcityToken
 * @dev A token with a 4-year cash flow scarcity advantage mechanism.
 */
contract CashFlowScarcityToken is ERC20, Ownable {
    // Duration of the scarcity advantage in seconds (4 years)
    uint256 public constant SCARCITY_DURATION = 4 * 365 days;

    // Timestamp when the scarcity advantage starts
    uint256 public scarcityStartTime;

    // Total supply of the token
    uint256 private _totalSupply;

    // Mapping to track the amount of tokens locked for scarcity
    mapping(address => uint256) private _lockedTokens;

    // Event emitted when tokens are locked
    event TokensLocked(address indexed account, uint256 amount);

    // Event emitted when tokens are unlocked
    event TokensUnlocked(address indexed account, uint256 amount);

    /**
     * @dev Constructor that initializes the token with a name and symbol.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        scarcityStartTime = block.timestamp;
    }

    /**
     * @dev Override the transfer function to implement the scarcity mechanism.
     * @param recipient The address to receive the tokens.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating success.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(block.timestamp >= scarcityStartTime + SCARCITY_DURATION, "Tokens are locked during scarcity period");
        return super.transfer(recipient, amount);
    }

    /**
     * @dev Override the transferFrom function to implement the scarcity mechanism.
     * @param sender The address sending the tokens.
     * @param recipient The address to receive the tokens.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating success.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(block.timestamp >= scarcityStartTime + SCARCITY_DURATION, "Tokens are locked during scarcity period");
        return super.transferFrom(sender, recipient, amount);
    }

    /**
     * @dev Function to lock tokens for the scarcity advantage.
     * @param amount The amount of tokens to lock.
     */
    function lockTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to lock");

        _lockedTokens[msg.sender] += amount;
        _totalSupply += amount;

        emit TokensLocked(msg.sender, amount);
    }

    /**
     * @dev Function to unlock tokens after the scarcity period.
     */
    function unlockTokens() external onlyOwner {
        require(block.timestamp >= scarcityStartTime + SCARCITY_DURATION, "Tokens are still locked");

        uint256 amount = _lockedTokens[msg.sender];
        require(amount > 0, "No tokens to unlock");

        _lockedTokens[msg.sender] = 0;
        _totalSupply -= amount;

        emit TokensUnlocked(msg.sender, amount);
    }

    /**
     * @dev Function to get the amount of locked tokens for an account.
     * @param account The address of the account.
     * @return The amount of locked tokens.
     */
    function getLockedTokens(address account) external view returns (uint256) {
        return _lockedTokens[account];
    }

    /**
     * @dev Function to get the total supply of locked tokens.
     * @return The total supply of locked tokens.
     */
    function totalLockedSupply() external view returns (uint256) {
        return _totalSupply;
    }
}
```
