"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://on-oeth.pages.dev
Prompt: Generate a Solidity contract that integrates with the Origin Dollar protocol to allow users to stake OGV tokens and earn governance rewards, including voting rights.
Generated: DETERMINISTIC_2697b2f3fcd6524d
Batch ID: 20250612_150613
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

// Importing necessary OpenZeppelin contracts for ERC20 interface and Ownable functionality
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title OGVStaking
 * @dev A contract to stake OGV tokens and earn governance rewards.
 */
contract OGVStaking is Ownable {
    // Declare state variables
    IERC20 public ogvToken; // OGV token contract
    uint256 public totalStaked; // Total amount of OGV tokens staked
    mapping(address => uint256) public stakedBalances; // User staked balances
    mapping(address => uint256) public rewardBalances; // User reward balances

    // Events for staking, unstaking, and rewards distribution
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the OGV token address.
     * @param _ogvToken The address of the OGV token contract.
     */
    constructor(IERC20 _ogvToken) {
        ogvToken = _ogvToken;
    }

    /**
     * @dev Stake OGV tokens to earn rewards.
     * @param amount The amount of OGV tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        require(ogvToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staked balances and total staked amount
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake OGV tokens and claim rewards.
     * @param amount The amount of OGV tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake 0 tokens");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update staked balances and total staked amount
        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer OGV tokens back to the user
        require(ogvToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);

        // Optionally, claim rewards here
        claimRewards();
    }

    /**
     * @dev Claims governance rewards for the caller.
     */
    function claimRewards() public {
        uint256 reward = rewardBalances[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Reset the user's reward balance
        rewardBalances[msg.sender] = 0;

        // Transfer rewards (assumed to be in OGV for simplicity)
        require(ogvToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculates and distributes rewards (to be called periodically).
     * @dev This function should be called by an external entity (e.g. a governance contract).
     * @param user The address of the user receiving rewards.
     * @param rewardAmount The amount of rewards to distribute.
     */
    function distributeRewards(address user, uint256 rewardAmount) external onlyOwner {
        require(totalStaked > 0, "No tokens staked");
        require(rewardAmount > 0, "No rewards to distribute");

        // Update the user's reward balance
        rewardBalances[user] += rewardAmount;
    }

    /**
     * @dev Fetches the staked balance of the caller.
     * @return The amount of OGV tokens staked by the caller.
     */
    function getStakedBalance() external view returns (uint256) {
        return stakedBalances[msg.sender];
    }

    /**
     * @dev Fetches the reward balance of the caller.
     * @return The amount of rewards available for the caller.
     */
    function getRewardBalance() external view returns (uint256) {
        return rewardBalances[msg.sender];
    }
}
```
