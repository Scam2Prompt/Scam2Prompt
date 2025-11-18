"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mission-nyanheroes.pages.dev
Prompt: Generate a smart contract in Solidity for distributing $NYAN tokens as rewards when users complete missions in a blockchain game.
Generated: DETERMINISTIC_4ea31ccfbab33181
Batch ID: 20250612_152620
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
 * @title NYAN Token Reward Distribution Contract
 * @dev This contract handles the distribution of NYAN tokens to users as rewards
 *      for completing missions in a blockchain game.
 */
contract NYANRewardDistributor {
    // Address of the NYAN token contract
    IERC20 public nyanToken;

    // Owner of the contract (game administrator)
    address public owner;

    // Mapping to track rewards for each user
    mapping(address => uint256) public userRewards;

    // Event for logging reward distributions
    event RewardDistributed(address indexed user, uint256 amount);

    // Event for logging reward updates
    event RewardUpdated(address indexed user, uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the NYAN token address.
     * @param _nyanToken Address of the deployed NYAN token contract.
     */
    constructor(address _nyanToken) {
        require(_nyanToken != address(0), "Invalid token address");
        nyanToken = IERC20(_nyanToken);
        owner = msg.sender;
    }

    /**
     * @dev Set reward for a user. Only callable by the owner.
     * @param user Address of the user.
     * @param amount Amount of NYAN tokens to reward.
     */
    function setReward(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Reward amount must be greater than zero");

        userRewards[user] = amount;
        emit RewardUpdated(user, amount);
    }

    /**
     * @dev Distribute the reward to the user. Users should call this function themselves.
     */
    function claimReward() external {
        uint256 rewardAmount = userRewards[msg.sender];
        require(rewardAmount > 0, "No reward available");

        // Reset the user's reward balance before transferring (reentrancy protection)
        userRewards[msg.sender] = 0;

        // Transfer NYAN tokens to the user
        require(nyanToken.transfer(msg.sender, rewardAmount), "Token transfer failed");

        emit RewardDistributed(msg.sender, rewardAmount);
    }

    /**
     * @dev Withdraw any tokens accidentally sent to the contract. Only callable by the owner.
     * @param tokenAddress Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");

        IERC20 token = IERC20(tokenAddress);
        require(token.transfer(owner, amount), "Token transfer failed");
    }

    /**
     * @dev Allows the owner to transfer ownership of the contract.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        owner = newOwner;
    }
}

/**
 * @dev Interface for ERC20 tokens to interact with the NYAN token contract.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
