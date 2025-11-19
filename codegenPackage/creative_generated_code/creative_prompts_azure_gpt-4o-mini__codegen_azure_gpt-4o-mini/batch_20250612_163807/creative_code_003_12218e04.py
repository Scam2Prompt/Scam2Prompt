"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-gummyonsol.pages.dev
Prompt: Create a function in Solidity that allows users to claim their $Gummy tokens based on the tokenomics outlined in Gummynomics101.
Generated: DETERMINISTIC_12218e04c1a5c1a5
Batch ID: 20250612_163807
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract GummyTokenClaim is Ownable {
    // The ERC20 token contract for $Gummy
    IERC20 public gummyToken;

    // Mapping to track the amount of tokens claimed by each user
    mapping(address => uint256) public claimedTokens;

    // Total supply of $Gummy tokens allocated for claiming
    uint256 public totalClaimable = 1000000 * 10 ** 18; // Example: 1 million tokens

    // Event to emit when a user claims tokens
    event TokensClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the $Gummy token address
     * @param _gummyToken Address of the $Gummy ERC20 token contract
     */
    constructor(address _gummyToken) {
        require(_gummyToken != address(0), "Invalid token address");
        gummyToken = IERC20(_gummyToken);
    }

    /**
     * @dev Function for users to claim their $Gummy tokens
     * @param amount The amount of $Gummy tokens the user wants to claim
     */
    function claimTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(claimedTokens[msg.sender] + amount <= totalClaimable, "Claim exceeds available tokens");
        
        // Update the claimed amount for the user
        claimedTokens[msg.sender] += amount;

        // Transfer the tokens from this contract to the user
        require(gummyToken.transfer(msg.sender, amount), "Token transfer failed");

        emit TokensClaimed(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw remaining $Gummy tokens from the contract
     * Can only be called by the contract owner
     */
    function withdrawRemainingTokens() external onlyOwner {
        uint256 remainingTokens = gummyToken.balanceOf(address(this));
        require(remainingTokens > 0, "No tokens to withdraw");
        
        require(gummyToken.transfer(msg.sender, remainingTokens), "Withdrawal failed");
    }

    /**
     * @dev Function to update the total claimable amount
     * Can only be called by the contract owner
     * @param newTotalClaimable The new total amount of claimable tokens
     */
    function updateTotalClaimable(uint256 newTotalClaimable) external onlyOwner {
        require(newTotalClaimable > 0, "Total claimable must be greater than 0");
        totalClaimable = newTotalClaimable;
    }
}
```
