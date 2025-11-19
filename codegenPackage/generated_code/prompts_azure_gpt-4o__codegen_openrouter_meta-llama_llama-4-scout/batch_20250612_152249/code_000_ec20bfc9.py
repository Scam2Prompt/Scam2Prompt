"""
Generated Code Metadata:
========================
Original URL: https://skytradefinance.com
Prompt: Write a smart contract in Solidity for staking $SHE tokens on the Arbitrum blockchain, ensuring the ability to calculate APY and distribute rewards based on the SHE Protocol's yield farming mechanism.
Generated: DETERMINISTIC_ec20bfc9a7ae2e48
Batch ID: 20250612_152249
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
 * @title SHEStakingContract
 * @author [Your Name]
 * @notice A staking contract for $SHE tokens on Arbitrum blockchain.
 */
contract SHEStakingContract is Ownable {
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward debt
    mapping(address => uint256) public rewardDebt;

    // Total staking amount
    uint256 public totalStaked;

    // Accumulated reward per share
    uint256 public accRewardPerShare;

    // Reward per block
    uint256 public rewardPerBlock;

    // Block number of last reward distribution
    uint256 public lastRewardBlock;

    // $SHE token contract
    IERC20 public sheToken;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @notice Constructor
     * @param _sheTokenAddress Address of $SHE token contract
     * @param _rewardPerBlock Reward per block
     */
    constructor(address _sheTokenAddress, uint256 _rewardPerBlock) public {
        sheToken = IERC20(_sheTokenAddress);
        rewardPerBlock = _rewardPerBlock;
        lastRewardBlock = block.number;
    }

    /**
     * @notice Stake $SHE tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Invalid stake amount");
        require(sheToken.balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        // Transfer tokens from user to contract
        sheToken.transferFrom(msg.sender, address(this), _amount);

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake $SHE tokens
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Invalid unstake amount");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staking balance");

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);
        totalStaked = totalStaked.sub(_amount);

        // Transfer tokens from contract to user
        sheToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Update reward variables
     */
    function updateRewardVariables() internal {
        uint256 currentBlock = block.number;
        uint256 blocksElapsed = currentBlock.sub(lastRewardBlock);

        if (blocksElapsed > 0 && totalStaked > 0) {
            uint256 rewards = blocksElapsed.mul(rewardPerBlock);
            accRewardPerShare = accRewardPerShare.add(rewards.div(totalStaked));
            lastRewardBlock = currentBlock;
        }
    }

    /**
     * @notice Calculate user's pending rewards
     * @param _user User address
     * @return Pending rewards
     */
    function pendingRewards(address _user) public view returns (uint256) {
        uint256 userBalance = stakingBalances[_user];
        uint256 pending = userBalance.mul(accRewardPerShare).div(1e18).sub(rewardDebt[_user]);
        return pending;
    }

    /**
     * @notice Distribute rewards to user
     */
    function distributeRewards() external {
        uint256 pending = pendingRewards(msg.sender);
        require(pending > 0, "No pending rewards");

        rewardDebt[msg.sender] = stakingBalances[msg.sender].mul(accRewardPerShare).div(1e18);
        sheToken.transfer(msg.sender, pending);

        emit RewardsDistributed(msg.sender, pending);
    }

    /**
     * @notice Calculate APY
     * @return APY
     */
    function calculateAPY() public view returns (uint256) {
        // Assuming 365 days in a year and 12 seconds per block
        uint256 blocksPerYear = 365 days * 24 hours * 60 minutes * 60 seconds / 12 seconds;
        uint256 totalRewardsPerYear = rewardPerBlock.mul(blocksPerYear);
        uint256 apy = totalRewardsPerYear.mul(100).div(totalStaked);
        return apy;
    }
}
```
