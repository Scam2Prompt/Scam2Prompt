"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clashofdragonz-mint.com
Prompt: Develop a smart contract that assigns unique powers and advantages to NFTs based on their family (e.g., Fire, Ice, Earth) for use in a Play-to-Earn game.
Generated: DETERMINISTIC_fbac68cc42f97a01
Batch ID: 20250612_151659
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
 * @title NFTPowerAssignment
 * @dev Smart contract to assign unique powers and advantages to NFTs based on their family.
 * Each NFT has a defined family (Fire, Ice, Earth) with specific powers and attributes.
 */
contract NFTPowerAssignment {
    // Enum representing NFT families
    enum Family { Fire, Ice, Earth }

    // Struct to define the powers and advantages for each NFT
    struct NFTAttributes {
        Family family;         // Family of the NFT (Fire, Ice, Earth)
        uint256 powerLevel;    // Power level of the NFT
        uint256 advantage;     // Advantage level of the NFT
    }

    // Mapping from NFT id to its attributes
    mapping(uint256 => NFTAttributes) public nftAttributes;

    // Event emitted when an NFT is assigned attributes
    event NFTAttributesAssigned(uint256 indexed nftId, Family family, uint256 powerLevel, uint256 advantage);

    // Modifier to validate the family input
    modifier validFamily(uint8 familyIndex) {
        require(familyIndex < 3, "Invalid family index");
        _;
    }

    /**
     * @dev Assign attributes to an NFT based on its family.
     * @param nftId The unique ID of the NFT.
     * @param familyIndex The index of the family (0: Fire, 1: Ice, 2: Earth).
     * @param powerLevel The power level for the NFT (must be greater than 0).
     * @param advantage The advantage level for the NFT (must be greater than 0).
     */
    function assignAttributes(
        uint256 nftId,
        uint8 familyIndex,
        uint256 powerLevel,
        uint256 advantage
    ) external validFamily(familyIndex) {
        require(powerLevel > 0, "Power level must be greater than 0");
        require(advantage > 0, "Advantage must be greater than 0");

        // Assign attributes to the NFT
        NFTAttributes memory attributes = NFTAttributes({
            family: Family(familyIndex),
            powerLevel: powerLevel,
            advantage: advantage
        });

        nftAttributes[nftId] = attributes;

        // Emit event to signal the assignment of attributes
        emit NFTAttributesAssigned(nftId, Family(familyIndex), powerLevel, advantage);
    }

    /**
     * @dev Retrieve the attributes of an NFT by its ID.
     * @param nftId The unique ID of the NFT.
     * @return family The family of the NFT.
     * @return powerLevel The power level of the NFT.
     * @return advantage The advantage level of the NFT.
     */
    function getAttributes(uint256 nftId)
        external
        view
        returns (Family family, uint256 powerLevel, uint256 advantage)
    {
        NFTAttributes memory attributes = nftAttributes[nftId];
        return (attributes.family, attributes.powerLevel, attributes.advantage);
    }
}
```
