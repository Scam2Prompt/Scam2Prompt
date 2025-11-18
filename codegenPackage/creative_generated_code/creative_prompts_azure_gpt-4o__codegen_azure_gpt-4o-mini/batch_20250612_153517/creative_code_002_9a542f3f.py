"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hashai.pages.dev
Prompt: Create a smart contract in Solidity that distributes income from AI-enhanced mining rigs to token holders, referencing the Hash AI token model.
Generated: DETERMINISTIC_9a542f3f034c823c
Batch ID: 20250612_153517
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for standard functionalities
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/// @title Hash AI Token
/// @notice This contract allows for income distribution to token holders from AI-enhanced mining rigs
contract HashAIToken is ERC20, Ownable {
    // Total income collected from mining rigs
    uint256 public totalIncome;
    // Mapping to keep track of last claimed income for each address
    mapping(address => uint256) public lastClaimedIncome;
    // Mapping of user shares
    mapping(address => uint256) public shares;

    // Event for income distribution
    event IncomeDistributed(uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor(uint256 initialSupply) ERC20("Hash AI Token", "HAI") {
        _mint(msg.sender, initialSupply * (10 ** uint256(decimals())));
    }

    /// @notice Distribute income to token holders
    /// @dev Only callable by the contract owner
    /// @param amount The amount of income to be distributed
    function distributeIncome(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(totalSupply() > 0, "No tokens in circulation");

        totalIncome += amount;
        emit IncomeDistributed(amount);
    }

    /// @notice Claim available income for the sender
    /// @dev Calculates the claimable income based on shares
    function claimIncome() external {
        uint256 owed = calculateIncome(msg.sender);
        require(owed > 0, "No income to claim");

        // Resetting last claimed income for the sender
        lastClaimedIncome[msg.sender] = totalIncome;
        
        // Transfer income to the sender
        payable(msg.sender).transfer(owed);
    }

    /// @notice Calculate income owed to a specific address
    /// @param account The address to calculate income for
    /// @return The amount of income owed
    function calculateIncome(address account) public view returns (uint256) {
        // Calculate the share of the total income
        uint256 userIncome = (totalIncome - lastClaimedIncome[account]) * balanceOf(account) / totalSupply();
        return userIncome;
    }

    /// @notice Allow the contract to receive Ether
    receive() external payable {}
    
    /// @notice Fallback function to receive Ether
    fallback() external payable {}
}
```
