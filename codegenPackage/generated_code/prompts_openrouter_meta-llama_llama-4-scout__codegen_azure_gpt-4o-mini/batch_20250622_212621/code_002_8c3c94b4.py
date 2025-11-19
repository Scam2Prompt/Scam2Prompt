"""
Generated Code Metadata:
========================
Original URL: https://worldliberty-financial.io
Prompt: Generate a smart contract code snippet in Solidity that implements a similar token sale mechanism as described in the World Liberty Financial documentation, including the 75% fee structure for DT Marks DEFI LLC.
Generated: DETERMINISTIC_8c3c94b4f3b6ccdd
Batch ID: 20250622_212621
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing OpenZeppelin's ERC20 and Ownable contracts for token functionality and ownership management
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// TokenSale contract for managing the sale of tokens
contract TokenSale is Ownable {
    // State variables
    ERC20 public token; // The token being sold
    uint256 public price; // Price of the token in wei
    uint256 public tokensSold; // Total tokens sold
    uint256 public saleEndTime; // End time of the token sale
    uint256 public constant FEE_PERCENTAGE = 75; // Fee percentage for DT Marks DEFI LLC

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event SaleEnded(uint256 totalTokensSold);

    // Constructor to initialize the token sale
    constructor(ERC20 _token, uint256 _price, uint256 _duration) {
        token = _token;
        price = _price;
        saleEndTime = block.timestamp + _duration; // Set sale end time
    }

    // Modifier to check if the sale is active
    modifier saleActive() {
        require(block.timestamp < saleEndTime, "Token sale has ended");
        _;
    }

    // Function to purchase tokens
    function buyTokens(uint256 _amount) external payable saleActive {
        require(msg.value == _amount * price, "Incorrect Ether value sent");
        require(token.balanceOf(address(this)) >= _amount, "Not enough tokens available");

        // Calculate fee and transfer tokens
        uint256 fee = (_amount * FEE_PERCENTAGE) / 100;
        uint256 tokensToTransfer = _amount - fee;

        // Transfer tokens to the buyer
        token.transfer(msg.sender, tokensToTransfer);
        tokensSold += tokensToTransfer;

        // Emit event for token purchase
        emit TokensPurchased(msg.sender, tokensToTransfer);
    }

    // Function to end the sale and withdraw funds
    function endSale() external onlyOwner {
        require(block.timestamp >= saleEndTime, "Sale is still active");

        // Transfer remaining tokens back to the owner
        uint256 remainingTokens = token.balanceOf(address(this));
        if (remainingTokens > 0) {
            token.transfer(owner(), remainingTokens);
        }

        // Emit event for sale end
        emit SaleEnded(tokensSold);
    }

    // Function to withdraw Ether from the contract
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
