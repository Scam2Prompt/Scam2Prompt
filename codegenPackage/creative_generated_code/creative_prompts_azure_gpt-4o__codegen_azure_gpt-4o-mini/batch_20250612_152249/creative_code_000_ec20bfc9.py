"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skytradefinance.com
Prompt: Write a smart contract in Solidity for staking $SHE tokens on the Arbitrum blockchain, ensuring the ability to calculate APY and distribute rewards based on the SHE Protocol's yield farming mechanism.
Generated: DETERMINISTIC_ec20bfc9a7ae2e48
Batch ID: 20250612_152249
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

// Import the interface for the ERC20 standard
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title SHEStaking
 * @dev A smart contract for staking SHE tokens, calculating APY, and distributing rewards.
 */
contract SHEStaking is Ownable {
    // The SHE token contract
    IERC20 public sheToken;

    // Struct to hold information about each staker
    struct Staker {
        uint256 amount; // Amount staked
        uint256 lastUpdated; // Last timestamp when the staker updated their stake
        uint256 rewards; // Earned rewards
    }

    // Mapping of stakers
    mapping(address => Staker) public stakers;

    // APY in percentage (e.g., 10 means 10% per year)
    uint256 public apy;
    // Total staked amount
    uint256 public totalStaked;

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the SHE token address and initial APY.
     * @param _sheToken The address of the SHE token contract.
     * @param _apy The initial Annual Percentage Yield (APY).
     */
    constructor(IERC20 _sheToken, uint256 _apy) {
        sheToken = _sheToken;
        apy = _apy;
    }

    /**
     * @dev Function to stake SHE tokens.
     * @param amount The amount of SHE tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount should be greater than 0");

        // Update rewards before staking
        updateRewards(msg.sender);

        // Transfer SHE tokens from the staker to this contract
        sheToken.transferFrom(msg.sender, address(this), amount);

        // Update staker information
        stakers[msg.sender].amount += amount;
        stakers[msg.sender].lastUpdated = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to unstake SHE tokens.
     * @param amount The amount of SHE tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount should be greater than 0");
        require(stakers[msg.sender].amount >= amount, "Insufficient staked amount");

        // Update rewards before unstaking
        updateRewards(msg.sender);

        // Update staker information
        stakers[msg.sender].amount -= amount;
        totalStaked -= amount;

        // Transfer SHE tokens back to the staker
        sheToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Function to claim rewards.
     */
    function claimRewards() external {
        updateRewards(msg.sender);
        uint256 rewardAmount = stakers[msg.sender].rewards;
        require(rewardAmount > 0, "No rewards to claim");

        // Reset the staker's rewards to zero
        stakers[msg.sender].rewards = 0;

        // Transfer rewards (you might want to implement a reward token)
        // For simplicity, we assume SHE tokens are used as rewards
        sheToken.transfer(msg.sender, rewardAmount);

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Internal function to update the rewards of a staker.
     * @param stakerAddress The address of the staker.
     */
    function updateRewards(address stakerAddress) internal {
        Staker storage staker = stakers[stakerAddress];

        // If the staker has staked tokens, calculate rewards
        if (staker.amount > 0) {
            uint256 timeStaked = block.timestamp - staker.lastUpdated;
            uint256 reward = (staker.amount * apy * timeStaked) / (365 days * 100); // Calculate rewards
            staker.rewards += reward;
            staker.lastUpdated = block.timestamp; // Update last updated time
        }
    }

    /**
     * @dev Function to set a new APY.
     * @param newApy The new Annual Percentage Yield (APY).
     */
    function setAPY(uint256 newApy) external onlyOwner {
        apy = newApy;
    }

    /**
     * @dev Function to withdraw tokens from the contract (for emergency).
     * @param amount The amount of SHE tokens to withdraw.
     */
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount <= sheToken.balanceOf(address(this)), "Insufficient balance");
        sheToken.transfer(msg.sender, amount);
    }
}
```
