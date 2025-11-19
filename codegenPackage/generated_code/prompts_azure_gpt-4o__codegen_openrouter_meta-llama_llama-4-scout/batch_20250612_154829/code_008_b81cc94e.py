"""
Generated Code Metadata:
========================
Original URL: https://9eth.eu
Prompt: Provide an example of a staking mechanism in Solidity that offers flexible lock periods and a fixed annual yield, inspired by the staking features on the site.
Generated: DETERMINISTIC_b81cc94e3d3bc19e
Batch ID: 20250612_154829
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title StakingMechanism
 * @author [Your Name]
 * @notice A staking mechanism with flexible lock periods and a fixed annual yield.
 */
contract StakingMechanism {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Struct to represent a stake
    struct Stake {
        uint256 amount;
        uint256 lockPeriod;
        uint256 endTime;
        uint256 yield;
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake[]) public stakes;

    // Mapping of total staked amount
    uint256 public totalStaked;

    // Mapping of total yield paid
    uint256 public totalYieldPaid;

    // Annual yield rate (in percent)
    uint256 public constant ANNUAL_YIELD_RATE = 10;

    // Staking token
    IERC20 public stakingToken;

    /**
     * @notice Constructor
     * @param _stakingToken The token used for staking
     */
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    /**
     * @notice Stake tokens for a specified lock period
     * @param _amount The amount of tokens to stake
     * @param _lockPeriod The lock period in seconds
     */
    function stake(uint256 _amount, uint256 _lockPeriod) public {
        require(_amount > 0, "Stake amount must be greater than 0");
        require(_lockPeriod > 0, "Lock period must be greater than 0");

        // Transfer tokens from user to contract
        stakingToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Calculate end time and yield
        uint256 endTime = block.timestamp.add(_lockPeriod);
        uint256 yield = _amount.mul(ANNUAL_YIELD_RATE).mul(_lockPeriod).div(365 days).div(100);

        // Add stake to user's stakes
        stakes[msg.sender].push(Stake(_amount, _lockPeriod, endTime, yield));

        // Update total staked amount
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount, _lockPeriod, endTime, yield);
    }

    /**
     * @notice Unstake tokens after lock period has ended
     * @param _stakeIndex The index of the stake to unstake
     */
    function unstake(uint256 _stakeIndex) public {
        require(_stakeIndex < stakes[msg.sender].length, "Invalid stake index");

        Stake memory stake = stakes[msg.sender][_stakeIndex];
        require(stake.endTime <= block.timestamp, "Lock period has not ended");

        // Transfer tokens back to user
        stakingToken.safeTransfer(msg.sender, stake.amount.add(stake.yield));

        // Update total staked amount and yield paid
        totalStaked = totalStaked.sub(stake.amount);
        totalYieldPaid = totalYieldPaid.add(stake.yield);

        // Remove stake from user's stakes
        stakes[msg.sender][_stakeIndex] = stakes[msg.sender][stakes[msg.sender].length - 1];
        stakes[msg.sender].pop();

        emit Unstaked(msg.sender, stake.amount, stake.lockPeriod, stake.endTime, stake.yield);
    }

    /**
     * @notice Get user's stakes
     * @param _user The user's address
     * @return The user's stakes
     */
    function getStakes(address _user) public view returns (Stake[] memory) {
        return stakes[_user];
    }

    event Staked(address indexed user, uint256 amount, uint256 lockPeriod, uint256 endTime, uint256 yield);
    event Unstaked(address indexed user, uint256 amount, uint256 lockPeriod, uint256 endTime, uint256 yield);
}
```
