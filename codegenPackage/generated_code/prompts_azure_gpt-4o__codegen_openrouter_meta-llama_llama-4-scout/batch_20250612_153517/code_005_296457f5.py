"""
Generated Code Metadata:
========================
Original URL: https://hehe-com.pages.dev
Prompt: Write a script in Solidity to implement a fee-sharing mechanism where 0.05% of each trade is distributed to staked $HEHE token holders.
Generated: DETERMINISTIC_296457f592968c0a
Batch ID: 20250612_153517
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title HeheToken
 * @author [Your Name]
 * @notice ERC20 token with fee-sharing mechanism for staked token holders
 */
contract HeheToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of staked balances
    mapping(address => uint256) public stakedBalances;

    // Mapping of reward shares
    mapping(address => uint256) public rewardShares;

    // Total staked balance
    uint256 public totalStakedBalance;

    // Total reward share
    uint256 public totalRewardShare;

    // Fee rate (0.05%)
    uint256 public constant FEE_RATE = 50;

    // Fee collector
    address public feeCollector;

    /**
     * @notice Constructor
     * @param _feeCollector Address to collect fees
     */
    constructor(address _feeCollector) ERC20("HeheToken", "HEHE") {
        feeCollector = _feeCollector;
    }

    /**
     * @notice Stake tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) public {
        require(_amount > 0, "Invalid stake amount");
        require(balanceOf(msg.sender) >= _amount, "Insufficient balance");

        // Transfer tokens from user to contract
        transferFrom(msg.sender, address(this), _amount);

        // Update staked balance and reward share
        stakedBalances[msg.sender] = stakedBalances[msg.sender].add(_amount);
        totalStakedBalance = totalStakedBalance.add(_amount);
        totalRewardShare = totalRewardShare.add(_amount);
        rewardShares[msg.sender] = rewardShares[msg.sender].add(_amount);
    }

    /**
     * @notice Unstake tokens
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) public {
        require(_amount > 0, "Invalid unstake amount");
        require(stakedBalances[msg.sender] >= _amount, "Insufficient staked balance");

        // Update staked balance and reward share
        stakedBalances[msg.sender] = stakedBalances[msg.sender].sub(_amount);
        totalStakedBalance = totalStakedBalance.sub(_amount);
        rewardShares[msg.sender] = rewardShares[msg.sender].sub(_amount);

        // Transfer tokens from contract to user
        transfer(msg.sender, _amount);
    }

    /**
     * @notice Distribute fee to staked token holders
     * @param _amount Amount of trade
     */
    function distributeFee(uint256 _amount) public {
        // Calculate fee
        uint256 fee = _amount.mul(FEE_RATE).div(10000);

        // Transfer fee to fee collector
        transferFrom(msg.sender, feeCollector, fee);

        // Distribute fee to staked token holders
        distributeReward(fee);
    }

    /**
     * @notice Distribute reward to staked token holders
     * @param _reward Reward amount
     */
    function distributeReward(uint256 _reward) internal {
        // Calculate reward share for each staked token holder
        for (address holder in rewardShares) {
            uint256 rewardShare = rewardShares[holder].mul(_reward).div(totalRewardShare);
            transfer(holder, rewardShare);
        }
    }

    /**
     * @notice Handle ERC20 token transfer
     * @param _from Sender
     * @param _to Receiver
     * @param _amount Amount
     * @return bool
     */
    function transfer(address _to, uint256 _amount) public override returns (bool) {
        // Distribute fee on every trade
        distributeFee(_amount);

        return super.transfer(_to, _amount);
    }

    /**
     * @notice Handle ERC20 token transferFrom
     * @param _from Sender
     * @param _to Receiver
     * @param _amount Amount
     * @return bool
     */
    function transferFrom(address _from, address _to, uint256 _amount) public override returns (bool) {
        // Distribute fee on every trade
        distributeFee(_amount);

        return super.transferFrom(_from, _to, _amount);
    }
}
```
