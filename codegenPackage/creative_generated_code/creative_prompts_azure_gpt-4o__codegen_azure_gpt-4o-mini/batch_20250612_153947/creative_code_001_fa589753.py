"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://berryeth.vip
Prompt: Generate Solidity code for a smart contract that integrates with the $BERRY token, allowing users to claim tokens based on specific conditions.
Generated: DETERMINISTIC_fa58975309de691f
Batch ID: 20250612_153947
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

// Importing the ERC20 interface to interact with the $BERRY token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract BerryTokenClaimer {
    // State variable to hold the address of the $BERRY token contract
    IERC20 public berryToken;

    // Mapping to track claimed tokens for each user
    mapping(address => uint256) public claimedAmounts;

    // Event to log claims
    event TokensClaimed(address indexed user, uint256 amount);
    
    // Modifier to check if the user is eligible to claim
    modifier eligibleToClaim(uint256 amount) {
        require(amount > 0, "Claim amount must be greater than zero");
        require(claimedAmounts[msg.sender] + amount <= 100 * (10 ** 18), "Exceeds claim limit"); // Example limit
        _;
    }

    // Constructor to set the $BERRY token contract address
    constructor(address _berryTokenAddress) {
        require(_berryTokenAddress != address(0), "Invalid token address");
        berryToken = IERC20(_berryTokenAddress);
    }

    // Function to claim $BERRY tokens
    function claimTokens(uint256 amount) external eligibleToClaim(amount) {
        require(berryToken.balanceOf(address(this)) >= amount, "Insufficient tokens in contract");

        // Update the claimed amount
        claimedAmounts[msg.sender] += amount;

        // Transfer the tokens to the user
        bool success = berryToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        // Emit the claim event
        emit TokensClaimed(msg.sender, amount);
    }

    // Function to withdraw tokens from the contract (only owner can withdraw)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(berryToken.balanceOf(address(this)) >= amount, "Insufficient tokens in contract");

        // Transfer the tokens to the owner
        bool success = berryToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");
    }

    // Modifier to restrict access to the owner (for the withdraw function)
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // State variable to hold the owner's address
    address private owner;

    // Constructor to set the contract deployer as the owner
    constructor() {
        owner = msg.sender;
    }
}
```
