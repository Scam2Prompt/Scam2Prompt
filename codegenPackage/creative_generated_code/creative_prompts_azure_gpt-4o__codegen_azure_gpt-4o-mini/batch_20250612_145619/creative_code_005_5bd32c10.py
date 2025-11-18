"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bogeonbase.pages.dev
Prompt: Develop a smart contract for staking $BOGE tokens on the Base blockchain. Include functionality for depositing tokens, calculating rewards, and withdrawing tokens.
Generated: DETERMINISTIC_5bd32c1053923cbd
Batch ID: 20250612_145619
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

// Import OpenZeppelin's ERC20 interface and SafeMath library for safe arithmetic operations
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title BOGEStaking
 * @dev A smart contract for staking BOGE tokens
 */
contract BOGEStaking {
    using SafeMath for uint256;

    // Token to be staked
    IERC20 public token;

    // Mapping of user addresses to their staked amounts and reward debts
    mapping(address => uint256) public stakedAmounts;
    mapping(address => uint256) public rewardDebts;

    // Total staked amount
    uint256 public totalStaked;

    // Reward per block for simplicity
    uint256 public rewardRate = 1 ether; // Example: 1 BOGE per block

    // Event emitted when tokens are deposited
    event Deposited(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    constructor(address _tokenAddress) {
        token = IERC20(_tokenAddress);
    }

    /**
     * @dev Deposit BOGE tokens for staking
     * @param amount Amount of tokens to stake
     */
    function deposit(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from user to this contract
        token.transferFrom(msg.sender, address(this), amount);

        // Calculate pending rewards
        uint256 pendingRewards = calculateRewards(msg.sender);

        // Update user state
        stakedAmounts[msg.sender] = stakedAmounts[msg.sender].add(amount);
        totalStaked = totalStaked.add(amount);
        rewardDebts[msg.sender] = rewardDebts[msg.sender].add(pendingRewards);

        emit Deposited(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked BOGE tokens and claim rewards
     * @param amount Amount of tokens to withdraw
     */
    function withdraw(uint256 amount) external {
        require(stakedAmounts[msg.sender] >= amount, "Insufficient staked amount");

        // Calculate pending rewards
        uint256 pendingRewards = calculateRewards(msg.sender);

        // Update user state
        stakedAmounts[msg.sender] = stakedAmounts[msg.sender].sub(amount);
        totalStaked = totalStaked.sub(amount);
        rewardDebts[msg.sender] = rewardDebts[msg.sender].add(pendingRewards);

        // Transfer tokens back to user
        token.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
        if (pendingRewards > 0) {
            emit RewardsClaimed(msg.sender, pendingRewards);
            token.transfer(msg.sender, pendingRewards);
        }
    }

    /**
     * @dev Calculate rewards for a user
     * @param user Address of the user
     * @return uint256 Calculated rewards
     */
    function calculateRewards(address user) public view returns (uint256) {
        return stakedAmounts[user].mul(rewardRate).div(1 ether).sub(rewardDebts[user]);
    }

    /**
     * @dev Allow user to claim their rewards
     */
    function claimRewards() external {
        uint256 pendingRewards = calculateRewards(msg.sender);
        require(pendingRewards > 0, "No rewards to claim");

        // Reset reward debt
        rewardDebts[msg.sender] = rewardDebts[msg.sender].add(pendingRewards);

        // Transfer rewards to user
        token.transfer(msg.sender, pendingRewards);
        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    /**
     * @dev Get the total amount of rewards earned by a user
     * @param user Address of the user
     * @return uint256 Total rewards earned
     */
    function getTotalRewards(address user) external view returns (uint256) {
        return calculateRewards(user);
    }
}
```
