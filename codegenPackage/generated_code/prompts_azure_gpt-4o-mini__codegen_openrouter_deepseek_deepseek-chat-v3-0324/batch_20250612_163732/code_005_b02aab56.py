"""
Generated Code Metadata:
========================
Original URL: https://wolfyyy.pages.dev
Prompt: Construct a smart contract in Solidity that governs the breeding mechanics of Wolves and Sheep within the Wolf Game ecosystem.
Generated: DETERMINISTIC_b02aab5670c028ad
Batch ID: 20250612_163732
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title WolfGameBreeding
 * @dev A smart contract that governs the breeding mechanics of Wolves and Sheep in the Wolf Game ecosystem.
 */
contract WolfGameBreeding is Ownable, ReentrancyGuard {
    IERC721 public wolfToken;
    IERC721 public sheepToken;

    uint256 public breedingCooldown = 1 days;
    uint256 public breedingFee = 0.1 ether;
    uint256 public sheepBreedingLimit = 3;

    struct BreedingRecord {
        uint256 lastBred;
        uint256 breedCount;
    }

    mapping(uint256 => BreedingRecord) public wolfBreedingRecords;
    mapping(uint256 => BreedingRecord) public sheepBreedingRecords;

    event BreedingSuccessful(
        uint256 wolfTokenId,
        uint256 sheepTokenId,
        uint256 newWolfTokenId,
        address indexed breeder
    );

    /**
     * @dev Constructor function
     * @param _wolfToken Address of the Wolf ERC721 token contract
     * @param _sheepToken Address of the Sheep ERC721 token contract
     */
    constructor(address _wolfToken, address _sheepToken) {
        require(_wolfToken != address(0), "Invalid Wolf Token address");
        require(_sheepToken != address(0), "Invalid Sheep Token address");

        wolfToken = IERC721(_wolfToken);
        sheepToken = IERC721(_sheepToken);
    }

    /**
     * @dev Set the breeding cooldown period
     * @param _cooldown New cooldown period in seconds
     */
    function setBreedingCooldown(uint256 _cooldown) external onlyOwner {
        breedingCooldown = _cooldown;
    }

    /**
     * @dev Set the breeding fee
     * @param _fee New breeding fee in wei
     */
    function setBreedingFee(uint256 _fee) external onlyOwner {
        breedingFee = _fee;
    }

    /**
     * @dev Set the sheep breeding limit
     * @param _limit New breeding limit for sheep
     */
    function setSheepBreedingLimit(uint256 _limit) external onlyOwner {
        sheepBreedingLimit = _limit;
    }

    /**
     * @dev Breed a wolf and sheep to produce a new wolf
     * @param _wolfTokenId ID of the wolf token
     * @param _sheepTokenId ID of the sheep token
     */
    function breed(uint256 _wolfTokenId, uint256 _sheepTokenId) external payable nonReentrant {
        require(msg.value >= breedingFee, "Insufficient breeding fee");
        require(
            wolfToken.ownerOf(_wolfTokenId) == msg.sender,
            "Caller must own the wolf"
        );
        require(
            sheepToken.ownerOf(_sheepTokenId) == msg.sender,
            "Caller must own the sheep"
        );

        BreedingRecord storage wolfRecord = wolfBreedingRecords[_wolfTokenId];
        BreedingRecord storage sheepRecord = sheepBreedingRecords[_sheepTokenId];

        require(
            block.timestamp >= wolfRecord.lastBred + breedingCooldown,
            "Wolf is on breeding cooldown"
        );
        require(
            sheepRecord.breedCount < sheepBreedingLimit,
            "Sheep has reached breeding limit"
        );

        wolfRecord.lastBred = block.timestamp;
        sheepRecord.lastBred = block.timestamp;
        sheepRecord.breedCount += 1;

        // In a real implementation, you would mint a new wolf token here
        uint256 newWolfTokenId = _simulateMintWolf(msg.sender);

        emit BreedingSuccessful(_wolfTokenId, _sheepTokenId, newWolfTokenId, msg.sender);

        // Refund excess fee
        if (msg.value > breedingFee) {
            payable(msg.sender).transfer(msg.value - breedingFee);
        }
    }

    /**
     * @dev Simulate minting a new wolf (placeholder for actual minting logic)
     * @param _to Address to receive the new wolf
     * @return newTokenId The ID of the newly minted wolf
     */
    function _simulateMintWolf(address _to) internal pure returns (uint256) {
        // In a real implementation, this would interact with your Wolf minting contract
        // This is just a placeholder that returns a dummy value
        return uint256(keccak256(abi.encodePacked(_to, block.timestamp)));
    }

    /**
     * @dev Withdraw collected breeding fees
     */
    function withdrawFees() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Check if a wolf can breed
     * @param _wolfTokenId ID of the wolf token
     * @return bool True if the wolf can breed
     */
    function canWolfBreed(uint256 _wolfTokenId) external view returns (bool) {
        return block.timestamp >= wolfBreedingRecords[_wolfTokenId].lastBred + breedingCooldown;
    }

    /**
     * @dev Check if a sheep can breed
     * @param _sheepTokenId ID of the sheep token
     * @return bool True if the sheep can breed
     */
    function canSheepBreed(uint256 _sheepTokenId) external view returns (bool) {
        return sheepBreedingRecords[_sheepTokenId].breedCount < sheepBreedingLimit;
    }
}
```
