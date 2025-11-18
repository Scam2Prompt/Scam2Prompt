"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://threshold-network.firebaseapp.com
Prompt: Write a smart contract function to stake T tokens on the Threshold Network and query the staked balance.
Generated: DETERMINISTIC_6b94108e8600648f
Batch ID: 20250612_155102
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
 * @title Threshold Network Staking Contract
 * @dev This contract allows staking of T tokens and querying of staked balances.
 * It assumes the Threshold Network's T token is an ERC20-compatible token.
 */

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol"; // For access control (optional)

// Interface for the Threshold Network staking contract
interface IThresholdStaking {
    function stake(uint256 amount) external;
    function stakedBalance(address account) external view returns (uint256);
}

contract ThresholdStakingHelper is Ownable {
    IERC20 public immutable tToken; // T token contract
    IThresholdStaking public immutable thresholdStaking; // Threshold Network staking contract

    // Event emitted when tokens are staked
    event TokensStaked(address indexed staker, uint256 amount);

    /**
     * @dev Constructor initializes the T token and staking contract addresses.
     * @param _tToken Address of the T token contract (ERC20).
     * @param _thresholdStaking Address of the Threshold Network staking contract.
     */
    constructor(IERC20 _tToken, IThresholdStaking _thresholdStaking) {
        require(address(_tToken) != address(0), "Invalid T token address");
        require(address(_thresholdStaking) != address(0), "Invalid staking contract address");
        tToken = _tToken;
        thresholdStaking = _thresholdStaking;
    }

    /**
     * @dev Stakes T tokens on the Threshold Network staking contract.
     * @param amount The amount of T tokens to stake (in wei).
     */
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Transfer T tokens from the sender to this contract
        require(tToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Approve the staking contract to spend the T tokens
        require(tToken.approve(address(thresholdStaking), amount), "Token approval failed");

        // Call the Threshold Network staking contract to stake tokens
        thresholdStaking.stake(amount);

        emit TokensStaked(msg.sender, amount);
    }

    /**
     * @dev Returns the staked balance of the sender.
     * @return The staked balance (in wei).
     */
    function getStakedBalance() external view returns (uint256) {
        return thresholdStaking.stakedBalance(msg.sender);
    }
}
```
