"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blastup-en.pages.dev
Prompt: Explain how to implement a buy-back mechanism for the BlastUP token using a percentage of funds raised from projects.
Generated: DETERMINISTIC_a8a8a8add42fe893
Batch ID: 20250612_161700
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

// Interface for interacting with the BlastUP token
interface IBlastUP is IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

/**
 * @title BuyBackMechanism
 * @notice This contract implements a buy-back mechanism for the BlastUP token
 * using a percentage of funds raised from projects.
 */
contract BuyBackMechanism is Ownable {
    IBlastUP public blastUpToken; // Address of the BlastUP token
    uint256 public buyBackPercentage; // Percentage of funds for buy-back (in basis points)
    
    event BuyBackExecuted(uint256 amountSpent, uint256 tokensPurchased);

    /**
     * @param _blastUpToken Address of the BlastUP token contract
     * @param _buyBackPercentage Initial buy-back percentage (in basis points)
     */
    constructor(address _blastUpToken, uint256 _buyBackPercentage) {
        require(_blastUpToken != address(0), "Invalid token address");
        require(_buyBackPercentage > 0 && _buyBackPercentage <= 10000, "Percentage must be between 0 and 10000");
        
        blastUpToken = IBlastUP(_blastUpToken);
        buyBackPercentage = _buyBackPercentage;
    }

    /**
     * @notice Execute the buy-back using a specified amount of funds raised.
     * @param totalFundsRaised Amount of funds raised from the project
     * @return amountSpent The amount of funds spent for buy-back
     * @return tokensPurchased The number of tokens purchased in the buy-back
     */
    function executeBuyBack(uint256 totalFundsRaised) external onlyOwner returns (uint256 amountSpent, uint256 tokensPurchased) {
        require(totalFundsRaised > 0, "Total funds raised must be greater than zero");
        
        // Calculate the amount to spend on buy-back
        amountSpent = (totalFundsRaised * buyBackPercentage) / 10000;

        // Ensure the contract has enough funds to execute the buy-back
        require(address(this).balance >= amountSpent, "Insufficient balance for buy-back");

        // Purchase BlastUP tokens
        tokensPurchased = amountSpent; // This should be replaced with actual token purchase logic
        
        // Transfer the purchased tokens back to the contract
        require(blastUpToken.transferFrom(address(this), msg.sender, tokensPurchased), "Token transfer failed");

        emit BuyBackExecuted(amountSpent, tokensPurchased);
    }

    /**
     * @notice Update the buy-back percentage.
     * @param newPercentage New buy-back percentage (in basis points)
     */
    function updateBuyBackPercentage(uint256 newPercentage) external onlyOwner {
        require(newPercentage > 0 && newPercentage <= 10000, "Percentage must be between 0 and 10000");
        buyBackPercentage = newPercentage;
    }

    /**
     * @notice Allow the contract to receive ether.
     */
    receive() external payable {}
}
```
