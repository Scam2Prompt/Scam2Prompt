"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nanagetxyz.web.app
Prompt: Create a smart contract for a meme-based token pre-sale (e.g., $CHILL) that integrates Solana payments and QR code functionality.
Generated: DETERMINISTIC_2cacca305b55e2e6
Batch ID: 20250612_152710
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

// Importing OpenZeppelin's ERC20 Contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for the meme-based token $CHILL
contract ChillToken is ERC20, Ownable {
    // State variable to hold the token price in SOL
    uint256 public tokenPrice;
    // State variable to track the total tokens sold
    uint256 public totalTokensSold;
    // State variable for the presale active status
    bool public presaleActive;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("ChillToken", "$CHILL") {
        tokenPrice = 0.01 ether; // Price set to 0.01 SOL per token
        presaleActive = false; // Presale is initially inactive
    }

    // Modifier to check if presale is active
    modifier whenPresaleActive() {
        require(presaleActive, "Presale is not active.");
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

    // Function to purchase tokens during presale
    function purchaseTokens(uint256 tokenAmount) external payable whenPresaleActive {
        require(msg.value == tokenAmount * tokenPrice, "Incorrect Ether sent.");
        require(totalSupply() + tokenAmount <= 1000000 * 10 ** decimals(), "Purchase exceeds supply.");

        // Minting tokens to the buyer's address
        _mint(msg.sender, tokenAmount);
        totalTokensSold += tokenAmount;

        // Emit the TokensPurchased event
        emit TokensPurchased(msg.sender, tokenAmount);
    }

    // Function to withdraw the collected funds
    function withdrawFunds() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to set the price of tokens
    function setTokenPrice(uint256 newPrice) external onlyOwner {
        tokenPrice = newPrice;
    }

    // Function to retrieve the current token price
    function getTokenPrice() external view returns (uint256) {
        return tokenPrice;
    }
}
```

Please note that QR code functionality is typically handled on the front-end and not directly in a smart contract. You can use libraries such as `qrcode` in JavaScript or similar libraries in your preferred front-end technology to generate QR codes based on the payment information.
