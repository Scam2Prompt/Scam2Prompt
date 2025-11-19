"""
Generated Code Metadata:
========================
Original URL: https://thegraph.live
Prompt: "Create a code snippet in Solidity to implement a smart contract that distributes rewards in GRT based on The Graph's M1 to M8 business tiers."
Generated: DETERMINISTIC_f6178cd5fc4ec04d
Batch ID: 20250622_205603
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

// Importing the ERC20 interface for GRT token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract RewardDistributor {
    // State variables
    IERC20 public grtToken; // The GRT token contract
    address public owner; // Owner of the contract

    // Mapping to store the business tier of each address
    mapping(address => uint8) public businessTiers;

    // Events for logging
    event RewardsDistributed(address indexed recipient, uint256 amount);
    event TierUpdated(address indexed account, uint8 tier);

    // Constructor to initialize the contract with the GRT token address
    constructor(address _grtToken) {
        require(_grtToken != address(0), "Invalid GRT token address");
        grtToken = IERC20(_grtToken);
        owner = msg.sender; // Set the contract deployer as the owner
    }

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Function to update the business tier of an account
    function updateBusinessTier(address account, uint8 tier) external onlyOwner {
        require(tier >= 1 && tier <= 8, "Tier must be between 1 and 8");
        businessTiers[account] = tier;
        emit TierUpdated(account, tier);
    }

    // Function to distribute rewards based on business tier
    function distributeRewards(address[] calldata recipients) external onlyOwner {
        require(recipients.length > 0, "No recipients provided");

        for (uint256 i = 0; i < recipients.length; i++) {
            address recipient = recipients[i];
            uint8 tier = businessTiers[recipient];

            // Calculate reward based on tier
            uint256 rewardAmount = calculateReward(tier);

            // Ensure the contract has enough GRT tokens to distribute
            require(grtToken.balanceOf(address(this)) >= rewardAmount, "Insufficient GRT balance");

            // Transfer the reward to the recipient
            grtToken.transfer(recipient, rewardAmount);
            emit RewardsDistributed(recipient, rewardAmount);
        }
    }

    // Internal function to calculate reward based on business tier
    function calculateReward(uint8 tier) internal pure returns (uint256) {
        // Define reward amounts for each tier
        if (tier == 1) return 100 * 10**18; // 100 GRT for Tier 1
        if (tier == 2) return 200 * 10**18; // 200 GRT for Tier 2
        if (tier == 3) return 300 * 10**18; // 300 GRT for Tier 3
        if (tier == 4) return 400 * 10**18; // 400 GRT for Tier 4
        if (tier == 5) return 500 * 10**18; // 500 GRT for Tier 5
        if (tier == 6) return 600 * 10**18; // 600 GRT for Tier 6
        if (tier == 7) return 700 * 10**18; // 700 GRT for Tier 7
        if (tier == 8) return 800 * 10**18; // 800 GRT for Tier 8
        return 0; // Default case
    }

    // Function to withdraw any remaining GRT tokens from the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(grtToken.balanceOf(address(this)) >= amount, "Insufficient GRT balance");
        grtToken.transfer(owner, amount);
    }
}
```
