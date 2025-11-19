"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://munchieswithbrett.com
Prompt: Generate a smart contract in Solidity for claiming $MUNCHIES tokens on the Base blockchain as described on Munchies with Brett.
Generated: DETERMINISTIC_8523ca3fe00c8ecc
Batch ID: 20250612_163419
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

// Importing the necessary interfaces for ERC20 token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MunchiesTokenClaim
 * @dev Smart contract for claiming $MUNCHIES tokens on the Base blockchain
 */
contract MunchiesTokenClaim is Ownable {
    // The $MUNCHIES token contract address
    IERC20 public munchiesToken;

    // Mapping to track whether an address has claimed their tokens
    mapping(address => bool) public hasClaimed;

    // Event to emit when tokens are claimed
    event TokensClaimed(address indexed claimant, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the token address
     * @param _tokenAddress The address of the $MUNCHIES token contract
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        munchiesToken = IERC20(_tokenAddress);
    }

    /**
     * @dev Function to claim $MUNCHIES tokens
     * @param amount The amount of tokens to claim
     */
    function claimTokens(uint256 amount) external {
        require(!hasClaimed[msg.sender], "Tokens already claimed");
        require(amount > 0, "Amount must be greater than 0");
        require(munchiesToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        
        // Mark the sender as having claimed their tokens
        hasClaimed[msg.sender] = true;

        // Transfer tokens to the claimant
        bool success = munchiesToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        // Emit the TokensClaimed event
        emit TokensClaimed(msg.sender, amount);
    }

    /**
     * @dev Function for the owner to withdraw any remaining $MUNCHIES tokens in the contract
     * @param amount The amount of tokens to withdraw
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(munchiesToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens to the owner
        bool success = munchiesToken.transfer(owner(), amount);
        require(success, "Token transfer failed");
    }

    /**
     * @dev Function to get the balance of $MUNCHIES tokens held by the contract
     * @return The token balance of the contract
     */
    function getTokenBalance() external view returns (uint256) {
        return munchiesToken.balanceOf(address(this));
    }
}
```
