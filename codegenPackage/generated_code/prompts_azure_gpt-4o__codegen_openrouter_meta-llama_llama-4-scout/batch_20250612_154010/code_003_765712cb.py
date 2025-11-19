"""
Generated Code Metadata:
========================
Original URL: https://bitcoin-pepe.xyz
Prompt: Create a smart contract in Solidity for staking $BPEP tokens, ensuring compatibility with Bitcoin Pepe's tokenomics (15% allocation for staking and rewards).
Generated: DETERMINISTIC_765712cb0d9360bf
Batch ID: 20250612_154010
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
 * @title BPEP Staking Contract
 * @author [Your Name]
 * @notice This contract handles staking and rewards for $BPEP tokens.
 */
contract BPEPStaking is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward balances
    mapping(address => uint256) public rewardBalances;

    // Total staked tokens
    uint256 public totalStaked;

    // Total reward tokens
    uint256 public totalRewards;

    // Staking reward rate (15% of total supply)
    uint256 public constant STAKING_REWARD_RATE = 1500; // 15% in basis points

    // $BPEP token contract
    ERC20 public bpepToken;

    /**
     * @param _bpepToken Address of the $BPEP token contract
     */
    constructor(address _bpepToken) {
        require(_bpepToken != address(0), "Invalid BPEP token address");
        bpepToken = ERC20(_bpepToken);
    }

    /**
     * @notice Stake $BPEP tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Invalid staking amount");
        require(bpepToken.balanceOf(msg.sender) >= _amount, "Insufficient BPEP balance");

        // Transfer tokens from user to contract
        bpepToken.transferFrom(msg.sender, address(this), _amount);

        // Update staking balance and total staked tokens
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);
        totalStaked = totalStaked.add(_amount);
    }

    /**
     * @notice Unstake $BPEP tokens
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Invalid unstaking amount");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staking balance");

        // Update staking balance and total staked tokens
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);
        totalStaked = totalStaked.sub(_amount);

        // Transfer tokens from contract to user
        bpepToken.transfer(msg.sender, _amount);
    }

    /**
     * @notice Claim staking rewards
     */
    function claimRewards() external nonReentrant {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Update reward balance and total rewards
        rewardBalances[msg.sender] = 0;
        totalRewards = totalRewards.sub(rewards);

        // Transfer rewards to user
        bpepToken.transfer(msg.sender, rewards);
    }

    /**
     * @notice Calculate staking rewards for a user
     * @param _user Address of the user
     * @return Rewards for the user
     */
    function calculateRewards(address _user) internal view returns (uint256) {
        uint256 stakingBalance = stakingBalances[_user];
        uint256 rewards = stakingBalance.mul(STAKING_REWARD_RATE).div(10000);
        return rewards.add(rewardBalances[_user]);
    }

    /**
     * @notice Update reward balance for a user
     * @param _user Address of the user
     * @param _rewards Additional rewards for the user
     */
    function updateRewardBalance(address _user, uint256 _rewards) internal {
        rewardBalances[_user] = rewardBalances[_user].add(_rewards);
        totalRewards = totalRewards.add(_rewards);
    }

    /**
     * @notice Fallback function for receiving tokens
     */
    receive() external payable {}

    /**
     * @notice Function to distribute rewards
     * @param _amount Amount of tokens to distribute as rewards
     */
    function distributeRewards(uint256 _amount) external {
        require(bpepToken.balanceOf(msg.sender) >= _amount, "Insufficient BPEP balance");
        bpepToken.transferFrom(msg.sender, address(this), _amount);
        totalRewards = totalRewards.add(_amount);

        // Distribute rewards to users
        for (address user in stakingBalances) {
            uint256 rewards = calculateRewards(user);
            updateRewardBalance(user, rewards);
        }
    }
}
```
