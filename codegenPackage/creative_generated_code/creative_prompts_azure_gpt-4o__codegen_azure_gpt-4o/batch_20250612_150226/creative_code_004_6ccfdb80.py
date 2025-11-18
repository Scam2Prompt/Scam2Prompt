"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matmo-ccdashboard.pages.dev
Prompt: Write a function in Solidity to implement retroactive public goods funding, allocating percentages (e.g., 22% for public goods) as described in Matmo's tokenomics.
Generated: DETERMINISTIC_6ccfdb80d6319803
Batch ID: 20250612_150226
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
 * @title RetroactivePublicGoodsFunding
 * @dev Implements retroactive public goods funding with percentage-based allocations.
 *      Example percentage: 22% for public goods.
 */
contract RetroactivePublicGoodsFunding {
    // Address where public goods funding will be sent
    address payable public publicGoodsAddress;

    // Percentage allocated for public goods funding (e.g., 22%)
    uint256 public publicGoodsPercentage;

    // Event emitted when funds are distributed
    event FundsDistributed(
        uint256 totalAmount,
        uint256 publicGoodsAmount,
        uint256 remainder
    );

    // Constructor to initialize the contract
    constructor(address payable _publicGoodsAddress, uint256 _publicGoodsPercentage) {
        require(_publicGoodsAddress != address(0), "Invalid public goods address");
        require(_publicGoodsPercentage > 0 && _publicGoodsPercentage <= 100, "Percentage must be between 1 and 100");
        
        publicGoodsAddress = _publicGoodsAddress;
        publicGoodsPercentage = _publicGoodsPercentage;
    }

    /**
     * @dev Distributes funds according to the specified percentage.
     *      Sends percentage of funds to public goods and remainder back to the sender.
     */
    function distributeFunds() external payable {
        require(msg.value > 0, "No ether sent");

        // Calculate the amount for public goods
        uint256 publicGoodsAmount = (msg.value * publicGoodsPercentage) / 100;

        // Calculate the remainder
        uint256 remainder = msg.value - publicGoodsAmount;

        // Transfer the funds for public goods
        (bool publicGoodsTransferSuccess, ) = publicGoodsAddress.call{value: publicGoodsAmount}("");
        require(publicGoodsTransferSuccess, "Public goods transfer failed");

        // Send the remainder back to the sender
        (bool remainderTransferSuccess, ) = msg.sender.call{value: remainder}("");
        require(remainderTransferSuccess, "Remainder transfer failed");

        // Emit event for tracking distributions
        emit FundsDistributed(msg.value, publicGoodsAmount, remainder);
    }

    /**
     * @dev Updates the address for public goods funding.
     * @param _newAddress The new address for public goods funding.
     */
    function updatePublicGoodsAddress(address payable _newAddress) external {
        require(_newAddress != address(0), "Invalid public goods address");
        publicGoodsAddress = _newAddress;
    }

    /**
     * @dev Updates the percentage allocated for public goods funding.
     * @param _newPercentage The new percentage for public goods funding.
     */
    function updatePublicGoodsPercentage(uint256 _newPercentage) external {
        require(_newPercentage > 0 && _newPercentage <= 100, "Percentage must be between 1 and 100");
        publicGoodsPercentage = _newPercentage;
    }

    // Fallback function to prevent accidental ether loss
    fallback() external payable {
        revert("Direct transfers not allowed");
    }

    receive() external payable {
        revert("Direct transfers not allowed");
    }
}
```
