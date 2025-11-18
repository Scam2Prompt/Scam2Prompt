"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubeta-presales.pages.dev
Prompt: Write a smart contract in Solidity for staking $QUBE tokens that distributes rewards based on a 5% sell tax, as described in InQubeta's tokenomics.
Generated: DETERMINISTIC_9f5f007a1b81c787
Batch ID: 20250612_153420
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

// Importing required interfaces for ERC20 token and Ownable contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title QUBEStaking
 * @dev A smart contract for staking QUBE tokens with reward distribution based on sell tax.
 */
contract QUBEStaking is Ownable {
    // The QUBE token contract
    IERC20 public qubeToken;

    // Total staked amount
    uint256 public totalStaked;

    // Mapping of stakers and their stakes
    mapping(address => uint256) public stakes;

    // Events for tracking staking and reward distribution
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsDistributed(uint256 totalRewards);

    // Constructor to initialize the QUBE token contract
    constructor(address _qubeToken) {
        require(_qubeToken != address(0), "Invalid token address");
        qubeToken = IERC20(_qubeToken);
    }

    /**
     * @dev Stake QUBE tokens
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(qubeToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staking details
        stakes[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake QUBE tokens
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender] >= amount, "Insufficient staked amount");

        // Update staking details
        stakes[msg.sender] -= amount;
        totalStaked -= amount;

        require(qubeToken.transfer(msg.sender, amount), "Transfer failed");
        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Distribute rewards based on a 5% sell tax.
     * The contract should be funded with QUBE tokens representing the rewards.
     */
    function distributeRewards() external onlyOwner {
        uint256 totalRewards = qubeToken.balanceOf(address(this));
        require(totalRewards > 0, "No rewards available");

        // Distributing rewards to all stakers
        for (uint256 i = 0; i < totalStaked; i++) {
            // Calculate user share based on their stake
            address staker = address(uint160(i)); // This should be replaced by actual staker addresses
            uint256 userShare = (stakes[staker] * totalRewards) / totalStaked;

            if (userShare > 0) {
                require(qubeToken.transfer(staker, userShare), "Reward transfer failed");
            }
        }

        emit RewardsDistributed(totalRewards);
    }

    /**
     * @dev Get the staked amount of a user
     * @param user Address of the user
     * @return The amount staked by the user
     */
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user];
    }

    /**
     * @dev Get the total amount staked in the contract
     * @return Total staked amount
     */
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }
}
```
