"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aethirclaim-ifbf5prj-iamsorryman.4everland.app
Prompt: Explain how to set up a presale cap for a token sale using smart contracts, referencing the BCKR presale details.
Generated: DETERMINISTIC_a59fd24f1cc99b35
Batch ID: 20250612_155337
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

// Import the necessary OpenZeppelin contracts
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Presale contract for BCKR token
contract BCKRPresale is Ownable {
    // State variables
    IERC20 public bckrToken; // The BCKR token to be sold in the presale
    uint256 public presaleCap; // Maximum amount of funds to be raised
    uint256 public totalRaised; // Total amount raised in the presale
    uint256 public tokenPrice; // Price of one BCKR token in wei
    mapping(address => uint256) public contributions; // Track contributions of each participant
    bool public presaleActive; // Presale state

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleFinalized();

    // Constructor to initialize the contract
    constructor(IERC20 _bckrToken, uint256 _presaleCap, uint256 _tokenPrice) {
        require(address(_bckrToken) != address(0), "Invalid token address");
        require(_presaleCap > 0, "Presale cap must be greater than 0");
        require(_tokenPrice > 0, "Token price must be greater than 0");

        bckrToken = _bckrToken;
        presaleCap = _presaleCap;
        tokenPrice = _tokenPrice;
        presaleActive = true; // Start presale as active
    }

    // Function to buy tokens during the presale
    function buyTokens() external payable {
        require(presaleActive, "Presale is not active");
        require(msg.value > 0, "Must send ether to purchase tokens");
        require(totalRaised + msg.value <= presaleCap, "Presale cap exceeded");

        // Calculate the number of tokens to purchase
        uint256 tokensToPurchase = msg.value / tokenPrice;
        require(tokensToPurchase > 0, "Insufficient funds to purchase tokens");

        // Update the state
        contributions[msg.sender] += msg.value;
        totalRaised += msg.value;

        // Emit an event for the transaction
        emit TokensPurchased(msg.sender, tokensToPurchase);
    }

    // Function to finalize the presale
    function finalizePresale() external onlyOwner {
        require(presaleActive, "Presale already finalized");

        // Finalize presale state
        presaleActive = false;

        // Transfer the raised funds to the owner
        payable(owner()).transfer(address(this).balance);

        // Emit event
        emit PresaleFinalized();
    }

    // Function to withdraw tokens in case of failure
    function withdrawUnsoldTokens() external onlyOwner {
        require(!presaleActive, "Presale is still active");

        // Calculate unsold tokens
        uint256 unsoldTokens = bckrToken.balanceOf(address(this));
        require(unsoldTokens > 0, "No unsold tokens to withdraw");

        // Transfer unsold tokens back to the owner
        bckrToken.transfer(owner(), unsoldTokens);
    }

    // Function to get the current ETH balance of the contract
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
