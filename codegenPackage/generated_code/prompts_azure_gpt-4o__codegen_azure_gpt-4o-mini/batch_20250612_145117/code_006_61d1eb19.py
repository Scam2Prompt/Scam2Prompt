"""
Generated Code Metadata:
========================
Original URL: https://zombi.finance
Prompt: Create a smart contract that interacts with a connected wallet to enable app access, based on the principles used by Zombi Finance.
Generated: DETERMINISTIC_61d1eb19860c8485
Batch ID: 20250612_145117
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

// Importing OpenZeppelin's Ownable contract for access control
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Smart contract to manage app access based on wallet interactions
contract AppAccessManager is Ownable {
    // Mapping to track user access status
    mapping(address => bool) private _hasAccess;

    // The token used for access payments
    IERC20 public accessToken;

    // Event emitted when access is granted
    event AccessGranted(address indexed user);

    // Event emitted when access is revoked
    event AccessRevoked(address indexed user);

    // Constructor to set the access token address
    constructor(address tokenAddress) {
        require(tokenAddress != address(0), "Invalid token address");
        accessToken = IERC20(tokenAddress);
    }

    // Function to grant access to a user
    function grantAccess(address user) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(!_hasAccess[user], "User already has access");

        _hasAccess[user] = true;
        emit AccessGranted(user);
    }

    // Function to revoke access from a user
    function revokeAccess(address user) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(_hasAccess[user], "User does not have access");

        _hasAccess[user] = false;
        emit AccessRevoked(user);
    }

    // Function to purchase access using tokens
    function purchaseAccess(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(accessToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from the user to the contract
        bool success = accessToken.transfer(address(this), amount);
        require(success, "Token transfer failed");

        // Grant access to the user
        _hasAccess[msg.sender] = true;
        emit AccessGranted(msg.sender);
    }

    // Function to check if a user has access
    function hasAccess(address user) external view returns (bool) {
        return _hasAccess[user];
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(accessToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        bool success = accessToken.transfer(msg.sender, amount);
        require(success, "Token withdrawal failed");
    }
}
```
