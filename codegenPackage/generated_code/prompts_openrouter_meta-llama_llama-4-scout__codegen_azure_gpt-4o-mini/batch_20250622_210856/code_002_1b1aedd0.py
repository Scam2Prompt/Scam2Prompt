"""
Generated Code Metadata:
========================
Original URL: https://pundu-en.pages.dev
Prompt: Generate a Solidity (or Rust, if applicable) code snippet for a smart contract that implements a token distribution mechanism similar to PUNDU's, with 45% of tokens going to LP and 45% to presale participants.
Generated: DETERMINISTIC_1b1aedd03d0b1f6e
Batch ID: 20250622_210856
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

// Importing OpenZeppelin's ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract TokenDistribution is ERC20, Ownable {
    // Total supply of tokens
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10 ** 18; // 1 million tokens with 18 decimals
    // Distribution percentages
    uint256 public constant LP_PERCENTAGE = 45; // 45% for Liquidity Pool
    uint256 public constant PRESALE_PERCENTAGE = 45; // 45% for Presale Participants

    // Addresses for distribution
    address public liquidityPoolAddress;
    address public presaleAddress;

    // Events for logging
    event TokensDistributed(address indexed to, uint256 amount);

    // Constructor to initialize the token and distribute tokens
    constructor(address _liquidityPoolAddress, address _presaleAddress) ERC20("MyToken", "MTK") {
        require(_liquidityPoolAddress != address(0), "Invalid liquidity pool address");
        require(_presaleAddress != address(0), "Invalid presale address");

        liquidityPoolAddress = _liquidityPoolAddress;
        presaleAddress = _presaleAddress;

        // Minting tokens according to the distribution plan
        uint256 lpAmount = (TOTAL_SUPPLY * LP_PERCENTAGE) / 100;
        uint256 presaleAmount = (TOTAL_SUPPLY * PRESALE_PERCENTAGE) / 100;

        _mint(liquidityPoolAddress, lpAmount);
        _mint(presaleAddress, presaleAmount);

        emit TokensDistributed(liquidityPoolAddress, lpAmount);
        emit TokensDistributed(presaleAddress, presaleAmount);
    }

    // Function to retrieve the total supply of tokens
    function totalSupply() public view override returns (uint256) {
        return TOTAL_SUPPLY;
    }

    // Function to retrieve the balance of a specific address
    function balanceOf(address account) public view override returns (uint256) {
        return super.balanceOf(account);
    }

    // Function to transfer tokens (inherited from ERC20)
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        return super.transfer(recipient, amount);
    }

    // Function to approve tokens for spending (inherited from ERC20)
    function approve(address spender, uint256 amount) public override returns (bool) {
        return super.approve(spender, amount);
    }

    // Function to transfer tokens from one address to another (inherited from ERC20)
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        return super.transferFrom(sender, recipient, amount);
    }
}
```
