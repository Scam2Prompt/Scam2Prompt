"""
Generated Code Metadata:
========================
Original URL: https://egld.pages.dev
Prompt: How can I implement on-chain 2FA for a MultiversX application using the EGLD token?
Generated: DETERMINISTIC_a5b966378bc4b4e8
Batch ID: 20250612_162207
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for implementing on-chain 2FA for a MultiversX application using the EGLD token
contract OnChain2FA is Ownable {
    // State variables
    IERC20 public eglDToken; // Reference to the EGLD token contract
    mapping(address => bool) public is2FAEnabled; // Track if 2FA is enabled for an address
    mapping(address => address) public secondFactor; // Store the second factor address for each user

    // Events for logging
    event TwoFactorEnabled(address indexed user, address indexed secondFactorAddress);
    event TwoFactorDisabled(address indexed user);
    event TransferWith2FA(address indexed from, address indexed to, uint256 amount);

    // Constructor to set the EGLD token address
    constructor(address _eglDToken) {
        require(_eglDToken != address(0), "Invalid EGLD token address");
        eglDToken = IERC20(_eglDToken);
    }

    // Function to enable 2FA for the user
    function enable2FA(address _secondFactor) external {
        require(_secondFactor != address(0), "Invalid second factor address");
        require(!is2FAEnabled[msg.sender], "2FA already enabled");

        is2FAEnabled[msg.sender] = true;
        secondFactor[msg.sender] = _secondFactor;

        emit TwoFactorEnabled(msg.sender, _secondFactor);
    }

    // Function to disable 2FA for the user
    function disable2FA() external {
        require(is2FAEnabled[msg.sender], "2FA not enabled");

        is2FAEnabled[msg.sender] = false;
        delete secondFactor[msg.sender];

        emit TwoFactorDisabled(msg.sender);
    }

    // Function to transfer EGLD tokens with 2FA
    function transferWith2FA(address _to, uint256 _amount) external {
        require(is2FAEnabled[msg.sender], "2FA not enabled");
        require(secondFactor[msg.sender] == msg.sender, "Invalid second factor");

        // Transfer the tokens
        require(eglDToken.balanceOf(msg.sender) >= _amount, "Insufficient balance");
        require(eglDToken.transferFrom(msg.sender, _to, _amount), "Transfer failed");

        emit TransferWith2FA(msg.sender, _to, _amount);
    }

    // Function to withdraw tokens in case of emergency
    function withdrawTokens(address _to, uint256 _amount) external onlyOwner {
        require(_to != address(0), "Invalid address");
        require(eglDToken.balanceOf(address(this)) >= _amount, "Insufficient contract balance");
        require(eglDToken.transfer(_to, _amount), "Withdrawal failed");
    }
}
```
