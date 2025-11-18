"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asx-capital.pages.dev
Prompt: Write a Solidity function that calculates and distributes yield from DeFi investments to $ASX token holders, ensuring safety mechanisms for risk mitigation as outlined on the ASX Capital site.
Generated: DETERMINISTIC_9ef3ed47bf190f71
Batch ID: 20250612_152018
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for yield generating contracts
interface IYieldGenerator {
    function calculateYield(address tokenHolder) external view returns (uint256);
    function distributeYield(address to, uint256 amount) external;
}

// ASXToken contract to manage ASX token holders and yield distribution
contract ASXToken is Ownable {
    // Mapping to track balances of $ASX token holders
    mapping(address => uint256) public balances;
    
    // Total supply of $ASX tokens
    uint256 public totalSupply;
    
    // Yield generator contract
    IYieldGenerator public yieldGenerator;

    // Event to log yield distribution
    event YieldDistributed(address indexed holder, uint256 amount);

    // Constructor to initialize the yield generator
    constructor(IYieldGenerator _yieldGenerator) {
        yieldGenerator = _yieldGenerator;
    }

    // Function to mint new $ASX tokens to an address
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than zero");

        balances[to] += amount;
        totalSupply += amount;
    }

    // Function to calculate and distribute yield to $ASX token holders
    function distributeYield() external {
        for (uint256 i = 0; i < totalSupply; i++) {
            address holder = address(uint160(i)); // This is a placeholder; implement logic to fetch actual holders
            
            uint256 yieldAmount = yieldGenerator.calculateYield(holder);
            if (yieldAmount > 0) {
                // Distribute the yield
                yieldGenerator.distributeYield(holder, yieldAmount);
                emit YieldDistributed(holder, yieldAmount);
            }
        }
    }

    // Function to allow withdrawal of funds by the contract owner
    function withdrawFunds(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(msg.sender, amount);
    }

    // Fallback function to accept ETH
    receive() external payable {}

    // Ensure contract can be paused for safety
    function pause() external onlyOwner {
        // Implement pausing mechanism if needed
    }

    function unpause() external onlyOwner {
        // Implement unpausing mechanism if needed
    }
}
```
