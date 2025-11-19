"""
Generated Code Metadata:
========================
Original URL: https://daoprivateai.pages.dev
Prompt: Create a smart contract using Solidity to manage data sharing, monetization, and incentivization for data owners and contributors on the PrivateAI platform.
Generated: DETERMINISTIC_1a14ed94ed1eb5c5
Batch ID: 20250622_211405
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

/**
 * @title PrivateAIDataSharing
 * @dev Smart contract for managing data sharing, monetization, and incentivization
 * on the PrivateAI platform.
 */
contract PrivateAIDataSharing is Ownable, ReentrancyGuard {
    // Struct to represent a data contribution
    struct DataContribution {
        address contributor;
        string dataHash;
        string metadata;
        uint256 timestamp;
        uint256 price;
        bool isAvailable;
    }

    // Struct to represent a data purchase
    struct DataPurchase {
        address buyer;
        uint256 contributionId;
        uint256 timestamp;
        uint256 amountPaid;
    }

    // Token used for payments
    IERC20 public paymentToken;

    // Platform fee percentage (1 = 1%)
    uint256 public platformFeePercentage;

    // Mapping of contribution ID to DataContribution
    mapping(uint256 => DataContribution) public contributions;

    // Mapping of purchase ID to DataPurchase
    mapping(uint256 => DataPurchase) public purchases;

    // Mapping of contributor to their contribution IDs
    mapping(address => uint256[]) public contributorToIds;

    // Mapping of buyer to their purchase IDs
    mapping(address => uint256[]) public buyerToIds;

    // Total number of contributions
    uint256 public totalContributions;

    // Total number of purchases
    uint256 public totalPurchases;

    // Events
    event ContributionAdded(
        uint256 indexed contributionId,
        address indexed contributor,
        string dataHash,
        uint256 price
    );
    event ContributionUpdated(
        uint256 indexed contributionId,
        uint256 newPrice,
        bool isAvailable
    );
    event DataPurchased(
        uint256 indexed purchaseId,
        uint256 indexed contributionId,
        address indexed buyer,
        uint256 amountPaid
    );
    event PlatformFeeUpdated(uint256 newFeePercentage);
    event FundsWithdrawn(address indexed recipient, uint256 amount);

    /**
     * @dev Constructor
     * @param _paymentToken Address of the ERC20 token used for payments
     * @param _platformFeePercentage Initial platform fee percentage
     */
    constructor(address _paymentToken, uint256 _platformFeePercentage) {
        require(_paymentToken != address(0), "Invalid token address");
        require(_platformFeePercentage <= 100, "Fee cannot exceed 100%");
        
        paymentToken = IERC20(_paymentToken);
        platformFeePercentage = _platformFeePercentage;
    }

    /**
     * @dev Add a new data contribution
     * @param _dataHash Hash of the contributed data
     * @param _metadata Metadata describing the data
     * @param _price Price for accessing this data
     */
    function addContribution(
        string memory _dataHash,
        string memory _metadata,
        uint256 _price
    ) external {
        require(bytes(_dataHash).length > 0, "Data hash cannot be empty");
        
        totalContributions++;
        contributions[totalContributions] = DataContribution({
            contributor: msg.sender,
            dataHash: _dataHash,
            metadata: _metadata,
            timestamp: block.timestamp,
            price: _price,
            isAvailable: true
        });
        
        contributorToIds[msg.sender].push(totalContributions);
        
        emit ContributionAdded(
            totalContributions,
            msg.sender,
            _dataHash,
            _price
        );
    }

    /**
     * @dev Update an existing contribution
     * @param _contributionId ID of the contribution to update
     * @param _newPrice New price for the contribution
     * @param _isAvailable Whether the contribution is available for purchase
     */
    function updateContribution(
        uint256 _contributionId,
        uint256 _newPrice,
        bool _isAvailable
    ) external {
        require(
            _contributionId > 0 && _contributionId <= totalContributions,
            "Invalid contribution ID"
        );
        require(
            contributions[_contributionId].contributor == msg.sender,
            "Only contributor can update"
        );
        
        contributions[_contributionId].price = _newPrice;
        contributions[_contributionId].isAvailable = _isAvailable;
        
        emit ContributionUpdated(_contributionId, _newPrice, _isAvailable);
    }

    /**
     * @dev Purchase access to a data contribution
     * @param _contributionId ID of the contribution to purchase
     */
    function purchaseData(uint256 _contributionId) external nonReentrant {
        require(
            _contributionId > 0 && _contributionId <= totalContributions,
            "Invalid contribution ID"
        );
        
        DataContribution storage contribution = contributions[_contributionId];
        
        require(contribution.isAvailable, "Contribution not available");
        require(
            contribution.contributor != msg.sender,
            "Cannot purchase your own contribution"
        );
        
        uint256 amount = contribution.price;
        uint256 platformFee = (amount * platformFeePercentage) / 100;
        uint256 contributorAmount = amount - platformFee;
        
        require(
            paymentToken.transferFrom(msg.sender, address(this), amount),
            "Payment failed"
        );
        
        // Transfer to contributor
        require(
            paymentToken.transfer(contribution.contributor, contributorAmount),
            "Transfer to contributor failed"
        );
        
        totalPurchases++;
        purchases[totalPurchases] = DataPurchase({
            buyer: msg.sender,
            contributionId: _contributionId,
            timestamp: block.timestamp,
            amountPaid: amount
        });
        
        buyerToIds[msg.sender].push(totalPurchases);
        
        emit DataPurchased(
            totalPurchases,
            _contributionId,
            msg.sender,
            amount
        );
    }

    /**
     * @dev Update platform fee percentage (owner only)
     * @param _newFeePercentage New fee percentage
     */
    function updatePlatformFee(uint256 _newFeePercentage) external onlyOwner {
        require(_newFeePercentage <= 100, "Fee cannot exceed 100%");
        platformFeePercentage = _newFeePercentage;
        emit PlatformFeeUpdated(_newFeePercentage);
    }

    /**
     * @dev Withdraw accumulated platform fees (owner only)
     */
    function withdrawPlatformFees() external onlyOwner nonReentrant {
        uint256 balance = paymentToken.balanceOf(address(this));
        require(balance > 0, "No funds to withdraw");
        
        require(
            paymentToken.transfer(msg.sender, balance),
            "Withdrawal failed"
        );
        
        emit FundsWithdrawn(msg.sender, balance);
    }

    /**
     * @dev Get contribution IDs for a contributor
     * @param _contributor Address of the contributor
     * @return Array of contribution IDs
     */
    function getContributionsByAddress(address _contributor)
        external
        view
        returns (uint256[] memory)
    {
        return contributorToIds[_contributor];
    }

    /**
     * @dev Get purchase IDs for a buyer
     * @param _buyer Address of the buyer
     * @return Array of purchase IDs
     */
    function getPurchasesByAddress(address _buyer)
        external
        view
        returns (uint256[] memory)
    {
        return buyerToIds[_buyer];
    }

    /**
     * @dev Get details of a contribution
     * @param _contributionId ID of the contribution
     * @return DataContribution struct
     */
    function getContributionDetails(uint256 _contributionId)
        external
        view
        returns (DataContribution memory)
    {
        require(
            _contributionId > 0 && _contributionId <= totalContributions,
            "Invalid contribution ID"
        );
        return contributions[_contributionId];
    }

    /**
     * @dev Get details of a purchase
     * @param _purchaseId ID of the purchase
     * @return DataPurchase struct
     */
    function getPurchaseDetails(uint256 _purchaseId)
        external
        view
        returns (DataPurchase memory)
    {
        require(
            _purchaseId > 0 && _purchaseId <= totalPurchases,
            "Invalid purchase ID"
        );
        return purchases[_purchaseId];
    }
}
```
