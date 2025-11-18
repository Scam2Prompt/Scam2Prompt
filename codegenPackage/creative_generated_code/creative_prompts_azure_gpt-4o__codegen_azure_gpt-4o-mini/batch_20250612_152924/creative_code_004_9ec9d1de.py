"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeigfvszp46s3snhdvtr6cjaqasj42yritad4wljrbrflup5v5itywu.ipfs.dweb.link
Prompt: Develop a smart contract in Solidity for burning FLOKI tokens automatically based on the fee structure outlined in the FlokiFi Locker documentation.
Generated: DETERMINISTIC_9ec9d1de63003f9b
Batch ID: 20250612_152924
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

contract FlokiBurner is Ownable {
    // The token to be burned
    IERC20 public flokiToken;

    // Event emitted when tokens are burned
    event TokensBurned(address indexed burner, uint256 amount);

    // Constructor to initialize the token address
    constructor(address _flokiToken) {
        require(_flokiToken != address(0), "Invalid token address");
        flokiToken = IERC20(_flokiToken);
    }

    // Function to burn tokens based on fee structure
    function burnTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(flokiToken.balanceOf(address(this)) >= amount, "Insufficient balance to burn");

        // Transfer tokens from contract to the burn address (zero address)
        flokiToken.transfer(address(0), amount);
        
        // Emit the burn event
        emit TokensBurned(msg.sender, amount);
    }

    // Function to withdraw accidentally sent tokens (not FLOKI)
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(flokiToken), "Cannot withdraw FLOKI tokens");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }

    // Function to set a new FLOKI token address (if needed)
    function setFlokiToken(address _flokiToken) external onlyOwner {
        require(_flokiToken != address(0), "Invalid token address");
        flokiToken = IERC20(_flokiToken);
    }
}
```
