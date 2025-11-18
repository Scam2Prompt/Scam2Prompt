"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokenscreator-free-pro.pages.dev
Prompt: Generate a Solidity code snippet for a token creation process that includes transferring the token to a liquidity pool and listing it on decentralized trading platforms, as described on the Tokens Creator website.
Generated: DETERMINISTIC_c125122d7e6471ae
Batch ID: 20250612_145916
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Token contract that implements ERC20 functionality
contract MyToken is ERC20, ERC20Burnable, Ownable {
    using SafeMath for uint256;

    // Address of the liquidity pool
    address public liquidityPool;

    // Event emitted when tokens are added to the liquidity pool
    event LiquidityAdded(address indexed pool, uint256 amount);

    // Constructor to initialize the token with name and symbol
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Mint initial supply to the owner
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }

    // Function to set the liquidity pool address
    function setLiquidityPool(address _liquidityPool) external onlyOwner {
        require(_liquidityPool != address(0), "Invalid liquidity pool address");
        liquidityPool = _liquidityPool;
    }

    // Function to transfer tokens to liquidity pool
    function addLiquidity(uint256 amount) external onlyOwner {
        require(liquidityPool != address(0), "Liquidity pool not set");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer the specified amount to the liquidity pool
        _transfer(msg.sender, liquidityPool, amount);
        
        // Emit event for liquidity addition
        emit LiquidityAdded(liquidityPool, amount);
    }

    // Function to approve tokens for a decentralized exchange listing
    function approveForExchange(address exchange, uint256 amount) external onlyOwner {
        require(exchange != address(0), "Invalid exchange address");
        require(amount > 0, "Amount must be greater than zero");

        // Approve the exchange to spend tokens on behalf of the owner
        _approve(msg.sender, exchange, amount);
    }

    // Fallback function to prevent sending ether directly to the contract
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
