"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retik-claims.pages.dev
Prompt: Develop a Solidity smart contract for managing Retik's tier-based rewards system, including cashback percentages and card costs.
Generated: DETERMINISTIC_2a3b409b5382a477
Batch ID: 20250612_153713
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

/**
 * @title RetikTierRewards
 * @dev A smart contract to manage Retik's tier-based rewards system.
 * It includes cashback percentages and card costs for different tiers.
 */
contract RetikTierRewards {
    // Struct to define a tier
    struct Tier {
        string name;          // Name of the tier
        uint256 cashback;     // Cashback percentage (e.g., 5 means 5%)
        uint256 cost;         // Cost of the tier card in wei
    }

    // Mapping to store tiers by their ID (e.g., 1 for Silver, 2 for Gold)
    mapping(uint256 => Tier) public tiers;

    // Variable to track the total number of tiers
    uint256 public totalTiers;

    // Address of the contract owner
    address public owner;

    // Modifier to restrict function access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this operation.");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner.
     */
    constructor() {
        owner = msg.sender; // Set the deployer as the owner
    }

    /**
     * @dev Function to add a new rewards tier.
     * @param _name Name of the tier (e.g., Silver, Gold, Platinum)
     * @param _cashback Cashback percentage for this tier (integer value)
     * @param _cost Cost of the tier card in wei
     */
    function addTier(string memory _name, uint256 _cashback, uint256 _cost) public onlyOwner {
        require(bytes(_name).length > 0, "Tier name cannot be empty.");
        require(_cashback > 0, "Cashback percentage must be greater than 0.");
        require(_cost > 0, "Tier cost must be greater than 0.");

        totalTiers++;
        tiers[totalTiers] = Tier(_name, _cashback, _cost);
    }

    /**
     * @dev Function to update an existing tier.
     * @param _id ID of the tier to update
     * @param _name New name of the tier
     * @param _cashback New cashback percentage for this tier
     * @param _cost New cost of the tier card in wei
     */
    function updateTier(uint256 _id, string memory _name, uint256 _cashback, uint256 _cost) public onlyOwner {
        require(_id > 0 && _id <= totalTiers, "Invalid tier ID.");
        require(bytes(_name).length > 0, "Tier name cannot be empty.");
        require(_cashback > 0, "Cashback percentage must be greater than 0.");
        require(_cost > 0, "Tier cost must be greater than 0.");

        tiers[_id] = Tier(_name, _cashback, _cost);
    }

    /**
     * @dev Function to fetch tier details by ID.
     * @param _id ID of the tier to fetch
     * @return Tier details including name, cashback percentage, and card cost
     */
    function getTier(uint256 _id) public view returns (Tier memory) {
        require(_id > 0 && _id <= totalTiers, "Invalid tier ID.");
        return tiers[_id];
    }
}
```
