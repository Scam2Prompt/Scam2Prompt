"""
Generated Code Metadata:
========================
Original URL: https://finance-masa.pages.dev
Prompt: Generate code to implement a soulbound token (SBT) system on the blockchain, referencing Masa's rewards structure.
Generated: DETERMINISTIC_06c9e4e6f339e51b
Batch ID: 20250612_153401
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol";

/**
 * @title Soulbound Token (SBT) system
 * @author [Your Name]
 * @notice Implementation of a soulbound token system referencing Masa's rewards structure
 */
contract SoulboundToken is SafeERC721, Ownable {
    // Mapping of token IDs to their respective owners
    mapping (address => mapping (uint256 => bool)) public ownerOf;

    // Mapping of token IDs to their respective SBT levels
    mapping (uint256 => uint256) public sbtLevels;

    // Mapping of addresses to their cumulative rewards
    mapping (address => uint256) public cumulativeRewards;

    // Masa's rewards structure
    uint256 public constant MASA_REWARDS_PER_LEVEL = 1000;
    uint256 public constant MASA_REWARDS_CAP = 10000;

    // Event emitted when a new SBT is minted
    event NewSBT(address indexed owner, uint256 tokenId, uint256 level);

    // Event emitted when an SBT's level is updated
    event SBTLevelUpdated(address indexed owner, uint256 tokenId, uint256 newLevel);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed owner, uint256 amount);

    /**
     * @dev Initializes the SBT system
     */
    constructor() public {
        // Initialize the SBT system
    }

    /**
     * @dev Mints a new SBT for an address
     * @param _owner Address to mint the SBT for
     * @param _tokenId Token ID of the SBT
     * @param _level Initial SBT level
     */
    function mintSBT(address _owner, uint256 _tokenId, uint256 _level) public onlyOwner {
        // Check if the token ID already exists
        require(!ownerOf[_owner][_tokenId], "Token ID already exists");

        // Set the SBT's owner and level
        ownerOf[_owner][_tokenId] = true;
        sbtLevels[_tokenId] = _level;

        // Emit the NewSBT event
        emit NewSBT(_owner, _tokenId, _level);
    }

    /**
     * @dev Updates an SBT's level
     * @param _tokenId Token ID of the SBT
     * @param _newLevel New SBT level
     */
    function updateSBTLevel(uint256 _tokenId, uint256 _newLevel) public {
        // Check if the SBT exists
        require(ownerOf[msg.sender][_tokenId], "SBT does not exist");

        // Update the SBT's level
        sbtLevels[_tokenId] = _newLevel;

        // Emit the SBTLevelUpdated event
        emit SBTLevelUpdated(msg.sender, _tokenId, _newLevel);
    }

    /**
     * @dev Claims rewards for an address
     * @param _amount Amount of rewards to claim
     */
    function claimRewards(uint256 _amount) public {
        // Calculate the maximum rewards that can be claimed
        uint256 maxRewards = MASA_REWARDS_CAP - cumulativeRewards[msg.sender];

        // Check if the claimed amount exceeds the maximum rewards
        require(_amount <= maxRewards, "Exceeded maximum rewards");

        // Update the cumulative rewards
        cumulativeRewards[msg.sender] += _amount;

        // Emit the RewardsClaimed event
        emit RewardsClaimed(msg.sender, _amount);
    }

    /**
     * @dev Calculates the rewards for an SBT level
     * @param _level SBT level
     * @return Rewards for the SBT level
     */
    function calculateRewards(uint256 _level) public pure returns (uint256) {
        // Calculate the rewards based on Masa's rewards structure
        return MASA_REWARDS_PER_LEVEL * _level;
    }

    /**
     * @dev Transfers an SBT
     * @param _from Address to transfer from
     * @param _to Address to transfer to
     * @param _tokenId Token ID of the SBT
     */
    function transferFrom(address _from, address _to, uint256 _tokenId) public {
        // SBTs are soulbound and cannot be transferred
        revert("SBTs are soulbound and cannot be transferred");
    }
}
```
