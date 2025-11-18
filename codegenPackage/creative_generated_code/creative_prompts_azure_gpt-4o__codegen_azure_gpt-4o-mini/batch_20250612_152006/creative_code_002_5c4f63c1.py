"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token2049.vercel.app
Prompt: Generate a smart contract in Solidity for the 2049 tokenomics model, incorporating a 6% buy/sell tax for repurchasing, token destruction, and marketing.
Generated: DETERMINISTIC_5c4f63c1ef9980ef
Batch ID: 20250612_152006
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

// Importing the necessary OpenZeppelin contracts
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// The 2049Token contract implements a token with a buy/sell tax mechanism
contract 2049Token is ERC20, Ownable {
    // Tax rates
    uint256 public buySellTax = 6; // 6% buy/sell tax
    uint256 public totalTaxCollected; // Tracks total tax collected

    // Addresses for tax allocation
    address public marketingAddress;
    address public repurchaseAddress;
    address public burnAddress; // A burn address for token destruction

    // Events for logging
    event TaxDistributed(uint256 amount, address indexed recipient);
    event TokensBurned(uint256 amount);

    // Constructor to set initial supply and addresses
    constructor(uint256 initialSupply, address _marketingAddress, address _repurchaseAddress) 
        ERC20("2049 Token", "2049T") 
    {
        require(_marketingAddress != address(0), "Invalid marketing address");
        require(_repurchaseAddress != address(0), "Invalid repurchase address");
        
        marketingAddress = _marketingAddress;
        repurchaseAddress = _repurchaseAddress;
        burnAddress = address(0); // Use the zero address for burning
        
        // Mint the initial supply to the contract deployer
        _mint(msg.sender, initialSupply * (10 ** decimals()));
    }

    // Override the _transfer function to include tax logic
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        // Calculate the tax amount
        uint256 taxAmount = (amount * buySellTax) / 100;
        uint256 amountAfterTax = amount - taxAmount;

        // Transfer the tax to the respective addresses
        super._transfer(sender, marketingAddress, taxAmount / 3); // 1/3 to marketing
        super._transfer(sender, repurchaseAddress, taxAmount / 3); // 1/3 to repurchase
        super._transfer(sender, burnAddress, taxAmount / 3); // 1/3 to burn

        // Update the total tax collected
        totalTaxCollected += taxAmount;

        // Transfer the remaining amount to the recipient
        super._transfer(sender, recipient, amountAfterTax);
    }

    // Function to view total tax collected
    function getTotalTaxCollected() external view returns (uint256) {
        return totalTaxCollected;
    }

    // Function to burn tokens
    function burn(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        _burn(msg.sender, amount);
        emit TokensBurned(amount);
    }

    // Function to withdraw tokens accidentally sent to the contract
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(this), "Cannot withdraw native token");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
