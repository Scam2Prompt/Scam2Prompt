"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wwwasterdex.com
Prompt: Develop a smart contract that interacts with Aster DEX to automate staking and reward distribution for supported assets like BTC and CAKE.
Generated: DETERMINISTIC_47d8b166505406b5
Batch ID: 20250612_154021
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
 * @title Automated Staking and Reward Distribution Contract
 * @dev This contract interacts with Aster DEX to automate staking and reward distribution 
 *      for supported assets like BTC and CAKE.
 * @author Developer
 */

interface IAsterDEX {
    function stake(address token, uint256 amount) external;
    function unstake(address token, uint256 amount) external;
    function claimRewards(address token) external returns (uint256);
    function getRewardsBalance(address token, address user) external view returns (uint256);
}

interface IERC20 {
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract AutomatedStaking {
    address public owner; // Owner of the contract
    IAsterDEX public asterDEX; // Instance of the Aster DEX contract

    event Staked(address indexed user, address indexed token, uint256 amount);
    event Unstaked(address indexed user, address indexed token, uint256 amount);
    event RewardsDistributed(address indexed user, address indexed token, uint256 rewardAmount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    constructor(address _asterDEX) {
        require(_asterDEX != address(0), "Invalid AsterDEX address");
        owner = msg.sender;
        asterDEX = IAsterDEX(_asterDEX);
    }

    /**
     * @dev Stake tokens into Aster DEX
     * @param token Address of the ERC20 token to stake
     * @param amount Amount of tokens to stake
     */
    function stakeTokens(address token, uint256 amount) external {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");

        IERC20(token).transferFrom(msg.sender, address(this), amount); // Transfer tokens to contract
        IERC20(token).approve(address(asterDEX), amount); // Approve Aster DEX to spend tokens

        asterDEX.stake(token, amount); // Stake tokens via Aster DEX
        emit Staked(msg.sender, token, amount);
    }

    /**
     * @dev Unstake tokens from Aster DEX
     * @param token Address of the ERC20 token to unstake
     * @param amount Amount of tokens to unstake
     */
    function unstakeTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");

        asterDEX.unstake(token, amount); // Unstake tokens via Aster DEX
        IERC20(token).transfer(msg.sender, amount); // Transfer tokens back to the owner

        emit Unstaked(msg.sender, token, amount);
    }

    /**
     * @dev Claim rewards for a token and distribute them
     * @param token Address of the ERC20 token for which rewards are claimed
     */
    function claimAndDistributeRewards(address token) external onlyOwner {
        require(token != address(0), "Invalid token address");

        uint256 rewardAmount = asterDEX.claimRewards(token); // Claim rewards from Aster DEX
        require(rewardAmount > 0, "No rewards available to claim");

        IERC20(token).transfer(msg.sender, rewardAmount); // Transfer rewards to the owner

        emit RewardsDistributed(msg.sender, token, rewardAmount);
    }

    /**
     * @dev View reward balance available for a token
     * @param token Address of the ERC20 token
     * @return uint256 Reward balance available
     */
    function viewRewardBalance(address token) external view returns (uint256) {
        return asterDEX.getRewardsBalance(token, address(this));
    }

    /**
     * @dev Transfer ownership of the contract to a new address
     * @param newOwner Address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        owner = newOwner;
    }
}
```
