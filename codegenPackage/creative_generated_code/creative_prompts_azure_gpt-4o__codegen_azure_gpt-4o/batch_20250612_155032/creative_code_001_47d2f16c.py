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

/**
 * @title FTMToSMigration
 * @dev A smart contract to facilitate the migration of $FTM tokens to $S tokens at a 1:1 conversion rate.
 */
contract FTMToSMigration {
    // Address of the $FTM token contract
    IERC20 public ftmToken;

    // Address of the $S token contract
    IERC20 public sToken;

    // Address of the contract owner
    address public owner;

    /**
     * @dev Modifier to restrict access to only the owner of the contract.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _ftmToken Address of the $FTM token contract.
     * @param _sToken Address of the $S token contract.
     */
    constructor(address _ftmToken, address _sToken) {
        require(_ftmToken != address(0), "FTM token address cannot be zero");
        require(_sToken != address(0), "S token address cannot be zero");
        ftmToken = IERC20(_ftmToken);
        sToken = IERC20(_sToken);
        owner = msg.sender;
    }

    /**
     * @dev Facilitates the migration of $FTM tokens to $S tokens at a 1:1 ratio.
     * @param amount Amount of $FTM tokens to migrate.
     */
    function migrate(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Check sender's $FTM token balance
        uint256 ftmBalance = ftmToken.balanceOf(msg.sender);
        require(ftmBalance >= amount, "Insufficient FTM token balance");

        // Check contract's $S token balance
        uint256 contractSBal = sToken.balanceOf(address(this));
        require(contractSBal >= amount, "Insufficient S token balance in contract");

        // Transfer $FTM tokens from sender to contract
        require(ftmToken.transferFrom(msg.sender, address(this), amount), "FTM token transfer failed");

        // Transfer $S tokens from contract to sender
        require(sToken.transfer(msg.sender, amount), "S token transfer failed");
    }

    /**
     * @dev Allows the owner to withdraw any remaining $FTM tokens in the contract.
     * @param amount Amount of $FTM tokens to withdraw.
     */
    function withdrawFTMTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        uint256 contractFTMBal = ftmToken.balanceOf(address(this));
        require(contractFTMBal >= amount, "Insufficient FTM token balance in contract");
        require(ftmToken.transfer(owner, amount), "FTM token withdrawal failed");
    }

    /**
     * @dev Allows the owner to withdraw any remaining $S tokens in the contract.
     * @param amount Amount of $S tokens to withdraw.
     */
    function withdrawSTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        uint256 contractSBal = sToken.balanceOf(address(this));
        require(contractSBal >= amount, "Insufficient S token balance in contract");
        require(sToken.transfer(owner, amount), "S token withdrawal failed");
    }
}

/**
 * @dev Interface for ERC20 tokens.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
