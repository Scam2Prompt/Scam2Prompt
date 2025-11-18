"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lightchain.live-apps.com
Prompt: Develop a smart contract for token allocation and presale management using Lightchain AI’s tokenomics structure.
Generated: DETERMINISTIC_38dcd3479bcaeb0e
Batch ID: 20250612_145615
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

// Importing OpenZeppelin's ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// A smart contract for token allocation and presale management
contract TokenPresale is ERC20, Ownable, ReentrancyGuard {
    // Total supply of tokens
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10 ** decimals();
    // Presale price per token (in wei)
    uint256 public presalePrice;
    // Amount of tokens sold during presale
    uint256 public tokensSold;
    // Indicates if presale is active
    bool public presaleActive;

    // Event declarations
    event PresaleStarted(uint256 price);
    event PresaleEnded();
    event TokensPurchased(address buyer, uint256 amount);

    // Constructor to initialize token details
    constructor(string memory name, string memory symbol, uint256 _presalePrice) 
        ERC20(name, symbol) {
        _mint(address(this), TOTAL_SUPPLY); // Mint tokens to the contract
        presalePrice = _presalePrice; // Set presale price
        presaleActive = false; // Set presale status to inactive
    }

    // Function to start the presale
    function startPresale() external onlyOwner {
        require(!presaleActive, "Presale is already active");
        presaleActive = true;
        emit PresaleStarted(presalePrice);
    }

    // Function to end the presale
    function endPresale() external onlyOwner {
        require(presaleActive, "Presale is not active");
        presaleActive = false;
        emit PresaleEnded();
    }

    // Function to purchase tokens during the presale
    function purchaseTokens(uint256 amount) external payable nonReentrant {
        require(presaleActive, "Presale is not active");
        require(msg.value == amount * presalePrice, "Incorrect Ether amount sent");
        require(tokensSold + amount <= TOTAL_SUPPLY, "Not enough tokens available");

        tokensSold += amount;
        _transfer(address(this), msg.sender, amount); // Transfer tokens to buyer

        emit TokensPurchased(msg.sender, amount);
    }

    // Function to withdraw funds from presale
    function withdrawFunds() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to prevent Ether from being sent directly to the contract
    receive() external payable {
        revert("Direct payments not allowed. Use the purchaseTokens function.");
    }

    // Function to get the remaining tokens available for presale
    function remainingTokens() external view returns (uint256) {
        return TOTAL_SUPPLY - tokensSold;
    }
}
```
