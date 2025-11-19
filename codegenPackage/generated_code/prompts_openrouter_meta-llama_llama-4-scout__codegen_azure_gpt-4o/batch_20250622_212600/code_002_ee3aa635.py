"""
Generated Code Metadata:
========================
Original URL: https://rocket-pool.xyz
Prompt: Develop a smart contract that utilizes Rocket Pool's rETH for staking and yield generation, and describe how to distribute rewards and calculate the rETH/ETH exchange rate.
Generated: DETERMINISTIC_ee3aa635ceb51563
Batch ID: 20250622_212600
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

/**
 * @title StakingContract
 * @dev A smart contract that interacts with Rocket Pool's rETH for staking and yield generation.
 *      It allows users to deposit ETH, receive rETH, and distribute rewards proportionally.
 */
interface IRocketTokenRETH {
    function getExchangeRate() external view returns (uint256);
    function deposit() external payable;
}

contract StakingContract {
    // Address of the Rocket Pool rETH contract
    address public immutable rETHAddress;

    // Mapping to track user balances in rETH
    mapping(address => uint256) public userBalances;

    // Total rETH staked in the contract
    uint256 public totalStakedRETH;

    // Events
    event Deposited(address indexed user, uint256 ethAmount, uint256 rETHAmount);
    event RewardsDistributed(uint256 totalRewards, uint256 exchangeRate);

    /**
     * @dev Constructor to set the rETH contract address.
     * @param _rETHAddress Address of the Rocket Pool rETH contract.
     */
    constructor(address _rETHAddress) {
        require(_rETHAddress != address(0), "Invalid rETH address");
        rETHAddress = _rETHAddress;
    }

    /**
     * @dev Deposit ETH into the contract and receive rETH.
     */
    function deposit() external payable {
        require(msg.value > 0, "Must send ETH to deposit");

        // Interact with Rocket Pool's rETH contract to deposit ETH
        IRocketTokenRETH rETH = IRocketTokenRETH(rETHAddress);
        uint256 initialRETHBalance = address(this).balance;
        rETH.deposit{value: msg.value}();
        uint256 rETHReceived = address(this).balance - initialRETHBalance;

        // Update user balance and total staked rETH
        userBalances[msg.sender] += rETHReceived;
        totalStakedRETH += rETHReceived;

        emit Deposited(msg.sender, msg.value, rETHReceived);
    }

    /**
     * @dev Distribute rewards proportionally to all users based on their rETH holdings.
     * @param totalRewards The total amount of ETH rewards to distribute.
     */
    function distributeRewards(uint256 totalRewards) external {
        require(totalRewards > 0, "Rewards must be greater than zero");
        require(totalStakedRETH > 0, "No rETH staked");

        // Calculate the rETH/ETH exchange rate
        IRocketTokenRETH rETH = IRocketTokenRETH(rETHAddress);
        uint256 exchangeRate = rETH.getExchangeRate();

        // Distribute rewards proportionally
        for (address user : userBalances) {
            uint256 userShare = (userBalances[user] * totalRewards) / totalStakedRETH;
            payable(user).transfer(userShare);
        }

        emit RewardsDistributed(totalRewards, exchangeRate);
    }

    /**
     * @dev Get the current rETH/ETH exchange rate.
     * @return The current exchange rate.
     */
    function getExchangeRate() external view returns (uint256) {
        IRocketTokenRETH rETH = IRocketTokenRETH(rETHAddress);
        return rETH.getExchangeRate();
    }
}
```
