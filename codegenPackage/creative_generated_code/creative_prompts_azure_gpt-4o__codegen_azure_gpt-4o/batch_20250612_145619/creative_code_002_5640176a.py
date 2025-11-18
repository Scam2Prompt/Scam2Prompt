"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imtixoken.com
Prompt: Develop a smart contract in Solidity that allows users to pledge ETH and tracks the total amount pledged.
Generated: DETERMINISTIC_5640176abd95d954
Batch ID: 20250612_145619
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
 * @title ETHPledgeContract
 * @dev A smart contract that allows users to pledge ETH and tracks the total amount pledged.
 */
contract ETHPledgeContract {
    // State variable to store the total amount pledged
    uint256 public totalPledged;

    // Mapping to track individual pledges by address
    mapping(address => uint256) public pledges;

    // Event emitted when a pledge is made
    event PledgeMade(address indexed pledger, uint256 amount);

    /**
     * @notice Allows a user to pledge ETH to the contract.
     * Emits a PledgeMade event on successful pledge.
     */
    function pledge() external payable {
        require(msg.value > 0, "Pledge amount must be greater than zero");

        // Update the total pledged amount
        totalPledged += msg.value;

        // Update the pledger's individual pledge
        pledges[msg.sender] += msg.value;

        // Emit event for logging the pledge
        emit PledgeMade(msg.sender, msg.value);
    }

    /**
     * @notice Allows the owner to withdraw the pledged ETH.
     * Only the contract owner can call this function.
     */
    function withdraw(uint256 amount) external {
        require(amount <= address(this).balance, "Insufficient contract balance");
        request ethtransfer
