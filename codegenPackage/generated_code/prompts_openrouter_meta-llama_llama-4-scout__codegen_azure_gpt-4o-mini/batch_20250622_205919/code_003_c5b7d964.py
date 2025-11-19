"""
Generated Code Metadata:
========================
Original URL: https://c3a60044.hashai.pages.dev
Prompt: Design a smart contract for a Hash AI token, where income from AI-enhanced mining rigs is shared with token holders, using Solidity or another suitable programming language.
Generated: DETERMINISTIC_c5b7d96437f653cb
Batch ID: 20250622_205919
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

// HashAIToken is an ERC20 token that allows income from AI-enhanced mining rigs to be shared with token holders.
contract HashAIToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Total income generated from mining
    uint256 public totalIncome;

    // Mapping to track the last claimed income for each holder
    mapping(address => uint256) public lastClaimedIncome;

    // Event emitted when income is distributed
    event IncomeDistributed(uint256 amount);

    // Event emitted when a holder claims their income
    event IncomeClaimed(address indexed holder, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("Hash AI Token", "HAI") {
        totalIncome = 0;
    }

    // Function to allow the owner to distribute income to the contract
    function distributeIncome() external payable onlyOwner {
        require(msg.value > 0, "Income must be greater than zero");
        totalIncome = totalIncome.add(msg.value);
        emit IncomeDistributed(msg.value);
    }

    // Function to claim income based on the holder's balance
    function claimIncome() external {
        uint256 incomeToClaim = calculateIncome(msg.sender);
        require(incomeToClaim > 0, "No income to claim");

        // Update the last claimed income for the holder
        lastClaimedIncome[msg.sender] = totalIncome;

        // Transfer the income to the holder
        payable(msg.sender).transfer(incomeToClaim);
        emit IncomeClaimed(msg.sender, incomeToClaim);
    }

    // Function to calculate the income for a specific holder
    function calculateIncome(address holder) public view returns (uint256) {
        uint256 holderBalance = balanceOf(holder);
        if (holderBalance == 0) {
            return 0;
        }

        // Calculate the share of income based on the holder's balance
        uint256 incomeSinceLastClaim = totalIncome.sub(lastClaimedIncome[holder]);
        return incomeSinceLastClaim.mul(holderBalance).div(totalSupply());
    }

    // Function to mint new tokens, only callable by the owner
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }

    // Function to burn tokens, only callable by the owner
    function burn(address from, uint256 amount) external onlyOwner {
        _burn(from, amount);
    }
}
```
