"""
Generated Code Metadata:
========================
Original URL: https://ethkd.com
Prompt: Write a Solidity function that validates ETH pledges and ensures the pledged amount meets a minimum threshold before accepting the transaction.
Generated: DETERMINISTIC_e9a3d386e48f265f
Batch ID: 20250612_145245
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

contract PledgeValidator {
    uint256 public minPledgeAmount;

    event PledgeAccepted(address indexed pledger, uint256 amount);
    event PledgeRejected(address indexed pledger, uint256 amount, string reason);

    constructor(uint256 _minPledgeAmount) {
        require(_minPledgeAmount > 0, "Minimum pledge amount must be greater than 0");
        minPledgeAmount = _minPledgeAmount;
    }

    /**
     * @dev Validates and accepts ETH pledges
     * @notice Requires the sent ETH to meet the minimum pledge amount
     */
    function pledge() external payable {
        require(msg.value > 0, "Pledge amount must be greater than 0");
        
        if (msg.value < minPledgeAmount) {
            emit PledgeRejected(
                msg.sender,
                msg.value,
                "Pledge amount below minimum threshold"
            );
            // Return funds to sender
            (bool sent, ) = msg.sender.call{value: msg.value}("");
            require(sent, "Failed to return ETH");
            return;
        }

        emit PledgeAccepted(msg.sender, msg.value);
    }

    /**
     * @dev Allows the owner to update the minimum pledge amount
     * @param _newMinPledge The new minimum pledge amount in wei
     */
    function updateMinPledge(uint256 _newMinPledge) external {
        require(_newMinPledge > 0, "Minimum pledge amount must be greater than 0");
        minPledgeAmount = _newMinPledge;
    }
}
```
