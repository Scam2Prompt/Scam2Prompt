"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bruhxdrop.web.app
Prompt: Develop a smart contract for the $BRUH token pre-sale that incorporates Helio's payment platform and supports free transactions.
Generated: DETERMINISTIC_ea795eca20fb91ee
Batch ID: 20250612_153659
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

// Importing OpenZeppelin's ERC20 token implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Smart contract for the $BRUH token pre-sale
contract BruhToken is ERC20, Ownable {
    using SafeMath for uint256;

    // State variables
    uint256 public constant MAX_SUPPLY = 1_000_000 * 10**18; // Total supply of $BRUH tokens
    uint256 public tokenPrice; // Price of $BRUH token in wei
    bool public isPresaleActive; // Presale status

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleStatusChanged(bool isActive);

    // Constructor to initialize the token
    constructor(uint256 _tokenPrice) ERC20("BRUH Token", "BRUH") {
        require(_tokenPrice > 0, "Token price must be greater than zero");
        tokenPrice = _tokenPrice;
        isPresaleActive = false; // Presale is inactive at the start
    }

    // Function to start the presale
    function startPresale() external onlyOwner {
        isPresaleActive = true;
        emit PresaleStatusChanged(true);
    }

    // Function to stop the presale
    function stopPresale() external onlyOwner {
        isPresaleActive = false;
        emit PresaleStatusChanged(false);
    }

    // Function to purchase tokens during the presale
    function purchaseTokens(uint256 tokenAmount) external payable {
        require(isPresaleActive, "Presale is not active");
        require(tokenAmount > 0, "Token amount must be greater than zero");

        uint256 totalCost = tokenAmount.mul(tokenPrice);
        require(msg.value >= totalCost, "Insufficient ETH sent");

        // Check if the token supply limit is reached
        require(totalSupply().add(tokenAmount) <= MAX_SUPPLY, "Max supply exceeded");

        // Mint the tokens to the buyer
        _mint(msg.sender, tokenAmount);
        emit TokensPurchased(msg.sender, tokenAmount);

        // Refund excess ETH if applicable
        if (msg.value > totalCost) {
            payable(msg.sender).transfer(msg.value.sub(totalCost));
        }
    }

    // Function to withdraw funds from the contract
    function withdrawFunds() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to accept ETH
    receive() external payable {}
}
```
