"""
Generated Code Metadata:
========================
Original URL: https://ziber.io
Prompt: Write a smart contract in Solidity that implements the ICO terms described on the Ziber platform, including token distribution, bonus allocation, and fund rejection for early transactions. Ensure the gas limit is set to 250,000.
Generated: DETERMINISTIC_051574c2086f9cd1
Batch ID: 20250612_151531
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

contract ZiberToken is ERC20, Ownable {
    using SafeMath for uint256;

    // ICO parameters
    uint256 public constant TOKEN_PRICE = 0.001 ether; // Price per token
    uint256 public constant BONUS_PERCENTAGE = 20; // Bonus percentage for early investors
    uint256 public constant MAX_TOKENS = 1000000 * 10 ** decimals(); // Total tokens available for ICO
    uint256 public tokensSold; // Track the number of tokens sold
    bool public isICOActive; // ICO status

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event ICOStarted();
    event ICOEnded();

    // Modifier to check if ICO is active
    modifier icoActive() {
        require(isICOActive, "ICO is not active");
        _;
    }

    // Constructor to initialize the token
    constructor() ERC20("ZiberToken", "ZIB") {
        _mint(address(this), MAX_TOKENS); // Mint tokens to the contract
    }

    // Function to start the ICO
    function startICO() external onlyOwner {
        require(!isICOActive, "ICO is already active");
        isICOActive = true;
        emit ICOStarted();
    }

    // Function to end the ICO
    function endICO() external onlyOwner {
        require(isICOActive, "ICO is not active");
        isICOActive = false;
        emit ICOEnded();
    }

    // Function to purchase tokens during the ICO
    function buyTokens(uint256 _amount) external payable icoActive {
        require(msg.value == _amount.mul(TOKEN_PRICE), "Incorrect Ether value sent");
        require(tokensSold.add(_amount) <= MAX_TOKENS, "Not enough tokens available");

        uint256 bonusTokens = _amount.mul(BONUS_PERCENTAGE).div(100);
        uint256 totalTokens = _amount.add(bonusTokens);

        tokensSold = tokensSold.add(totalTokens);
        _transfer(address(this), msg.sender, totalTokens); // Transfer tokens to the buyer

        emit TokensPurchased(msg.sender, totalTokens);
    }

    // Function to withdraw funds from the contract
    function withdrawFunds() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to reject any Ether sent directly to the contract
    receive() external payable {
        revert("Direct Ether transfer not allowed");
    }

    // Function to check the remaining tokens available for sale
    function remainingTokens() external view returns (uint256) {
        return MAX_TOKENS.sub(tokensSold);
    }
}
```
