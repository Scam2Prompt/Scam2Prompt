"""
Generated Code Metadata:
========================
Original URL: https://triaslabonemigration.pages.dev
Prompt: Create a Solidity smart contract snippet that facilitates the 1:1 migration of TRIAS tokens from BEP20/ERC20 to TEP20 on the NetX network, as outlined in the migration process.
Generated: DETERMINISTIC_cbb081296e0cbec6
Batch ID: 20250612_145228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing the interface for ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Migration contract for TRIAS tokens from BEP20/ERC20 to TEP20
contract TRIASMigration {
    // Address of the source token (BEP20/ERC20)
    IERC20 public sourceToken;
    // Address of the destination token (TEP20)
    IERC20 public destinationToken;

    // Mapping to track migrated addresses
    mapping(address => bool) public hasMigrated;

    // Event to log successful migrations
    event Migration(address indexed user, uint256 amount);

    // Constructor to set the source and destination token addresses
    constructor(address _sourceToken, address _destinationToken) {
        require(_sourceToken != address(0), "Invalid source token address");
        require(_destinationToken != address(0), "Invalid destination token address");

        sourceToken = IERC20(_sourceToken);
        destinationToken = IERC20(_destinationToken);
    }

    // Function to migrate tokens
    function migrate(uint256 amount) external {
        // Check if the user has already migrated
        require(!hasMigrated[msg.sender], "Already migrated");

        // Check if the user has enough source tokens
        require(sourceToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer source tokens from the user to this contract
        bool success = sourceToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Mint or transfer the equivalent amount of destination tokens to the user
        // Assuming the destination token contract has a mint function
        // Uncomment the following line if the destination token supports minting
        // destinationToken.mint(msg.sender, amount);
        
        // If the destination token does not support minting, use transfer instead
        success = destinationToken.transfer(msg.sender, amount);
        require(success, "Token transfer to user failed");

        // Mark the user as having migrated
        hasMigrated[msg.sender] = true;

        // Emit migration event
        emit Migration(msg.sender, amount);
    }

    // Function to withdraw any remaining source tokens in the contract
    function withdrawSourceTokens() external {
        // Only the contract owner can withdraw
        // Implement ownership check here (e.g., using Ownable from OpenZeppelin)
        // require(msg.sender == owner, "Only owner can withdraw");

        uint256 balance = sourceToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        // Transfer remaining source tokens to the owner
        bool success = sourceToken.transfer(msg.sender, balance);
        require(success, "Withdrawal failed");
    }

    // Function to withdraw any remaining destination tokens in the contract
    function withdrawDestinationTokens() external {
        // Only the contract owner can withdraw
        // Implement ownership check here (e.g., using Ownable from OpenZeppelin)
        // require(msg.sender == owner, "Only owner can withdraw");

        uint256 balance = destinationToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        // Transfer remaining destination tokens to the owner
        bool success = destinationToken.transfer(msg.sender, balance);
        require(success, "Withdrawal failed");
    }
}
```
