"""
Generated Code Metadata:
========================
Original URL: https://chain-sourcesmart.pages.dev
Prompt: Write a Solidity smart contract that interacts with a DAO like Lil Nouns to manage NFT contributions and rewards, inspired by the DAO examples on the Chain Source Smart webpage.
Generated: DETERMINISTIC_49928d1f190039f0
Batch ID: 20250612_155852
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

// Importing OpenZeppelin's ERC721 implementation for NFTs
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the DAO to interact with
interface IDAO {
    function contribute(uint256 amount) external;
    function rewardContributors(address contributor, uint256 rewardAmount) external;
}

// NFT contract for managing contributions and rewards
contract ContributionNFT is ERC721Enumerable, Ownable {
    // Struct to hold contributor information
    struct Contributor {
        uint256 contributions;
        uint256 rewards;
    }

    // Mapping from token ID to Contributor information
    mapping(uint256 => Contributor) public contributors;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed contributor, uint256 rewardAmount);

    // Counter for token IDs
    uint256 private _tokenIdCounter;

    // DAO contract address
    IDAO public dao;

    // Constructor to initialize the contract
    constructor(string memory name, string memory symbol, address daoAddress) ERC721(name, symbol) {
        dao = IDAO(daoAddress);
    }

    // Function to mint a new NFT for a contributor
    function mintNFT(address to) external onlyOwner {
        _tokenIdCounter++;
        _mint(to, _tokenIdCounter);
        emit NFTMinted(to, _tokenIdCounter);
    }

    // Function to contribute to the DAO
    function contributeToDAO(uint256 amount) external {
        require(amount > 0, "Contribution must be greater than zero");
        
        // Call the DAO's contribute function
        dao.contribute(amount);
        
        // Update contributor's contributions
        uint256 tokenId = tokenOfOwnerByIndex(msg.sender, balanceOf(msg.sender) - 1);
        contributors[tokenId].contributions += amount;
    }

    // Function to distribute rewards to contributors
    function distributeRewards(address contributor, uint256 rewardAmount) external onlyOwner {
        require(rewardAmount > 0, "Reward amount must be greater than zero");
        
        // Call the DAO's reward function
        dao.rewardContributors(contributor, rewardAmount);
        
        // Update contributor's rewards
        uint256 tokenId = tokenOfOwnerByIndex(contributor, balanceOf(contributor) - 1);
        contributors[tokenId].rewards += rewardAmount;

        emit RewardsDistributed(contributor, rewardAmount);
    }

    // Function to get contributor information
    function getContributorInfo(uint256 tokenId) external view returns (Contributor memory) {
        return contributors[tokenId];
    }
}
```
