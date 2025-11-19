"""
Generated Code Metadata:
========================
Original URL: https://lookscoin.com
Prompt: Write a code snippet that demonstrates how to implement a payment distribution mechanism on the LookRev blockchain using the $LOOK token.
Generated: DETERMINISTIC_8ad229c2775be1a1
Batch ID: 20250612_155538
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract LookRevPaymentDistributor is Ownable {
    using SafeMath for uint256;

    IERC20 public lookToken;
    
    struct Recipient {
        address wallet;
        uint256 percentage; // Basis points (1% = 100)
    }
    
    Recipient[] public recipients;
    uint256 public totalPercentage;

    event PaymentDistributed(address indexed recipient, uint256 amount);
    event RecipientAdded(address indexed recipient, uint256 percentage);
    event RecipientRemoved(address indexed recipient);
    event RecipientUpdated(address indexed oldRecipient, address indexed newRecipient, uint256 newPercentage);

    constructor(address _lookTokenAddress) {
        require(_lookTokenAddress != address(0), "Invalid token address");
        lookToken = IERC20(_lookTokenAddress);
    }

    function addRecipient(address _wallet, uint256 _percentage) external onlyOwner {
        require(_wallet != address(0), "Invalid wallet address");
        require(_percentage > 0, "Percentage must be greater than 0");
        require(totalPercentage.add(_percentage) <= 10000, "Total percentage exceeds 100%");

        recipients.push(Recipient({
            wallet: _wallet,
            percentage: _percentage
        }));
        totalPercentage = totalPercentage.add(_percentage);
        
        emit RecipientAdded(_wallet, _percentage);
    }

    function removeRecipient(uint256 _index) external onlyOwner {
        require(_index < recipients.length, "Invalid recipient index");
        
        address wallet = recipients[_index].wallet;
        uint256 percentage = recipients[_index].percentage;
        
        if (_index < recipients.length - 1) {
            recipients[_index] = recipients[recipients.length - 1];
        }
        recipients.pop();
        totalPercentage = totalPercentage.sub(percentage);
        
        emit RecipientRemoved(wallet);
    }

    function updateRecipient(uint256 _index, address _newWallet, uint256 _newPercentage) external onlyOwner {
        require(_index < recipients.length, "Invalid recipient index");
        require(_newWallet != address(0), "Invalid wallet address");
        require(_newPercentage > 0, "Percentage must be greater than 0");
        
        Recipient storage recipient = recipients[_index];
        uint256 oldPercentage = recipient.percentage;
        
        require(totalPercentage.sub(oldPercentage).add(_newPercentage) <= 10000, "Total percentage exceeds 100%");
        
        address oldWallet = recipient.wallet;
        recipient.wallet = _newWallet;
        recipient.percentage = _newPercentage;
        totalPercentage = totalPercentage.sub(oldPercentage).add(_newPercentage);
        
        emit RecipientUpdated(oldWallet, _newWallet, _newPercentage);
    }

    function distributePayments(uint256 _totalAmount) external {
        require(_totalAmount > 0, "Amount must be greater than 0");
        require(recipients.length > 0, "No recipients configured");
        require(totalPercentage == 10000, "Total percentage must equal 100%");
        
        uint256 balance = lookToken.balanceOf(msg.sender);
        require(balance >= _totalAmount, "Insufficient token balance");
        
        bool success = lookToken.transferFrom(msg.sender, address(this), _totalAmount);
        require(success, "Token transfer failed");
        
        for (uint256 i = 0; i < recipients.length; i++) {
            Recipient memory recipient = recipients[i];
            uint256 amount = _totalAmount.mul(recipient.percentage).div(10000);
            
            if (amount > 0) {
                success = lookToken.transfer(recipient.wallet, amount);
                require(success, "Token transfer to recipient failed");
                emit PaymentDistributed(recipient.wallet, amount);
            }
        }
    }

    function emergencyWithdraw(address _tokenAddress) external onlyOwner {
        IERC20 token = IERC20(_tokenAddress);
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        
        bool success = token.transfer(owner(), balance);
        require(success, "Emergency withdrawal failed");
    }
}
```
