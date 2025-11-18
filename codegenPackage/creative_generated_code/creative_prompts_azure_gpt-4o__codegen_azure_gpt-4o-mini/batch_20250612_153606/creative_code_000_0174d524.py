"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gofurs-cash.pages.dev
Prompt: Write a smart contract in Solidity that implements the ERC404 token standard, including the functionality to mint an NFT when the token balance exceeds 1 and burn the NFT when the balance drops below 1. Ensure compatibility with Uniswap V3 pools.
Generated: DETERMINISTIC_0174d5240124d9c5
Batch ID: 20250612_153606
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

// Importing the necessary interfaces for ERC20 and ERC721
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// ERC404Token is a standard ERC20 token that also mints and burns an NFT based on its token balance
contract ERC404Token is ERC20, Ownable {
    using Counters for Counters.Counter;

    // NFT contract to be minted and burned
    ERC721 public nftContract;
    // Counter for NFT IDs
    Counters.Counter private _nftIdCounter;

    // Event emitted when an NFT is minted
    event NftMinted(address indexed owner, uint256 indexed tokenId);
    // Event emitted when an NFT is burned
    event NftBurned(address indexed owner, uint256 indexed tokenId);

    // Mapping to track ownership of NFTs
    mapping(address => uint256) public nftOwnership;

    // Constructor to initialize the token
    constructor(string memory name, string memory symbol, address _nftContract) ERC20(name, symbol) {
        nftContract = ERC721(_nftContract);
    }

    // Mint new ERC20 tokens
    function mintTokens(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
        checkAndUpdateNft(to);
    }

    // Override the _burn function to include NFT burning logic
    function _burn(address account, uint256 amount) internal override {
        super._burn(account, amount);
        checkAndUpdateNft(account);
    }

    // Function to check the balance and manage NFT minting/burning
    function checkAndUpdateNft(address account) internal {
        uint256 balance = balanceOf(account);

        if (balance > 1 && nftOwnership[account] == 0) {
            // Mint NFT if balance exceeds 1 and no NFT exists
            _nftIdCounter.increment();
            uint256 newNftId = _nftIdCounter.current();
            nftContract.mint(account, newNftId);
            nftOwnership[account] = newNftId;
            emit NftMinted(account, newNftId);
        } else if (balance <= 1 && nftOwnership[account] != 0) {
            // Burn NFT if balance drops below 1
            uint256 nftId = nftOwnership[account];
            nftContract.burn(nftId);
            nftOwnership[account] = 0;
            emit NftBurned(account, nftId);
        }
    }
}

// Assume ERC721 is implemented with mint and burn functions
contract SimpleNFT is ERC721, Ownable {
    constructor() ERC721("SimpleNFT", "SNFT") {}

    // Mint a new NFT
    function mint(address to, uint256 tokenId) external onlyOwner {
        _safeMint(to, tokenId);
    }

    // Burn an NFT
    function burn(uint256 tokenId) external onlyOwner {
        _burn(tokenId);
    }
}
```
