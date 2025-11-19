"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-dogcoin.pages.dev
Prompt: Develop a Solidity contract that enables users to buy $DOG tokens at the specified rates during the presale phase.
Generated: DETERMINISTIC_96c1e5871f3f1c9e
Batch ID: 20250612_162228
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

// Importing OpenZeppelin's ERC20 and Ownable contracts
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for the $DOG token
contract DogToken is ERC20, Ownable {
    // Token price in wei (adjust for your presale)
    uint256 public tokenPrice;
    // Boolean to track presale status
    bool public presaleActive;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 totalCost);

    // Constructor to initialize token name, symbol, presale price, and status
    constructor(uint256 _initialSupply, uint256 _tokenPrice) ERC20("DogToken", "$DOG") {
        _mint(msg.sender, _initialSupply * (10 ** decimals())); // Mint initial supply to the owner
        tokenPrice = _tokenPrice;
        presaleActive = false; // Presale is initially inactive
    }

    // Modifier to check if presale is active
    modifier onlyDuringPresale() {
        require(presaleActive, "Presale is not active");
        _;
    }

    // Function to start the presale
    function startPresale() external onlyOwner {
        presaleActive = true;
    }

    // Function to stop the presale
    function stopPresale() external onlyOwner {
        presaleActive = false;
    }

    // Function to buy tokens during the presale
    function buyTokens(uint256 _amount) external payable onlyDuringPresale {
        uint256 totalCost = tokenPrice * _amount;

        // Check if the value sent is sufficient
        require(msg.value >= totalCost, "Insufficient Ether sent");

        // Mint the requested amount of tokens to the buyer
        _mint(msg.sender, _amount * (10 ** decimals()));

        // Emit the purchase event
        emit TokensPurchased(msg.sender, _amount, totalCost);
        
        // Refund excess Ether, if any
        if (msg.value > totalCost) {
            payable(msg.sender).transfer(msg.value - totalCost);
        }
    }

    // Function to withdraw Ether from the contract
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
