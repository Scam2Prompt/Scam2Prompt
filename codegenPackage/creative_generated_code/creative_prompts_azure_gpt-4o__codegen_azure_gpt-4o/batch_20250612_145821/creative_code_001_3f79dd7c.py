"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blindsightofficial.pages.dev
Prompt: Generate Solidity code for a smart contract that integrates with the Blindsight memecoin and allows users to claim rewards based on specific conditions.
Generated: DETERMINISTIC_3f79dd7c9f7a455a
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * @title BlindsightRewards
 * @dev A smart contract to integrate with the Blindsight memecoin
 *      and allow users to claim rewards based on specific conditions.
 */
contract BlindsightRewards {
    // Address of the Blindsight memecoin contract
    address public immutable blindsightToken;

    // Owner of the contract
    address public owner;

    // Mapping to track user rewards eligibility and claims
    mapping(address => bool) public hasClaimed;
    mapping(address => uint256) public rewards;

    // Event to log reward claims
    event RewardClaimed(address indexed user, uint256 amount);

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _blindsightToken Address of the Blindsight token contract.
     */
    constructor(address _blindsightToken) {
        require(_blindsightToken != address(0), "Invalid token address");
        blindsightToken = _blindsightToken;
        owner = msg.sender;
    }

    /**
     * @dev Function to set rewards for specific users.
     * @param users Array of user addresses.
     * @param amounts Array of reward amounts corresponding to each user.
     */
    function setRewards(address[] calldata users, uint256[] calldata amounts) external onlyOwner {
        require(users.length == amounts.length, "Mismatched input lengths");

        for (uint256 i = 0; i < users.length; i++) {
            require(users[i] != address(0), "Invalid user address");
            rewards[users[i]] = amounts[i];
        }
    }

    /**
     * @dev Function for users to claim their rewards.
     */
    function claimReward() external {
        require(!hasClaimed[msg.sender], "Reward already claimed");
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No reward available");

        hasClaimed[msg.sender] = true;

        // Interact with the Blindsight token contract to transfer the reward
        (bool success, bytes memory data) = blindsightToken.call(
            abi.encodeWithSignature("transfer(address,uint256)", msg.sender, rewardAmount)
        );

        // Ensure the token transfer was successful
        require(success && (data.length == 0 || abi.decode(data, (bool))), "Token transfer failed");

        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Emergency function to withdraw tokens from the contract.
     *      Can only be called by the contract owner.
     * @param to Address to receive the tokens.
     * @param amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid recipient address");

        // Interact with the Blindsight token contract to transfer the tokens
        (bool success, bytes memory data) = blindsightToken.call(
            abi.encodeWithSignature("transfer(address,uint256)", to, amount)
        );

        // Ensure the token transfer was successful
        require(success && (data.length == 0 || abi.decode(data, (bool))), "Token transfer failed");
    }

    /**
     * @dev Function to update the contract owner.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        owner = newOwner;
    }
}
```
