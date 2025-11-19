"""
Generated Code Metadata:
========================
Original URL: https://mewnbase.pages.dev
Prompt: Write a Solidity smart contract snippet that implements a buy/sell tax mechanism similar to the 6.9% tax described on the Mewnbase platform, distributing ETH directly to wallets based on volume and bag size.
Generated: DETERMINISTIC_41d12efa922ceec4
Batch ID: 20250612_152358
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

contract TaxToken is ERC20, Ownable {
    uint256 public constant TAX_PERCENTAGE = 690; // 6.9% represented as basis points (690/10000)
    address[] public taxRecipients;
    mapping(address => uint256) public recipientWeights;
    uint256 public totalWeight;

    event TaxDistributed(address indexed recipient, uint256 amount);

    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply
    ) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply);
    }

    function addTaxRecipient(address recipient, uint256 weight) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(weight > 0, "Weight must be greater than 0");

        taxRecipients.push(recipient);
        recipientWeights[recipient] = weight;
        totalWeight += weight;
    }

    function removeTaxRecipient(address recipient) external onlyOwner {
        require(recipientWeights[recipient] > 0, "Recipient not found");

        // Remove from array
        for (uint256 i = 0; i < taxRecipients.length; i++) {
            if (taxRecipients[i] == recipient) {
                taxRecipients[i] = taxRecipients[taxRecipients.length - 1];
                taxRecipients.pop();
                break;
            }
        }

        // Update total weight
        totalWeight -= recipientWeights[recipient];
        delete recipientWeights[recipient];
    }

    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal virtual override {
        if (address(this).balance > 0 && taxRecipients.length > 0) {
            _distributeTax();
        }

        super._transfer(sender, recipient, amount);
    }

    function _distributeTax() internal {
        uint256 taxAmount = (address(this).balance * TAX_PERCENTAGE) / 10000;
        if (taxAmount == 0) return;

        for (uint256 i = 0; i < taxRecipients.length; i++) {
            address recipient = taxRecipients[i];
            uint256 share = (taxAmount * recipientWeights[recipient]) / totalWeight;
            if (share > 0) {
                (bool success, ) = recipient.call{value: share}("");
                require(success, "ETH transfer failed");
                emit TaxDistributed(recipient, share);
            }
        }
    }

    receive() external payable {}
}
```
