"""
Generated Code Metadata:
========================
Original URL: https://cumrockets.pages.dev
Prompt: Write a guide on how to use the CumRocket token contract to create a custom utility token with similar features, such as 0% token tax and meme-driven branding.
Generated: DETERMINISTIC_1ace4eaa4e98b367
Batch ID: 20250612_151343
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

// Importing OpenZeppelin's ERC20 implementation for standard token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// CustomToken is a simple ERC20 token with no transaction tax
contract CustomToken is ERC20, Ownable {
    // Mapping to keep track of addresses that are excluded from fees (if any)
    mapping(address => bool) private _isExcludedFromFee;

    // Event to log when an address is excluded from fees
    event ExcludedFromFee(address indexed account);

    // Constructor to initialize the token with a name and symbol
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Mint an initial supply to the contract deployer
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Mint 1 million tokens
    }

    // Function to exclude an address from fees
    function excludeFromFee(address account) external onlyOwner {
        require(!_isExcludedFromFee[account], "Account is already excluded");
        _isExcludedFromFee[account] = true;
        emit ExcludedFromFee(account);
    }

    // Override the _transfer function to implement custom logic
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        // Check for zero amount transfer
        require(amount > 0, "Transfer amount must be greater than zero");

        // If the sender is excluded from fees, proceed without any fees
        if (_isExcludedFromFee[sender] || _isExcludedFromFee[recipient]) {
            super._transfer(sender, recipient, amount);
        } else {
            // For this token, we have 0% tax, so just transfer the amount
            super._transfer(sender, recipient, amount);
        }
    }

    // Function to withdraw any ERC20 tokens sent to this contract by mistake
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(this), "Cannot withdraw native token");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }

    // Function to withdraw Ether sent to this contract by mistake
    function withdrawEther() external onlyOwner {
        payable(msg.sender).transfer(address(this).balance);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
