"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://award-topg.pages.dev
Prompt: Generate a smart contract code snippet for a token presale that caps at 1000 ETH, similar to the $TOPG presale model.
Generated: DETERMINISTIC_a89d63e406beca85
Batch ID: 20250612_163305
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract TokenPresale is Ownable {
    // The token being sold
    IERC20 public token;

    // Presale parameters
    uint256 public constant CAP = 1000 ether; // Maximum funding cap
    uint256 public totalRaised; // Total amount raised
    uint256 public tokenPrice; // Price of one token in wei
    bool public isPresaleActive; // Presale status

    // Mapping of addresses to their contributions
    mapping(address => uint256) public contributions;

    // Events for logging
    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleStarted();
    event PresaleEnded();
    
    // Modifier to ensure presale is active
    modifier presaleActive() {
        require(isPresaleActive, "Presale is not active");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _tokenAddress, uint256 _tokenPrice) {
        token = IERC20(_tokenAddress);
        tokenPrice = _tokenPrice;
    }

    // Start the presale
    function startPresale() external onlyOwner {
        isPresaleActive = true;
        emit PresaleStarted();
    }

    // End the presale
    function endPresale() external onlyOwner {
        isPresaleActive = false;
        emit PresaleEnded();
    }

    // Function to purchase tokens during the presale
    function buyTokens() external payable presaleActive {
        require(msg.value > 0, "No ETH sent");
        require(totalRaised + msg.value <= CAP, "Cap exceeded");

        // Calculate number of tokens to purchase
        uint256 tokenAmount = msg.value / tokenPrice;

        // Update total raised and buyer's contributions
        totalRaised += msg.value;
        contributions[msg.sender] += msg.value;

        // Transfer tokens to buyer
        require(token.balanceOf(address(this)) >= tokenAmount, "Insufficient tokens in presale contract");
        token.transfer(msg.sender, tokenAmount);

        emit TokensPurchased(msg.sender, tokenAmount);
    }

    // Function to withdraw funds from the presale
    function withdrawFunds() external onlyOwner {
        require(!isPresaleActive, "Presale is still active");
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        // Transfer the balance to the owner's address
        (bool success, ) = owner().call{value: balance}("");
        require(success, "Transfer failed");
    }

    // Fallback function to prevent ETH from being sent directly to the contract
    receive() external payable {
        revert("Direct ETH transfers not allowed; use buyTokens function.");
    }
}
```
