"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-humanizedai.web.app
Prompt: How can I implement a staking mechanism for HMZ tokens that allows users to lock their tokens for different durations and earn weekly yields?
Generated: DETERMINISTIC_acd734c9bd284665
Batch ID: 20250612_161353
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract HMZStaking {
    using SafeMath for uint256;

    // Struct to hold staking information for each user
    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 duration;
        uint256 yield;
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Token to be staked
    IERC20 public hmzToken;

    // Weekly yield percentage (e.g., 5% would be 5 * 10^18 / 100)
    uint256 public weeklyYieldPercentage;

    // Events
    event Staked(address indexed user, uint256 amount, uint256 duration);
    event Unstaked(address indexed user, uint256 amount, uint256 yield);
    
    // Constructor to set the HMZ token address and yield percentage
    constructor(IERC20 _hmzToken, uint256 _weeklyYieldPercentage) {
        require(address(_hmzToken) != address(0), "Invalid token address");
        require(_weeklyYieldPercentage > 0, "Yield percentage must be greater than 0");
        
        hmzToken = _hmzToken;
        weeklyYieldPercentage = _weeklyYieldPercentage;
    }

    // Function to stake HMZ tokens for a specified duration
    function stake(uint256 amount, uint256 duration) external {
        require(amount > 0, "Amount must be greater than 0");
        require(duration > 0, "Duration must be greater than 0");
        require(stakes[msg.sender].amount == 0, "Already staking");

        // Transfer HMZ tokens from user to this contract
        require(hmzToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        stakes[msg.sender] = Stake({
            amount: amount,
            startTime: block.timestamp,
            duration: duration,
            yield: calculateYield(amount, duration)
        });

        emit Staked(msg.sender, amount, duration);
    }

    // Function to calculate yield based on amount and duration
    function calculateYield(uint256 amount, uint256 duration) internal view returns (uint256) {
        // Calculate the yield for the entire staking duration
        return amount.mul(weeklyYieldPercentage).mul(duration).div(100).div(1 weeks);
    }

    // Function to unstake tokens and claim yield
    function unstake() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No active stake");
        require(block.timestamp >= userStake.startTime + userStake.duration, "Stake is still locked");

        // Calculate total yield
        uint256 totalYield = userStake.yield;
        
        // Reset the stake for the user
        delete stakes[msg.sender];

        // Transfer the original staked amount and yield back to the user
        require(hmzToken.transfer(msg.sender, userStake.amount.add(totalYield)), "Token transfer failed");

        emit Unstaked(msg.sender, userStake.amount, totalYield);
    }
}
```
