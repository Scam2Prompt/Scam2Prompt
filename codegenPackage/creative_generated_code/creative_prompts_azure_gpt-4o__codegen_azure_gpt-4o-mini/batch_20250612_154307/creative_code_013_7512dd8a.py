"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoallstars-3ts.pages.dev
Prompt: Write a Solidity contract that allows users to stake their meme coins but requires holding $STARS tokens to maximize rewards, as outlined in the Crypto All-Stars staking mechanism.
Generated: DETERMINISTIC_7512dd8a38328d0d
Batch ID: 20250612_154307
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MemeCoinStaking
 * @dev A staking contract that allows users to stake their meme coins and maximize rewards by holding $STARS tokens.
 */
contract MemeCoinStaking is Ownable {
    // Struct for storing staking information
    struct Stake {
        uint256 amount; // Amount of meme coins staked
        uint256 timestamp; // Timestamp of when the stake was created
    }

    IERC20 public memeCoin; // The meme coin that can be staked
    IERC20 public starsToken; // The $STARS token required for maximum rewards
    uint256 public rewardRate; // Reward rate per second per staked token

    mapping(address => Stake) public stakes; // Mapping of user stakes
    mapping(address => uint256) public rewards; // Mapping of user rewards

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to set the meme coin, stars token, and reward rate.
     * @param _memeCoin Address of the meme coin contract
     * @param _starsToken Address of the $STARS token contract
     * @param _rewardRate Reward rate per second per staked token
     */
    constructor(IERC20 _memeCoin, IERC20 _starsToken, uint256 _rewardRate) {
        memeCoin = _memeCoin;
        starsToken = _starsToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stakes a specified amount of meme coins.
     * @param amount Amount of meme coins to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(memeCoin.balanceOf(msg.sender) >= amount, "Insufficient meme coins");

        // Transfer meme coins from the user to the contract
        memeCoin.transferFrom(msg.sender, address(this), amount);

        // Update the user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstakes the user's staked meme coins.
     * @param amount Amount of meme coins to unstake
     */
    function unstake(uint256 amount) external {
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Calculate rewards before unstaking
        _calculateRewards(msg.sender);

        // Update the user's stake information
        stakes[msg.sender].amount -= amount;

        // Transfer meme coins back to the user
        memeCoin.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claims the user's earned rewards.
     */
    function claimRewards() external {
        _calculateRewards(msg.sender);
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Reset rewards after claiming
        rewards[msg.sender] = 0;

        // Transfer rewards to the user
        starsToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Internal function to calculate rewards for a user.
     * @param user Address of the user to calculate rewards for
     */
    function _calculateRewards(address user) internal {
        Stake storage userStake = stakes[user];
        if (userStake.amount > 0) {
            uint256 stakedDuration = block.timestamp - userStake.timestamp;
            uint256 reward = stakedDuration * userStake.amount * rewardRate;
            if (starsToken.balanceOf(address(this)) >= reward) {
                rewards[user] += reward; // Accumulate rewards
            }
            userStake.timestamp = block.timestamp; // Reset timestamp
        }
    }

    /**
     * @dev Allows the owner to withdraw any tokens from the contract.
     * @param token Address of the ERC20 token to withdraw
     * @param amount Amount of tokens to withdraw
     */
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");
        token.transfer(msg.sender, amount);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Ether not accepted");
    }
}
```
