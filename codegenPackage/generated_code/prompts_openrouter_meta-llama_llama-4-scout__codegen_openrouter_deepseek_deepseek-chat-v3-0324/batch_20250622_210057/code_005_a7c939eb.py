"""
Generated Code Metadata:
========================
Original URL: https://arbius-en.pages.dev
Prompt: "Develop a code example for a model creator to earn income by setting a base fee for invocations of their model on the Arbius network."
Generated: DETERMINISTIC_a7c939eb550630c9
Batch ID: 20250622_210057
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
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract ModelFeeManager is Ownable, Pausable {
    // Token used for payments
    IERC20 public paymentToken;

    // Model creator address
    address public modelCreator;

    // Base fee for model invocations
    uint256 public baseFee;

    // Events
    event FeeUpdated(uint256 newFee);
    event PaymentReceived(address payer, uint256 amount);
    event Withdrawal(address recipient, uint256 amount);

    /**
     * @dev Constructor
     * @param _paymentToken Address of ERC20 token used for payments
     * @param _modelCreator Address of the model creator
     * @param _baseFee Initial base fee for model invocations
     */
    constructor(
        address _paymentToken,
        address _modelCreator,
        uint256 _baseFee
    ) {
        require(_paymentToken != address(0), "Invalid payment token address");
        require(_modelCreator != address(0), "Invalid model creator address");
        
        paymentToken = IERC20(_paymentToken);
        modelCreator = _modelCreator;
        baseFee = _baseFee;
    }

    /**
     * @dev Pay the fee to invoke the model
     * @param amount Amount to pay (must be >= baseFee)
     */
    function payFee(uint256 amount) external whenNotPaused {
        require(amount >= baseFee, "Payment must cover base fee");
        require(
            paymentToken.transferFrom(msg.sender, address(this), amount),
            "Payment transfer failed"
        );
        emit PaymentReceived(msg.sender, amount);
    }

    /**
     * @dev Update the base fee (only callable by model creator)
     * @param newFee New base fee amount
     */
    function updateBaseFee(uint256 newFee) external onlyOwner {
        require(newFee != baseFee, "Fee must be different");
        baseFee = newFee;
        emit FeeUpdated(newFee);
    }

    /**
     * @dev Withdraw accumulated fees (only callable by model creator)
     * @param amount Amount to withdraw
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(
            paymentToken.transfer(modelCreator, amount),
            "Withdrawal transfer failed"
        );
        emit Withdrawal(modelCreator, amount);
    }

    /**
     * @dev Pause contract (only callable by model creator)
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause contract (only callable by model creator)
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Get current contract balance
     * @return Current balance of payment tokens
     */
    function getBalance() external view returns (uint256) {
        return paymentToken.balanceOf(address(this));
    }
}
```
