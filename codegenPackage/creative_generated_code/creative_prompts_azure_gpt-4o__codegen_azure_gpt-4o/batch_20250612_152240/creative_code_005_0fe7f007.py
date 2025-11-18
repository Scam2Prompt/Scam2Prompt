"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swap-dogs.pages.dev
Prompt: Develop a smart contract for distributing $DOGS tokens as rewards to users based on specific criteria within the TON ecosystem.
Generated: DETERMINISTIC_0fe7f0073cbe6e12
Batch ID: 20250612_152240
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
 * @title RewardDistributor
 * @dev A smart contract for distributing $DOGS tokens as rewards to users based on specific criteria.
 */
contract RewardDistributor {
    // ERC20 token interface for $DOGS
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
        function allowance(address owner, address spender) external view returns (uint256);
        function approve(address spender, uint256 amount) external returns (bool);
    }

    // Address of the $DOGS token contract
    IERC20 public dogsToken;

    // Contract owner
    address public owner;

    // Mapping to store user reward eligibility
    mapping(address => uint256) public rewards;

    // Events for logging activities
    event RewardUpdated(address indexed user, uint256 rewardAmount);
    event RewardDistributed(address indexed user, uint256 rewardAmount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    /**
     * @dev Constructor sets the $DOGS token contract address and initializes the contract owner.
     * @param _dogsToken Address of the $DOGS token contract.
     */
    constructor(address _dogsToken) {
        require(_dogsToken != address(0), "Invalid token address");
        dogsToken = IERC20(_dogsToken);
        owner = msg.sender;
    }

    /**
     * @dev Updates reward criteria for a user.
     * @param user Address of the user.
     * @param rewardAmount Amount of $DOGS tokens to set as reward.
     */
    function updateReward(address user, uint256 rewardAmount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        rewards[user] = rewardAmount;
        emit RewardUpdated(user, rewardAmount);
    }

    /**
     * @dev Distributes rewards to a user based on eligibility.
     * @param user Address of the user.
     */
    function distributeReward(address user) external {
        require(user != address(0), "Invalid user address");
        uint256 rewardAmount = rewards[user];
        require(rewardAmount > 0, "No rewards available");
        require(dogsToken.balanceOf(address(this)) >= rewardAmount, "Insufficient token balance");

        // Transfer the reward to the user
        bool success = dogsToken.transfer(user, rewardAmount);
        require(success, "Token transfer failed");

        // Reset user's reward to prevent re-distribution
        rewards[user] = 0;
        emit RewardDistributed(user, rewardAmount);
    }

    /**
     * @dev Allows the owner to withdraw tokens from the contract.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(dogsToken.balanceOf(address(this)) >= amount, "Insufficient token balance");
        bool success = dogsToken.transfer(owner, amount);
        require(success, "Token transfer failed");
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
```
