"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-community.web.app
Prompt: Develop a smart contract in Solidity for a "Mystery Box NFT" system that includes free minting functionality and a reward distribution mechanism.
Generated: DETERMINISTIC_1b16e67427ee375e
Batch ID: 20250612_145931
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

// Importing ERC721 and Ownable from OpenZeppelin contracts for NFT implementation and ownership control
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MysteryBoxNFT is ERC721Enumerable, Ownable {
    // Event emitted when a new NFT is minted
    event Minted(address indexed owner, uint256 indexed tokenId);
    
    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed recipient, uint256 amount);

    // Base URI for NFT metadata
    string private baseURI;

    // Reward distribution pool
    uint256 public totalRewards;
    
    // Mapping to track claimed rewards by each address
    mapping(address => uint256) public claimedRewards;

    // Counter for the token IDs
    uint256 private _tokenIdCounter;

    constructor(string memory name, string memory symbol, string memory _baseURI) 
        ERC721(name, symbol) 
    {
        baseURI = _baseURI;
    }

    // Function to mint a new Mystery Box NFT for free
    function mint() external {
        uint256 tokenId = _tokenIdCounter++;
        _safeMint(msg.sender, tokenId);
        emit Minted(msg.sender, tokenId);
    }

    // Function to set the base URI for the NFT metadata
    function setBaseURI(string memory _baseURI) external onlyOwner {
        baseURI = _baseURI;
    }

    // Override the base URI function to serve the correct metadata URL
    function _baseURI() internal view override returns (string memory) {
        return baseURI;
    }

    // Function to distribute rewards to an address
    function distributeRewards(address recipient, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(totalRewards + amount >= totalRewards, "Overflow detected in rewards distribution");
        
        totalRewards += amount;
        claimedRewards[recipient] += amount;
        emit RewardsDistributed(recipient, amount);
    }

    // Function to claim rewards for the caller
    function claimRewards() external {
        uint256 amount = claimedRewards[msg.sender];
        require(amount > 0, "No rewards to claim");

        claimedRewards[msg.sender] = 0; // Reset claimed rewards
        // Here you would transfer the rewards, e.g., using an ERC20 token contract
        // This is just a placeholder to show the logic
        // token.transfer(msg.sender, amount);

        emit RewardsDistributed(msg.sender, amount);
    }

    // Function to get the total rewards claimed by an address
    function getClaimedRewards(address user) external view returns (uint256) {
        return claimedRewards[user];
    }
}
```
