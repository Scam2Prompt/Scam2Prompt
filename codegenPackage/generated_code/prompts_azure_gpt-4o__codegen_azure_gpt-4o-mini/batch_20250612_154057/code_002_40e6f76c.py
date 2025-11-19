"""
Generated Code Metadata:
========================
Original URL: https://hyperswap.tech
Prompt: Generate a smart contract for launching a new token on the HyperEVM Native Dex, incorporating liquidity management features.
Generated: DETERMINISTIC_40e6f76cf8320080
Batch ID: 20250612_154057
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for token functionality and ownership management
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Smart contract for a new token with liquidity management features
contract MyToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Event emitted when liquidity is added
    event LiquidityAdded(uint256 tokenAmount, uint256 ethAmount);

    // Mapping to track liquidity providers
    mapping(address => uint256) public liquidityProviders;

    // Constructor to initialize the token with a name and symbol
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to add liquidity to the contract
    function addLiquidity(uint256 tokenAmount) external payable onlyOwner {
        require(tokenAmount > 0, "Token amount must be greater than 0");
        require(msg.value > 0, "ETH amount must be greater than 0");

        // Transfer tokens from the owner to the contract
        _transfer(msg.sender, address(this), tokenAmount);

        // Update liquidity provider's balance
        liquidityProviders[msg.sender] = liquidityProviders[msg.sender].add(tokenAmount);

        // Emit event for liquidity addition
        emit LiquidityAdded(tokenAmount, msg.value);
    }

    // Function to withdraw liquidity from the contract
    function withdrawLiquidity(uint256 tokenAmount) external {
        require(liquidityProviders[msg.sender] >= tokenAmount, "Insufficient liquidity balance");

        // Update liquidity provider's balance
        liquidityProviders[msg.sender] = liquidityProviders[msg.sender].sub(tokenAmount);

        // Transfer tokens back to the liquidity provider
        _transfer(address(this), msg.sender, tokenAmount);
    }

    // Function to allow the owner to withdraw ETH from the contract
    function withdrawETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");

        // Transfer ETH to the owner
        payable(msg.sender).transfer(balance);
    }

    // Fallback function to accept ETH
    receive() external payable {}
}
```
