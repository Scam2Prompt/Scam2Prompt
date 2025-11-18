"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jwzt-dashboard-inqubeta.pages.dev
Prompt: Create a tutorial for deploying a smart contract on the Ethereum network that implements InQubeta's tokenomics, including buy and sell taxes for rewards, liquidity, marketing, and burning.
Generated: DETERMINISTIC_00d3d31b6ae14a9e
Batch ID: 20250612_145619
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

// Import OpenZeppelin contracts for ERC20 and Ownable functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract InQubetaToken is ERC20, Ownable {
    // Define tax rates for different functionalities
    uint256 public buyTax = 5; // 5% buy tax
    uint256 public sellTax = 10; // 10% sell tax

    // Define recipient addresses for tax allocations
    address public rewardsAddress;
    address public liquidityAddress;
    address public marketingAddress;
    address public burnAddress;

    // Events for logging
    event TaxChanged(string taxType, uint256 newTax);
    event AddressesUpdated(address rewards, address liquidity, address marketing, address burn);

    constructor(
        string memory name,
        string memory symbol,
        address _rewardsAddress,
        address _liquidityAddress,
        address _marketingAddress,
        address _burnAddress
    ) ERC20(name, symbol) {
        // Set initial balances
        rewardsAddress = _rewardsAddress;
        liquidityAddress = _liquidityAddress;
        marketingAddress = _marketingAddress;
        burnAddress = _burnAddress;

        // Mint initial supply to the contract deployer
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Mint 1 million tokens
    }

    // Function to change tax rates
    function setTaxRates(uint256 _buyTax, uint256 _sellTax) external onlyOwner {
        require(_buyTax <= 10, "Buy tax cannot exceed 10%");
        require(_sellTax <= 15, "Sell tax cannot exceed 15%");
        
        buyTax = _buyTax;
        sellTax = _sellTax;

        emit TaxChanged("Buy Tax", buyTax);
        emit TaxChanged("Sell Tax", sellTax);
    }

    // Function to update recipient addresses
    function updateAddresses(
        address _rewardsAddress,
        address _liquidityAddress,
        address _marketingAddress,
        address _burnAddress
    ) external onlyOwner {
        rewardsAddress = _rewardsAddress;
        liquidityAddress = _liquidityAddress;
        marketingAddress = _marketingAddress;
        burnAddress = _burnAddress;

        emit AddressesUpdated(rewardsAddress, liquidityAddress, marketingAddress, burnAddress);
    }

    // Override the _transfer function to implement tax logic
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        uint256 taxAmount;

        // Determine if the transfer is a buy or a sell
        if (recipient == address(this)) {
            // Sell
            taxAmount = (amount * sellTax) / 100;
        } else if (sender == address(this)) {
            // Buy
            taxAmount = (amount * buyTax) / 100;
        }

        // Distribute taxes
        if (taxAmount > 0) {
            uint256 rewards = (taxAmount * 50) / 100; // 50% to rewards
            uint256 liquidity = (taxAmount * 30) / 100; // 30% to liquidity
            uint256 marketing = (taxAmount * 20) / 100; // 20% to marketing

            super._transfer(sender, rewardsAddress, rewards);
            super._transfer(sender, liquidityAddress, liquidity);
            super._transfer(sender, marketingAddress, marketing);

            // Burn the remaining tax amount
            uint256 burnAmount = taxAmount - (rewards + liquidity + marketing);
            if (burnAmount > 0) {
                super._transfer(sender, burnAddress, burnAmount);
            }
            amount -= taxAmount; // Deduct tax from the amount
        }

        // Proceed with the standard transfer
        super._transfer(sender, recipient, amount);
    }
}
```

### Notes:
- This smart contract implements the specified tokenomics of InQubeta and includes buy/sell tax logic.
- The contract uses OpenZeppelin's ERC20 and Ownable contracts for security and best practices.
- Proper error handling and events are included for state changes.
- Ensure that the OpenZeppelin contracts (ERC20 and Ownable) are correctly installed in your project for this code to run.
