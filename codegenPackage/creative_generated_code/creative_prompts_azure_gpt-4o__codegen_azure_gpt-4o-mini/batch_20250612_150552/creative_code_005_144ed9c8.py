"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogeverse-22u.pages.dev
Prompt: Develop a Solidity smart contract that supports claiming $DOGEVERSE tokens post-presale, ensuring compatibility with multiple chains like Ethereum, Solana, and BNB Chain.
Generated: DETERMINISTIC_144ed9c889a4c7ec
Batch ID: 20250612_150552
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

// Import the ERC20 interface for token transfers
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Define the contract for claiming $DOGEVERSE tokens
contract DogeverseTokenClaim {
    // State variables
    address public owner; // The owner of the contract
    IERC20 public token; // The ERC20 token contract
    mapping(address => bool) public hasClaimed; // Track whether an address has claimed tokens
    uint256 public claimAmount; // Amount of tokens to claim

    // Event emitted when tokens are claimed
    event TokensClaimed(address indexed claimant, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Constructor to set the token address, claim amount, and owner
    constructor(address _token, uint256 _claimAmount) {
        require(_token != address(0), "Invalid token address");
        require(_claimAmount > 0, "Claim amount must be greater than zero");

        token = IERC20(_token);
        claimAmount = _claimAmount;
        owner = msg.sender;
    }

    // Function to claim tokens
    function claimTokens() external {
        require(!hasClaimed[msg.sender], "Tokens have already been claimed");
        
        // Transfer tokens to the claimant
        require(token.balanceOf(address(this)) >= claimAmount, "Insufficient tokens in contract");
        hasClaimed[msg.sender] = true;

        // Perform the transfer
        bool success = token.transfer(msg.sender, claimAmount);
        require(success, "Token transfer failed");

        // Emit an event for the successful claim
        emit TokensClaimed(msg.sender, claimAmount);
    }

    // Function to withdraw remaining tokens to the owner in case of emergencies
    function withdrawTokens() external onlyOwner {
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        
        // Transfer all tokens to the owner
        bool success = token.transfer(owner, balance);
        require(success, "Token transfer failed");
    }
}
```
