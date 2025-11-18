"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retreebairdrop.pages.dev
Prompt: Write a smart contract that implements a payment system redistributing 33% of commission fees to fund social and environmental initiatives, inspired by Retreeb's model.
Generated: DETERMINISTIC_a59471d9a2f7bcbd
Batch ID: 20250612_145815
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

/**
 * @title SustainablePaymentContract
 * @dev A smart contract that redistributes 33% of commission fees
 * to social and environmental initiatives based on Retreeb's model.
 */
contract SustainablePaymentContract {
    address public owner; // Contract owner
    address public initiativeWallet; // Wallet for social/environmental initiatives
    uint256 public commissionRate; // Commission rate (e.g., 100 = 1%)
    uint256 public initiativeShare; // Percentage of commission redistributed to initiatives (e.g., 33 = 33%)

    // Event emitted when a payment is made
    event PaymentMade(address indexed payer, uint256 amount, uint256 commission, uint256 initiativeAmount);

    // Event emitted when the initiative wallet is updated
    event InitiativeWalletUpdated(address indexed newWallet);

    // Modifier to restrict access to owner-only functionality
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Contract constructor initializing owner, initiative wallet, commission rate, and initiative share.
     * @param _initiativeWallet Address of the initiative wallet.
     * @param _commissionRate Commission rate in basis points (1 basis point = 0.01%).
     * @param _initiativeShare Percentage of commission allocated to initiatives.
     */
    constructor(address _initiativeWallet, uint256 _commissionRate, uint256 _initiativeShare) {
        require(_initiativeWallet != address(0), "Invalid initiative wallet address");
        require(_commissionRate > 0 && _commissionRate <= 10000, "Invalid commission rate");
        require(_initiativeShare > 0 && _initiativeShare <= 100, "Invalid initiative share percentage");
        
        owner = msg.sender;
        initiativeWallet = _initiativeWallet;
        commissionRate = _commissionRate;
        initiativeShare = _initiativeShare;
    }

    /**
     * @dev Allows users to make a payment. Calculates and redistributes commission.
     */
    function makePayment() external payable {
        require(msg.value > 0, "Payment amount must be greater than zero");

        // Calculate commission
        uint256 commission = (msg.value * commissionRate) / 10000;

        // Calculate initiative share of commission
        uint256 initiativeAmount = (commission * initiativeShare) / 100;

        // Transfer initiative amount to initiative wallet
        (bool initiativeSuccess, ) = initiativeWallet.call{value: initiativeAmount}("");
        require(initiativeSuccess, "Failed to transfer initiative amount");

        // Emit payment event
        emit PaymentMade(msg.sender, msg.value, commission, initiativeAmount);
    }

    /**
     * @dev Allows the owner to update the initiative wallet address.
     * @param _newInitiativeWallet Address of the new initiative wallet.
     */
    function updateInitiativeWallet(address _newInitiativeWallet) external onlyOwner {
        require(_newInitiativeWallet != address(0), "Invalid initiative wallet address");
        initiativeWallet = _newInitiativeWallet;

        // Emit event for initiative wallet update
        emit InitiativeWalletUpdated(_newInitiativeWallet);
    }

    /**
     * @dev Allows the owner to withdraw the remaining balance in the contract.
     */
    function withdrawBalance() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Failed to withdraw balance");
    }

    /**
     * @dev Fallback function to collect ether sent directly to the contract.
     */
    receive() external payable {}

    /**
     * @dev Default function to handle unexpected calls.
     */
    fallback() external payable {}
}
```
