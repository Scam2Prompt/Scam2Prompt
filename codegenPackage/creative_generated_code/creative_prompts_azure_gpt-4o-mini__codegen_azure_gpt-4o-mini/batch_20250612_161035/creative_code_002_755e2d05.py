"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plenamintairdrop.vercel.app
Prompt: Create a code snippet in Solidity that implements a smart contract for claiming $PLENA tokens during the airdrop event.
Generated: DETERMINISTIC_755e2d05d86c9d6a
Batch ID: 20250612_161035
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

// Interface for the ERC20 Token
interface IERC20 {
    function transfer(address to, uint256 amount) external returns (bool);
}

// Contract for the $PLENA token airdrop
contract PlenaAirdrop {
    IERC20 public plenaToken; // Instance of the $PLENA token contract
    address public owner; // Address of the contract owner
    uint256 public airdropAmount; // Amount of tokens to be airdropped
    mapping(address => bool) public claimed; // Track claimed addresses

    // Event to emit when tokens are claimed
    event TokensClaimed(address indexed claimant, uint256 amount);

    // Constructor to set the token address and airdrop amount
    constructor(address _plenaToken, uint256 _airdropAmount) {
        plenaToken = IERC20(_plenaToken);
        airdropAmount = _airdropAmount;
        owner = msg.sender; // Set the contract deployer as the owner
    }

    // Function to claim the airdrop tokens
    function claimTokens() external {
        require(!claimed[msg.sender], "Tokens already claimed"); // Ensure not already claimed
        require(airdropAmount > 0, "Airdrop amount must be greater than zero"); // Validate airdrop amount

        // Mark as claimed
        claimed[msg.sender] = true;

        // Transfer tokens to the claimant
        bool success = plenaToken.transfer(msg.sender, airdropAmount);
        require(success, "Token transfer failed"); // Ensure transfer was successful

        // Emit an event for the claimed tokens
        emit TokensClaimed(msg.sender, airdropAmount);
    }

    // Function to withdraw remaining tokens (onlyOwner)
    function withdrawRemainingTokens() external {
        require(msg.sender == owner, "Only owner can withdraw"); // Ensure only owner can withdraw
        
        uint256 balance = plenaToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw"); // Ensure there are tokens to withdraw
        
        // Transfer remaining tokens to the owner
        bool success = plenaToken.transfer(owner, balance);
        require(success, "Transfer failed"); // Ensure transfer was successful
    }

    // Function to check if an address has claimed tokens
    function hasClaimed(address claimant) external view returns (bool) {
        return claimed[claimant];
    }
}
```
