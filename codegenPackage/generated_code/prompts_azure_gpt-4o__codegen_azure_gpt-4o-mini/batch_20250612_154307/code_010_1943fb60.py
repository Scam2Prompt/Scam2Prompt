"""
Generated Code Metadata:
========================
Original URL: https://cryptoallstars-3ts.pages.dev
Prompt: Write a Solidity contract that implements a reward distribution mechanism for $STARS holders, ensuring higher rewards for larger token holdings, as described in the Crypto All-Stars tokenomics.
Generated: DETERMINISTIC_1943fb6032be838e
Batch ID: 20250612_154307
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

// Importing the ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title StarsRewardDistribution
 * @dev A contract for distributing rewards to $STARS token holders based on their holdings.
 */
contract StarsRewardDistribution is Ownable {
    // The ERC20 token contract
    IERC20 public starsToken;

    // Total rewards distributed
    uint256 public totalRewards;

    // Mapping to track rewards for each holder
    mapping(address => uint256) public rewards;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed holder, uint256 amount);

    /**
     * @dev Constructor to set the $STARS token address.
     * @param _starsToken Address of the $STARS token contract.
     */
    constructor(address _starsToken) {
        require(_starsToken != address(0), "Invalid token address");
        starsToken = IERC20(_starsToken);
    }

    /**
     * @dev Distributes rewards to all $STARS holders based on their holdings.
     * @param totalRewardAmount The total amount of rewards to distribute.
     */
    function distributeRewards(uint256 totalRewardAmount) external onlyOwner {
        require(totalRewardAmount > 0, "Reward amount must be greater than zero");
        require(starsToken.totalSupply() > 0, "No tokens in circulation");

        // Calculate rewards for each holder
        uint256 totalSupply = starsToken.totalSupply();
        for (uint256 i = 0; i < totalSupply; i++) {
            address holder = starsToken.holderAt(i); // Assuming holderAt is a function that returns the holder's address
            uint256 holderBalance = starsToken.balanceOf(holder);
            if (holderBalance > 0) {
                uint256 reward = (holderBalance * totalRewardAmount) / totalSupply;
                rewards[holder] += reward;
                emit RewardsDistributed(holder, reward);
            }
        }
        totalRewards += totalRewardAmount;
    }

    /**
     * @dev Allows holders to claim their accumulated rewards.
     */
    function claimRewards() external {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Reset the reward for the holder
        rewards[msg.sender] = 0;

        // Transfer the rewards to the holder
        require(starsToken.transfer(msg.sender, reward), "Transfer failed");
    }

    /**
     * @dev Allows the owner to withdraw any tokens sent to the contract by mistake.
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(starsToken), "Cannot withdraw $STARS tokens");
        IERC20(token).transfer(owner(), amount);
    }
}
```
