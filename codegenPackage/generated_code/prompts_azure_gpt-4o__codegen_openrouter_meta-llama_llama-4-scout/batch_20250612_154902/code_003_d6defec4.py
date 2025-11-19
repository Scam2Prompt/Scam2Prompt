"""
Generated Code Metadata:
========================
Original URL: https://crudo-protocol.xyz
Prompt: Write a Solidity contract that implements a staking mechanism for CRUDO tokens, allowing users to lock their tokens and earn passive income based on a predefined reward rate.
Generated: DETERMINISTIC_d6defec47971cd40
Batch ID: 20250612_154902
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
 * @title CrudoStakingContract
 * @author [Your Name]
 * @notice A staking contract for CRUDO tokens, allowing users to lock their tokens and earn passive income.
 */
contract CrudoStakingContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping (address => Staker) public stakers;

    // CRUDO token contract
    IERC20 public crudoToken;

    // Reward rate per block
    uint256 public rewardRate;

    // Total staked tokens
    uint256 public totalStaked;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when a user claims rewards
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @param _crudoToken Address of the CRUDO token contract
     * @param _rewardRate Reward rate per block
     */
    constructor(address _crudoToken, uint256 _rewardRate) public {
        require(_crudoToken != address(0), "CRUDO token address cannot be zero");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        crudoToken = IERC20(_crudoToken);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake CRUDO tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(crudoToken.balanceOf(msg.sender) >= _amount, "Insufficient CRUDO token balance");

        // Update staker information
        stakers[msg.sender].staked = stakers[msg.sender].staked.add(_amount);
        stakers[msg.sender].lastClaimed = block.number;

        // Update total staked tokens
        totalStaked = totalStaked.add(_amount);

        // Transfer tokens to the contract
        crudoToken.transferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake CRUDO tokens
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(stakers[msg.sender].staked >= _amount, "Insufficient staked tokens");

        // Update staker information
        stakers[msg.sender].staked = stakers[msg.sender].staked.sub(_amount);

        // Update total staked tokens
        totalStaked = totalStaked.sub(_amount);

        // Transfer tokens to the user
        crudoToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim rewards
     */
    function claimRewards() external nonReentrant {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Update staker information
        stakers[msg.sender].lastClaimed = block.number;

        // Transfer rewards to the user
        crudoToken.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Calculate rewards for a user
     * @param _user Address of the user
     * @return Rewards amount
     */
    function calculateRewards(address _user) public view returns (uint256) {
        uint256 staked = stakers[_user].staked;
        uint256 blocksElapsed = block.number.sub(stakers[_user].lastClaimed);
        uint256 rewards = staked.mul(rewardRate).mul(blocksElapsed);

        return rewards;
    }

    /**
     * @dev Get staker information
     * @param _user Address of the user
     * @return Staker information
     */
    function getStakerInfo(address _user) public view returns (uint256, uint256) {
        return (stakers[_user].staked, stakers[_user].lastClaimed);
    }

    struct Staker {
        uint256 staked;
        uint256 lastClaimed;
    }
}
```
