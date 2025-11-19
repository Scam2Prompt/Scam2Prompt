"""
Generated Code Metadata:
========================
Original URL: https://bonk-layer-auth.pages.dev
Prompt: Generate a Solidity code snippet to create a smart contract that utilizes Bonk Coin as a utility token for a gaming application on the Solana blockchain.
Generated: DETERMINISTIC_0724e475a3c83733
Batch ID: 20250622_204722
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

/**
 * @title BonkGameContract
 * @dev A smart contract for a gaming application that utilizes Bonk Coin as a utility token.
 * Note: This contract assumes Bonk Coin is an ERC-20 token deployed on Ethereum-compatible chains.
 * Solana integration would require additional bridging mechanisms, which are outside the scope of this contract.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract BonkGameContract {
    // Address of the Bonk Coin ERC-20 token contract
    IERC20 public bonkToken;

    // Owner of the contract
    address public owner;

    // Event emitted when tokens are spent in the game
    event TokensSpent(address indexed player, uint256 amount);

    // Event emitted when tokens are rewarded to a player
    event TokensRewarded(address indexed player, uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the Bonk Coin token address.
     * @param _bonkToken Address of the Bonk Coin ERC-20 token contract.
     */
    constructor(address _bonkToken) {
        require(_bonkToken != address(0), "Invalid token address");
        bonkToken = IERC20(_bonkToken);
        owner = msg.sender;
    }

    /**
     * @dev Function to spend Bonk tokens in the game.
     * @param amount Amount of Bonk tokens to spend.
     */
    function spendTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(bonkToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from the player to the contract
        bool success = bonkToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        emit TokensSpent(msg.sender, amount);
    }

    /**
     * @dev Function to reward Bonk tokens to a player.
     * @param player Address of the player to reward.
     * @param amount Amount of Bonk tokens to reward.
     */
    function rewardTokens(address player, uint256 amount) external onlyOwner {
        require(player != address(0), "Invalid player address");
        require(amount > 0, "Amount must be greater than zero");
        require(bonkToken.balanceOf(address(this)) >= amount, "Insufficient contract token balance");

        // Transfer tokens from the contract to the player
        bool success = bonkToken.transfer(player, amount);
        require(success, "Token transfer failed");

        emit TokensRewarded(player, amount);
    }

    /**
     * @dev Function to withdraw Bonk tokens from the contract.
     * @param amount Amount of Bonk tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(bonkToken.balanceOf(address(this)) >= amount, "Insufficient contract token balance");

        // Transfer tokens from the contract to the owner
        bool success = bonkToken.transfer(owner, amount);
        require(success, "Token transfer failed");
    }

    /**
     * @dev Function to update the Bonk Coin token address.
     * @param _bonkToken New address of the Bonk Coin ERC-20 token contract.
     */
    function updateTokenAddress(address _bonkToken) external onlyOwner {
        require(_bonkToken != address(0), "Invalid token address");
        bonkToken = IERC20(_bonkToken);
    }
}
```
