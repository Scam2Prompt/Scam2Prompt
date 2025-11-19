"""
Generated Code Metadata:
========================
Original URL: https://trumpinucoin.com
Prompt: Write a smart contract in Solidity for a cryptocurrency project that donates a percentage of transaction fees to non-profit charities, similar to TRUMP INU's 1% tax donation mechanism.
Generated: DETERMINISTIC_cc5d5a6df726aaf3
Batch ID: 20250622_210216
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

contract CharityToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Charity address
    address public charityAddress;
    
    // Transaction fee percentage (1% = 100)
    uint256 public transactionFeePercent = 100;
    
    // Events
    event CharityAddressUpdated(address newCharityAddress);
    event TransactionFeeUpdated(uint256 newFeePercent);
    event DonationSent(address charity, uint256 amount);

    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        address initialCharityAddress
    ) ERC20(name, symbol) {
        require(initialCharityAddress != address(0), "Charity address cannot be zero");
        _mint(msg.sender, initialSupply);
        charityAddress = initialCharityAddress;
    }

    // Override transfer function to include donation fee
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        uint256 fee = amount.mul(transactionFeePercent).div(10000);
        uint256 amountAfterFee = amount.sub(fee);
        
        _transfer(msg.sender, recipient, amountAfterFee);
        _transfer(msg.sender, charityAddress, fee);
        
        emit DonationSent(charityAddress, fee);
        return true;
    }

    // Override transferFrom function to include donation fee
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override returns (bool) {
        uint256 fee = amount.mul(transactionFeePercent).div(10000);
        uint256 amountAfterFee = amount.sub(fee);
        
        _transfer(sender, recipient, amountAfterFee);
        _transfer(sender, charityAddress, fee);
        
        emit DonationSent(charityAddress, fee);
        
        uint256 currentAllowance = allowance(sender, msg.sender);
        require(currentAllowance >= amount, "ERC20: transfer amount exceeds allowance");
        _approve(sender, msg.sender, currentAllowance.sub(amount));
        
        return true;
    }

    // Owner functions
    function updateCharityAddress(address newCharityAddress) external onlyOwner {
        require(newCharityAddress != address(0), "Charity address cannot be zero");
        charityAddress = newCharityAddress;
        emit CharityAddressUpdated(newCharityAddress);
    }

    function updateTransactionFee(uint256 newFeePercent) external onlyOwner {
        require(newFeePercent <= 500, "Fee cannot exceed 5%");
        transactionFeePercent = newFeePercent;
        emit TransactionFeeUpdated(newFeePercent);
    }
}
```
