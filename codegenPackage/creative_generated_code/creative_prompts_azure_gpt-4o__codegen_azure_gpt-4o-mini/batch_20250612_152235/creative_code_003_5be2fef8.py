"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://octa-claim.pages.dev
Prompt: Generate a smart contract snippet to facilitate the claiming of $OCTA tokens during the Octa.Space airdrop event.
Generated: DETERMINISTIC_5be2fef8d66cb712
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

// Import the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for the Octa.Space Airdrop
contract OctaSpaceAirdrop is Ownable {
    // Mapping to track if an address has claimed their tokens
    mapping(address => bool) public hasClaimed;

    // Address of the $OCTA token contract
    IERC20 public octaToken;

    // Amount of tokens each user can claim
    uint256 public claimAmount;

    // Event emitted when tokens are claimed
    event TokensClaimed(address indexed claimant, uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC20 _octaToken, uint256 _claimAmount) {
        octaToken = _octaToken;
        claimAmount = _claimAmount;
    }

    // Function to claim $OCTA tokens
    function claimTokens() external {
        // Check if the caller has already claimed tokens
        require(!hasClaimed[msg.sender], "Tokens already claimed");

        // Check the contract has enough tokens to fulfill the claim
        require(octaToken.balanceOf(address(this)) >= claimAmount, "Insufficient tokens in contract");

        // Update the state to indicate the tokens have been claimed
        hasClaimed[msg.sender] = true;

        // Transfer the tokens to the claimant
        bool success = octaToken.transfer(msg.sender, claimAmount);
        require(success, "Token transfer failed");

        // Emit an event for the claim
        emit TokensClaimed(msg.sender, claimAmount);
    }

    // Function to withdraw any leftover tokens from the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(octaToken.balanceOf(address(this)) >= amount, "Insufficient tokens to withdraw");
        bool success = octaToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");
    }

    // Function to set a new claim amount (onlyOwner)
    function setClaimAmount(uint256 newClaimAmount) external onlyOwner {
        claimAmount = newClaimAmount;
    }
}
```
