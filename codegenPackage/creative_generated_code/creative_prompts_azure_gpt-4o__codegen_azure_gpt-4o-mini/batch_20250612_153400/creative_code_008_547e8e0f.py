"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20in.pages.dev
Prompt: Write a Solidity contract that ensures DOGE20 tokens are distributed fairly during presale claiming and prevents double claiming.
Generated: DETERMINISTIC_547e8e0ff9c272b6
Batch ID: 20250612_153400
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

// Interface for the ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}

// Contract for DOGE20 presale claiming
contract Doge20Presale {
    // State variables
    address public owner;                     // Owner of the contract
    IERC20 public dogeToken;                  // Address of the DOGE20 token contract
    uint256 public totalSupply;                // Total supply allocated for presale
    uint256 public totalClaimed;               // Total DOGE20 tokens claimed
    mapping(address => bool) public hasClaimed; // Track if an address has claimed

    // Events
    event TokensClaimed(address indexed claimant, uint256 amount);

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to initialize contract state
    constructor(address _dogeToken, uint256 _totalSupply) {
        owner = msg.sender;                     // Set the contract deployer as owner
        dogeToken = IERC20(_dogeToken);        // Set the DOGE20 token contract
        totalSupply = _totalSupply;             // Set the total presale supply
        totalClaimed = 0;                       // Initialize total claimed to zero
    }

    // Function to claim DOGE20 tokens
    function claimTokens(uint256 amount) external {
        // Check if the user has already claimed
        require(!hasClaimed[msg.sender], "Already claimed");

        // Check if the requested amount is valid
        require(amount > 0, "Amount must be greater than zero");
        require(totalClaimed + amount <= totalSupply, "Exceeds total supply");

        // Mark the user as having claimed
        hasClaimed[msg.sender] = true;

        // Update total claimed amount
        totalClaimed += amount;

        // Transfer tokens to the claimant
        require(dogeToken.transfer(msg.sender, amount), "Token transfer failed");

        // Emit an event for the claim
        emit TokensClaimed(msg.sender, amount);
    }

    // Function to withdraw remaining tokens by owner
    function withdrawRemainingTokens() external onlyOwner {
        uint256 remaining = totalSupply - totalClaimed;
        require(remaining > 0, "No remaining tokens to withdraw");

        // Transfer remaining tokens to owner
        require(dogeToken.transfer(owner, remaining), "Withdrawal failed");
    }

    // Fallback function to prevent sending Ether to the contract
    receive() external payable {
        revert("Contract does not accept Ether");
    }
}
```
