"""
Generated Code Metadata:
========================
Original URL: https://borroefinnance.web.app
Prompt: Write a smart contract that allows Web3 businesses to offer discounts and incentives to buyers for funding requests, as described in Borroe Finance's solution.
Generated: DETERMINISTIC_df9649ca5a6c107f
Batch ID: 20250612_145319
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

contract BorroeFinanceDiscounts is Ownable, ReentrancyGuard {
    // Struct to store discount details
    struct Discount {
        uint256 discountPercentage; // Percentage discount (e.g., 10 for 10%)
        uint256 minFundingAmount;  // Minimum funding amount to qualify
        uint256 expiryTimestamp;   // When the discount expires
        bool isActive;             // Whether discount is active
    }

    // Struct to store funding request details
    struct FundingRequest {
        address requester;         // Address of the business requesting funds
        uint256 amountRequested;   // Total amount requested
        uint256 amountFunded;      // Amount already funded
        bool isActive;             // Whether request is active
    }

    // Mapping from request ID to FundingRequest
    mapping(uint256 => FundingRequest) public fundingRequests;

    // Mapping from request ID to Discount
    mapping(uint256 => Discount) public discounts;

    // Supported payment token (e.g., USDC, DAI)
    IERC20 public paymentToken;

    // Counter for request IDs
    uint256 public nextRequestId;

    // Events
    event FundingRequestCreated(
        uint256 indexed requestId,
        address indexed requester,
        uint256 amount,
        uint256 discountPercentage,
        uint256 expiryTimestamp
    );
    event FundingContributed(
        uint256 indexed requestId,
        address indexed contributor,
        uint256 amount,
        uint256 discountApplied
    );
    event DiscountUpdated(
        uint256 indexed requestId,
        uint256 newDiscountPercentage,
        uint256 newMinAmount,
        uint256 newExpiry
    );
    event RequestCompleted(uint256 indexed requestId);
    event RequestCancelled(uint256 indexed requestId);

    constructor(address _paymentToken) {
        require(_paymentToken != address(0), "Invalid payment token address");
        paymentToken = IERC20(_paymentToken);
    }

    /**
     * @notice Create a new funding request with discount options
     * @param _amountRequested Total amount needed
     * @param _discountPercentage Discount percentage for early contributors
     * @param _minFundingAmount Minimum amount to qualify for discount
     * @param _expiryTimestamp When the discount expires
     */
    function createFundingRequest(
        uint256 _amountRequested,
        uint256 _discountPercentage,
        uint256 _minFundingAmount,
        uint256 _expiryTimestamp
    ) external {
        require(_amountRequested > 0, "Amount must be greater than 0");
        require(_discountPercentage <= 100, "Discount cannot exceed 100%");
        require(_expiryTimestamp > block.timestamp, "Expiry must be in the future");

        uint256 requestId = nextRequestId++;
        
        fundingRequests[requestId] = FundingRequest({
            requester: msg.sender,
            amountRequested: _amountRequested,
            amountFunded: 0,
            isActive: true
        });

        discounts[requestId] = Discount({
            discountPercentage: _discountPercentage,
            minFundingAmount: _minFundingAmount,
            expiryTimestamp: _expiryTimestamp,
            isActive: true
        });

        emit FundingRequestCreated(
            requestId,
            msg.sender,
            _amountRequested,
            _discountPercentage,
            _expiryTimestamp
        );
    }

    /**
     * @notice Contribute to a funding request and receive discount if eligible
     * @param _requestId ID of the funding request
     * @param _amount Amount to contribute
     */
    function contributeToRequest(uint256 _requestId, uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        
        FundingRequest storage request = fundingRequests[_requestId];
        Discount storage discount = discounts[_requestId];

        require(request.isActive, "Request is not active");
        require(discount.isActive, "Discount is not active");
        require(request.amountFunded + _amount <= request.amountRequested, "Exceeds requested amount");

        uint256 discountAmount = 0;
        
        // Check if contributor is eligible for discount
        if (block.timestamp <= discount.expiryTimestamp && _amount >= discount.minFundingAmount) {
            discountAmount = (_amount * discount.discountPercentage) / 100;
        }

        // Calculate final amount after discount
        uint256 finalAmount = _amount - discountAmount;

        // Transfer tokens from contributor to requester
        require(
            paymentToken.transferFrom(msg.sender, request.requester, finalAmount),
            "Token transfer failed"
        );

        // Update funded amount
        request.amountFunded += _amount;

        emit FundingContributed(_requestId, msg.sender, _amount, discountAmount);

        // Check if request is fully funded
        if (request.amountFunded == request.amountRequested) {
            request.isActive = false;
            discount.isActive = false;
            emit RequestCompleted(_requestId);
        }
    }

    /**
     * @notice Update discount parameters for a request (only requester)
     * @param _requestId ID of the funding request
     * @param _newDiscountPercentage New discount percentage
     * @param _newMinFundingAmount New minimum funding amount
     * @param _newExpiryTimestamp New expiry timestamp
     */
    function updateDiscount(
        uint256 _requestId,
        uint256 _newDiscountPercentage,
        uint256 _newMinFundingAmount,
        uint256 _newExpiryTimestamp
    ) external {
        FundingRequest storage request = fundingRequests[_requestId];
        Discount storage discount = discounts[_requestId];

        require(msg.sender == request.requester, "Only requester can update");
        require(request.isActive, "Request is not active");
        require(_newDiscountPercentage <= 100, "Discount cannot exceed 100%");
        require(_newExpiryTimestamp > block.timestamp, "Expiry must be in the future");

        discount.discountPercentage = _newDiscountPercentage;
        discount.minFundingAmount = _newMinFundingAmount;
        discount.expiryTimestamp = _newExpiryTimestamp;

        emit DiscountUpdated(
            _requestId,
            _newDiscountPercentage,
            _newMinFundingAmount,
            _newExpiryTimestamp
        );
    }

    /**
     * @notice Cancel a funding request (only requester)
     * @param _requestId ID of the funding request to cancel
     */
    function cancelRequest(uint256 _requestId) external {
        FundingRequest storage request = fundingRequests[_requestId];
        Discount storage discount = discounts[_requestId];

        require(msg.sender == request.requester, "Only requester can cancel");
        require(request.isActive, "Request is not active");

        request.isActive = false;
        discount.isActive = false;

        emit RequestCancelled(_requestId);
    }

    /**
     * @notice Emergency function to change payment token (only owner)
     * @param _newPaymentToken Address of new payment token
     */
    function setPaymentToken(address _newPaymentToken) external onlyOwner {
        require(_newPaymentToken != address(0), "Invalid token address");
        paymentToken = IERC20(_newPaymentToken);
    }
}
```
