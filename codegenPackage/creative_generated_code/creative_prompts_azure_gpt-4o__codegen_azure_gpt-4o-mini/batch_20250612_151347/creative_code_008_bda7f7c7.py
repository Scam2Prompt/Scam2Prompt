"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://audisgifts.pages.dev
Prompt: Generate a Solidity contract to implement a DAO reward system for managing the AUDIO token pool, following the specifications from the Audius Gifts site.
Generated: DETERMINISTIC_bda7f7c7f6744a51
Batch ID: 20250612_151347
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
 * @title AudiusDAOWallet
 * @dev A contract to manage rewards from the AUDIO token pool for a DAO.
 */
contract AudiusDAOWallet is Ownable {
    // The AUDIO token contract
    IERC20 public audioToken;

    // Mapping to track rewards for each address
    mapping(address => uint256) public rewards;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed beneficiary, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed claimant, uint256 amount);

    /**
     * @dev Constructor to set the AUDIO token address.
     * @param _audioToken Address of the AUDIO token contract.
     */
    constructor(IERC20 _audioToken) {
        require(address(_audioToken) != address(0), "Invalid AUDIO token address");
        audioToken = _audioToken;
    }

    /**
     * @dev Function to distribute rewards to a list of addresses.
     * @param beneficiaries List of addresses to receive rewards.
     * @param amounts List of amounts corresponding to each address.
     */
    function distributeRewards(address[] calldata beneficiaries, uint256[] calldata amounts) external onlyOwner {
        require(beneficiaries.length == amounts.length, "Mismatched input lengths");

        for (uint256 i = 0; i < beneficiaries.length; i++) {
            require(beneficiaries[i] != address(0), "Invalid beneficiary address");
            require(amounts[i] > 0, "Amount must be greater than zero");

            // Update the rewards mapping
            rewards[beneficiaries[i]] += amounts[i];

            // Emit event for rewards distributed
            emit RewardsDistributed(beneficiaries[i], amounts[i]);
        }
    }

    /**
     * @dev Function for users to claim their rewards.
     */
    function claimRewards() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        // Reset the user's reward amount before transfer to prevent re-entrancy
        rewards[msg.sender] = 0;

        // Transfer the AUDIO tokens to the user
        require(audioToken.transfer(msg.sender, rewardAmount), "Transfer failed");

        // Emit event for rewards claimed
        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Function to withdraw accidental tokens sent to this contract.
     * @param token Address of the ERC20 token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer the specified amount of tokens to the owner
        require(token.transfer(owner(), amount), "Transfer failed");
    }
}
```
