"""
Generated Code Metadata:
========================
Original URL: https://walletconnect.com
Prompt: Generate an example of integrating multiple features from Reown's toolkit to maximize efficiency in an onchain payment application.
Generated: DETERMINISTIC_94e92230181254b5
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract EfficientPaymentProcessor is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Payment structure
    struct Payment {
        address payer;
        address payee;
        address token;
        uint256 amount;
        uint256 timestamp;
        bool isCompleted;
    }

    // Supported tokens
    mapping(address => bool) public supportedTokens;
    
    // Payment records
    mapping(bytes32 => Payment) public payments;
    
    // Fee configuration
    uint256 public feePercentage; // Basis points (1% = 100)
    address public feeCollector;

    // Events
    event PaymentInitiated(
        bytes32 paymentId,
        address indexed payer,
        address indexed payee,
        address indexed token,
        uint256 amount
    );
    
    event PaymentCompleted(
        bytes32 paymentId,
        address indexed payer,
        address indexed payee,
        address indexed token,
        uint256 amount,
        uint256 fee
    );
    
    event TokenSupportUpdated(address token, bool isSupported);
    event FeeConfigUpdated(uint256 newFeePercentage, address newFeeCollector);

    constructor(uint256 _feePercentage, address _feeCollector) {
        require(_feePercentage <= 1000, "Fee cannot exceed 10%");
        require(_feeCollector != address(0), "Invalid fee collector");
        
        feePercentage = _feePercentage;
        feeCollector = _feeCollector;
    }

    /**
     * @dev Initialize a new payment
     * @param payee Recipient address
     * @param token ERC20 token address
     * @param amount Payment amount
     * @return paymentId Unique payment identifier
     */
    function initiatePayment(
        address payee,
        address token,
        uint256 amount
    ) external nonReentrant returns (bytes32 paymentId) {
        require(payee != address(0), "Invalid payee address");
        require(supportedTokens[token], "Token not supported");
        require(amount > 0, "Amount must be positive");

        paymentId = keccak256(
            abi.encodePacked(
                msg.sender,
                payee,
                token,
                amount,
                block.timestamp
            )
        );

        payments[paymentId] = Payment({
            payer: msg.sender,
            payee: payee,
            token: token,
            amount: amount,
            timestamp: block.timestamp,
            isCompleted: false
        });

        emit PaymentInitiated(paymentId, msg.sender, payee, token, amount);
        return paymentId;
    }

    /**
     * @dev Complete a payment by transferring tokens
     * @param paymentId Payment identifier
     */
    function completePayment(bytes32 paymentId) external nonReentrant {
        Payment storage payment = payments[paymentId];
        require(payment.payer == msg.sender, "Only payer can complete");
        require(!payment.isCompleted, "Payment already completed");

        uint256 fee = payment.amount.mul(feePercentage).div(10000);
        uint256 payeeAmount = payment.amount.sub(fee);

        IERC20 token = IERC20(payment.token);
        
        // Transfer tokens from payer to contract
        require(
            token.transferFrom(msg.sender, address(this), payment.amount),
            "Transfer failed"
        );
        
        // Transfer fee to collector
        if (fee > 0) {
            require(
                token.transfer(feeCollector, fee),
                "Fee transfer failed"
            );
        }
        
        // Transfer remaining to payee
        require(
            token.transfer(payment.payee, payeeAmount),
            "Payee transfer failed"
        );

        payment.isCompleted = true;
        
        emit PaymentCompleted(
            paymentId,
            payment.payer,
            payment.payee,
            payment.token,
            payment.amount,
            fee
        );
    }

    /**
     * @dev Update supported tokens
     * @param token Token address
     * @param isSupported Whether to support or not
     */
    function updateTokenSupport(address token, bool isSupported) external onlyOwner {
        supportedTokens[token] = isSupported;
        emit TokenSupportUpdated(token, isSupported);
    }

    /**
     * @dev Update fee configuration
     * @param newFeePercentage New fee percentage in basis points
     * @param newFeeCollector New fee collector address
     */
    function updateFeeConfig(uint256 newFeePercentage, address newFeeCollector) external onlyOwner {
        require(newFeePercentage <= 1000, "Fee cannot exceed 10%");
        require(newFeeCollector != address(0), "Invalid fee collector");
        
        feePercentage = newFeePercentage;
        feeCollector = newFeeCollector;
        
        emit FeeConfigUpdated(newFeePercentage, newFeeCollector);
    }

    /**
     * @dev Emergency withdraw tokens (owner only)
     * @param token Token address
     * @param amount Amount to withdraw
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(owner(), amount);
    }
}
```
