"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://diamond-7n0.pages.dev
Prompt: Provide an example of a Solidity smart contract that includes both staking functionality and a crypto swap feature, inspired by the utilities described for Diamond Coin.
Generated: DETERMINISTIC_871f8f9c481408eb
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
 * @title Staking and Crypto Swap Smart Contract
 * @dev This contract allows users to stake tokens and swap between two cryptocurrencies.
 */
contract StakingAndSwap {
    // ERC20 token interface
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
        function approve(address spender, uint256 amount) external returns (bool);
    }

    // Token addresses
    address public tokenA; // Staking token
    address public tokenB; // Swap token

    // Staking data
    struct Staker {
        uint256 stakedAmount; // Amount staked by the user
        uint256 stakingStart; // Timestamp when staking started
    }

    mapping(address => Staker) public stakers;
    uint256 public rewardRate = 100; // Reward rate per second per token
    bool public stakingPaused = false;

    // Swap rate
    uint256 public swapRate; // e.g., 1 TokenA = X TokenB

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event Swapped(address indexed user, uint256 amountIn, uint256 amountOut);

    constructor(address _tokenA, address _tokenB, uint256 _swapRate) {
        tokenA = _tokenA;
        tokenB = _tokenB;
        swapRate = _swapRate;
    }

    /**
     * @dev Stake a specified amount of tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(!stakingPaused, "Staking is currently paused");
        require(amount > 0, "Cannot stake zero amount");

        // Transfer tokens from the user to the contract
        IERC20(tokenA).transferFrom(msg.sender, address(this), amount);

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.stakedAmount += amount;
        if (staker.stakingStart == 0) {
            staker.stakingStart = block.timestamp;
        }

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens and claim rewards.
     */
    function unstake() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmount > 0, "No staked tokens to unstake");

        // Calculate rewards: (time staked) * (amount staked) * (reward rate)
        uint256 stakingDuration = block.timestamp - staker.stakingStart;
        uint256 reward = stakingDuration * staker.stakedAmount * rewardRate;

        uint256 amountToTransfer = staker.stakedAmount;
        staker.stakedAmount = 0;
        staker.stakingStart = 0;

        // Transfer staked tokens and rewards back to the user
        require(IERC20(tokenA).transfer(msg.sender, amountToTransfer), "Token transfer failed");
        // Optionally mint or distribute rewards here

        emit Unstaked(msg.sender, amountToTransfer, reward);
    }

    /**
     * @dev Swap TokenA for TokenB based on the fixed swap rate.
     * @param amount Amount of TokenA to swap.
     */
    function swap(uint256 amount) external {
        require(amount > 0, "Cannot swap zero amount");

        // Calculate the amount of TokenB to transfer
        uint256 amountOut = amount * swapRate;

        // Transfer TokenA from the user to the contract
        IERC20(tokenA).transferFrom(msg.sender, address(this), amount);

        // Transfer TokenB from the contract to the user
        require(IERC20(tokenB).transfer(msg.sender, amountOut), "Token transfer failed");

        emit Swapped(msg.sender, amount, amountOut);
    }

    /**
     * @dev Pause or resume staking functionality.
     * @param _paused Status to set for staking.
     */
    function setStakingPaused(bool _paused) external {
        // Only contract owner/modifier logic could be added here for security
        stakingPaused = _paused;
    }

    /**
     * @dev Update the swap rate.
     * @param _swapRate New swap rate.
     */
    function setSwapRate(uint256 _swapRate) external {
        // Only contract owner/modifier logic could be added here for security
        require(_swapRate > 0, "Swap rate must be greater than zero");
        swapRate = _swapRate;
    }
}
```
