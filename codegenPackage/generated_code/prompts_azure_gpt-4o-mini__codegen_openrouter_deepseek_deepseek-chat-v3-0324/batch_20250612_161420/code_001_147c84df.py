"""
Generated Code Metadata:
========================
Original URL: https://otsea-migration.web.app
Prompt: What are the key changes in the new $OTSEA token compared to the previous version, particularly regarding tax adjustments and reward systems?
Generated: DETERMINISTIC_147c84df256f29d5
Batch ID: 20250612_161420
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

contract OTSEAToken is ERC20, Ownable {
    // Tax and reward parameters
    uint256 public constant MAX_TAX = 25; // Maximum tax percentage (2.5%)
    uint256 public buyTax = 10; // 1% default buy tax
    uint256 public sellTax = 20; // 2% default sell tax
    uint256 public transferTax = 5; // 0.5% default transfer tax
    
    // Reward distribution parameters
    uint256 public rewardPoolPercentage = 40; // 40% of taxes go to reward pool
    uint256 public liquidityPoolPercentage = 30; // 30% of taxes go to liquidity
    uint256 public treasuryPercentage = 30; // 30% of taxes go to treasury
    
    // Addresses
    address public rewardPool;
    address public liquidityPool;
    address public treasury;
    
    // Exclusions
    mapping(address => bool) public isExcludedFromTax;
    
    // Events
    event TaxUpdated(string taxType, uint256 newValue);
    event DistributionUpdated(uint256 reward, uint256 liquidity, uint256 treasury);
    event AddressesUpdated(address rewardPool, address liquidityPool, address treasury);
    
    constructor(
        uint256 initialSupply,
        address _rewardPool,
        address _liquidityPool,
        address _treasury
    ) ERC20("OTSEA Token", "OTSEA") {
        _mint(msg.sender, initialSupply);
        
        rewardPool = _rewardPool;
        liquidityPool = _liquidityPool;
        treasury = _treasury;
        
        // Exclude system addresses from tax
        isExcludedFromTax[msg.sender] = true;
        isExcludedFromTax[_rewardPool] = true;
        isExcludedFromTax[_liquidityPool] = true;
        isExcludedFromTax[_treasury] = true;
    }
    
    // Override transfer functions to implement tax logic
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal virtual override {
        if (isExcludedFromTax[sender] || isExcludedFromTax[recipient]) {
            super._transfer(sender, recipient, amount);
            return;
        }
        
        uint256 taxAmount = 0;
        
        // Determine tax based on transaction type
        if (recipient == address(this)) {
            // Sell transaction
            taxAmount = (amount * sellTax) / 1000;
        } else if (sender == address(this)) {
            // Buy transaction
            taxAmount = (amount * buyTax) / 1000;
        } else {
            // Transfer transaction
            taxAmount = (amount * transferTax) / 1000;
        }
        
        if (taxAmount > 0) {
            uint256 rewardAmount = (taxAmount * rewardPoolPercentage) / 100;
            uint256 liquidityAmount = (taxAmount * liquidityPoolPercentage) / 100;
            uint256 treasuryAmount = taxAmount - rewardAmount - liquidityAmount;
            
            super._transfer(sender, rewardPool, rewardAmount);
            super._transfer(sender, liquidityPool, liquidityAmount);
            super._transfer(sender, treasury, treasuryAmount);
            
            amount -= taxAmount;
        }
        
        super._transfer(sender, recipient, amount);
    }
    
    // Admin functions
    function setBuyTax(uint256 _buyTax) external onlyOwner {
        require(_buyTax <= MAX_TAX, "Tax too high");
        buyTax = _buyTax;
        emit TaxUpdated("buy", _buyTax);
    }
    
    function setSellTax(uint256 _sellTax) external onlyOwner {
        require(_sellTax <= MAX_TAX, "Tax too high");
        sellTax = _sellTax;
        emit TaxUpdated("sell", _sellTax);
    }
    
    function setTransferTax(uint256 _transferTax) external onlyOwner {
        require(_transferTax <= MAX_TAX, "Tax too high");
        transferTax = _transferTax;
        emit TaxUpdated("transfer", _transferTax);
    }
    
    function setDistributionPercentages(
        uint256 _rewardPoolPercentage,
        uint256 _liquidityPoolPercentage,
        uint256 _treasuryPercentage
    ) external onlyOwner {
        require(
            _rewardPoolPercentage + _liquidityPoolPercentage + _treasuryPercentage == 100,
            "Percentages must sum to 100"
        );
        
        rewardPoolPercentage = _rewardPoolPercentage;
        liquidityPoolPercentage = _liquidityPoolPercentage;
        treasuryPercentage = _treasuryPercentage;
        
        emit DistributionUpdated(_rewardPoolPercentage, _liquidityPoolPercentage, _treasuryPercentage);
    }
    
    function setSystemAddresses(
        address _rewardPool,
        address _liquidityPool,
        address _treasury
    ) external onlyOwner {
        require(_rewardPool != address(0), "Invalid reward pool");
        require(_liquidityPool != address(0), "Invalid liquidity pool");
        require(_treasury != address(0), "Invalid treasury");
        
        rewardPool = _rewardPool;
        liquidityPool = _liquidityPool;
        treasury = _treasury;
        
        emit AddressesUpdated(_rewardPool, _liquidityPool, _treasury);
    }
    
    function excludeFromTax(address account, bool excluded) external onlyOwner {
        isExcludedFromTax[account] = excluded;
    }
}
```
