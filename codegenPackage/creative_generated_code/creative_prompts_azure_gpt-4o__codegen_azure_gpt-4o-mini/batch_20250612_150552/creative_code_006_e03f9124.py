"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oraclememe-sale.pages.dev
Prompt: Write a smart contract for a layer-2 scaling solution on Binance Smart Chain that supports fast and low-cost transactions for meme-related assets, as described in the Oracle Meme roadmap.
Generated: DETERMINISTIC_e03f912402f48bcb
Batch ID: 20250612_150552
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
 * @title OracleMemeToken
 * @dev ERC20 Token contract for meme-related assets on Binance Smart Chain Layer-2
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @notice This contract implements an ERC20 token that allows users to send and receive meme-related assets.
 * It is designed to be deployed on a Layer-2 solution to ensure fast and low-cost transactions.
 */
contract OracleMemeToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Event emitted when tokens are minted
    event TokensMinted(address indexed to, uint256 amount);

    // Event emitted when tokens are burned
    event TokensBurned(address indexed from, uint256 amount);

    /**
     * @dev Constructor that initializes the token with a name and symbol
     * @param name The name of the token
     * @param symbol The symbol of the token
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    /**
     * @notice Mint new tokens to a specific address
     * @param to The address that will receive the newly minted tokens
     * @param amount The amount of tokens to mint
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Mint amount must be greater than zero");

        _mint(to, amount);
        emit TokensMinted(to, amount);
    }

    /**
     * @notice Burn tokens from a specific address
     * @param amount The amount of tokens to burn
     */
    function burn(uint256 amount) external {
        require(amount > 0, "Burn amount must be greater than zero");

        _burn(msg.sender, amount);
        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @notice Transfer tokens from the caller to a specified address
     * @param recipient The address to which the tokens will be sent
     * @param amount The amount of tokens to be sent
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        return super.transfer(recipient, amount);
    }

    /**
     * @notice Transfer tokens from one address to another on behalf of a specified address
     * @param sender The address from which tokens will be transferred
     * @param recipient The address to which tokens will be sent
     * @param amount The amount of tokens to be sent
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        return super.transferFrom(sender, recipient, amount);
    }

    /**
     * @dev Override the _beforeTokenTransfer function to implement custom logic if needed
     * @param from The address tokens are being transferred from
     * @param to The address tokens are being transferred to
     * @param amount The amount of tokens being transferred
     */
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override {
        super._beforeTokenTransfer(from, to, amount);
        // Implement custom logic if needed
    }
}
```
