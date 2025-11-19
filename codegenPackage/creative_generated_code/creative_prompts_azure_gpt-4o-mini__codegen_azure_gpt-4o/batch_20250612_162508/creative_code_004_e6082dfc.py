"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://y00topianft.web.app
Prompt: Illustrate how to implement a smart contract for minting y00ts NFTs based on the details from the y00topia project.
Generated: DETERMINISTIC_e6082dfc5d974934
Batch ID: 20250612_162508
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
 * @title Y00tsNFT
 * @dev A smart contract for minting y00ts NFTs as part of the y00topia project.
 */
contract Y00tsNFT {
    // State variables
    address public owner; // Contract owner
    uint256 public totalSupply; // Total number of NFTs minted
    uint256 public maxSupply; // Maximum number of NFTs allowed
    uint256 public mintPrice; // Price for minting an NFT
    mapping(uint256 => address) private tokenOwners; // Mapping from token ID to owner
    mapping(address => uint256[]) private ownerTokens; // Mapping from owner address to their tokens

    // Events
    event Mint(address indexed minter, uint256 indexed tokenId);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Constructor to initialize the contract
    constructor(uint256 _maxSupply, uint256 _mintPrice) {
        require(_maxSupply > 0, "Max supply must be greater than zero");
        require(_mintPrice > 0, "Mint price must be greater than zero");

        owner = msg.sender;
        maxSupply = _maxSupply;
        mintPrice = _mintPrice;
    }

    // Modifier to check if caller is the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Function to mint a new NFT
    function mint() external payable {
        require(totalSupply < maxSupply, "Max supply reached");
        require(msg.value >= mintPrice, "Insufficient funds for minting");

        uint256 newTokenId = totalSupply + 1; // Generate a new token ID
        tokenOwners[newTokenId] = msg.sender; // Assign token ownership
        ownerTokens[msg.sender].push(newTokenId); // Track ownership
        totalSupply++; // Increment total supply

        emit Mint(msg.sender, newTokenId); // Emit Mint event
    }

    // Function to get the tokens owned by an address
    function tokensOfOwner(address _owner) external view returns (uint256[] memory) {
        return ownerTokens[_owner];
    }

    // Function to transfer contract ownership
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "New owner address cannot be zero");
        emit OwnershipTransferred(owner, _newOwner);
        owner = _newOwner;
    }

    // Function to withdraw contract balance (only owner)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance; // Get contract balance
        require(balance > 0, "No balance to withdraw");
        payable(owner).transfer(balance); // Transfer balance to owner
    }

    // Function to fallback for receiving Ether directly
    receive() external payable {
        // Accept Ether deposits; useful for donations or funding
    }
}
```
