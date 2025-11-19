"""
Generated Code Metadata:
========================
Original URL: https://presale-artyfact.pages.dev
Prompt: "Generate a smart contract in Solidity to create and manage $ARTY tokens on a blockchain network, considering the tokenomics and deflationary design of the Artyfact ecosystem."
Generated: DETERMINISTIC_3f545a18a6e0e425
Batch ID: 20250622_205553
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

/**
 * @title ArtyToken ($ARTY)
 * @dev ERC20-compliant smart contract with deflationary tokenomics for the Artyfact ecosystem.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ArtyToken is ERC20, Ownable {
    // Deflationary parameters
    uint256 public burnRate; // Percentage of tokens to burn per transaction (e.g., 2%)
    uint256 public maxSupply; // Maximum supply of $ARTY tokens

    event Burn(address indexed from, uint256 amount);

    /**
     * @dev Constructor to initialize the $ARTY token.
     * @param _name Name of the token.
     * @param _symbol Symbol of the token.
     * @param _initialSupply Initial supply of tokens.
     * @param _burnRate Burn rate percentage (e.g., 2 for 2%).
     * @param _maxSupply Maximum supply of tokens.
     */
    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _initialSupply,
        uint256 _burnRate,
        uint256 _maxSupply
    ) ERC20(_name, _symbol) {
        require(_burnRate <= 100, "Burn rate must be between 0 and 100");
        require(_initialSupply <= _maxSupply, "Initial supply exceeds max supply");

        burnRate = _burnRate;
        maxSupply = _maxSupply;

        // Mint initial supply to the contract owner
        _mint(msg.sender, _initialSupply);
    }

    /**
     * @dev Override the transfer function to include deflationary burn logic.
     * @param recipient Address to receive the tokens.
     * @param amount Amount of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        uint256 burnAmount = (amount * burnRate) / 100;
        uint256 transferAmount = amount - burnAmount;

        // Burn the tokens
        if (burnAmount > 0) {
            _burn(msg.sender, burnAmount);
            emit Burn(msg.sender, burnAmount);
        }

        // Perform the transfer
        return super.transfer(recipient, transferAmount);
    }

    /**
     * @dev Override the transferFrom function to include deflationary burn logic.
     * @param sender Address sending the tokens.
     * @param recipient Address receiving the tokens.
     * @param amount Amount of tokens to transfer.
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override returns (bool) {
        uint256 burnAmount = (amount * burnRate) / 100;
        uint256 transferAmount = amount - burnAmount;

        // Burn the tokens
        if (burnAmount > 0) {
            _burn(sender, burnAmount);
            emit Burn(sender, burnAmount);
        }

        // Perform the transfer
        return super.transferFrom(sender, recipient, transferAmount);
    }

    /**
     * @dev Mint new tokens. Only the owner can mint, and total supply cannot exceed maxSupply.
     * @param account Address to receive the minted tokens.
     * @param amount Amount of tokens to mint.
     */
    function mint(address account, uint256 amount) external onlyOwner {
        require(totalSupply() + amount <= maxSupply, "Minting exceeds max supply");
        _mint(account, amount);
    }

    /**
     * @dev Update the burn rate. Only the owner can update this value.
     * @param _burnRate New burn rate percentage.
     */
    function setBurnRate(uint256 _burnRate) external onlyOwner {
        require(_burnRate <= 100, "Burn rate must be between 0 and 100");
        burnRate = _burnRate;
    }
}
```
