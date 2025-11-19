"""
Generated Code Metadata:
========================
Original URL: https://mileimoneda.pages.dev
Prompt: Write a smart contract in Solidity for a cryptocurrency token that includes features like token burning, airdrops, and liquidity pool allocation, inspired by the $MEDA tokenomics described on the Milei Moneda website.
Generated: DETERMINISTIC_e0840432ff9c18a3
Batch ID: 20250612_153401
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

contract MEDAToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Events
    event TokensBurned(address indexed burner, uint256 amount);
    event Airdrop(address indexed recipient, uint256 amount);
    event LiquidityPoolAllocated(address indexed recipient, uint256 amount);

    // Total supply cap
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens

    // Airdrop allocation
    uint256 public airdropAmount;

    // Liquidity pool allocation
    uint256 public liquidityPoolAmount;

    // Constructor to initialize the token
    constructor(uint256 _airdropAmount, uint256 _liquidityPoolAmount) ERC20("MEDA Token", "MEDA") {
        require(_airdropAmount > 0, "Airdrop amount must be greater than 0");
        require(_liquidityPoolAmount > 0, "Liquidity pool amount must be greater than 0");
        
        airdropAmount = _airdropAmount;
        liquidityPoolAmount = _liquidityPoolAmount;

        // Mint initial supply to the contract owner
        _mint(msg.sender, MAX_SUPPLY);
    }

    // Function to burn tokens
    function burn(uint256 amount) external {
        require(amount > 0, "Burn amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        _burn(msg.sender, amount);
        emit TokensBurned(msg.sender, amount);
    }

    // Function to airdrop tokens to a list of addresses
    function airdropTokens(address[] calldata recipients) external onlyOwner {
        require(recipients.length > 0, "No recipients provided");
        uint256 totalAirdropAmount = airdropAmount.mul(recipients.length);
        require(totalAirdropAmount <= balanceOf(msg.sender), "Insufficient balance for airdrop");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid recipient address");
            _transfer(msg.sender, recipients[i], airdropAmount);
            emit Airdrop(recipients[i], airdropAmount);
        }
    }

    // Function to allocate tokens to a liquidity pool
    function allocateToLiquidityPool(address recipient) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(balanceOf(msg.sender) >= liquidityPoolAmount, "Insufficient balance for liquidity allocation");

        _transfer(msg.sender, recipient, liquidityPoolAmount);
        emit LiquidityPoolAllocated(recipient, liquidityPoolAmount);
    }

    // Function to withdraw tokens mistakenly sent to the contract
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(this), "Cannot withdraw MEDA tokens");
        require(amount > 0, "Amount must be greater than 0");

        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
