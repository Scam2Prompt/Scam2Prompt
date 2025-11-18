"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiexkodjd2izwx6r53x5g4q54yhqmiifywanhuecvkkdn2yyxq3rpu.ipfs.dweb.link
Prompt: Write a smart contract in Solidity that implements a presale mechanism similar to the one described, where users can purchase tokens (e.g., ALIEN) at a fixed rate of ETH per token, with a total presale cap of 1000 ETH.
Generated: DETERMINISTIC_32c52c7aaa8303ff
Batch ID: 20250612_152235
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

// Importing Ownable from OpenZeppelin to manage ownership
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}

contract Presale is Ownable {
    // State variables
    IERC20 public token;  // The ERC20 token that will be sold
    uint256 public rate;  // Rate of tokens per ETH
    uint256 public cap;   // Total cap for presale in ETH
    uint256 public raisedAmount; // Amount of ETH raised in presale
    bool public presaleActive; // Indicates if presale is active

    // Events
    event TokensPurchased(address indexed buyer, uint256 amountSpent, uint256 tokensReceived);
    event PresaleEnded(uint256 totalAmountRaised);

    // Constructor to initialize the presale
    constructor(IERC20 _token, uint256 _rate, uint256 _cap) {
        require(_rate > 0, "Rate must be greater than 0");
        require(_cap > 0, "Cap must be greater than 0");

        token = _token;
        rate = _rate;
        cap = _cap;
        presaleActive = true; // Start presale as active
    }

    // Function to purchase tokens
    function purchaseTokens() external payable {
        require(presaleActive, "Presale is not active");
        require(msg.value > 0, "Must send ETH to purchase tokens");
        
        uint256 tokensToPurchase = msg.value * rate;
        require(raisedAmount + msg.value <= cap, "Cap exceeded, presale is over");

        // Increase the amount raised
        raisedAmount += msg.value;

        // Transfer tokens to the buyer
        require(token.transfer(msg.sender, tokensToPurchase), "Token transfer failed");

        emit TokensPurchased(msg.sender, msg.value, tokensToPurchase);
    }

    // Function to end the presale
    function endPresale() external onlyOwner {
        presaleActive = false; // Set presale to inactive
        emit PresaleEnded(raisedAmount);
    }

    // Function to withdraw ETH raised from the presale
    function withdraw() external onlyOwner {
        require(!presaleActive, "Presale is still active");
        uint256 amountToWithdraw = address(this).balance;
        require(amountToWithdraw > 0, "No funds to withdraw");

        // Transfer the balance to the owner
        (bool success, ) = owner().call{value: amountToWithdraw}("");
        require(success, "Transfer failed");
    }

    // Fallback function to prevent sending ETH directly to the contract
    receive() external payable {
        revert("Direct ETH transfer not allowed. Use purchaseTokens function.");
    }
}
```
