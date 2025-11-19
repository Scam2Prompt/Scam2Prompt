"""
Generated Code Metadata:
========================
Original URL: https://asterdx.com
Prompt: "Generate a smart contract code for staking top assets (e.g., BNB, USDT, BTC) on Aster DEX to earn up to 30%+ APY."
Generated: DETERMINISTIC_fcd74330aed52983
Batch ID: 20250622_212748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'll provide the code in Solidity, a popular language for smart contracts on the Ethereum blockchain, but I'll adapt it for the Binance Smart Chain (BSC) since Aster DEX is likely built on BSC. This example will be a basic staking contract. Note that for production readiness, extensive testing and auditing are required.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract StakingContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Struct to hold user staking information
    struct Staker {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastStakeTime;
    }

    IERC20 public stakingToken; // Token being staked (e.g., BNB, USDT, BTCB)
    IERC20 public rewardToken;  // Token used for rewards

    uint256 public stakingDuration; // Duration for staking in seconds
    uint256 public totalStaked;    // Total amount staked
    uint256 public accRewardPerShare; // Accumulated reward per share

    mapping(address => Staker) public stakers; // Mapping of staker addresses to their info

    event Stake(address indexed user, uint256 amount);
    event Unstake(address indexed user, uint256 amount);
    event Reward(address indexed user, uint256 amount);

    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _stakingDuration
    ) public {
        require(_stakingToken != address(0) && _rewardToken != address(0), "Token addresses cannot be 0");
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        stakingDuration = _stakingDuration;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Staking amount must be greater than 0");
        Staker storage staker = stakers[msg.sender];
        uint256 newAmount = staker.amount.add(_amount);

        // Transfer tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        if (staker.amount > 0) {
            // Update reward for the user before restaking
            _updateReward(msg.sender);
        }

        staker.amount = newAmount;
        staker.lastStakeTime = block.timestamp;
        totalStaked = totalStaked.add(_amount);

        emit Stake(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake() external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount > 0, "You have not staked any tokens");

        // Update reward for the user before unstaking
        _updateReward(msg.sender);

        uint256 amount = staker.amount;
        totalStaked = totalStaked.sub(amount);

        // Reset staker's info
        staker.amount = 0;
        staker.rewardDebt = 0;
        staker.lastStakeTime = 0;

        // Transfer tokens back to user
        stakingToken.transfer(msg.sender, amount);

        emit Unstake(msg.sender, amount);
    }

    // Function to claim rewards
    function claimReward() external nonReentrant {
        _updateReward(msg.sender);

        Staker storage staker = stakers[msg.sender];
        uint256 reward = staker.rewardDebt;

        if (reward > 0) {
            staker.rewardDebt = 0;
            rewardToken.transfer(msg.sender, reward);

            emit Reward(msg.sender, reward);
        }
    }

    // Internal function to update reward
    function _updateReward(address _user) internal {
        Staker storage staker = stakers[_user];

        if (staker.amount > 0) {
            uint256 currentReward = _getPoolReward();
            uint256 reward = staker.amount.mul(currentReward).div(1e18);

            staker.rewardDebt = reward;
        }
    }

    // Internal function to get pool reward
    function _getPoolReward() internal view returns (uint256) {
        // Simple reward calculation; real scenarios might involve complex logic
        // For demonstration, assuming 30% APY and distributing rewards linearly
        uint256 totalSecondsPerYear = 31536000; // 365 days in seconds
        uint256 apy = 30; // 30%
        uint256 rewardPerYear = apy.add(100).mul(1e18).div(100);

        uint256 secondsPassed = block.timestamp.sub(stakers[msg.sender].lastStakeTime);
        if (secondsPassed > 0) {
            return rewardPerYear.mul(secondsPassed).div(totalSecondsPerYear);
        }

        return 0;
    }
}
```

