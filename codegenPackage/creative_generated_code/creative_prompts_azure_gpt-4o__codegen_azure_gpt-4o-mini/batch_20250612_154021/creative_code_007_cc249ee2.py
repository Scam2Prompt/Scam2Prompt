"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://duckybsc-claim.pages.dev
Prompt: Develop a smart contract that allows users to claim $Ducky tokens automatically after verifying their wallet address.
Generated: DETERMINISTIC_cc249ee21e1f8ca4
Batch ID: 20250612_154021
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

// Importing the OpenZeppelin ERC20 token contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Smart contract for automatic $Ducky token claims
contract DuckyTokenClaim is Ownable {
    using SafeMath for uint256;

    // Instance of the $Ducky token
    IERC20 public duckyToken;

    // Mapping to track claimed addresses
    mapping(address => bool) public hasClaimed;

    // Event emitted when tokens are claimed
    event TokensClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(address _duckyTokenAddress) {
        require(_duckyTokenAddress != address(0), "Invalid token address");
        duckyToken = IERC20(_duckyTokenAddress);
    }

    // Function to allow users to claim $Ducky tokens
    function claimTokens(uint256 amount) external {
        require(!hasClaimed[msg.sender], "Tokens already claimed");
        require(amount > 0, "Amount must be greater than zero");
        require(duckyToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Mark the user as having claimed tokens
        hasClaimed[msg.sender] = true;

        // Transfer $Ducky tokens to the user
        bool success = duckyToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        // Emit the TokensClaimed event
        emit TokensClaimed(msg.sender, amount);
    }

    // Function to allow the owner to withdraw any remaining tokens
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(duckyToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens to the owner
        bool success = duckyToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");
    }

    // Function to check the contract's token balance
    function contractTokenBalance() external view returns (uint256) {
        return duckyToken.balanceOf(address(this));
    }
}
```
