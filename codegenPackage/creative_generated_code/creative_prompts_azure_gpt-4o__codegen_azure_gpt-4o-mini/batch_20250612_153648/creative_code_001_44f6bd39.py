"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paseceoooveceee.pages.dev
Prompt: Create a smart contract in Solidity for managing the pre-sale of the Portal gaming coin, including features like token distribution and wallet connection.
Generated: DETERMINISTIC_44f6bd39b21f18b5
Batch ID: 20250612_153648
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

// Importing OpenZeppelin's ERC20 interface and Ownable contract for secure ownership management
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract PortalPreSale is Ownable {
    // Struct to represent each participant in the pre-sale
    struct Participant {
        uint256 amountInvested; // Amount invested by the participant
        bool hasClaimed; // Flag to check if the participant has claimed their tokens
    }

    // State variables
    IERC20 public token; // The token being sold
    uint256 public tokenPrice; // Token price in wei
    uint256 public totalTokensSold; // Total tokens sold during the pre-sale
    uint256 public constant MAX_TOKENS = 1000000 * 10 ** 18; // Maximum tokens available for sale
    mapping(address => Participant) public participants; // Mapping of participants' addresses to their data

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event TokensClaimed(address indexed claimant, uint256 amount);

    // Constructor to set the token and price
    constructor(IERC20 _token, uint256 _tokenPrice) {
        require(address(_token) != address(0), "Token address cannot be zero");
        require(_tokenPrice > 0, "Token price must be greater than zero");

        token = _token;
        tokenPrice = _tokenPrice;
    }

    // Function to buy tokens during the pre-sale
    function buyTokens() external payable {
        require(msg.value > 0, "Ether value must be greater than zero");
        
        uint256 tokensToPurchase = (msg.value * 10 ** 18) / tokenPrice; // Calculate how many tokens can be purchased
        require(totalTokensSold + tokensToPurchase <= MAX_TOKENS, "Exceeds maximum tokens available");

        // Update participant's investment and total tokens sold
        participants[msg.sender].amountInvested += msg.value;
        totalTokensSold += tokensToPurchase;

        emit TokensPurchased(msg.sender, tokensToPurchase);
    }

    // Function to claim tokens after the pre-sale
    function claimTokens() external {
        Participant storage participant = participants[msg.sender];
        require(participant.amountInvested > 0, "No tokens to claim");
        require(!participant.hasClaimed, "Tokens already claimed");

        uint256 tokensToClaim = (participant.amountInvested * 10 ** 18) / tokenPrice; // Calculate tokens to claim
        participant.hasClaimed = true; // Mark as claimed

        // Transfer tokens to the participant
        require(token.transfer(msg.sender, tokensToClaim), "Token transfer failed");
        
        emit TokensClaimed(msg.sender, tokensToClaim);
    }

    // Function to withdraw Ether raised from the pre-sale to the owner's wallet
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");

        // Transfer the balance to the owner's address
        payable(owner()).transfer(balance);
    }

    // Function to allow the owner to withdraw unsold tokens after the pre-sale
    function withdrawUnsoldTokens() external onlyOwner {
        uint256 unsoldTokens = MAX_TOKENS - totalTokensSold;
        require(unsoldTokens > 0, "No unsold tokens to withdraw");

        // Transfer unsold tokens to the owner's address
        require(token.transfer(owner(), unsoldTokens), "Token transfer failed");
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfers not allowed, please use buyTokens function");
    }
}
```
