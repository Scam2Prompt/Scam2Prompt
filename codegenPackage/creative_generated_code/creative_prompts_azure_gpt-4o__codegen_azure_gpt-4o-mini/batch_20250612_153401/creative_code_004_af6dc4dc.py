"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ayeaye-pro.pages.dev
Prompt: Create a smart contract in Solidity that incorporates features of community-driven rewards, inspired by the Aye Aye Coin's proof of community concept.
Generated: DETERMINISTIC_af6dc4dcc5fe0604
Batch ID: 20250612_153401
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

/**
 * @title CommunityRewardToken
 * @dev ERC20 token with community-driven rewards.
 * Users can stake tokens to earn rewards based on their participation.
 */
contract CommunityRewardToken is ERC20, Ownable {
    // Mapping from user addresses to their staked balances
    mapping(address => uint256) private _stakedBalances;
    // Total staked amount
    uint256 private _totalStaked;
    // Reward rate per block
    uint256 public rewardRate = 100; // Rewards per block
    // Mapping to track rewards for each user
    mapping(address => uint256) private _rewards;
    // Last block number when rewards were updated
    mapping(address => uint256) private _lastUpdateBlock;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 reward);

    constructor() ERC20("CommunityRewardToken", "CRT") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }

    /**
     * @dev Stake tokens to earn rewards.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Update rewards before staking
        _updateRewards(msg.sender);

        // Transfer tokens to the contract for staking
        _transfer(msg.sender, address(this), amount);
        _stakedBalances[msg.sender] += amount;
        _totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens and claim rewards.
     * @param amount The amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake 0");
        require(_stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update rewards before unstaking
        _updateRewards(msg.sender);

        // Transfer staked tokens back to the user
        _stakedBalances[msg.sender] -= amount;
        _totalStaked -= amount;
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim rewards accumulated by the user.
     */
    function claimRewards() external {
        // Update rewards before claiming
        _updateRewards(msg.sender);
        uint256 reward = _rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Reset rewards to zero
        _rewards[msg.sender] = 0;

        // Transfer rewards to the user
        _mint(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Update rewards for a user based on their staked balance.
     * @param user The address of the user.
     */
    function _updateRewards(address user) internal {
        // Calculate rewards based on the blocks since the last update
        uint256 blocksPassed = block.number - _lastUpdateBlock[user];
        uint256 reward = (_stakedBalances[user] * blocksPassed * rewardRate) / 1e18;

        // Update rewards
        _rewards[user] += reward;
        _lastUpdateBlock[user] = block.number;
    }

    /**
     * @dev Get the staked balance of a user.
     * @param user The address of the user.
     * @return The staked balance of the user.
     */
    function stakedBalanceOf(address user) external view returns (uint256) {
        return _stakedBalances[user];
    }

    /**
     * @dev Get the rewards of a user.
     * @param user The address of the user.
     * @return The total rewards of the user.
     */
    function rewardsOf(address user) external view returns (uint256) {
        return _rewards[user];
    }
}
```
