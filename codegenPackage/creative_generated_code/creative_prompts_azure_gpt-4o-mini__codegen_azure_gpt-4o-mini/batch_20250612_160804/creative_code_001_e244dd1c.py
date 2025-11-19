"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ronin-cyberkongz.pages.dev
Prompt: Write a Solidity contract that utilizes the Guardian Contract for on-chain two-factor authentication for NFTs.
Generated: DETERMINISTIC_e244dd1c47d6ae35
Batch ID: 20250612_160804
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

// Interface for the Guardian contract
interface IGuardian {
    function isAuthorized(address user, bytes32 messageHash, bytes memory signature) external view returns (bool);
}

// NFT Contract with Guardian for two-factor authentication
contract AuthenticatedNFT {
    string public name; // Name of the NFT collection
    string public symbol; // Symbol of the NFT collection
    
    // Mapping from token ID to owner address
    mapping(uint256 => address) private _owners;
    // Mapping from owner address to number of tokens owned
    mapping(address => uint256) private _balances;
    // Mapping from token ID to approved address
    mapping(uint256 => address) private _tokenApprovals;
    
    // Guardian contract address
    IGuardian public guardianContract;

    // Event emitted when a new NFT is minted
    event Minted(address indexed to, uint256 indexed tokenId);
    
    // Modifier to check if the caller is the owner of the token
    modifier onlyOwner(uint256 tokenId) {
        require(ownerOf(tokenId) == msg.sender, "Not the token owner");
        _;
    }

    // Constructor to initialize the NFT contract
    constructor(string memory _name, string memory _symbol, address _guardianAddress) {
        name = _name;
        symbol = _symbol;
        guardianContract = IGuardian(_guardianAddress);
    }

    // Function to mint a new NFT with two-factor authentication
    function mint(address to, uint256 tokenId, bytes32 messageHash, bytes memory signature) public {
        // Check if the user is authorized via guardian contract
        require(guardianContract.isAuthorized(to, messageHash, signature), "User not authorized");
        
        // Mint the NFT
        _mint(to, tokenId);
    }

    // Internal function to handle minting logic
    function _mint(address to, uint256 tokenId) internal {
        require(to != address(0), "Cannot mint to zero address");
        require(_owners[tokenId] == address(0), "Token already minted");

        _owners[tokenId] = to;
        _balances[to] += 1;

        emit Minted(to, tokenId);
    }

    // Function to get the owner of a token ID
    function ownerOf(uint256 tokenId) public view returns (address) {
        address owner = _owners[tokenId];
        require(owner != address(0), "Token does not exist");
        return owner;
    }

    // Function to get the balance of an address
    function balanceOf(address owner) public view returns (uint256) {
        require(owner != address(0), "Address zero is not valid");
        return _balances[owner];
    }

    // Function to approve another address to transfer a specific token ID
    function approve(address to, uint256 tokenId) public onlyOwner(tokenId) {
        _tokenApprovals[tokenId] = to;
    }

    // Function to get the approved address for a token ID
    function getApproved(uint256 tokenId) public view returns (address) {
        return _tokenApprovals[tokenId];
    }
}
```
