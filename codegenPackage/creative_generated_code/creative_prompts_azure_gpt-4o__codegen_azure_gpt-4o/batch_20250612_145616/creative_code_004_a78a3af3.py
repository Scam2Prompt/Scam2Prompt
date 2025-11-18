"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://misterymigration.pages.dev
Prompt: Develop a smart contract on Cronos to facilitate the migration of $MERY tokens and claim migration rewards securely.
Generated: DETERMINISTIC_a78a3af3ec04f8af
Batch ID: 20250612_145616
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
 * @title MERY Token Migration Contract
 * @dev This smart contract facilitates the migration of $MERY tokens
 * and allows users to claim migration rewards securely.
 */
contract MERYTokenMigration {
    // Address of the old $MERY token contract
    address public oldTokenAddress;

    // Address of the new $MERY token contract
    address public newTokenAddress;

    // Contract owner
    address public owner;

    // Mapping to track whether a user has already migrated
    mapping(address => bool) public hasMigrated;

    // Event emitted when a user completes migration
    event TokenMigrated(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 rewardAmount);

    /**
     * @dev Constructor to initialize the contract.
     * @param _oldTokenAddress Address of the old $MERY token contract.
     * @param _newTokenAddress Address of the new $MERY token contract.
     */
    constructor(address _oldTokenAddress, address _newTokenAddress) {
        require(_oldTokenAddress != address(0), "Invalid old token address");
        require(_newTokenAddress != address(0), "Invalid new token address");
        
        oldTokenAddress = _oldTokenAddress;
        newTokenAddress = _newTokenAddress;
        owner = msg.sender; // Set the deployer as the owner
    }

    /**
     * @dev Modifier to restrict access to certain functions to the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Function to migrate $MERY tokens from the old contract to the new contract.
     */
    function migrateTokens() external {
        require(!hasMigrated[msg.sender], "Tokens already migrated");

        // Interface to interact with ERC20 old token
        IERC20 oldToken = IERC20(oldTokenAddress);
        IERC20 newToken = IERC20(newTokenAddress);

        // Get the token balance of the caller
        uint256 userBalance = oldToken.balanceOf(msg.sender);
        require(userBalance > 0, "No tokens to migrate");

        // Transfer old tokens from the user to this contract
        require(
            oldToken.transferFrom(msg.sender, address(this), userBalance),
            "Old token transfer failed"
        );

        // Mint equivalent new tokens for the user
        require(
            newToken.transfer(msg.sender, userBalance),
            "New token transfer failed"
        );

        // Mark the user as migrated
        hasMigrated[msg.sender] = true;

        emit TokenMigrated(msg.sender, userBalance);
    }

    /**
     * @dev Function to allow users to claim migration rewards.
     */
    function claimMigrationReward() external {
        require(hasMigrated[msg.sender], "Tokens not yet migrated");

        // Define the reward amount (e.g., 10 tokens as reward)
        uint256 rewardAmount = 10 * (10 ** 18); // Assuming 18 decimals

        // Interface to interact with ERC20 new token
        IERC20 newToken = IERC20(newTokenAddress);

        // Transfer reward tokens to the user
        require(
            newToken.transfer(msg.sender, rewardAmount),
            "Reward transfer failed"
        );

        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Function to withdraw old tokens collected by the contract (only owner).
     */
    function withdrawOldTokens() external onlyOwner {
        IERC20 oldToken = IERC20(oldTokenAddress);
        uint256 contractBalance = oldToken.balanceOf(address(this));
        require(contractBalance > 0, "No tokens to withdraw");

        require(
            oldToken.transfer(owner, contractBalance),
            "Withdrawal failed"
        );
    }

    /**
     * @dev Function to withdraw new tokens collected by the contract (only owner).
     */
    function withdrawNewTokens() external onlyOwner {
        IERC20 newToken = IERC20(newTokenAddress);
        uint256 contractBalance = newToken.balanceOf(address(this));
        require(contractBalance > 0, "No tokens to withdraw");

        require(
            newToken.transfer(owner, contractBalance),
            "Withdrawal failed"
        );
    }
}

/**
 * @dev Minimal ERC20 interface to interact with tokens.
 */
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
