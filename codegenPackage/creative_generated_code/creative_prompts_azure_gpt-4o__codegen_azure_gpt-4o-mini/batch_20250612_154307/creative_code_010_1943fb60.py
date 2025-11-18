"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoallstars-3ts.pages.dev
Prompt: Write a Solidity contract that implements a reward distribution mechanism for $STARS holders, ensuring higher rewards for larger token holdings, as described in the Crypto All-Stars tokenomics.
Generated: DETERMINISTIC_1943fb6032be838e
Batch ID: 20250612_154307
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

/**
 * @title RewardDistributor
 * @dev This contract distributes rewards to $STARS token holders based on the amount they hold.
 * Higher holdings result in higher rewards.
 */
contract RewardDistributor is Ownable {
    IERC20 public starsToken; // The $STARS token contract

    // Total rewards pool
    uint256 public totalRewards;

    // Mapping to keep track of rewards for each address
    mapping(address => uint256) public rewards;
    
    // Mapping to keep track of last claimed rewards for each address
    mapping(address => uint256) public lastClaimed;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed holder, uint256 amount);

    // Constructor to initialize the contract with the $STARS token address
    constructor(address _starsToken) {
        require(_starsToken != address(0), "Invalid token address");
        starsToken = IERC20(_starsToken);
    }

    /**
     * @dev Allows the owner to deposit rewards into the pool.
     * @param amount The amount of rewards to deposit.
     */
    function depositRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        totalRewards += amount;
        // Transfer rewards from owner to this contract
        bool sent = starsToken.transferFrom(msg.sender, address(this), amount);
        require(sent, "Transfer failed");
    }

    /**
     * @dev Distributes rewards to $STARS holders based on their holdings.
     * This function can be called multiple times to distribute rewards.
     */
    function distributeRewards() external {
        uint256 totalSupply = starsToken.totalSupply();
        require(totalSupply > 0, "No tokens minted");

        // Calculate rewards for each holder
        for (uint256 i = 0; i < totalSupply; i++) {
            address holder = starsToken.holderAt(i); // Hypothetical function for example
            uint256 balance = starsToken.balanceOf(holder);

            if (balance > 0) {
                uint256 reward = (totalRewards * balance) / totalSupply;
                rewards[holder] += reward;
                emit RewardsDistributed(holder, reward);
            }
        }
        // Reset total rewards after distribution
        totalRewards = 0;
    }

    /**
     * @dev Allows holders to claim their rewards.
     */
    function claimRewards() external {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Reset claimed rewards for the caller
        rewards[msg.sender] = 0;

        // Transfer rewards to the caller
        bool sent = starsToken.transfer(msg.sender, reward);
        require(sent, "Transfer failed");
    }

    /**
     * @dev Get the rewards balance for a specific holder.
     * @param holder The address of the token holder.
     * @return The amount of rewards available for the holder.
     */
    function getRewardsBalance(address holder) external view returns (uint256) {
        return rewards[holder];
    }
}
```
