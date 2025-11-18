"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retrobridge.pages.dev
Prompt: Develop a smart contract that interacts with RetroBridge to facilitate cross-chain swaps and reward users with Soulbound NFTs.
Generated: DETERMINISTIC_926eb2f8c3c63ebe
Batch ID: 20250612_151611
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

// Importing OpenZeppelin contracts for safe math operations and ERC721 implementations
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for RetroBridge to facilitate cross-chain swaps
interface IRetroBridge {
    function swapTokens(address token, uint256 amount, address recipient, uint256 destinationChain) external returns (bool);
}

// Soulbound NFT contract for rewarding users
contract SoulboundNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    
    // Counter for minting NFTs
    Counters.Counter private _tokenIdCounter;
    
    // Mapping to keep track of whether an address has received a Soulbound NFT
    mapping(address => bool) private _hasSoulbound;

    // Event emitted when a user receives a Soulbound NFT
    event SoulboundMinted(address indexed user, uint256 tokenId);

    // Constructor to initialize the ERC721 token
    constructor() ERC721("SoulboundNFT", "SBNFT") {}

    // Function to mint a Soulbound NFT
    function mintSoulboundNFT(address to) external onlyOwner {
        require(!_hasSoulbound[to], "User already has a Soulbound NFT");

        uint256 tokenId = _tokenIdCounter.current();
        _mint(to, tokenId);
        _hasSoulbound[to] = true;
        _tokenIdCounter.increment();

        emit SoulboundMinted(to, tokenId);
    }
}

// Main contract to handle cross-chain swaps and NFT rewards
contract CrossChainSwapper is Ownable {
    IRetroBridge public retroBridge;
    SoulboundNFT public soulboundNFT;

    // Event emitted when a swap is executed
    event SwapExecuted(address indexed user, address token, uint256 amount, uint256 destinationChain);

    // Constructor to initialize the RetroBridge and SoulboundNFT contracts
    constructor(address _retroBridge, address _soulboundNFT) {
        require(_retroBridge != address(0), "Invalid RetroBridge address");
        require(_soulboundNFT != address(0), "Invalid SoulboundNFT address");

        retroBridge = IRetroBridge(_retroBridge);
        soulboundNFT = SoulboundNFT(_soulboundNFT);
    }

    // Function to perform cross-chain swaps
    function executeSwap(address token, uint256 amount, uint256 destinationChain) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer the tokens from the user to this contract
        // This assumes the user has already approved this contract to spend their tokens
        bool success = retroBridge.swapTokens(token, amount, msg.sender, destinationChain);
        require(success, "Token swap failed");

        // Mint a Soulbound NFT as a reward
        soulboundNFT.mintSoulboundNFT(msg.sender);

        emit SwapExecuted(msg.sender, token, amount, destinationChain);
    }

    // Function to update the RetroBridge address (onlyOwner)
    function updateRetroBridge(address _retroBridge) external onlyOwner {
        require(_retroBridge != address(0), "Invalid address");
        retroBridge = IRetroBridge(_retroBridge);
    }
}
```
