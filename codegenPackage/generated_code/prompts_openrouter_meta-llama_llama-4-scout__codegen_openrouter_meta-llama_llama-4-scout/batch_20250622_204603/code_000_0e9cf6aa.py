"""
Generated Code Metadata:
========================
Original URL: https://layerzero-e32.pages.dev
Prompt: Write a smart contract in Solidity to calculate total value locked and APY for a cryptocurrency campaign on Ethereum, similar to Puffy's Crunchy Carrot Quest.
Generated: DETERMINISTIC_0e9cf6aa49969d0b
Batch ID: 20250622_204603
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
import "@openzeppelin/contracts/math/SafeMath.sol";

/**
 * @title CampaignContract
 * @author [Your Name]
 * @notice Calculates total value locked and APY for a cryptocurrency campaign
 */
contract CampaignContract {
    using SafeMath for uint256;

    // Mapping of user deposits
    mapping (address => uint256) public deposits;

    // Mapping of user rewards
    mapping (address => uint256) public rewards;

    // Total value locked
    uint256 public totalValueLocked;

    // Campaign start time
    uint256 public startTime;

    // Campaign end time
    uint256 public endTime;

    // APY (Annual Percentage Yield)
    uint256 public apy;

    // Reward token
    IERC20 public rewardToken;

    // Deposit token
    IERC20 public depositToken;

    /**
     * @notice Constructor
     * @param _rewardToken Address of the reward token
     * @param _depositToken Address of the deposit token
     * @param _startTime Campaign start time
     * @param _endTime Campaign end time
     * @param _apy APY (Annual Percentage Yield)
     */
    constructor(
        address _rewardToken,
        address _depositToken,
        uint256 _startTime,
        uint256 _endTime,
        uint256 _apy
    ) public {
        rewardToken = IERC20(_rewardToken);
        depositToken = IERC20(_depositToken);
        startTime = _startTime;
        endTime = _endTime;
        apy = _apy;
    }

    /**
     * @notice Deposit tokens
     * @param _amount Amount to deposit
     */
    function deposit(uint256 _amount) public {
        require(depositToken.balanceOf(msg.sender) >= _amount, "Insufficient balance");
        require(block.timestamp >= startTime, "Campaign not started");

        deposits[msg.sender] = deposits[msg.sender].add(_amount);
        totalValueLocked = totalValueLocked.add(_amount);

        // Transfer deposit tokens to contract
        depositToken.transferFrom(msg.sender, address(this), _amount);
    }

    /**
     * @notice Withdraw tokens
     * @param _amount Amount to withdraw
     */
    function withdraw(uint256 _amount) public {
        require(deposits[msg.sender] >= _amount, "Insufficient deposit");
        require(block.timestamp >= endTime, "Campaign not ended");

        deposits[msg.sender] = deposits[msg.sender].sub(_amount);
        totalValueLocked = totalValueLocked.sub(_amount);

        // Transfer deposit tokens to user
        depositToken.transfer(msg.sender, _amount);
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() public {
        require(block.timestamp >= endTime, "Campaign not ended");

        uint256 reward = calculateReward(msg.sender);
        rewards[msg.sender] = reward;

        // Transfer reward tokens to user
        rewardToken.transfer(msg.sender, reward);
    }

    /**
     * @notice Calculate reward for a user
     * @param _user User address
     * @return Reward amount
     */
    function calculateReward(address _user) internal view returns (uint256) {
        uint256 deposit = deposits[_user];
        uint256 duration = endTime.sub(startTime);
        uint256 reward = deposit.mul(apy).mul(duration).div(365 days).div(100);

        return reward;
    }

    /**
     * @notice Calculate APY
     * @return APY
     */
    function calculateApy() public view returns (uint256) {
        return apy;
    }

    /**
     * @notice Calculate total value locked
     * @return Total value locked
     */
    function calculateTotalValueLocked() public view returns (uint256) {
        return totalValueLocked;
    }
}
```
