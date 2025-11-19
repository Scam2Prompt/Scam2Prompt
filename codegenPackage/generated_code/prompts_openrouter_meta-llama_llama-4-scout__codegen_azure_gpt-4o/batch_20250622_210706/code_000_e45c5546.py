"""
Generated Code Metadata:
========================
Original URL: https://lookscoin.com
Prompt: Write a smart contract in Solidity that automates payment distribution to product creators and contributors on a blockchain-based platform like LookRev.
Generated: DETERMINISTIC_e45c554675f25d7a
Batch ID: 20250622_210706
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

/**
 * @title PaymentDistributor
 * @dev A smart contract to automate payment distribution to product creators and contributors.
 */
contract PaymentDistributor {
    // Struct to store contributor details
    struct Contributor {
        address payable wallet; // Wallet address of the contributor
        uint256 sharePercentage; // Share percentage (e.g., 20 for 20%)
    }

    // Mapping to store contributors for each product
    mapping(uint256 => Contributor[]) private productContributors;

    // Event emitted when a payment is distributed
    event PaymentDistributed(uint256 indexed productId, uint256 totalAmount);

    /**
     * @dev Add contributors for a specific product.
     * @param productId The ID of the product.
     * @param wallets Array of contributor wallet addresses.
     * @param percentages Array of share percentages corresponding to the wallets.
     */
    function addContributors(
        uint256 productId,
        address payable[] memory wallets,
        uint256[] memory percentages
    ) external {
        require(wallets.length == percentages.length, "Mismatched arrays");
        require(wallets.length > 0, "No contributors provided");

        uint256 totalPercentage = 0;

        // Clear existing contributors for the product
        delete productContributors[productId];

        for (uint256 i = 0; i < wallets.length; i++) {
            require(percentages[i] > 0, "Share percentage must be greater than 0");
            totalPercentage += percentages[i];

            productContributors[productId].push(
                Contributor({wallet: wallets[i], sharePercentage: percentages[i]})
            );
        }

        require(totalPercentage == 100, "Total share percentage must equal 100");
    }

    /**
     * @dev Distribute payment to contributors for a specific product.
     * @param productId The ID of the product.
     */
    function distributePayment(uint256 productId) external payable {
        require(msg.value > 0, "Payment amount must be greater than 0");
        require(productContributors[productId].length > 0, "No contributors for this product");

        uint256 totalAmount = msg.value;

        for (uint256 i = 0; i < productContributors[productId].length; i++) {
            Contributor memory contributor = productContributors[productId][i];
            uint256 payment = (totalAmount * contributor.sharePercentage) / 100;

            // Transfer payment to the contributor
            (bool success, ) = contributor.wallet.call{value: payment}("");
            require(success, "Payment transfer failed");
        }

        emit PaymentDistributed(productId, totalAmount);
    }

    /**
     * @dev Fallback function to accept Ether.
     */
    receive() external payable {}

    /**
     * @dev Withdraw any remaining Ether in the contract (only callable by the contract owner).
     */
    function withdraw() external {
        require(msg.sender == address(this), "Only contract owner can withdraw");
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");

        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Withdrawal failed");
    }
}
```
