"""
Generated Code Metadata:
========================
Original URL: https://claim-beefmeme.pages.dev
Prompt: Develop a smart contract using Solidity to create a token with a similar deflationary tokenomics model to BEEF Coin, with a finite supply and a burn mechanism.
Generated: DETERMINISTIC_2c24e60ed03837ee
Batch ID: 20250622_205623
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title DeflationaryToken
 * @author [Your Name]
 * @notice A deflationary token with a finite supply and burn mechanism.
 */
contract DeflationaryToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Maximum supply of tokens
    uint256 public immutable MAX_SUPPLY;

    // Burn fee percentage (in basis points)
    uint256 public burnFee;

    /**
     * @notice Constructor
     * @param name Token name
     * @param symbol Token symbol
     * @param maxSupply Maximum supply of tokens
     * @param initialSupply Initial supply of tokens
     * @param burnFeePercentage Burn fee percentage (in basis points)
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 maxSupply,
        uint256 initialSupply,
        uint256 burnFeePercentage
    ) ERC20(name, symbol) {
        require(maxSupply > 0, "Max supply must be greater than 0");
        require(initialSupply <= maxSupply, "Initial supply cannot exceed max supply");
        require(burnFeePercentage <= 10000, "Burn fee percentage must not exceed 100%");

        MAX_SUPPLY = maxSupply;
        burnFee = burnFeePercentage;
        _mint(msg.sender, initialSupply);
    }

    /**
     * @notice Transfer tokens with burn fee
     * @param from Sender
     * @param to Recipient
     * @param amount Amount to transfer
     * @return bool Success
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        uint256 fee = amount.mul(burnFee).div(10000);
        uint256 netAmount = amount.sub(fee);

        // Burn fee
        _burn(msg.sender, fee);

        // Transfer net amount
        super.transferFrom(from, to, netAmount);

        return true;
    }

    /**
     * @notice Transfer tokens with burn fee
     * @param to Recipient
     * @param amount Amount to transfer
     * @return bool Success
     */
    function transfer(
        address to,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        uint256 fee = amount.mul(burnFee).div(10000);
        uint256 netAmount = amount.sub(fee);

        // Burn fee
        _burn(msg.sender, fee);

        // Transfer net amount
        super.transfer(to, netAmount);

        return true;
    }

    /**
     * @notice Burn tokens
     * @param amount Amount to burn
     */
    function burn(uint256 amount) public override {
        require(amount > 0, "Amount to burn must be greater than 0");
        _burn(msg.sender, amount);
    }

    /**
     * @notice Mint tokens (only for initial supply)
     * @param to Recipient
     * @param amount Amount to mint
     */
    function mint(address to, uint256 amount) internal {
        require(totalSupply().add(amount) <= MAX_SUPPLY, "Mint exceeds max supply");
        _mint(to, amount);
    }
}
```
