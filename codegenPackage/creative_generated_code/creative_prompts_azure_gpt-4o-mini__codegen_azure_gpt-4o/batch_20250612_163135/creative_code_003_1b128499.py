"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zealy-io.github.io
Prompt: Develop a smart contract that allows users to provide liquidity to Zealy's liquidity pools and earn rewards in ORB tokens.
Generated: DETERMINISTIC_1b128499a9287848
Batch ID: 20250612_163135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, production-ready Solidity smart contract for the requested functionality:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title ZealyLiquidityPool
 * @dev Smart contract for providing liquidity to Zealy pools and earning rewards in ORB tokens.
 */
contract ZealyLiquidityPool {
    // Address of the ORB token contract
    address public orbToken;

    // Struct to track liquidity provider details
    struct LiquidityProvider {
        uint256 providedLiquidity; // Amount of liquidity provided by the user
        uint256 rewards;           // Rewards earned by the user
        uint256 lastUpdateTime;    // Last time rewards were updated
    }

    // Mapping of user addresses to their liquidity information
    mapping(address => LiquidityProvider) public liquidityProviders;

    // Total liquidity in the pool
    uint256 public totalLiquidity;

    // Reward rate (ORB tokens earned per second per unit of liquidity)
    uint256 public rewardRate;

    // Events
    event LiquidityProvided(address indexed user, uint256 amount);
    event LiquidityWithdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the ORB token address and reward rate.
     * @param _orbToken Address of the ORB token contract.
     * @param _rewardRate Reward rate (ORB tokens earned per second per unit of liquidity).
     */
    constructor(address _orbToken, uint256 _rewardRate) {
        require(_orbToken != address(0), "Invalid ORB token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        orbToken = _orbToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Modifier to update the user's rewards before executing a function.
     */
    modifier updateRewards(address _user) {
        if (liquidityProviders[_user].providedLiquidity > 0) {
            // Calculate rewards based on time elapsed and update user's rewards
            uint256 timeElapsed = block.timestamp - liquidityProviders[_user].lastUpdateTime;
            uint256 newRewards = timeElapsed * rewardRate * liquidityProviders[_user].providedLiquidity;
            liquidityProviders[_user].rewards += newRewards;
        }
        liquidityProviders[_user].lastUpdateTime = block.timestamp;
        _;
    }

    /**
     * @dev Function to provide liquidity to the pool.
     * @param _amount Amount of liquidity to provide (in Wei).
     */
    function provideLiquidity(uint256 _amount) external payable updateRewards(msg.sender) {
        require(_amount > 0, "Amount must be greater than zero");
        require(msg.value == _amount, "Ether value sent must match the provided amount");

        liquidityProviders[msg.sender].providedLiquidity += _amount;
        totalLiquidity += _amount;

        emit LiquidityProvided(msg.sender, _amount);
    }

    /**
     * @dev Function to withdraw liquidity from the pool.
     * @param _amount Amount of liquidity to withdraw (in Wei).
     */
    function withdrawLiquidity(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Amount must be greater than zero");
        require(liquidityProviders[msg.sender].providedLiquidity >= _amount, "Insufficient liquidity");

        liquidityProviders[msg.sender].providedLiquidity -= _amount;
        totalLiquidity -= _amount;

        payable(msg.sender).transfer(_amount);

        emit LiquidityWithdrawn(msg.sender, _amount);
    }

    /**
     * @dev Function to claim ORB token rewards earned by the user.
     */
    function claimRewards() external updateRewards(msg.sender) {
        uint256 rewards = liquidityProviders[msg.sender].rewards;
        require(rewards > 0, "No rewards available");

        liquidityProviders[msg.sender].rewards = 0;

        // Transfer ORB tokens to the user
        (bool success, ) = orbToken.call(
            abi.encodeWithSignature("transfer(address,uint256)", msg.sender, rewards)
        );
        require(success, "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Function to update the reward rate (only by the contract owner).
     * @param _newRewardRate New reward rate (ORB tokens earned per second per unit of liquidity).
     */
    function updateRewardRate(uint256 _newRewardRate) external {
        require(msg.sender == orbToken, "Only owner can update reward rate");
        require(_newRewardRate > 0, "Reward rate must be greater than zero");

        rewardRate = _newRewardRate;
    }
}
```

This contract assumes that ORB tokens follow the ERC-20 standard. Make sure you deploy and test this code in a test environment before deploying to production.
