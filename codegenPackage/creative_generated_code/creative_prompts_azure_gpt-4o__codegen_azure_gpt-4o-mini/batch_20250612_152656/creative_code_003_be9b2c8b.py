"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ghozali-49z.pages.dev
Prompt: Provide an example of how to create a hybrid memecoin and NFT smart contract, inspired by "Ghozali 404," on the Base platform.
Generated: DETERMINISTIC_be9b2c8be77129b0
Batch ID: 20250612_152656
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

// Import OpenZeppelin's ERC721 and Ownable contracts
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// HybridMemecoinNFT contract definition
contract HybridMemecoinNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // State variables to track token information
    Counters.Counter private _tokenIdCounter;
    string public baseTokenURI;

    // Memecoin-related variables
    mapping(address => uint256) public balances;
    string public constant name = "Ghozali 404 Memecoin";
    string public constant symbol = "GHZ404";
    uint256 public totalSupply;
    uint256 public constant maxSupply = 1000000 * 10**18; // 1 million memecoins

    // Events for logging
    event Minted(address indexed recipient, uint256 tokenId);
    event Purchased(address indexed buyer, uint256 amount);

    // Constructor to initialize the contract
    constructor(string memory _baseTokenURI) ERC721("Ghozali 404 NFT", "G404") {
        baseTokenURI = _baseTokenURI;
    }

    // Override the tokenURI function to return the base URI
    function _baseURI() internal view override returns (string memory) {
        return baseTokenURI;
    }

    // Function to mint a new NFT
    function mintNFT() external onlyOwner {
        require(_tokenIdCounter.current() < maxSupply, "Max supply reached");
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        _tokenIdCounter.increment();
        emit Minted(msg.sender, tokenId);
    }

    // Function to buy memecoins
    function buyMemecoin(uint256 amount) external payable {
        require(msg.value > 0, "Send ether to purchase memecoins");
        require(totalSupply + amount <= maxSupply, "Exceeds max supply");
        
        // Calculate the price of memecoins (1 ether = 1000 memecoins)
        uint256 price = amount * (1 ether / 1000);
        require(msg.value >= price, "Insufficient ether sent");

        // Update the balances and total supply
        balances[msg.sender] += amount;
        totalSupply += amount;
        emit Purchased(msg.sender, amount);

        // Refund excess ether
        if (msg.value > price) {
            payable(msg.sender).transfer(msg.value - price);
        }
    }

    // Function to withdraw contract balance to owner
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner()).transfer(balance);
    }

    // Function to check the balance of memecoins for a specific address
    function getMemecoinBalance(address account) external view returns (uint256) {
        return balances[account];
    }

    // Fallback function to handle accidental ether transfers
    receive() external payable {
        revert("Please use the buyMemecoin function");
    }
}
```
