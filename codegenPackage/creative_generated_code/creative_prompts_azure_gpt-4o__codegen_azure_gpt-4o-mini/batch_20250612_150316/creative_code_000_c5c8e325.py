"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bibbydivs.com
Prompt: Write a smart contract in Solidity that implements a token investment system with a 2% entry fee, a 2% exit fee, and a dividend redistribution mechanism similar to the $BIBBY ecosystem described on BibbyDivs.com.
Generated: DETERMINISTIC_c5c8e32559171f7f
Batch ID: 20250612_150316
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

// Import OpenZeppelin's ERC20 implementation and Ownable contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// TokenInvestment contract to manage token investments with entry and exit fees and dividend redistribution
contract TokenInvestment is ERC20, Ownable {
    // State variables
    uint256 public constant ENTRY_FEE_PERCENTAGE = 2; // 2% entry fee
    uint256 public constant EXIT_FEE_PERCENTAGE = 2; // 2% exit fee
    uint256 public totalDividends; // Total dividends accumulated for distribution
    mapping(address => uint256) public dividends; // Dividends owed to investors
    mapping(address => uint256) public investmentBalances; // Track the investment balance of each investor

    // Events
    event Invested(address indexed investor, uint256 amount);
    event Withdrawn(address indexed investor, uint256 amount);
    event DividendsDistributed(uint256 amount);

    // Constructor to initialize the token
    constructor() ERC20("InvestmentToken", "ITK") {}

    // Function for investment into the token with an entry fee
    function invest(uint256 amount) external {
        require(amount > 0, "Investment amount must be greater than zero");
        uint256 entryFee = (amount * ENTRY_FEE_PERCENTAGE) / 100;
        uint256 netAmount = amount - entryFee;

        _mint(msg.sender, netAmount); // Mint tokens to investor minus the entry fee
        investmentBalances[msg.sender] += netAmount; // Update investment balance
        totalDividends += entryFee; // Accumulate the entry fee into dividends

        emit Invested(msg.sender, netAmount);
    }

    // Function to withdraw investment with an exit fee
    function withdraw(uint256 amount) external {
        require(investmentBalances[msg.sender] >= amount, "Insufficient balance to withdraw");
        
        uint256 exitFee = (amount * EXIT_FEE_PERCENTAGE) / 100;
        uint256 netAmount = amount - exitFee;

        _burn(msg.sender, amount); // Burn the tokens being withdrawn
        investmentBalances[msg.sender] -= amount; // Update investment balance
        totalDividends += exitFee; // Accumulate the exit fee into dividends

        // Transfer net amount back to investor
        payable(msg.sender).transfer(netAmount); 

        emit Withdrawn(msg.sender, netAmount);
    }

    // Function to claim dividends for the investor
    function claimDividends() external {
        uint256 owed = dividends[msg.sender];
        require(owed > 0, "No dividends available to claim");
        
        dividends[msg.sender] = 0; // Reset the owed dividends
        payable(msg.sender).transfer(owed); // Transfer dividends to the investor

        emit DividendsDistributed(owed);
    }

    // Function to distribute dividends to all holders proportionally
    function distributeDividends() external onlyOwner {
        require(totalDividends > 0, "No dividends to distribute");
        for (uint256 i = 0; i < totalSupply(); i++) {
            address account = address(uint160(i)); // This is a simplification, replace with actual address retrieval logic
            uint256 balance = balanceOf(account);
            if (balance > 0) {
                dividends[account] += (balance * totalDividends) / totalSupply(); // Accumulate dividends
            }
        }
        totalDividends = 0; // Reset total dividends
    }

    // Receive function to accept ETH sent directly to the contract
    receive() external payable {}
}
```
