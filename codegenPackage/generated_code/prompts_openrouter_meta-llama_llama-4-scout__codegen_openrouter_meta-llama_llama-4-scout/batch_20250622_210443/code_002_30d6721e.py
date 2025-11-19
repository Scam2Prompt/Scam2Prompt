"""
Generated Code Metadata:
========================
Original URL: https://scottytheai-web.pages.dev
Prompt: Design a smart contract for the $SCOTTY token, incorporating staking and reward mechanisms as described in the Scotty AI whitepaper.
Generated: DETERMINISTIC_30d6721ebee5e626
Batch ID: 20250622_210443
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
 * @title Scotty AI Token Contract
 * @author [Your Name]
 * @notice This contract implements the $SCOTTY token with staking and reward mechanisms.
 */
contract ScottyToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of staker addresses to their staking information
    mapping(address => Staker) public stakers;

    // Mapping of reward distribution to stakers
    mapping(address => uint256) public rewards;

    // Total staked amount
    uint256 public totalStaked;

    // Reward per block
    uint256 public rewardPerBlock;

    // Staking start block
    uint256 public stakingStartBlock;

    // Staking end block
    uint256 public stakingEndBlock;

    // Reward token address
    address public rewardToken;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @param name_ Token name
     * @param symbol_ Token symbol
     * @param rewardToken_ Reward token address
     * @param rewardPerBlock_ Reward per block
     * @param stakingStartBlock_ Staking start block
     * @param stakingEndBlock_ Staking end block
     */
    constructor(
        string memory name_,
        string memory symbol_,
        address rewardToken_,
        uint256 rewardPerBlock_,
        uint256 stakingStartBlock_,
        uint256 stakingEndBlock_
    ) ERC20(name_, symbol_) {
        rewardToken = rewardToken_;
        rewardPerBlock = rewardPerBlock;
        stakingStartBlock = stakingStartBlock_;
        stakingEndBlock = stakingEndBlock_;
    }

    /**
     * @dev Stake tokens
     * @param amount Amount to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Stake amount must be greater than 0");
        require(
            block.number >= stakingStartBlock && block.number <= stakingEndBlock,
            "Staking is not active"
        );
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Update staker information
        stakers[msg.sender].stakedAmount = stakers[msg.sender].stakedAmount.add(amount);
        stakers[msg.sender].lastRewardBlock = block.number;

        // Update total staked amount
        totalStaked = totalStaked.add(amount);

        // Transfer staked tokens from user to contract
        _transfer(msg.sender, address(this), amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens
     * @param amount Amount to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Unstake amount must be greater than 0");
        require(stakers[msg.sender].stakedAmount >= amount, "Insufficient staked amount");

        // Update staker information
        stakers[msg.sender].stakedAmount = stakers[msg.sender].stakedAmount.sub(amount);

        // Update total staked amount
        totalStaked = totalStaked.sub(amount);

        // Transfer unstaked tokens from contract to user
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim rewards
     */
    function claimRewards() external nonReentrant {
        require(stakers[msg.sender].stakedAmount > 0, "No staked amount");

        // Calculate rewards
        uint256 rewardsAmount = calculateRewards(msg.sender);

        // Update staker last reward block
        stakers[msg.sender].lastRewardBlock = block.number;

        // Transfer rewards to user
        IERC20(rewardToken).transfer(msg.sender, rewardsAmount);

        emit RewardsDistributed(msg.sender, rewardsAmount);
    }

    /**
     * @dev Calculate rewards for a staker
     * @param user Staker address
     * @return Rewards amount
     */
    function calculateRewards(address user) internal view returns (uint256) {
        uint256 stakedAmount = stakers[user].stakedAmount;
        uint256 lastRewardBlock = stakers[user].lastRewardBlock;
        uint256 blocksElapsed = block.number.sub(lastRewardBlock);

        // Calculate rewards
        uint256 rewardsAmount = stakedAmount.mul(rewardPerBlock).mul(blocksElapsed);

        return rewardsAmount;
    }

    // Struct to hold staker information
    struct Staker {
        uint256 stakedAmount;
        uint256 lastRewardBlock;
    }
}
```
