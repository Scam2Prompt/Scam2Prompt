"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tenderize.xyz
Prompt: Write a smart contract in Solidity that mimics the functionality of Tenderize's liquid staking process, where users deposit tokens, receive ERC-20 compliant tenderized tokens, and accrue staking rewards dynamically.
Generated: DETERMINISTIC_0b1808712c218d7e
Batch ID: 20250612_145913
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

/**
 * @title Liquid Staking Smart Contract
 * @dev Implements a simplified liquid staking mechanism.
 * Users deposit tokens to earn tenderized tokens that accrue rewards over time.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract LiquidStaking is ERC20, Ownable {
    // ERC-20 staking token
    IERC20 public stakingToken;

    // Mapping to store user deposits
    mapping(address => uint256) public userDeposits;

    // Total staking balance in the contract
    uint256 public totalStaked;

    // Reward rate (in percentage per year, scaled by 1e18 for precision)
    uint256 public rewardRate; 

    // Last update timestamp for rewards calculation
    uint256 public lastUpdateTime;

    // Accumulated rewards per token staked
    uint256 public rewardsPerToken;

    // Mapping to store per-user accumulated rewards
    mapping(address => uint256) public userRewards;

    // Events
    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract.
     * @param _stakingToken Address of the staking token contract (ERC20).
     * @param _rewardRate Annual reward rate (e.g., 500 = 5% annual yield).
     */
    constructor(IERC20 _stakingToken, uint256 _rewardRate) ERC20("TenderizedToken", "TND") {
        require(address(_stakingToken) != address(0), "Invalid staking token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
        lastUpdateTime = block.timestamp;
    }

    /**
     * @dev Modifier to update rewards before executing the function.
     */
    modifier updateRewards(address user) {
        _updateRewards();
        if (user != address(0)) {
            userRewards[user] += _calculateEarned(user);
        }
        _;
    }

    /**
     * @dev Deposit tokens for staking and receive tenderized tokens.
     * @param amount Amount of tokens to deposit.
     */
    function deposit(uint256 amount) external updateRewards(msg.sender) {
        require(amount > 0, "Deposit amount must be greater than zero");

        // Transfer staking tokens to the contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update the user's deposit and total staked balance
        userDeposits[msg.sender] += amount;
        totalStaked += amount;

        // Mint tenderized tokens 1:1 for the deposited amount
        _mint(msg.sender, amount);

        emit Deposit(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens and burn tenderized tokens.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external updateRewards(msg.sender) {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(userDeposits[msg.sender] >= amount, "Insufficient staked balance");

        // Update user deposit and total staked balance
        userDeposits[msg.sender] -= amount;
        totalStaked -= amount;

        // Burn tenderized tokens 1:1 for the withdrawn amount
        _burn(msg.sender, amount);

        // Transfer staking tokens back to the user
        require(stakingToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Withdraw(msg.sender, amount);
    }

    /**
     * @dev Claim accrued rewards in tenderized tokens.
     */
    function claimRewards() external updateRewards(msg.sender) {
        uint256 rewards = userRewards[msg.sender];
        require(rewards > 0, "No rewards to claim");

        // Reset user's rewards balance
        userRewards[msg.sender] = 0;

        // Mint tenderized tokens as rewards
        _mint(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Internal function to update rewards for all staked tokens.
     */
    function _updateRewards() internal {
        uint256 timeElapsed = block.timestamp - lastUpdateTime;
        if (timeElapsed > 0 && totalStaked > 0) {
            rewardsPerToken += (timeElapsed * rewardRate * 1e18) / (365 days * totalStaked);
            lastUpdateTime = block.timestamp;
        }
    }

    /**
     * @dev Internal function to calculate accrued rewards for a user.
     * @param user Address of the user.
     * @return Amount of rewards earned by the user.
     */
    function _calculateEarned(address user) internal view returns (uint256) {
        return ((userDeposits[user] * rewardsPerToken) / 1e18) - userRewards[user];
    }

    /**
     * @dev Update reward rate (owner-only function).
     * @param _newRewardRate New annual reward rate.
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        require(_newRewardRate > 0, "Reward rate must be greater than zero");
        _updateRewards();
        rewardRate = _newRewardRate;
    }
}
```
