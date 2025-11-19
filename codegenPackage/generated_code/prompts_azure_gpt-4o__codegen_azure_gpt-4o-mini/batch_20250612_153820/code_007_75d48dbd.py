"""
Generated Code Metadata:
========================
Original URL: https://whale.market
Prompt: Suggest an approach to implement a DAO-controlled fee structure similar to Whales Market's roadmap for EVM and Cosmos chains.
Generated: DETERMINISTIC_75d48dbd8005cc6f
Batch ID: 20250612_153820
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title FeeManager
 * @dev This contract manages a DAO-controlled fee structure for transactions.
 */
contract FeeManager is Ownable {
    // Event emitted when the fee structure is updated
    event FeeUpdated(uint256 newFee);

    // Event emitted when a fee is collected
    event FeeCollected(address indexed collector, uint256 amount);

    // The fee percentage (in basis points, e.g., 100 = 1%)
    uint256 public feePercentage;

    // The address of the token used for fees
    IERC20 public feeToken;

    // Mapping to track fees collected by each address
    mapping(address => uint256) public feesCollected;

    /**
     * @dev Constructor to initialize the fee manager.
     * @param _feeToken The address of the ERC20 token used for fees.
     * @param _initialFee The initial fee percentage in basis points.
     */
    constructor(IERC20 _feeToken, uint256 _initialFee) {
        require(_initialFee <= 10000, "Fee cannot exceed 100%");
        feeToken = _feeToken;
        feePercentage = _initialFee;
    }

    /**
     * @dev Updates the fee percentage. Only callable by the contract owner.
     * @param _newFee The new fee percentage in basis points.
     */
    function updateFee(uint256 _newFee) external onlyOwner {
        require(_newFee <= 10000, "Fee cannot exceed 100%");
        feePercentage = _newFee;
        emit FeeUpdated(_newFee);
    }

    /**
     * @dev Collects fees from a transaction amount.
     * @param _amount The total transaction amount.
     * @return feeAmount The calculated fee amount.
     */
    function collectFee(uint256 _amount) external returns (uint256 feeAmount) {
        feeAmount = (_amount * feePercentage) / 10000;
        require(feeAmount > 0, "Fee amount must be greater than zero");

        // Transfer the fee from the sender to this contract
        require(feeToken.transferFrom(msg.sender, address(this), feeAmount), "Fee transfer failed");

        // Update the fees collected for the sender
        feesCollected[msg.sender] += feeAmount;

        emit FeeCollected(msg.sender, feeAmount);
    }

    /**
     * @dev Allows the owner to withdraw collected fees.
     * @param _to The address to withdraw fees to.
     * @param _amount The amount of fees to withdraw.
     */
    function withdrawFees(address _to, uint256 _amount) external onlyOwner {
        require(_amount <= feeToken.balanceOf(address(this)), "Insufficient balance");
        require(_to != address(0), "Invalid address");

        // Transfer the specified amount of fees to the owner
        feeToken.transfer(_to, _amount);
    }

    /**
     * @dev Returns the current fee percentage.
     * @return The current fee percentage in basis points.
     */
    function getCurrentFee() external view returns (uint256) {
        return feePercentage;
    }
}
```
