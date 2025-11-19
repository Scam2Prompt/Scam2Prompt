"""
Generated Code Metadata:
========================
Original URL: https://omnigenesis.vercel.app
Prompt: Write Solidity code to upgrade tokens for asset issuers on Omni Network, enabling global liquidity and adoption.
Generated: DETERMINISTIC_f3fee2ae3fd425bd
Batch ID: 20250612_153400
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

// Importing OpenZeppelin's ERC20 implementation for token standards
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Contract for the OmniToken which allows asset issuers to upgrade their tokens
contract OmniToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Mapping to track upgraded tokens
    mapping(address => bool) public upgradedTokens;

    // Event emitted when a token is upgraded
    event TokenUpgraded(address indexed issuer, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    // Function to mint new tokens for the asset issuer
    function mintTokens(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than zero");

        _mint(to, amount);
    }

    // Function to upgrade tokens for asset issuers
    function upgradeTokens(uint256 amount) external {
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance");
        require(!upgradedTokens[msg.sender], "Tokens already upgraded");

        // Mark the tokens as upgraded
        upgradedTokens[msg.sender] = true;

        // Burn the old tokens
        _burn(msg.sender, amount);

        // Mint new upgraded tokens (for simplicity, we mint the same amount)
        _mint(msg.sender, amount);

        // Emit the token upgrade event
        emit TokenUpgraded(msg.sender, amount);
    }

    // Function to check if an address has upgraded their tokens
    function hasUpgraded(address issuer) external view returns (bool) {
        return upgradedTokens[issuer];
    }

    // Function to withdraw any ERC20 tokens sent to this contract by mistake
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");

        ERC20 token = ERC20(tokenAddress);
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        token.transfer(msg.sender, amount);
    }
}
```
