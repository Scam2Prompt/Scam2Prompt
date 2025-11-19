"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qhozali.pages.dev
Prompt: Generate a code snippet to integrate a memecoin and NFT hybrid on the Base platform as described on Ghozali's page.
Generated: DETERMINISTIC_6223a07c4f8814a5
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

// Importing the required OpenZeppelin contracts for ERC20 and ERC721
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Memecoin contract inheriting from ERC20
contract MemeCoin is ERC20, Ownable {
    // Initial supply of the memecoin
    uint256 public constant INITIAL_SUPPLY = 1_000_000 * 10 ** 18;

    // Constructor to mint initial supply to the deployer
    constructor() ERC20("MemeCoin", "MEME") {
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    // Function to mint new tokens (only owner can call)
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }

    // Function to burn tokens (only owner can call)
    function burn(uint256 amount) external onlyOwner {
        _burn(msg.sender, amount);
    }
}

// NFT contract inheriting from ERC721
contract MemeNFT is ERC721, Ownable {
    // Counter for tracking token IDs
    uint256 private _tokenIdCounter;

    // Event for minting new NFT
    event MintedNFT(address indexed owner, uint256 indexed tokenId);

    // Constructor to set the NFT name and symbol
    constructor() ERC721("MemeNFT", "MNFT") {}

    // Function to mint a new NFT
    function mintNFT(address to) external onlyOwner {
        uint256 tokenId = _tokenIdCounter;
        _safeMint(to, tokenId);
        emit MintedNFT(to, tokenId);
        _tokenIdCounter++;
    }

    // Function to burn an NFT (only owner can call)
    function burnNFT(uint256 tokenId) external onlyOwner {
        _burn(tokenId);
    }
}

// Hybrid contract integrating both memecoin and NFT functionality
contract MemeCoinNFTHybrid is Ownable {
    MemeCoin public memeCoin;
    MemeNFT public memeNFT;

    // Event for staking actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Mapping to track user stakes
    mapping(address => uint256) public stakes;

    // Constructor to deploy both contracts
    constructor() {
        memeCoin = new MemeCoin();
        memeNFT = new MemeNFT();
    }

    // Function to stake memecoins
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(memeCoin.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        stakes[msg.sender] += amount;
        emit Staked(msg.sender, amount);
    }

    // Function to unstake memecoins
    function unstake(uint256 amount) external {
        require(stakes[msg.sender] >= amount, "Insufficient staked amount");

        stakes[msg.sender] -= amount;
        require(memeCoin.transfer(msg.sender, amount), "Transfer failed");
        emit Unstaked(msg.sender, amount);
    }

    // Function to mint NFT after staking
    function mintNFTAfterStaking() external {
        require(stakes[msg.sender] > 0, "You need to stake before minting NFT");

        memeNFT.mintNFT(msg.sender);
    }
}
```
