"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uxiom.trade
Prompt: Develop a smart contract for sending ETH that aligns with the cryptosend platform's use case and includes network fee handling.
Generated: DETERMINISTIC_4544f1a03cdb8825
Batch ID: 20250612_154131
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
 * @title CryptoSend Smart Contract
 * @dev A production-ready smart contract for sending ETH, including network fee handling.
 */
contract CryptoSend {
    // Address of the contract owner
    address public owner;

    // Fee percentage in basis points (e.g., 250 = 2.5%)
    uint256 public feeBasisPoints;

    // Event emitted when ETH is sent
    event EtherSent(address indexed sender, address indexed recipient, uint256 amount, uint256 fee);

    // Event emitted when the fee percentage is updated
    event FeeUpdated(uint256 oldFeeBasisPoints, uint256 newFeeBasisPoints);

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Contract constructor sets the initial owner and fee percentage.
     * @param _feeBasisPoints Initial fee percentage in basis points.
     */
    constructor(uint256 _feeBasisPoints) {
        require(_feeBasisPoints <= 10000, "Fee basis points must be <= 10000");
        owner = msg.sender;
        feeBasisPoints = _feeBasisPoints;
    }

    /**
     * @dev Updates the fee percentage.
     * @param _feeBasisPoints New fee percentage in basis points.
     */
    function updateFee(uint256 _feeBasisPoints) external onlyOwner {
        require(_feeBasisPoints <= 10000, "Fee basis points must be <= 10000");
        uint256 oldFeeBasisPoints = feeBasisPoints;
        feeBasisPoints = _feeBasisPoints;

        emit FeeUpdated(oldFeeBasisPoints, _feeBasisPoints);
    }

    /**
     * @dev Sends ETH to a specified recipient, deducting the platform fee.
     * @param recipient Address of the recipient.
     */
    function sendEther(address payable recipient) external payable {
        require(recipient != address(0), "Recipient address cannot be zero");
        require(msg.value > 0, "Amount must be greater than zero");

        uint256 fee = (msg.value * feeBasisPoints) / 10000; // Calculate fee
        uint256 amountToSend = msg.value - fee;            // Amount after fee deduction

        require(amountToSend > 0, "Insufficient ETH to send after fee deduction");

        // Transfer ETH to recipient
        recipient.transfer(amountToSend);

        // Transfer fee to contract owner
        payable(owner).transfer(fee);

        emit EtherSent(msg.sender, recipient, amountToSend, fee);
    }

    /**
     * @dev Fallback function to accept ETH directly into the contract.
     */
    receive() external payable {}

    /**
     * @dev Withdraws any ETH left in the contract to the owner.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH left to withdraw");

        payable(owner).transfer(balance);
    }
}
```
