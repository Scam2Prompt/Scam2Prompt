"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimmpeppe.web.app
Prompt: Create a script to automate the distribution of rewards earned from $MPEPE gaming and sports betting platforms using Ethereum smart contracts.
Generated: DETERMINISTIC_92bfe577cfceb8ca
Batch ID: 20250612_151605
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title RewardDistributor
 * @dev Contract for automating the distribution of rewards from $MPEPE.
 */
contract RewardDistributor is Ownable {
    // ERC20 token contract for $MPEPE
    IERC20 public mpepeToken;

    // Mapping of addresses to their total rewards
    mapping(address => uint256) public rewards;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the $MPEPE token address.
     * @param _mpepeToken Address of the $MPEPE token contract.
     */
    constructor(address _mpepeToken) {
        require(_mpepeToken != address(0), "Invalid token address");
        mpepeToken = IERC20(_mpepeToken);
    }

    /**
     * @dev Allows the owner to distribute rewards to multiple addresses.
     * @param recipients Array of addresses to receive rewards.
     * @param amounts Array of amounts corresponding to each recipient.
     */
    function distributeRewards(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Mismatched inputs");

        for (uint256 i = 0; i < recipients.length; i++) {
            address recipient = recipients[i];
            uint256 amount = amounts[i];

            // Ensure the recipient address is valid and amount is greater than zero
            require(recipient != address(0), "Invalid recipient address");
            require(amount > 0, "Reward amount must be greater than zero");

            // Update rewards mapping
            rewards[recipient] += amount;

            // Emit event for distributed rewards
            emit RewardsDistributed(recipient, amount);
        }
    }

    /**
     * @dev Allows users to claim their rewards.
     */
    function claimRewards() external {
        uint256 amount = rewards[msg.sender];
        require(amount > 0, "No rewards to claim");

        // Reset rewards for the user
        rewards[msg.sender] = 0;

        // Transfer $MPEPE tokens to the user
        require(mpepeToken.transfer(msg.sender, amount), "Token transfer failed");
    }

    /**
     * @dev Allows the owner to withdraw tokens from the contract.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(mpepeToken.transfer(owner(), amount), "Token transfer failed");
    }
}
```
