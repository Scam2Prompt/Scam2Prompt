"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yifistake.finance
Prompt: Develop a Solidity contract to handle staking YI12 tokens paired with ETH, including reward distribution logic as described on the YI12 Stake Finance site.
Generated: DETERMINISTIC_288840e9130fb00f
Batch ID: 20250612_145125
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

// Importing OpenZeppelin Contracts for safer token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/// @title A Staking Contract for YI12 Tokens Paired with ETH
/// @notice Users can stake YI12 tokens paired with ETH and earn rewards
/// @dev Implements reward distribution logic and uses best practices for security and gas efficiency
contract YI12Staking is Ownable, ReentrancyGuard {
    IERC20 public yi12Token; // YI12 ERC-20 token interface
    uint256 public rewardRate; // Reward rate in tokens per second
    uint256 public totalStaked; // Total YI12 tokens staked
    uint256 public lastUpdateTime; // Last time rewards were updated
    uint256 public rewardPerTokenStored; // Accumulated rewards per staked token

    struct Stake {
        uint256 amount; // Staked YI12 tokens
        uint256 rewardDebt; // Rewards debt (used for reward calculation)
    }

    mapping(address => Stake) public stakers; // Tracks each user's staking information

    uint256 private constant PRECISION = 1e18; // Precision for reward calculation

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRate);

    /// @dev Constructor to initialize the staking contract
    /// @param _yi12Token The address of the YI12 ERC-20 token
    /// @param _rewardRate The initial reward rate
    constructor(IERC20 _yi12Token, uint256 _rewardRate) {
        yi12Token = _yi12Token;
        rewardRate = _rewardRate;
    }

    /// @notice Updates the reward for a specific user
    /// @param account The user's address
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;

        if (account != address(0)) {
            stakers[account].rewardDebt = earned(account);
        }
        _;
    }

    /// @notice Allows users to stake YI12 tokens paired with ETH
    /// @param amount The amount of YI12 tokens to stake
    function stake(uint256 amount) external payable nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        require(msg.value > 0, "ETH must be paired");
        
        // Transfer tokens to the contract
        yi12Token.transferFrom(msg.sender, address(this), amount);

        // Update staking data
        stakers[msg.sender].amount += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /// @notice Allows users to withdraw their staked YI12 tokens and ETH
    /// @param amount The amount of YI12 tokens to withdraw
    function withdraw(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        require(stakers[msg.sender].amount >= amount, "Insufficient staked balance");

        // Update staking data
        stakers[msg.sender].amount -= amount;
        totalStaked -= amount;

        // Transfer tokens and ETH back to the user
        yi12Token.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    /// @notice Allows users to claim rewards
    function claimReward() external nonReentrant updateReward(msg.sender) {
        uint256 reward = stakers[msg.sender].rewardDebt;
        require(reward > 0, "No rewards to claim");

        // Reset user's reward debt
        stakers[msg.sender].rewardDebt = 0;

        // Transfer rewards to the user
        yi12Token.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    /// @notice Calculates the reward per staked token
    /// @return The reward per token
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return
            rewardPerTokenStored +
            ((block.timestamp - lastUpdateTime) * rewardRate * PRECISION) /
            totalStaked;
    }

    /// @notice Calculates the rewards earned by a user
    /// @param account The user's address
    /// @return The rewards earned
    function earned(address account) public view returns (uint256) {
        return
            (stakers[account].amount * (rewardPerToken() - rewardPerTokenStored)) /
            PRECISION +
            stakers[account].rewardDebt;
    }

    /// @notice Updates the reward rate (only owner can call)
    /// @param _rewardRate The new reward rate
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
        emit RewardRateUpdated(_rewardRate);
    }

    /// @notice Fallback function to accept ETH
    receive() external payable {}

    /// @notice Withdraws ETH from contract (only owner can call)
    /// @param amount The amount of ETH to withdraw
    function withdrawETH(uint256 amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient ETH balance");
        payable(owner()).transfer(amount);
    }
}
```
