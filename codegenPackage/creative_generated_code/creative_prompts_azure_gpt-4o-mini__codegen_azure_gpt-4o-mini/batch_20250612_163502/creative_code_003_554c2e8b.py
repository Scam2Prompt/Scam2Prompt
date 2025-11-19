"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thehuskyinu-io.pages.dev
Prompt: Explain how to implement a deflationary token model similar to $HINU, including token burning mechanisms and community rewards as outlined in the tokenomics section.
Generated: DETERMINISTIC_554c2e8bd6581b53
Batch ID: 20250612_163502
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DeflationaryToken
 * @dev Implementation of a deflationary token model with burning and community rewards.
 */
contract DeflationaryToken is ERC20, Ownable {
    // Total tokens burned
    uint256 public totalBurned;

    // Event emitted on token burn
    event TokensBurned(address indexed burner, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(uint256 totalReward, uint256 numberOfRecipients);

    // Mapping for community rewards
    mapping(address => uint256) public rewards;

    // Total reward pool
    uint256 public rewardPool;

    // Constructor to initialize the token
    constructor(uint256 initialSupply) ERC20("DeflationaryToken", "DFT") {
        _mint(msg.sender, initialSupply);
        rewardPool = 0;
    }

    /**
     * @dev Burns a specified amount of tokens from the caller's address.
     * @param amount The amount of tokens to be burned.
     */
    function burn(uint256 amount) external {
        require(amount > 0, "Burn amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        _burn(msg.sender, amount);
        totalBurned += amount;

        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @dev Allows the owner to distribute rewards to community members.
     * @param recipients The list of addresses to receive rewards.
     * @param rewardPerRecipient The amount of reward each recipient should receive.
     */
    function distributeRewards(address[] calldata recipients, uint256 rewardPerRecipient) external onlyOwner {
        require(recipients.length > 0, "No recipients provided");
        require(rewardPerRecipient > 0, "Reward must be greater than zero");
        require(rewardPool >= recipients.length * rewardPerRecipient, "Insufficient reward pool");

        for (uint256 i = 0; i < recipients.length; i++) {
            rewards[recipients[i]] += rewardPerRecipient;
        }

        rewardPool -= recipients.length * rewardPerRecipient;
        
        emit RewardsDistributed(recipients.length * rewardPerRecipient, recipients.length);
    }

    /**
     * @dev Function for users to claim their accumulated rewards.
     */
    function claimRewards() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        rewards[msg.sender] = 0;  // Reset the user's rewards
        _mint(msg.sender, rewardAmount); // Mint new tokens as rewards
    }

    /**
     * @dev Allows the owner to add to the reward pool.
     * @param amount The amount of tokens to add to the reward pool.
     */
    function addToRewardPool(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        _mint(address(this), amount);
        rewardPool += amount;
    }

    /**
     * @dev Gets the total supply of the token, accounting for burned tokens.
     * @return The total supply of the token.
     */
    function totalSupply() public view virtual override returns (uint256) {
        return super.totalSupply() - totalBurned;
    }
}
```
