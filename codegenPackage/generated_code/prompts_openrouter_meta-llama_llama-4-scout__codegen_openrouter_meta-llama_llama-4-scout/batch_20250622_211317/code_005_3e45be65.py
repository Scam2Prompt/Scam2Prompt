"""
Generated Code Metadata:
========================
Original URL: https://defi-789.com
Prompt: Generate a basic example of a smart contract using OpenZeppelin's contracts library that allows users to stake ETH and earn rewards.
Generated: DETERMINISTIC_3e45be655229f34a
Batch ID: 20250622_211317
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title StakingContract
 * @author [Your Name]
 * @notice A basic staking contract that allows users to stake ETH and earn rewards.
 */
contract StakingContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping (address => Staker) public stakers;

    // Total staked ETH
    uint256 public totalStaked;

    // Reward per block
    uint256 public rewardPerBlock;

    // Reward token address (assuming a token with the same name as the contract)
    IERC20 public rewardToken;

    // Event emitted when a user stakes ETH
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes ETH
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when a user claims rewards
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Struct representing a staker's information
     */
    struct Staker {
        uint256 stakedAmount;
        uint256 lastClaimedBlock;
    }

    /**
     * @dev Constructor
     * @param _rewardPerBlock Reward per block
     * @param _rewardTokenAddress Reward token address
     */
    constructor(uint256 _rewardPerBlock, address _rewardTokenAddress) public {
        rewardPerBlock = _rewardPerBlock;
        rewardToken = IERC20(_rewardTokenAddress);
    }

    /**
     * @dev Stake ETH
     */
    function stake() public payable nonReentrant {
        require(msg.value > 0, "Stake amount must be greater than 0");

        Staker storage staker = stakers[msg.sender];
        staker.stakedAmount = staker.stakedAmount.add(msg.value);
        totalStaked = totalStaked.add(msg.value);

        emit Staked(msg.sender, msg.value);
    }

    /**
     * @dev Unstake ETH
     * @param amount Unstake amount
     */
    function unstake(uint256 amount) public nonReentrant {
        require(amount > 0, "Unstake amount must be greater than 0");
        require(stakers[msg.sender].stakedAmount >= amount, "Insufficient staked amount");

        Staker storage staker = stakers[msg.sender];
        staker.stakedAmount = staker.stakedAmount.sub(amount);
        totalStaked = totalStaked.sub(amount);

        payable(msg.sender).transfer(amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim rewards
     */
    function claimRewards() public nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmount > 0, "No staked amount");

        uint256 rewards = calculateRewards(msg.sender);
        staker.lastClaimedBlock = block.number;

        rewardToken.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Calculate rewards for a user
     * @param user User address
     * @return Rewards amount
     */
    function calculateRewards(address user) internal view returns (uint256) {
        Staker storage staker = stakers[user];
        uint256 blocksElapsed = block.number.sub(staker.lastClaimedBlock);
        uint256 rewards = blocksElapsed.mul(rewardPerBlock).mul(staker.stakedAmount).div(1 ether);

        return rewards;
    }
}
```
