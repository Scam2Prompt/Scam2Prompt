"""
Generated Code Metadata:
========================
Original URL: https://chain-sourcesmart.pages.dev
Prompt: Write a Solidity smart contract that interacts with a DAO like Lil Nouns to manage NFT contributions and rewards, inspired by the DAO examples on the Chain Source Smart webpage.
Generated: DETERMINISTIC_49928d1f190039f0
Batch ID: 20250612_155852
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol": {
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
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";

/**
 * @title LilNounsDAOInteraction
 * @author [Your Name]
 * @notice This contract interacts with a DAO like Lil Nouns to manage NFT contributions and rewards.
 */
contract LilNounsDAOInteraction {
    using SafeMath for uint256;
    using SafeERC721 for *;

    // Mapping of contributor addresses to their contribution amounts
    mapping (address => uint256) public contributions;

    // Mapping of contributor addresses to their reward NFTs
    mapping (address => uint256) public rewards;

    // The Lil Nouns DAO contract address
    address public lilNounsDAO;

    // The NFT contract address
    address public nftContract;

    // Event emitted when a contribution is made
    event ContributionMade(address indexed contributor, uint256 amount);

    // Event emitted when a reward is claimed
    event RewardClaimed(address indexed contributor, uint256 nftId);

    /**
     * @dev Constructor
     * @param _lilNounsDAO The Lil Nouns DAO contract address
     * @param _nftContract The NFT contract address
     */
    constructor(address _lilNounsDAO, address _nftContract) public {
        lilNounsDAO = _lilNounsDAO;
        nftContract = _nftContract;
    }

    /**
     * @dev Make a contribution to the DAO
     * @param _amount The amount to contribute
     */
    function makeContribution(uint256 _amount) public {
        // Check if the contribution amount is valid
        require(_amount > 0, "Contribution amount must be greater than 0");

        // Transfer funds to the DAO
        // Assuming the DAO has a function to receive funds
        // For simplicity, this example uses a fictional function
        // In a real-world scenario, use a standard method like transferFrom
        bool sent = payable(lilNounsDAO).send(_amount);
        require(sent, "Failed to send funds to DAO");

        // Update the contributor's contribution amount
        contributions[msg.sender] = contributions[msg.sender].add(_amount);

        // Emit an event
        emit ContributionMade(msg.sender, _amount);
    }

    /**
     * @dev Claim a reward NFT
     * @param _nftId The ID of the reward NFT
     */
    function claimReward(uint256 _nftId) public {
        // Check if the contributor has a reward NFT
        require(rewards[msg.sender] == 0, "Contributor already has a reward NFT");

        // Check if the NFT exists and is owned by the DAO
        // Assuming the NFT contract has a function to check ownership
        // For simplicity, this example uses a fictional function
        // In a real-world scenario, use a standard method like ownerOf
        require(IERC721(nftContract).ownerOf(_nftId) == lilNounsDAO, "NFT does not exist or is not owned by the DAO");

        // Transfer the NFT to the contributor
        IERC721(nftContract).safeTransferFrom(lilNounsDAO, msg.sender, _nftId);

        // Update the contributor's reward NFT
        rewards[msg.sender] = _nftId;

        // Emit an event
        emit RewardClaimed(msg.sender, _nftId);
    }

    /**
     * @dev Get the contributor's contribution amount
     * @param _contributor The contributor's address
     * @return The contributor's contribution amount
     */
    function getContribution(address _contributor) public view returns (uint256) {
        return contributions[_contributor];
    }

    /**
     * @dev Get the contributor's reward NFT
     * @param _contributor The contributor's address
     * @return The contributor's reward NFT ID
     */
    function getReward(address _contributor) public view returns (uint256) {
        return rewards[_contributor];
    }
}

interface IERC721 {
    function ownerOf(uint256 tokenId) external view returns (address);
    function safeTransferFrom(address from, address to, uint256 tokenId) external;
}
```
