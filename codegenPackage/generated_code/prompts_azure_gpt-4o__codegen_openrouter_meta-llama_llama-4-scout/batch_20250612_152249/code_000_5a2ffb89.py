"""
Generated Code Metadata:
========================
Original URL: https://bafybeia5w6ij6k5e2i3vwagaacosirdjz6kce4q3y2thlqdaqcfnictzmu.ipfs.dweb.link
Prompt: Write a smart contract using Solidity that integrates with Berachain's Proof-of-Liquidity consensus mechanism to reward liquidity providers with non-purchasable staking tokens.
Generated: DETERMINISTIC_5a2ffb89a07a161d
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Berachain Proof-of-Liquidity Staking Contract
 * @author [Your Name]
 * @notice This contract integrates with Berachain's Proof-of-Liquidity consensus mechanism
 *         to reward liquidity providers with non-purchasable staking tokens.
 */
contract BerachainPoLStaking is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of liquidity providers to their staking information
    mapping(address => Staker) public stakers;

    // Mapping of staking token balances
    mapping(address => uint256) public stakingTokenBalances;

    // Berachain's Proof-of-Liquidity token address
    address public polToken;

    // Staking token address (non-purchasable)
    address public stakingToken;

    // Reward per block for liquidity providers
    uint256 public rewardPerBlock;

    // Total staking tokens distributed
    uint256 public totalStakingTokensDistributed;

    // Event emitted when a liquidity provider stakes
    event Staked(address indexed provider, uint256 amount);

    // Event emitted when a liquidity provider unstakes
    event Unstaked(address indexed provider, uint256 amount);

    // Event emitted when a reward is distributed
    event RewardDistributed(address indexed provider, uint256 amount);

    /**
     * @param _polToken Berachain's Proof-of-Liquidity token address
     * @param _stakingToken Staking token address (non-purchasable)
     * @param _rewardPerBlock Reward per block for liquidity providers
     */
    constructor(address _polToken, address _stakingToken, uint256 _rewardPerBlock) public {
        require(_polToken != address(0), "POL token address cannot be zero");
        require(_stakingToken != address(0), "Staking token address cannot be zero");
        require(_rewardPerBlock > 0, "Reward per block must be greater than zero");

        polToken = _polToken;
        stakingToken = _stakingToken;
        rewardPerBlock = _rewardPerBlock;
    }

    /**
     * @dev Stake liquidity
     * @param amount The amount of liquidity to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Stake amount must be greater than zero");
        require(stakers[msg.sender].stakedAmount.add(amount) >= 0, "Stake amount overflows");

        // Transfer POL tokens from the liquidity provider to the contract
        ERC20(polToken).transferFrom(msg.sender, address(this), amount);

        // Update staker information
        stakers[msg.sender].stakedAmount = stakers[msg.sender].stakedAmount.add(amount);
        stakers[msg.sender].lastRewardBlock = block.number;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake liquidity
     * @param amount The amount of liquidity to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Unstake amount must be greater than zero");
        require(stakers[msg.sender].stakedAmount >= amount, "Unstake amount exceeds staked amount");

        // Update staker information
        stakers[msg.sender].stakedAmount = stakers[msg.sender].stakedAmount.sub(amount);

        // Transfer POL tokens from the contract to the liquidity provider
        ERC20(polToken).transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Distribute rewards to liquidity providers
     */
    function distributeRewards() external nonReentrant {
        uint256 reward = rewardPerBlock.mul(stakers[msg.sender].stakedAmount);
        require(reward > 0, "Reward amount must be greater than zero");

        // Update staker information
        stakers[msg.sender].lastRewardBlock = block.number;

        // Transfer staking tokens from the contract to the liquidity provider
        ERC20(stakingToken).transfer(msg.sender, reward);

        // Update total staking tokens distributed
        totalStakingTokensDistributed = totalStakingTokensDistributed.add(reward);

        emit RewardDistributed(msg.sender, reward);
    }

    /**
     * @dev Get staker information
     * @param provider The address of the liquidity provider
     * @return stakedAmount The amount of liquidity staked
     * @return lastRewardBlock The block number of the last reward distribution
     */
    function getStakerInfo(address provider) external view returns (uint256 stakedAmount, uint256 lastRewardBlock) {
        return (stakers[provider].stakedAmount, stakers[provider].lastRewardBlock);
    }

    struct Staker {
        uint256 stakedAmount;
        uint256 lastRewardBlock;
    }
}
```
