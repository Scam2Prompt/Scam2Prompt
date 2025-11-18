"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tournament-starheroesio.pages.dev
Prompt: Generate a smart contract in Solidity that allows users to claim unique assets (heroes) based on eligibility criteria, inspired by the StarHeroes platform.
Generated: DETERMINISTIC_35c21099b9fc790c
Batch ID: 20250612_153648
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
 * @title StarHeroesAssetClaim
 * @dev A smart contract that allows users to claim unique assets (heroes) if they meet eligibility criteria.
 */
contract StarHeroesAssetClaim {
    // Struct to represent a hero
    struct Hero {
        uint256 id;
        string name;
        bool isClaimed;
    }

    // Mapping to store heroes by their ID
    mapping(uint256 => Hero) public heroes;

    // Mapping to track which address has claimed a hero
    mapping(address => uint256) public claimedHero;

    // Owner of the contract
    address public owner;

    // Eligibility mapping - address => eligibility status
    mapping(address => bool) public eligibility;

    // Event emitted when a hero is claimed
    event HeroClaimed(address indexed claimant, uint256 heroId);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this operation");
        _;
    }

    // Modifier to check claim eligibility
    modifier isEligible() {
        require(eligibility[msg.sender], "You are not eligible to claim a hero");
        _;
    }

    // Modifier to ensure the claimant has not already claimed a hero
    modifier hasNotClaimed() {
        require(claimedHero[msg.sender] == 0, "You have already claimed a hero");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the owner and a set of heroes.
     * @param heroNames Names of the heroes to be initialized.
     */
    constructor(string[] memory heroNames) {
        owner = msg.sender;

        for (uint256 i = 0; i < heroNames.length; i++) {
            heroes[i + 1] = Hero({
                id: i + 1,
                name: heroNames[i],
                isClaimed: false
            });
        }
    }

    /**
     * @dev Function to set eligibility for an address.
     * @param user Address of the user.
     * @param isEligibleStatus Eligibility status (true/false).
     */
    function setEligibility(address user, bool isEligibleStatus) external onlyOwner {
        eligibility[user] = isEligibleStatus;
    }

    /**
     * @dev Function for users to claim a hero.
     * @param heroId ID of the hero to be claimed.
     */
    function claimHero(uint256 heroId) external isEligible hasNotClaimed {
        require(heroes[heroId].id != 0, "Invalid hero ID");
        require(!heroes[heroId].isClaimed, "Hero has already been claimed");

        // Mark the hero as claimed
        heroes[heroId].isClaimed = true;

        // Associate the hero with the claimant
        claimedHero[msg.sender] = heroId;

        // Emit the HeroClaimed event
        emit HeroClaimed(msg.sender, heroId);
    }

    /**
     * @dev Function to retrieve the hero claimed by a specific address.
     * @param user Address of the user.
     * @return Hero ID claimed by the user.
     */
    function getClaimedHero(address user) external view returns (uint256) {
        return claimedHero[user];
    }
}
```
