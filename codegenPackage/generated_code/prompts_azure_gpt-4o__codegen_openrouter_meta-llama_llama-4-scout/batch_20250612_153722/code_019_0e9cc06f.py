"""
Generated Code Metadata:
========================
Original URL: https://cryptoallstars-launch.firebaseapp.com
Prompt: Write a Solidity contract that enables staking of top meme coins like Dogecoin, Shiba Inu, and Floki Inu, while requiring $STARS tokens for maximum rewards.
Generated: DETERMINISTIC_0e9cc06f72e25091
Batch ID: 20250612_153722
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title MemeCoinStakingContract
 * @author [Your Name]
 * @notice A contract for staking top meme coins and earning rewards in $STARS tokens.
 */
contract MemeCoinStakingContract is ReentrancyGuard {
    // Mapping of staker addresses to their staking information
    mapping(address => Staker) public stakers;

    // Mapping of supported meme coins to their respective reward rates
    mapping(address => uint256) public memeCoinRewardRates;

    // $STARS token contract address
    address public starsTokenAddress;

    // Event emitted when a user stakes meme coins
    event Staked(address indexed staker, address indexed memeCoin, uint256 amount);

    // Event emitted when a user unstakes meme coins
    event Unstaked(address indexed staker, address indexed memeCoin, uint256 amount);

    // Event emitted when a user claims rewards
    event RewardsClaimed(address indexed staker, uint256 amount);

    // Struct to store staker information
    struct Staker {
        mapping(address => uint256) stakedAmounts; // Mapping of meme coins to staked amounts
        uint256 lastRewardClaimTime; // Timestamp of last reward claim
        uint256 totalRewardsEarned; // Total rewards earned by the staker
    }

    /**
     * @notice Constructor for the MemeCoinStakingContract
     * @param _starsTokenAddress Address of the $STARS token contract
     */
    constructor(address _starsTokenAddress) {
        require(_starsTokenAddress != address(0), "Invalid $STARS token address");
        starsTokenAddress = _starsTokenAddress;

        // Initialize reward rates for supported meme coins
        memeCoinRewardRates[0xB8c77482e45F1EDeA1745a06C7447C58C3bDb4dA] = 100; // Dogecoin (DOGE)
        memeCoinRewardRates[0x95ad58c0001d5ee0b3db5c0B966CB5C9aa29f6F] = 50; // Shiba Inu (SHIB)
        memeCoinRewardRates[0xDa10009cBd5D07dd0CeCc66161F93D7c9000da1f] = 200; // Floki Inu (FLOKI)
    }

    /**
     * @notice Function to stake meme coins
     * @param _memeCoin Address of the meme coin to stake
     * @param _amount Amount of meme coins to stake
     */
    function stake(address _memeCoin, uint256 _amount) external nonReentrant {
        require(memeCoinRewardRates[_memeCoin] > 0, "Unsupported meme coin");
        require(_amount > 0, "Invalid stake amount");

        // Transfer meme coins from staker to contract
        IERC20(_memeCoin).transferFrom(msg.sender, address(this), _amount);

        // Update staker information
        stakers[msg.sender].stakedAmounts[_memeCoin] += _amount;

        emit Staked(msg.sender, _memeCoin, _amount);
    }

    /**
     * @notice Function to unstake meme coins
     * @param _memeCoin Address of the meme coin to unstake
     * @param _amount Amount of meme coins to unstake
     */
    function unstake(address _memeCoin, uint256 _amount) external nonReentrant {
        require(stakers[msg.sender].stakedAmounts[_memeCoin] >= _amount, "Insufficient staked amount");

        // Update staker information
        stakers[msg.sender].stakedAmounts[_memeCoin] -= _amount;

        // Transfer meme coins from contract to staker
        IERC20(_memeCoin).transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _memeCoin, _amount);
    }

    /**
     * @notice Function to claim rewards in $STARS tokens
     */
    function claimRewards() external nonReentrant {
        uint256 totalRewards = calculateRewards(msg.sender);
        require(totalRewards > 0, "No rewards to claim");

        // Update staker information
        stakers[msg.sender].lastRewardClaimTime = block.timestamp;
        stakers[msg.sender].totalRewardsEarned += totalRewards;

        // Transfer $STARS tokens to staker
        IERC20(starsTokenAddress).transfer(msg.sender, totalRewards);

        emit RewardsClaimed(msg.sender, totalRewards);
    }

    /**
     * @notice Function to calculate rewards for a staker
     * @param _staker Address of the staker
     * @return Total rewards in $STARS tokens
     */
    function calculateRewards(address _staker) internal view returns (uint256) {
        uint256 totalStakedAmount = 0;
        for (address memeCoin in stakers[_staker].stakedAmounts) {
            totalStakedAmount += stakers[_staker].stakedAmounts[memeCoin];
        }

        uint256 rewardRate = 0;
        for (address memeCoin in memeCoinRewardRates) {
            uint256 stakedAmount = stakers[_staker].stakedAmounts[memeCoin];
            if (stakedAmount > 0) {
                rewardRate += memeCoinRewardRates[memeCoin] * stakedAmount;
            }
        }

        uint256 timeElapsed = block.timestamp - stakers[_staker].lastRewardClaimTime;
        uint256 totalRewards = (totalStakedAmount * rewardRate * timeElapsed) / 365 days;

        return totalRewards;
    }
}
```
