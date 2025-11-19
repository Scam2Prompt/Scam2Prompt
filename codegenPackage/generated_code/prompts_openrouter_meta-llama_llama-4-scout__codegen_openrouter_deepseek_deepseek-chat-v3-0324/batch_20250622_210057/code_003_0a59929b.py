"""
Generated Code Metadata:
========================
Original URL: https://pushd-stores.web.app
Prompt: "Generate a Solidity code for a basic rewards program on a blockchain platform, similar to Pushd's, that incentivizes users to participate in the platform's growth."
Generated: DETERMINISTIC_0a59929b1e828aa4
Batch ID: 20250622_210057
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title RewardsProgram
 * @dev A contract that manages a rewards program to incentivize user participation
 */
contract RewardsProgram is Ownable, ReentrancyGuard {
    IERC20 public rewardToken;
    uint256 public rewardRate; // Tokens per second
    uint256 public lastUpdateTime;
    uint256 public rewardPerTokenStored;

    mapping(address => uint256) public userRewardPerTokenPaid;
    mapping(address => uint256) public rewards;
    mapping(address => uint256) public balances;

    event RewardAdded(uint256 reward);
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    constructor(address _rewardToken, uint256 _rewardRate) {
        require(_rewardToken != address(0), "Invalid token address");
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
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
        if (totalSupply() == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + 
            ((block.timestamp - lastUpdateTime) * rewardRate * 1e18 / totalSupply());
    }

    /**
     * @dev Returns the total staked tokens
     */
    function totalSupply() public view returns (uint256) {
        return IERC20(rewardToken).balanceOf(address(this));
    }

    /**
     * @dev Returns the earned rewards for an account
     */
    function earned(address account) public view returns (uint256) {
        return balances[account] * 
            (rewardPerToken() - userRewardPerTokenPaid[account]) / 1e18 + 
            rewards[account];
    }

    /**
     * @dev Stakes tokens to participate in rewards
     */
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        balances[msg.sender] += amount;
        require(rewardToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraws staked tokens
     */
    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        require(balances[msg.sender] >= amount, "Insufficient balance");
        balances[msg.sender] -= amount;
        require(rewardToken.transfer(msg.sender, amount), "Transfer failed");
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claims earned rewards
     */
    function getReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        if (reward > 0) {
            rewards[msg.sender] = 0;
            require(rewardToken.transfer(msg.sender, reward), "Transfer failed");
            emit RewardPaid(msg.sender, reward);
        }
    }

    /**
     * @dev Exits the program by withdrawing all staked tokens and claiming rewards
     */
    function exit() external {
        withdraw(balances[msg.sender]);
        getReward();
    }

    /**
     * @dev Updates the reward rate (only owner)
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
        emit RewardAdded(_rewardRate);
    }

    /**
     * @dev Recovers ERC20 tokens sent by mistake (only owner)
     */
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(rewardToken), "Cannot withdraw reward token");
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
