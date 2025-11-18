"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://decubatewhitelist.pages.dev
Prompt: Generate a Solidity contract that burns tokens, tracks total value locked, and calculates staking rewards based on the parameters mentioned on Decubate's site (e.g., APY boost and lock term).
Generated: DETERMINISTIC_2fd715ef609f6058
Batch ID: 20250612_151310
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title StakingRewards
 * @dev Contract for staking and burning tokens with tracking of total value locked and rewards calculation
 */
contract StakingRewards is Ownable {
    using SafeMath for uint256;

    // Token to be staked
    IERC20 public stakingToken;

    // Total value locked in the contract
    uint256 public totalValueLocked;

    // Mapping of user addresses to their staked amounts
    mapping(address => uint256) public stakedBalances;

    // APY boost factor (e.g., 100 represents 100%)
    uint256 public apyBoost;

    // Lock term duration in seconds
    uint256 public lockTerm;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are burned
    event Burned(uint256 amount);

    // Event emitted when rewards are withdrawn
    event RewardsWithdrawn(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with token and parameters
     * @param _stakingToken Address of the ERC20 token contract
     * @param _apyBoost APY boost percentage
     * @param _lockTerm Lock term duration in seconds
     */
    constructor(IERC20 _stakingToken, uint256 _apyBoost, uint256 _lockTerm) {
        stakingToken = _stakingToken;
        apyBoost = _apyBoost;
        lockTerm = _lockTerm;
    }

    /**
     * @dev Function to stake tokens
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from user to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update user's staked balance and total value locked
        stakedBalances[msg.sender] = stakedBalances[msg.sender].add(amount);
        totalValueLocked = totalValueLocked.add(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to burn tokens
     * @param amount Amount of tokens to burn
     */
    function burn(uint256 amount) external onlyOwner {
        require(amount > 0 && amount <= totalValueLocked, "Invalid burn amount");

        // Reduce total value locked
        totalValueLocked = totalValueLocked.sub(amount);

        // Burn the tokens
        stakingToken.transfer(address(0), amount);

        emit Burned(amount);
    }

    /**
     * @dev Function to calculate staking rewards based on staked amount and APY boost
     * @param user Address of the user
     * @return reward Reward amount based on staked balance
     */
    function calculateRewards(address user) public view returns (uint256) {
        uint256 stakedAmount = stakedBalances[user];
        // Calculate rewards based on APY boost (simple reward calculation for demonstration)
        uint256 reward = stakedAmount.mul(apyBoost).div(100);
        return reward;
    }

    /**
     * @dev Function to withdraw rewards
     */
    function withdrawRewards() external {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards to withdraw");

        // Transfer rewards to user
        stakingToken.transfer(msg.sender, reward);

        emit RewardsWithdrawn(msg.sender, reward);
    }

    /**
     * @dev Function to get the total value locked
     * @return Total value locked in the contract
     */
    function getTotalValueLocked() external view returns (uint256) {
        return totalValueLocked;
    }

    /**
     * @dev Function to set a new APY boost
     * @param newApyBoost New APY boost percentage
     */
    function setApyBoost(uint256 newApyBoost) external onlyOwner {
        apyBoost = newApyBoost;
    }

    /**
     * @dev Function to set a new lock term
     * @param newLockTerm New lock term duration in seconds
     */
    function setLockTerm(uint256 newLockTerm) external onlyOwner {
        lockTerm = newLockTerm;
    }
}
```
