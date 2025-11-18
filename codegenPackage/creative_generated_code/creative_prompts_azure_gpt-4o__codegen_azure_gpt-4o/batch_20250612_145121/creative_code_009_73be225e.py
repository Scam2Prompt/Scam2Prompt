"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://looksrare.tech
Prompt: Write a Solidity contract that implements a reward distribution system for early adopters, similar to the token distribution model described for LOOKS tokens on LooksRare.
Generated: DETERMINISTIC_73be225ef7fd8c75
Batch ID: 20250612_145121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title RewardDistribution
 * @dev This contract implements a reward distribution system for early adopters.
 * It allows the distribution of ERC20 tokens to eligible addresses based on their contributions.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract RewardDistribution {
    // Address of the ERC20 token used for rewards
    IERC20 public rewardToken;

    // Address of the contract owner
    address public owner;

    // Mapping to track rewards for early adopters
    mapping(address => uint256) public rewards;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed recipient, uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    /**
     * @dev Constructor to initialize the reward token and owner address.
     * @param _rewardToken Address of the ERC20 token used for rewards.
     */
    constructor(IERC20 _rewardToken) {
        rewardToken = _rewardToken;
        owner = msg.sender;
    }

    /**
     * @dev Allows the owner to set rewards for early adopters.
     * @param recipients Array of recipient addresses.
     * @param amounts Array of reward amounts corresponding to each recipient.
     */
    function setRewards(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Mismatched arrays");
        for (uint256 i = 0; i < recipients.length; i++) {
            rewards[recipients[i]] = amounts[i];
        }
    }

    /**
     * @dev Allows recipients to claim their rewards.
     */
    function claimReward() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards available");
        require(rewardToken.balanceOf(address(this)) >= rewardAmount, "Insufficient contract balance");

        // Set rewards to zero before transferring to prevent reentrancy
        rewards[msg.sender] = 0;

        // Transfer the reward tokens to the recipient
        require(rewardToken.transfer(msg.sender, rewardAmount), "Transfer failed");

        emit RewardsDistributed(msg.sender, rewardAmount);
    }

    /**
     * @dev Allows the owner to withdraw remaining tokens from the contract.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        require(rewardToken.transfer(owner, amount), "Transfer failed");
    }

    /**
     * @dev Fallback function to prevent accidental ETH deposits.
     */
    receive() external payable {
        revert("ETH not accepted");
    }
}
```
