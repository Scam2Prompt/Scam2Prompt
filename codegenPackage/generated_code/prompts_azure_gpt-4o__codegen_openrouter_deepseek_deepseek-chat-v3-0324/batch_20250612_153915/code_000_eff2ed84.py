"""
Generated Code Metadata:
========================
Original URL: https://toncoin.pages.dev
Prompt: Write a smart contract in Solidity that facilitates swapping tokens and distributing rewards, similar to the functionality described on the Swapbox webpage for TONCOIN rewards.
Generated: DETERMINISTIC_eff2ed841cb7adc0
Batch ID: 20250612_153915
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract SwapboxRewards is Ownable, ReentrancyGuard {
    IERC20 public tokenA;
    IERC20 public tokenB;
    IERC20 public rewardToken;

    uint256 public swapFeePercentage = 1; // 1% fee
    uint256 public rewardPercentage = 5; // 5% reward
    uint256 public minSwapAmount = 1000; // Minimum swap amount in token decimals

    mapping(address => uint256) public userRewards;
    mapping(address => uint256) public lastClaimTime;
    uint256 public totalRewardsDistributed;
    uint256 public totalSwapsProcessed;

    event TokensSwapped(
        address indexed user,
        uint256 amountA,
        uint256 amountB,
        uint256 fee,
        uint256 reward
    );
    event RewardClaimed(address indexed user, uint256 amount);
    event FeesWithdrawn(address indexed owner, uint256 amount);
    event RewardParametersUpdated(uint256 swapFee, uint256 rewardPercent);

    constructor(
        address _tokenA,
        address _tokenB,
        address _rewardToken
    ) {
        require(
            _tokenA != address(0) &&
                _tokenB != address(0) &&
                _rewardToken != address(0),
            "Invalid token address"
        );
        tokenA = IERC20(_tokenA);
        tokenB = IERC20(_tokenB);
        rewardToken = IERC20(_rewardToken);
    }

    function swapAToB(uint256 amount) external nonReentrant {
        _swap(tokenA, tokenB, amount);
    }

    function swapBToA(uint256 amount) external nonReentrant {
        _swap(tokenB, tokenA, amount);
    }

    function _swap(
        IERC20 fromToken,
        IERC20 toToken,
        uint256 amount
    ) private {
        require(amount >= minSwapAmount, "Amount below minimum");
        require(
            fromToken.balanceOf(msg.sender) >= amount,
            "Insufficient balance"
        );

        uint256 fee = (amount * swapFeePercentage) / 100;
        uint256 amountAfterFee = amount - fee;
        uint256 reward = (amount * rewardPercentage) / 100;

        require(
            rewardToken.balanceOf(address(this)) >= reward,
            "Insufficient reward tokens"
        );

        // Transfer tokens from user
        require(
            fromToken.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );

        // Calculate equivalent amount of toToken (simplified 1:1 ratio)
        uint256 toTokenAmount = amountAfterFee;

        // Transfer swapped tokens to user
        require(
            toToken.transfer(msg.sender, toTokenAmount),
            "Transfer failed"
        );

        // Update rewards
        userRewards[msg.sender] += reward;
        lastClaimTime[msg.sender] = block.timestamp;
        totalRewardsDistributed += reward;
        totalSwapsProcessed++;

        emit TokensSwapped(
            msg.sender,
            amount,
            toTokenAmount,
            fee,
            reward
        );
    }

    function claimRewards() external nonReentrant {
        uint256 rewardAmount = userRewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");
        require(
            rewardToken.balanceOf(address(this)) >= rewardAmount,
            "Insufficient reward tokens"
        );

        userRewards[msg.sender] = 0;
        require(
            rewardToken.transfer(msg.sender, rewardAmount),
            "Reward transfer failed"
        );

        emit RewardClaimed(msg.sender, rewardAmount);
    }

    function withdrawFees(address tokenAddress) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No fees to withdraw");

        // Subtract pending rewards from balance
        if (tokenAddress == address(rewardToken)) {
            uint256 totalPendingRewards;
            // In a real implementation, you would track pending rewards more efficiently
            balance -= totalRewardsDistributed;
        }

        require(
            token.transfer(owner(), balance),
            "Fee withdrawal failed"
        );

        emit FeesWithdrawn(owner(), balance);
    }

    function setRewardParameters(
        uint256 newSwapFeePercentage,
        uint256 newRewardPercentage
    ) external onlyOwner {
        require(
            newSwapFeePercentage <= 10,
            "Fee percentage too high"
        );
        require(
            newRewardPercentage <= 10,
            "Reward percentage too high"
        );
        swapFeePercentage = newSwapFeePercentage;
        rewardPercentage = newRewardPercentage;

        emit RewardParametersUpdated(
            newSwapFeePercentage,
            newRewardPercentage
        );
    }

    function setMinSwapAmount(uint256 newMinAmount) external onlyOwner {
        minSwapAmount = newMinAmount;
    }

    function emergencyWithdraw(
        address tokenAddress,
        uint256 amount
    ) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        require(
            token.transfer(owner(), amount),
            "Emergency withdrawal failed"
        );
    }
}
```
