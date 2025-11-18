"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nbnm.pages.dev
Prompt: Generate code for a smart contract that facilitates the migration of $FTM tokens to $S tokens at a 1:1 conversion rate, as described in Sonic's migration program.
Generated: DETERMINISTIC_47d2f16c658bd607
Batch ID: 20250612_155032
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

// Import the necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for the migration of $FTM tokens to $S tokens
contract TokenMigration is Ownable {
    // Address of the $FTM token
    IERC20 public ftmToken;
    // Address of the $S token
    IERC20 public sToken;

    // Event emitted when tokens are migrated
    event TokensMigrated(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the token addresses
    constructor(address _ftmToken, address _sToken) {
        require(_ftmToken != address(0), "Invalid FTM token address");
        require(_sToken != address(0), "Invalid S token address");

        ftmToken = IERC20(_ftmToken);
        sToken = IERC20(_sToken);
    }

    // Function to migrate $FTM tokens to $S tokens
    function migrateTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(ftmToken.balanceOf(msg.sender) >= amount, "Insufficient $FTM balance");

        // Transfer $FTM tokens from the user to this contract
        bool success = ftmToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Transfer of $FTM tokens failed");

        // Transfer equivalent $S tokens to the user at a 1:1 conversion rate
        success = sToken.transfer(msg.sender, amount);
        require(success, "Transfer of $S tokens failed");

        // Emit the migration event
        emit TokensMigrated(msg.sender, amount);
    }

    // Function for the owner to withdraw any $FTM tokens left in the contract
    function withdrawFTM(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(ftmToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        bool success = ftmToken.transfer(msg.sender, amount);
        require(success, "Withdrawal of $FTM tokens failed");
    }

    // Function for the owner to withdraw any $S tokens left in the contract
    function withdrawS(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(sToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        bool success = sToken.transfer(msg.sender, amount);
        require(success, "Withdrawal of $S tokens failed");
    }
}
```
