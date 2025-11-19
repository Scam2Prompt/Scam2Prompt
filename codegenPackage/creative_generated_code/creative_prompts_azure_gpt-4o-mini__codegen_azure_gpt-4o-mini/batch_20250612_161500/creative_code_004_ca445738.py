"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qhozali.pages.dev
Prompt: Provide an example of a smart contract for a memecoin that incorporates NFT features, inspired by the Ghozali 404 project.
Generated: DETERMINISTIC_ca445738edf97757
Batch ID: 20250612_161500
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

// Importing OpenZeppelin contracts for ERC20 and ERC721 functionalities
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Creating a Memecoin contract that extends ERC20
contract Memecoin is ERC20, Ownable {
    // Mapping to track if an NFT has been minted
    mapping(uint256 => bool) public mintedNFTs;

    // The constructor sets the token name and symbol
    constructor() ERC20("Memecoin", "MEME") {
        // Mint initial supply to the deployer
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }

    // Function to mint new Memecoins
    function mintMemecoin(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        _mint(msg.sender, amount);
    }

    // Function to burn Memecoins
    function burnMemecoin(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        _burn(msg.sender, amount);
    }
}

// Creating an NFT contract that extends ERC721
contract MemecoinNFT is ERC721, Ownable {
    // Counter for the total number of NFTs minted
    uint256 public totalSupply;

    // Memecoin instance for interacting with the token
    Memecoin public memecoin;

    // Events for NFT minting and burning
    event NFTMinted(address indexed owner, uint256 indexed tokenId);
    event NFTBurned(address indexed owner, uint256 indexed tokenId);

    // The constructor initializes the NFT contract and sets the Memecoin instance
    constructor(address _memecoinAddress) ERC721("MemecoinNFT", "MNFT") {
        memecoin = Memecoin(_memecoinAddress);
    }

    // Function to mint a new NFT
    function mintNFT() external {
        // Ensure that the sender has enough Memecoins to mint an NFT
        require(memecoin.balanceOf(msg.sender) >= 100 * 10 ** memecoin.decimals(), "Insufficient Memecoins");
        
        // Transfer Memecoins to the contract as payment
        memecoin.burn(100 * 10 ** memecoin.decimals());

        // Increment the total supply and mint the new NFT
        totalSupply++;
        _mint(msg.sender, totalSupply);
        
        // Emit the NFT minting event
        emit NFTMinted(msg.sender, totalSupply);
    }

    // Function to burn an NFT
    function burnNFT(uint256 tokenId) external {
        require(ownerOf(tokenId) == msg.sender, "You are not the owner of this NFT");
        
        // Burn the NFT
        _burn(tokenId);
        
        // Emit the NFT burning event
        emit NFTBurned(msg.sender, tokenId);
    }
}
```
