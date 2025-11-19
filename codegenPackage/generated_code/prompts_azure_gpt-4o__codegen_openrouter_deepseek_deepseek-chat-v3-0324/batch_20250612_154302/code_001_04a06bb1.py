"""
Generated Code Metadata:
========================
Original URL: https://czbull.com
Prompt: Generate Solidity code for a smart contract that mimics the features of $WINDY Once Again, including zero transaction taxes and a burned liquidity pool mechanism.
Generated: DETERMINISTIC_04a06bb106495ad2
Batch ID: 20250612_154302
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract WindyOnceAgain is ERC20, Ownable {
    using SafeMath for uint256;

    // Burn address where LP tokens are sent
    address public constant BURN_ADDRESS = 0x000000000000000000000000000000000000dEaD;

    // Max supply of tokens (1 trillion with 18 decimals)
    uint256 public constant MAX_SUPPLY = 1_000_000_000_000 * 10**18;

    // Initial liquidity amount (50% of total supply)
    uint256 public constant INITIAL_LIQUIDITY = MAX_SUPPLY / 2;

    // Flag to prevent multiple initializations
    bool private _initialized;

    constructor() ERC20("Windy Once Again", "WINDY") {
        _mint(msg.sender, MAX_SUPPLY);
        _initialized = false;
    }

    /**
     * @dev Initialize the contract by burning initial liquidity
     * Can only be called once by the owner
     */
    function initialize() external onlyOwner {
        require(!_initialized, "Contract already initialized");
        
        // Burn initial liquidity (50% of total supply)
        _transfer(owner(), BURN_ADDRESS, INITIAL_LIQUIDITY);
        
        _initialized = true;
    }

    /**
     * @dev Override transfer to ensure no fees are taken
     */
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal virtual override {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");

        super._transfer(sender, recipient, amount);
    }

    /**
     * @dev Function to burn tokens from any address
     * @param amount Amount of tokens to burn
     */
    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
    }

    /**
     * @dev Function to burn tokens from a specific address (only callable by owner)
     * @param account Address to burn tokens from
     * @param amount Amount of tokens to burn
     */
    function burnFrom(address account, uint256 amount) public onlyOwner {
        _spendAllowance(account, msg.sender, amount);
        _burn(account, amount);
    }

    /**
     * @dev Returns whether the contract has been initialized
     */
    function isInitialized() public view returns (bool) {
        return _initialized;
    }
}
```
