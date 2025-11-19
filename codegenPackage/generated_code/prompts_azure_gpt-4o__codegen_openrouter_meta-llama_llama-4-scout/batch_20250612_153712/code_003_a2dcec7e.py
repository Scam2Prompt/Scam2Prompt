"""
Generated Code Metadata:
========================
Original URL: https://appsmuhdorepositoryhub.pages.dev
Prompt: Generate a smart contract that supports staking DNA tokens in the Genesis Staking Pool, following the MuhdoHub ecosystem requirements.
Generated: DETERMINISTIC_a2dcec7ec3ab3616
Batch ID: 20250612_153712
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Pausable.sol";

/**
 * @title GenesisStakingPool
 * @author MuhdoHub
 * @notice A smart contract for staking DNA tokens in the Genesis Staking Pool.
 */
contract GenesisStakingPool is Ownable, Pausable {
    using SafeMath for uint256;

    // Mapping of staker addresses to their staking information
    mapping (address => Staker) public stakers;

    // DNA token contract
    IERC20 public dnaToken;

    // Genesis Staking Pool address
    address public genesisPoolAddress;

    // Staking rewards per block
    uint256 public rewardsPerBlock;

    // Staking start block
    uint256 public startBlock;

    // Staking end block
    uint256 public endBlock;

    // Total staked DNA tokens
    uint256 public totalStaked;

    // Event emitted when a user stakes DNA tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes DNA tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @param _dnaToken DNA token contract address
     * @param _genesisPoolAddress Genesis Staking Pool address
     * @param _rewardsPerBlock Staking rewards per block
     * @param _startBlock Staking start block
     * @param _endBlock Staking end block
     */
    constructor(
        address _dnaToken,
        address _genesisPoolAddress,
        uint256 _rewardsPerBlock,
        uint256 _startBlock,
        uint256 _endBlock
    ) public {
        dnaToken = IERC20(_dnaToken);
        genesisPoolAddress = _genesisPoolAddress;
        rewardsPerBlock = _rewardsPerBlock;
        startBlock = _startBlock;
        endBlock = _endBlock;
    }

    /**
     * @dev Stakes DNA tokens in the Genesis Staking Pool.
     * @param _amount Amount of DNA tokens to stake.
     */
    function stake(uint256 _amount) public whenNotPaused {
        require(_amount > 0, "Invalid stake amount");
        require(dnaToken.balanceOf(msg.sender) >= _amount, "Insufficient DNA token balance");
        require(block.number >= startBlock && block.number <= endBlock, "Staking period has not started or has ended");

        // Transfer DNA tokens to the contract
        dnaToken.transferFrom(msg.sender, address(this), _amount);

        // Update staker information
        stakers[msg.sender].staked = stakers[msg.sender].staked.add(_amount);
        stakers[msg.sender].lastClaimedBlock = block.number;

        // Update total staked DNA tokens
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstakes DNA tokens from the Genesis Staking Pool.
     * @param _amount Amount of DNA tokens to unstake.
     */
    function unstake(uint256 _amount) public whenNotPaused {
        require(_amount > 0, "Invalid unstake amount");
        require(stakers[msg.sender].staked >= _amount, "Insufficient staked DNA tokens");

        // Update staker information
        stakers[msg.sender].staked = stakers[msg.sender].staked.sub(_amount);

        // Transfer DNA tokens back to the user
        dnaToken.transfer(msg.sender, _amount);

        // Update total staked DNA tokens
        totalStaked = totalStaked.sub(_amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claims staking rewards.
     */
    function claimRewards() public whenNotPaused {
        require(stakers[msg.sender].staked > 0, "No staked DNA tokens");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);

        // Update staker information
        stakers[msg.sender].lastClaimedBlock = block.number;

        // Transfer rewards to the user
        dnaToken.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Calculates staking rewards for a user.
     * @param _user User address.
     * @return Rewards amount.
     */
    function calculateRewards(address _user) internal view returns (uint256) {
        uint256 blocksElapsed = block.number.sub(stakers[_user].lastClaimedBlock);
        uint256 rewards = blocksElapsed.mul(rewardsPerBlock).mul(stakers[_user].staked).div(totalStaked);
        return rewards;
    }

    /**
     * @dev Updates staking rewards per block.
     * @param _newRewardsPerBlock New rewards per block.
     */
    function updateRewardsPerBlock(uint256 _newRewardsPerBlock) public onlyOwner {
        rewardsPerBlock = _newRewardsPerBlock;
    }

    /**
     * @dev Pauses the contract.
     */
    function pause() public onlyOwner {
        _pause();
    }

    /**
     * @dev Unpauses the contract.
     */
    function unpause() public onlyOwner {
        _unpause();
    }

    struct Staker {
        uint256 staked;
        uint256 lastClaimedBlock;
    }
}
```
