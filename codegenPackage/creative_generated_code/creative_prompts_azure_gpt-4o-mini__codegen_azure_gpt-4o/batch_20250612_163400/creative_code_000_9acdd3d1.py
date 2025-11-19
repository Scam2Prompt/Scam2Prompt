"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grooveup.pages.dev
Prompt: How can I implement a smart contract for a decentralized music streaming service that rewards fans with $GROOVE tokens for streaming and sharing music?
Generated: DETERMINISTIC_9acdd3d15dec7ec5
Batch ID: 20250612_163400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title MusicStreamingRewards
 * @dev A smart contract for a decentralized music streaming service that rewards users with $GROOVE tokens.
 */
contract MusicStreamingRewards {
    // Token contract interface
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // $GROOVE Token contract address (should be updated with the correct deployed token address)
    IERC20 public grooveToken;

    // Owner address
    address public owner;

    // Mapping to track user rewards
    mapping(address => uint256) public userRewards;

    // Events
    event Streamed(address indexed user, uint256 reward);
    event Shared(address indexed user, uint256 reward);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor
    constructor(address _grooveTokenAddress) {
        require(_grooveTokenAddress != address(0), "Invalid token address");
        owner = msg.sender;
        grooveToken = IERC20(_grooveTokenAddress);
    }

    /**
     * @dev Rewards a user for streaming music.
     * @param user The address of the user.
     * @param rewardAmount The amount of $GROOVE tokens to reward.
     */
    function rewardForStreaming(address user, uint256 rewardAmount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(rewardAmount > 0, "Reward must be greater than zero");
        userRewards[user] += rewardAmount;
        emit Streamed(user, rewardAmount);
    }

    /**
     * @dev Rewards a user for sharing music.
     * @param user The address of the user.
     * @param rewardAmount The amount of $GROOVE tokens to reward.
     */
    function rewardForSharing(address user, uint256 rewardAmount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(rewardAmount > 0, "Reward must be greater than zero");
        userRewards[user] += rewardAmount;
        emit Shared(user, rewardAmount);
    }

    /**
     * @dev Allows users to claim their $GROOVE token rewards.
     */
    function claimRewards() external {
        uint256 amount = userRewards[msg.sender];
        require(amount > 0, "No rewards to claim");
        require(grooveToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        userRewards[msg.sender] = 0; // Reset user rewards
        require(grooveToken.transfer(msg.sender, amount), "Token transfer failed");
        
        emit RewardsClaimed(msg.sender, amount);
    }

    /**
     * @dev Allows the owner to withdraw excess $GROOVE tokens from the contract.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawExcessTokens(uint256 amount) external onlyOwner {
        require(grooveToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        require(grooveToken.transfer(owner, amount), "Token transfer failed");
    }

    /**
     * @dev Updates the $GROOVE token contract address (restricted to owner).
     * @param _grooveTokenAddress The new token contract address.
     */
    function updateTokenAddress(address _grooveTokenAddress) external onlyOwner {
        require(_grooveTokenAddress != address(0), "Invalid token address");
        grooveToken = IERC20(_grooveTokenAddress);
    }
}
```
