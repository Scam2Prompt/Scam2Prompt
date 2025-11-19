"""
Generated Code Metadata:
========================
Original URL: https://presale-jesse-9kw.pages.dev
Prompt: Generate a smart contract in Solidity for a presale event with a cap of 1000 BASE and a total supply of 100,000,000 JESSE tokens.
Generated: DETERMINISTIC_09101eea22e89c36
Batch ID: 20250612_161616
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

// Importing OpenZeppelin's ERC20 implementation for token creation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Presale contract for JESSE token
contract JessePresale is Ownable {
    // Token details
    ERC20 public jesseToken;
    uint256 public constant PRESALE_CAP = 1000 * 10 ** 18; // Presale cap in BASE (assuming BASE has 18 decimals)
    uint256 public totalRaised; // Total amount raised in the presale
    uint256 public presaleEndTime; // End time for the presale
    bool public presaleActive; // Flag to check if presale is active

    // Event to log purchases
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Constructor to initialize the presale with the JESSE token
    constructor(address _jesseTokenAddress, uint256 _durationInMinutes) {
        jesseToken = ERC20(_jesseTokenAddress);
        presaleEndTime = block.timestamp + (_durationInMinutes * 1 minutes);
        presaleActive = true;
    }

    // Function to purchase tokens during the presale
    function purchaseTokens(uint256 _amount) external payable {
        require(presaleActive, "Presale is not active");
        require(block.timestamp < presaleEndTime, "Presale has ended");
        require(totalRaised + _amount <= PRESALE_CAP, "Presale cap reached");
        require(msg.value == _amount, "Incorrect ETH amount sent");

        totalRaised += _amount;

        // Transfer JESSE tokens to the buyer
        require(jesseToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit TokensPurchased(msg.sender, _amount);
    }

    // Function to end the presale
    function endPresale() external onlyOwner {
        require(presaleActive, "Presale is already ended");
        presaleActive = false;
    }

    // Function to withdraw raised funds
    function withdrawFunds() external onlyOwner {
        require(!presaleActive, "Presale is still active");
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
