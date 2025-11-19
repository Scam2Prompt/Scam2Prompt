"""
Generated Code Metadata:
========================
Original URL: https://sun-dv6.pages.dev
Prompt: "Create a SunSwap V2 farm with SUN-USDT LP and APY UP TO 21.51%, using Solidity and TRON blockchain."
Generated: DETERMINISTIC_564be4f505b1dc3f
Batch ID: 20250622_210856
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/SafeERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title SunSwap V2 Farm contract
 * @author [Your Name]
 * @notice This contract represents a farm for SUN-USDT LP tokens with APY up to 21.51%
 * @dev This contract uses TRON blockchain and Solidity language
 */
contract SunSwapV2Farm is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for ERC20;

    // Constants
    uint256 public constant APY = 2151; // 21.51%
    uint256 public constant DURATION = 30 days; // 30 days

    // Variables
    address public sunTokenAddress;
    address public usdtTokenAddress;
    address public lpTokenAddress;
    uint256 public startTime;
    uint256 public endTime;
    uint256 public totalStaked;
    mapping(address => uint256) public userStakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @notice Constructor
     * @param _sunTokenAddress SUN token address
     * @param _usdtTokenAddress USDT token address
     * @param _lpTokenAddress SUN-USDT LP token address
     * @param _startTime Start time of the farm
     */
    constructor(
        address _sunTokenAddress,
        address _usdtTokenAddress,
        address _lpTokenAddress,
        uint256 _startTime
    ) public {
        sunTokenAddress = _sunTokenAddress;
        usdtTokenAddress = _usdtTokenAddress;
        lpTokenAddress = _lpTokenAddress;
        startTime = _startTime;
        endTime = startTime.add(DURATION);
    }

    /**
     * @notice Stake LP tokens
     * @param amount Amount of LP tokens to stake
     */
    function stake(uint256 amount) public {
        require(msg.sender != address(0), "Invalid address");
        require(amount > 0, "Invalid amount");
        require(block.timestamp >= startTime, "Farm not started");

        ERC20(lpTokenAddress).safeTransferFrom(msg.sender, address(this), amount);
        userStakes[msg.sender] = userStakes[msg.sender].add(amount);
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake LP tokens
     * @param amount Amount of LP tokens to unstake
     */
    function unstake(uint256 amount) public {
        require(msg.sender != address(0), "Invalid address");
        require(amount > 0, "Invalid amount");
        require(userStakes[msg.sender] >= amount, "Insufficient stake");

        userStakes[msg.sender] = userStakes[msg.sender].sub(amount);
        totalStaked = totalStaked.sub(amount);
        ERC20(lpTokenAddress).safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Claim rewards
     */
    function claimReward() public {
        require(msg.sender != address(0), "Invalid address");
        require(block.timestamp >= endTime, "Farm not ended");

        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No reward");

        // Transfer reward to user
        ERC20(sunTokenAddress).safeTransfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @notice Calculate reward for a user
     * @param user User address
     * @return Reward amount
     */
    function calculateReward(address user) internal view returns (uint256) {
        uint256 stakeDuration = block.timestamp.sub(startTime);
        uint256 apyReward = APY.mul(stakeDuration).div(10000);
        uint256 userStake = userStakes[user];
        return userStake.mul(apyReward).div(100);
    }

    /**
     * @notice Update farm end time
     * @param _endTime New end time
     */
    function updateEndTime(uint256 _endTime) public onlyOwner {
        require(_endTime > startTime, "Invalid end time");
        endTime = _endTime;
    }
}
```
