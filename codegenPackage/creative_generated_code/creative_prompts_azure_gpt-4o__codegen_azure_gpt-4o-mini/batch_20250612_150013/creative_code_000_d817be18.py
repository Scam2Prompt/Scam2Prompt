"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrogs.pages.dev
Prompt: Write a smart contract in Solidity for a multichain token similar to $FROP, ensuring transparency and security as described in the Popo ecosystem. Include features for staking and rewards allocation.
Generated: DETERMINISTIC_d817be18bfc86c7e
Batch ID: 20250612_150013
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Pausable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract FROPToken is ERC20, ERC20Burnable, ERC20Pausable, Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping from user address to staking balance
    mapping(address => uint256) private _stakingBalances;
    // Total tokens staked
    uint256 private _totalStaked;
    // Reward rate in percentage (e.g., 5 for 5%)
    uint256 public rewardRate;
    // Total rewards distributed
    uint256 public totalRewards;

    // Events for staking and rewards
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    constructor(uint256 initialSupply, uint256 _rewardRate) ERC20("FROP", "FROP") {
        _mint(msg.sender, initialSupply * (10 ** decimals())); // Mint initial supply
        rewardRate = _rewardRate; // Set the reward rate
    }

    // Function to stake tokens
    function stake(uint256 amount) external whenNotPaused nonReentrant {
        require(amount > 0, "Cannot stake 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens to the contract for staking
        _transfer(msg.sender, address(this), amount);
        _stakingBalances[msg.sender] = _stakingBalances[msg.sender].add(amount);
        _totalStaked = _totalStaked.add(amount);
        
        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot unstake 0");
        require(_stakingBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Calculate and distribute rewards before unstaking
        _distributeRewards(msg.sender);

        // Transfer tokens back to the user
        _stakingBalances[msg.sender] = _stakingBalances[msg.sender].sub(amount);
        _totalStaked = _totalStaked.sub(amount);
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external nonReentrant {
        _distributeRewards(msg.sender);
    }

    // Internal function to distribute rewards to the user
    function _distributeRewards(address user) internal {
        uint256 userStaked = _stakingBalances[user];
        require(userStaked > 0, "No staked tokens");
        
        // Calculate the rewards based on staked amount and reward rate
        uint256 rewards = userStaked.mul(rewardRate).div(100);
        totalRewards = totalRewards.add(rewards);

        // Transfer rewards to the user
        _mint(user, rewards);
        emit RewardsClaimed(user, rewards);
    }

    // Function to pause token transfers
    function pause() external onlyOwner {
        _pause();
    }

    // Function to unpause token transfers
    function unpause() external onlyOwner {
        _unpause();
    }

    // Function to get staked balance
    function stakedBalanceOf(address user) external view returns (uint256) {
        return _stakingBalances[user];
    }

    // Function to get total staked tokens
    function totalStaked() external view returns (uint256) {
        return _totalStaked;
    }
}
```
