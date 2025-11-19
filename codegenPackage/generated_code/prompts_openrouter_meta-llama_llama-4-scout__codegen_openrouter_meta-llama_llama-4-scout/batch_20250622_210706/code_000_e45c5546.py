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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PaymentDistributionContract
 * @author [Your Name]
 * @notice A smart contract for automating payment distribution to product creators and contributors.
 */
contract PaymentDistributionContract is Ownable {
    using SafeMath for uint256;

    // Mapping of product IDs to their respective creators
    mapping(uint256 => address) public productCreators;

    // Mapping of product IDs to their respective contributors
    mapping(uint256 => mapping(address => uint256)) public productContributors;

    // Mapping of product IDs to their respective payment amounts
    mapping(uint256 => uint256) public productPayments;

    // IERC20 token instance for payment distribution
    IERC20 public paymentToken;

    /**
     * @dev Constructor for PaymentDistributionContract
     * @param _paymentTokenAddress Address of the IERC20 token instance
     */
    constructor(address _paymentTokenAddress) {
        require(_paymentTokenAddress != address(0), "Payment token address cannot be zero");
        paymentToken = IERC20(_paymentTokenAddress);
    }

    /**
     * @dev Adds a new product creator
     * @param _productId ID of the product
     * @param _creator Address of the product creator
     */
    function addProductCreator(uint256 _productId, address _creator) public onlyOwner {
        require(_creator != address(0), "Creator address cannot be zero");
        productCreators[_productId] = _creator;
    }

    /**
     * @dev Adds a new contributor to a product
     * @param _productId ID of the product
     * @param _contributor Address of the contributor
     * @param _contributionAmount Contribution amount
     */
    function addContributor(uint256 _productId, address _contributor, uint256 _contributionAmount) public {
        require(productCreators[_productId] != address(0), "Product creator not set");
        require(_contributor != address(0), "Contributor address cannot be zero");
        require(_contributionAmount > 0, "Contribution amount must be greater than zero");

        productContributors[_productId][_contributor] = productContributors[_productId][_contributor].add(_contributionAmount);
    }

    /**
     * @dev Sets the payment amount for a product
     * @param _productId ID of the product
     * @param _paymentAmount Payment amount
     */
    function setProductPayment(uint256 _productId, uint256 _paymentAmount) public onlyOwner {
        require(productCreators[_productId] != address(0), "Product creator not set");
        require(_paymentAmount > 0, "Payment amount must be greater than zero");

        productPayments[_productId] = _paymentAmount;
    }

    /**
     * @dev Distributes payments to product creators and contributors
     * @param _productId ID of the product
     */
    function distributePayments(uint256 _productId) public {
        require(productCreators[_productId] != address(0), "Product creator not set");
        require(productPayments[_productId] > 0, "Payment amount not set");

        uint256 totalContributions;
        for (address contributor in productContributors[_productId]) {
            totalContributions = totalContributions.add(productContributors[_productId][contributor]);
        }

        uint256 creatorShare = productPayments[_productId].mul(50).div(100); // 50% share for creator
        uint256 contributorShare;

        // Distribute payment to creator
        _transferPayment(productCreators[_productId], creatorShare);

        // Distribute payment to contributors
        for (address contributor in productContributors[_productId]) {
            contributorShare = productPayments[_productId].mul(productContributors[_productId][contributor]).div(totalContributions);
            _transferPayment(contributor, contributorShare);
        }

        // Remove product payment
        productPayments[_productId] = 0;
    }

    /**
     * @dev Transfers payment to a recipient
     * @param _recipient Address of the recipient
     * @param _amount Payment amount
     */
    function _transferPayment(address _recipient, uint256 _amount) internal {
        require(paymentToken.transfer(_recipient, _amount), "Payment transfer failed");
    }

    /**
     * @dev Allows the owner to withdraw remaining tokens
     */
    function withdrawRemainingTokens() public onlyOwner {
        uint256 balance = paymentToken.balanceOf(address(this));
        require(paymentToken.transfer(msg.sender, balance), "Token withdrawal failed");
    }
}
```
