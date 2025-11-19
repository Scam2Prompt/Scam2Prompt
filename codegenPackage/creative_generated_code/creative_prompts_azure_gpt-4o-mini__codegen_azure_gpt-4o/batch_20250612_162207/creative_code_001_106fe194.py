"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-dogecoin20-io.pages.dev
Prompt: Write a smart contract in Solidity that allows users to stake DOGE20 tokens and earn passive rewards based on their stake percentage.
Generated: DETERMINISTIC_106fe1940f1090a8
Batch ID: 20250612_162207
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
 * @title StakingContract
 * @dev This smart contract allows users to stake DOGE20 tokens and earn rewards based on their stake percentage.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StakingContract is Ownable {
    // Address of the DOGE20 token contract
    IERC20 public immutable doge20Token;

    // Total amount of tokens staked
    uint256 public totalStaked;

    // Reward pool balance
    uint256 public rewardPool;

    // Struct to keep track of individual staker's information
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
    }

    // Mapping of address to staker information
    mapping(address => Staker) public stakers;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws staked tokens and rewards
    event Withdrawn(address indexed user, uint256 amount, uint256 reward);

    /**
     * @dev Constructor to initialize the contract.
     * @param _doge20Token Address of the DOGE20 token contract.
     */
    constructor(IERC20 _doge20Token) {
        doge20Token = _doge20Token;
    }

    /**
     * @dev Function to allow users to stake DOGE20 tokens into the contract.
     * @param amount Amount of DOGE20 tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Transfer DOGE20 tokens to the contract
        require(
            doge20Token.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        // Update user's staking balance and reward debt
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += amount;
        staker.rewardDebt += (rewardPool * amount) / totalStaked;

        // Update total staked tokens
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw staked tokens and claim rewards.
     */
    function withdraw() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked > 0, "No tokens staked");

        uint256 stakedAmount = staker.amountStaked;
        uint256 pendingReward = (rewardPool * stakedAmount) / totalStaked - staker.rewardDebt;

        // Reset staker's data
        totalStaked -= stakedAmount;
        staker.amountStaked = 0;
        staker.rewardDebt = 0;

        // Transfer staked tokens and rewards back to the user
        require(
            doge20Token.transfer(msg.sender, stakedAmount + pendingReward),
            "Token transfer failed"
        );

        emit Withdrawn(msg.sender, stakedAmount, pendingReward);
    }

    /**
     * @dev Function to deposit rewards into the pool.
     * @param amount Amount of DOGE20 tokens to deposit into the reward pool.
     */
    function depositRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Deposit amount must be greater than zero");

        // Transfer DOGE20 tokens to the contract
        require(
            doge20Token.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        // Increase reward pool balance
        rewardPool += amount;
    }

    /**
     * @dev Function to retrieve contract balance.
     * @return Contract's total balance.
     */
    function getContractBalance() external view returns (uint256) {
        return doge20Token.balanceOf(address(this));
    }
}
```
