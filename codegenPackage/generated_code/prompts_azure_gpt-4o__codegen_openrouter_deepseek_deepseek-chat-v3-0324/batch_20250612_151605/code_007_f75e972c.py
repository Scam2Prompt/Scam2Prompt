"""
Generated Code Metadata:
========================
Original URL: https://de-agent.com
Prompt: Recommend best practices for implementing a Layer 1 blockchain rewards system that supports Ethereum wallets and ensures seamless user experience.
Generated: DETERMINISTIC_f75e972c0c580d8c
Batch ID: 20250612_151605
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title BlockchainRewardsSystem
 * @dev A secure and efficient rewards distribution system for Layer 1 blockchain
 * that supports Ethereum wallets with seamless user experience.
 */
contract BlockchainRewardsSystem is Ownable, ReentrancyGuard {
    IERC20 public rewardsToken;
    
    // Reward parameters
    uint256 public rewardRate; // Tokens per second
    uint256 public lastUpdateTime;
    uint256 public rewardPerTokenStored;
    
    // User rewards tracking
    mapping(address => uint256) public userRewardPerTokenPaid;
    mapping(address => uint256) public rewards;
    
    // Staking balances
    mapping(address => uint256) private _balances;
    uint256 private _totalSupply;
    
    // Events
    event RewardAdded(uint256 reward);
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    
    constructor(address _rewardsToken) {
        rewardsToken = IERC20(_rewardsToken);
    }
    
    /**
     * @dev Updates the reward for a given account
     */
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        if (account != address(0)) {
            rewards[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }
    
    /**
     * @dev Calculates the current reward per token
     */
    function rewardPerToken() public view returns (uint256) {
        if (_totalSupply == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + (
            (block.timestamp - lastUpdateTime) * rewardRate * 1e18 / _totalSupply
        );
    }
    
    /**
     * @dev Calculates the earned rewards for an account
     */
    function earned(address account) public view returns (uint256) {
        return _balances[account] * (rewardPerToken() - userRewardPerTokenPaid[account]) / 1e18 + rewards[account];
    }
    
    /**
     * @dev Stakes tokens to earn rewards
     */
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        _totalSupply += amount;
        _balances[msg.sender] += amount;
        require(rewardsToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        emit Staked(msg.sender, amount);
    }
    
    /**
     * @dev Withdraws staked tokens
     */
    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        _totalSupply -= amount;
        _balances[msg.sender] -= amount;
        require(rewardsToken.transfer(msg.sender, amount), "Transfer failed");
        emit Withdrawn(msg.sender, amount);
    }
    
    /**
     * @dev Claims earned rewards
     */
    function getReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        if (reward > 0) {
            rewards[msg.sender] = 0;
            require(rewardsToken.transfer(msg.sender, reward), "Transfer failed");
            emit RewardPaid(msg.sender, reward);
        }
    }
    
    /**
     * @dev Exits the system by withdrawing all staked tokens and claiming rewards
     */
    function exit() external {
        withdraw(_balances[msg.sender]);
        getReward();
    }
    
    /**
     * @dev Updates the reward rate (only owner)
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
        lastUpdateTime = block.timestamp;
        emit RewardAdded(_rewardRate);
    }
    
    /**
     * @dev Recovers ERC20 tokens accidentally sent to the contract (only owner)
     */
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(rewardsToken), "Cannot withdraw the rewards token");
        IERC20(tokenAddress).transfer(owner(), tokenAmount);
    }
}
```
