"""
Generated Code Metadata:
========================
Original URL: https://stellarxdao.org
Prompt: Create a smart contract that automates the XLM airdrop event on StellarX, distributing rewards based on on-chain activity.
Generated: DETERMINISTIC_d4449a62e33bccfa
Batch ID: 20250622_212513
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
 * @title XLM Airdrop Smart Contract
 * @dev This contract automates the distribution of XLM rewards based on on-chain activity.
 * Note: This contract is designed for the Ethereum Virtual Machine (EVM) and assumes wrapped XLM (WXLM) tokens.
 */

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract XLMAirdrop {
    // Address of the WXLM token contract
    IERC20 public wXLM;

    // Owner of the contract
    address public owner;

    // Mapping to store user activity scores
    mapping(address => uint256) public activityScores;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 rewardAmount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _wXLM Address of the WXLM token contract.
     */
    constructor(address _wXLM) {
        require(_wXLM != address(0), "Invalid WXLM token address");
        wXLM = IERC20(_wXLM);
        owner = msg.sender;
    }

    /**
     * @dev Function to update user activity scores.
     * @param users Array of user addresses.
     * @param scores Array of corresponding activity scores.
     */
    function updateActivityScores(address[] calldata users, uint256[] calldata scores) external onlyOwner {
        require(users.length == scores.length, "Users and scores length mismatch");

        for (uint256 i = 0; i < users.length; i++) {
            activityScores[users[i]] = scores[i];
        }
    }

    /**
     * @dev Function to distribute rewards based on activity scores.
     * @param users Array of user addresses to distribute rewards to.
     * @param totalRewardPool Total amount of WXLM tokens available for distribution.
     */
    function distributeRewards(address[] calldata users, uint256 totalRewardPool) external onlyOwner {
        require(users.length > 0, "No users provided");
        require(totalRewardPool > 0, "Reward pool must be greater than zero");
        require(wXLM.balanceOf(address(this)) >= totalRewardPool, "Insufficient WXLM balance in contract");

        // Calculate total activity score
        uint256 totalActivityScore = 0;
        for (uint256 i = 0; i < users.length; i++) {
            totalActivityScore += activityScores[users[i]];
        }

        require(totalActivityScore > 0, "Total activity score must be greater than zero");

        // Distribute rewards proportionally based on activity scores
        for (uint256 i = 0; i < users.length; i++) {
            uint256 userScore = activityScores[users[i]];
            uint256 rewardAmount = (userScore * totalRewardPool) / totalActivityScore;

            if (rewardAmount > 0) {
                require(wXLM.transfer(users[i], rewardAmount), "Reward transfer failed");
                emit RewardsDistributed(users[i], rewardAmount);
            }
        }
    }

    /**
     * @dev Function to withdraw WXLM tokens from the contract.
     * @param amount Amount of WXLM tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(wXLM.balanceOf(address(this)) >= amount, "Insufficient WXLM balance in contract");

        require(wXLM.transfer(owner, amount), "Withdraw transfer failed");
    }
}
```
