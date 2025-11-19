"""
Generated Code Metadata:
========================
Original URL: https://mixtoearn-migration.pages.dev
Prompt: Create a relayer system in Solidity that allows users to process withdrawals without pre-funding their accounts, deducting transaction fees directly from the transferred amount, as described in the MixToEarn protocol.
Generated: DETERMINISTIC_5099bcba5200a687
Batch ID: 20250612_153420
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
 * @title MixToEarn Relayer
 * @dev Allows users to process withdrawals without pre-funding accounts
 * Fees are deducted directly from the transferred amount
 */
contract MixToEarnRelayer is Ownable, ReentrancyGuard {
    // Token to be used for transfers
    IERC20 public immutable token;

    // Fee percentage (e.g., 100 = 1%)
    uint256 public feePercentage;

    // Minimum fee amount
    uint256 public minFeeAmount;

    // Maximum fee amount
    uint256 public maxFeeAmount;

    // Address to collect fees
    address public feeCollector;

    // Events
    event WithdrawalProcessed(
        address indexed sender,
        address indexed recipient,
        uint256 amount,
        uint256 fee
    );
    event FeeParametersUpdated(
        uint256 feePercentage,
        uint256 minFeeAmount,
        uint256 maxFeeAmount
    );
    event FeeCollectorUpdated(address newFeeCollector);

    /**
     * @dev Constructor
     * @param _token Address of the ERC20 token
     * @param _feePercentage Initial fee percentage (100 = 1%)
     * @param _minFeeAmount Minimum fee amount
     * @param _maxFeeAmount Maximum fee amount
     * @param _feeCollector Address to collect fees
     */
    constructor(
        address _token,
        uint256 _feePercentage,
        uint256 _minFeeAmount,
        uint256 _maxFeeAmount,
        address _feeCollector
    ) {
        require(_token != address(0), "Invalid token address");
        require(_feeCollector != address(0), "Invalid fee collector address");
        require(_minFeeAmount <= _maxFeeAmount, "Invalid fee range");

        token = IERC20(_token);
        feePercentage = _feePercentage;
        minFeeAmount = _minFeeAmount;
        maxFeeAmount = _maxFeeAmount;
        feeCollector = _feeCollector;
    }

    /**
     * @dev Process withdrawal with fee deduction
     * @param recipient Address to receive the funds
     * @param amount Amount to withdraw before fee deduction
     */
    function processWithdrawal(address recipient, uint256 amount) external nonReentrant {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");

        uint256 fee = calculateFee(amount);
        uint256 amountAfterFee = amount - fee;

        require(
            token.transferFrom(msg.sender, address(this), amount),
            "TransferFrom failed"
        );

        // Transfer fee to collector
        if (fee > 0) {
            require(
                token.transfer(feeCollector, fee),
                "Fee transfer failed"
            );
        }

        // Transfer remaining amount to recipient
        require(
            token.transfer(recipient, amountAfterFee),
            "Transfer failed"
        );

        emit WithdrawalProcessed(msg.sender, recipient, amount, fee);
    }

    /**
     * @dev Calculate fee for a given amount
     * @param amount Amount to calculate fee for
     * @return fee Calculated fee amount
     */
    function calculateFee(uint256 amount) public view returns (uint256 fee) {
        fee = (amount * feePercentage) / 10000; // Divide by 10000 for basis points

        // Apply min/max bounds
        if (fee < minFeeAmount) {
            fee = minFeeAmount;
        } else if (fee > maxFeeAmount) {
            fee = maxFeeAmount;
        }

        return fee;
    }

    /**
     * @dev Update fee parameters (owner only)
     * @param _feePercentage New fee percentage (100 = 1%)
     * @param _minFeeAmount New minimum fee amount
     * @param _maxFeeAmount New maximum fee amount
     */
    function updateFeeParameters(
        uint256 _feePercentage,
        uint256 _minFeeAmount,
        uint256 _maxFeeAmount
    ) external onlyOwner {
        require(_minFeeAmount <= _maxFeeAmount, "Invalid fee range");
        
        feePercentage = _feePercentage;
        minFeeAmount = _minFeeAmount;
        maxFeeAmount = _maxFeeAmount;

        emit FeeParametersUpdated(_feePercentage, _minFeeAmount, _maxFeeAmount);
    }

    /**
     * @dev Update fee collector address (owner only)
     * @param _feeCollector New fee collector address
     */
    function updateFeeCollector(address _feeCollector) external onlyOwner {
        require(_feeCollector != address(0), "Invalid fee collector address");
        feeCollector = _feeCollector;
        emit FeeCollectorUpdated(_feeCollector);
    }

    /**
     * @dev Emergency withdraw any ERC20 tokens (owner only)
     * @param _token Token address to withdraw
     * @param _amount Amount to withdraw
     */
    function emergencyWithdraw(address _token, uint256 _amount) external onlyOwner {
        require(_token != address(token), "Cannot withdraw main token");
        IERC20(_token).transfer(owner(), _amount);
    }
}
```
