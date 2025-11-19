"""
Generated Code Metadata:
========================
Original URL: https://rocket-pool.xyz
Prompt: Write a smart contract in Solidity that integrates Rocket Pool's rETH token into a DeFi protocol, allowing users to stake rETH and earn rewards. Include functionality for calculating rETH/ETH exchange rates based on Rocket Pool's reward distribution mechanism.
Generated: DETERMINISTIC_06d5493fe64c50a2
Batch ID: 20250612_153821
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
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title rETH Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake rETH and earn rewards.
 */
contract rETHStakingContract is Ownable {
    using SafeMath for uint256;

    // rETH token contract
    IERC20 public rETH;

    // ETH token contract
    IERC20 public ETH;

    // Rocket Pool's reward distribution mechanism contract
    address public rocketPoolContract;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward balances
    mapping(address => uint256) public rewardBalances;

    // rETH/ETH exchange rate
    uint256 public exchangeRate;

    /**
     * @dev Constructor
     * @param _rETH rETH token contract address
     * @param _ETH ETH token contract address
     * @param _rocketPoolContract Rocket Pool's reward distribution mechanism contract address
     */
    constructor(address _rETH, address _ETH, address _rocketPoolContract) public {
        require(_rETH != address(0), "rETH token contract address is zero");
        require(_ETH != address(0), "ETH token contract address is zero");
        require(_rocketPoolContract != address(0), "Rocket Pool contract address is zero");

        rETH = IERC20(_rETH);
        ETH = IERC20(_ETH);
        rocketPoolContract = _rocketPoolContract;

        exchangeRate = 1 ether; // Initial exchange rate: 1 rETH = 1 ETH
    }

    /**
     * @dev Stake rETH
     * @param _amount Amount of rETH to stake
     */
    function stake(uint256 _amount) public {
        require(_amount > 0, "Stake amount is zero");
        require(rETH.balanceOf(msg.sender) >= _amount, "Insufficient rETH balance");

        // Transfer rETH from user to contract
        rETH.transferFrom(msg.sender, address(this), _amount);

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);

        // Calculate and update reward balance
        uint256 reward = calculateReward(_amount);
        rewardBalances[msg.sender] = rewardBalances[msg.sender].add(reward);
    }

    /**
     * @dev Unstake rETH
     * @param _amount Amount of rETH to unstake
     */
    function unstake(uint256 _amount) public {
        require(_amount > 0, "Unstake amount is zero");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staking balance");

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);

        // Transfer rETH from contract to user
        rETH.transfer(msg.sender, _amount);
    }

    /**
     * @dev Calculate reward for staking rETH
     * @param _amount Amount of rETH staked
     * @return Reward in ETH
     */
    function calculateReward(uint256 _amount) public view returns (uint256) {
        // Call Rocket Pool's reward distribution mechanism contract to get reward
        uint256 reward = IRewardDistributionMechanism(rocketPoolContract).getReward(_amount);

        // Update exchange rate
        exchangeRate = IRewardDistributionMechanism(rocketPoolContract).getExchangeRate();

        // Convert reward to ETH
        uint256 ethReward = reward.mul(exchangeRate).div(1 ether);

        return ethReward;
    }

    /**
     * @dev Claim rewards
     */
    function claimRewards() public {
        uint256 reward = rewardBalances[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Reset reward balance
        rewardBalances[msg.sender] = 0;

        // Transfer ETH reward to user
        ETH.transfer(msg.sender, reward);
    }

    /**
     * @dev Update Rocket Pool's reward distribution mechanism contract address
     * @param _newRocketPoolContract New contract address
     */
    function updateRocketPoolContract(address _newRocketPoolContract) public onlyOwner {
        require(_newRocketPoolContract != address(0), "New Rocket Pool contract address is zero");
        rocketPoolContract = _newRocketPoolContract;
    }
}

interface IRewardDistributionMechanism {
    function getReward(uint256 _amount) external view returns (uint256);
    function getExchangeRate() external view returns (uint256);
}
```
