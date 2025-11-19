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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract PaymentDistributor is Ownable, ReentrancyGuard {
    struct Contributor {
        address payable wallet;
        uint256 sharePercentage; // Basis points (10000 = 100%)
        bool active;
    }

    struct Product {
        address payable creator;
        Contributor[] contributors;
        uint256 totalShares;
        bool exists;
    }

    mapping(bytes32 => Product) public products;
    address public platformWallet;
    uint256 public platformFeePercentage; // Basis points (10000 = 100%)
    IERC20 public paymentToken;

    event ProductRegistered(bytes32 productId, address creator);
    event ContributorAdded(bytes32 productId, address contributor, uint256 sharePercentage);
    event PaymentDistributed(
        bytes32 productId,
        address recipient,
        uint256 amount,
        bool isPlatform
    );
    event PlatformWalletUpdated(address newWallet);
    event PlatformFeeUpdated(uint256 newFee);

    constructor(address _paymentTokenAddress, address _platformWallet, uint256 _platformFeePercentage) {
        require(_platformFeePercentage <= 10000, "Fee cannot exceed 100%");
        paymentToken = IERC20(_paymentTokenAddress);
        platformWallet = payable(_platformWallet);
        platformFeePercentage = _platformFeePercentage;
    }

    function registerProduct(bytes32 productId, address payable creator) external onlyOwner {
        require(!products[productId].exists, "Product already exists");
        
        Product storage newProduct = products[productId];
        newProduct.creator = creator;
        newProduct.exists = true;
        
        emit ProductRegistered(productId, creator);
    }

    function addContributor(
        bytes32 productId,
        address payable contributor,
        uint256 sharePercentage
    ) external onlyOwner {
        require(products[productId].exists, "Product does not exist");
        require(sharePercentage > 0, "Share must be greater than 0");
        
        Product storage product = products[productId];
        require(
            product.totalShares + sharePercentage <= 10000 - platformFeePercentage,
            "Total shares exceed available percentage"
        );

        product.contributors.push(Contributor({
            wallet: contributor,
            sharePercentage: sharePercentage,
            active: true
        }));
        
        product.totalShares += sharePercentage;
        
        emit ContributorAdded(productId, contributor, sharePercentage);
    }

    function distributePayment(bytes32 productId, uint256 totalAmount) external nonReentrant {
        require(products[productId].exists, "Product does not exist");
        require(totalAmount > 0, "Amount must be greater than 0");
        
        Product storage product = products[productId];
        uint256 platformFee = (totalAmount * platformFeePercentage) / 10000;
        uint256 remainingAmount = totalAmount - platformFee;

        // Transfer platform fee
        if (platformFee > 0) {
            require(
                paymentToken.transferFrom(msg.sender, platformWallet, platformFee),
                "Platform fee transfer failed"
            );
            emit PaymentDistributed(productId, platformWallet, platformFee, true);
        }

        // Transfer creator share
        uint256 creatorShare = remainingAmount;
        for (uint256 i = 0; i < product.contributors.length; i++) {
            if (product.contributors[i].active) {
                uint256 contributorShare = (remainingAmount * product.contributors[i].sharePercentage) / product.totalShares;
                creatorShare -= contributorShare;
                
                require(
                    paymentToken.transferFrom(msg.sender, product.contributors[i].wallet, contributorShare),
                    "Contributor transfer failed"
                );
                emit PaymentDistributed(
                    productId,
                    product.contributors[i].wallet,
                    contributorShare,
                    false
                );
            }
        }

        // Transfer remaining to creator
        if (creatorShare > 0) {
            require(
                paymentToken.transferFrom(msg.sender, product.creator, creatorShare),
                "Creator transfer failed"
            );
            emit PaymentDistributed(productId, product.creator, creatorShare, false);
        }
    }

    function updatePlatformWallet(address newWallet) external onlyOwner {
        require(newWallet != address(0), "Invalid wallet address");
        platformWallet = payable(newWallet);
        emit PlatformWalletUpdated(newWallet);
    }

    function updatePlatformFee(uint256 newFeePercentage) external onlyOwner {
        require(newFeePercentage <= 10000, "Fee cannot exceed 100%");
        platformFeePercentage = newFeePercentage;
        emit PlatformFeeUpdated(newFeePercentage);
    }

    function toggleContributorStatus(bytes32 productId, uint256 contributorIndex) external onlyOwner {
        require(products[productId].exists, "Product does not exist");
        require(contributorIndex < products[productId].contributors.length, "Invalid contributor index");
        
        Contributor storage contributor = products[productId].contributors[contributorIndex];
        contributor.active = !contributor.active;
    }

    function getProductContributors(bytes32 productId) external view returns (Contributor[] memory) {
        require(products[productId].exists, "Product does not exist");
        return products[productId].contributors;
    }
}
```
