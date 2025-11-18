"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sonic-labs.vercel.app
Prompt: Write a Solidity smart contract that utilizes Sonic's Fee Monetization feature to maximize developer earnings by boosting on-chain traffic. Include examples of how fees are distributed.
Generated: DETERMINISTIC_9998fe1cd7aee74a
Batch ID: 20250612_145917
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
 * @title SonicFeeMonetizationContract
 * @dev A smart contract to implement Sonic's Fee Monetization feature for maximizing developer earnings
 * and boosting on-chain traffic. Includes fee distribution functionality.
 */
contract SonicFeeMonetizationContract {
    // State variables
    address public owner; // Address of the contract owner
    uint256 public feePercentage; // Fee percentage (e.g., 5 means 5%)

    mapping(address => uint256) public feesCollected; // Mapping to keep track of fees collected by each address

    event FeeDistributed(address indexed recipient, uint256 amount);
    event FeeCollected(address indexed payer, uint256 amount);
    event FeePercentageUpdated(uint256 oldPercentage, uint256 newPercentage);

    /**
     * @dev Modifier to restrict certain actions to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with a default fee percentage.
     * @param _feePercentage Default fee percentage to set.
     */
    constructor(uint256 _feePercentage) {
        require(_feePercentage <= 100, "Fee percentage must be between 0 and 100");
        owner = msg.sender;
        feePercentage = _feePercentage;
    }

    /**
     * @dev Update the fee percentage. Only callable by the contract owner.
     * @param _newFeePercentage The new fee percentage to set.
     */
    function updateFeePercentage(uint256 _newFeePercentage) external onlyOwner {
        require(_newFeePercentage <= 100, "Fee percentage must be between 0 and 100");
        uint256 oldPercentage = feePercentage;
        feePercentage = _newFeePercentage;
        emit FeePercentageUpdated(oldPercentage, _newFeePercentage);
    }

    /**
     * @dev Collect fees from users for transactions.
     * @param _payer Address of the fee payer.
     * @param _transactionAmount Total transaction amount.
     */
    function collectFee(address _payer, uint256 _transactionAmount) external {
        require(_payer != address(0), "Invalid payer address");
        require(_transactionAmount > 0, "Transaction amount must be greater than zero");

        // Calculate the fee amount
        uint256 feeAmount = (_transactionAmount * feePercentage) / 100;

        // Update the fees collected mapping
        feesCollected[_payer] += feeAmount;

        emit FeeCollected(_payer, feeAmount);
    }

    /**
     * @dev Distribute collected fees to a specific recipient.
     * @param _recipient Address of the recipient.
     * @param _amount The amount to distribute.
     */
    function distributeFee(address _recipient, uint256 _amount) external onlyOwner {
        require(_recipient != address(0), "Invalid recipient address");
        require(_amount > 0, "Distribution amount must be greater than zero");
        require(address(this).balance >= _amount, "Insufficient contract balance");

        // Transfer the fee to the recipient
        (bool success, ) = _recipient.call{value: _amount}("");
        require(success, "Fee distribution failed");

        emit FeeDistributed(_recipient, _amount);
    }

    /**
     * @dev Function to receive ETH into the contract.
     */
    receive() external payable {}

    /**
     * @dev Fallback function to handle any sent ETH.
     */
    fallback() external payable {}
}
```
