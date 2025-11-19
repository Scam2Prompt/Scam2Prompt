"""
Generated Code Metadata:
========================
Original URL: https://beacons-dabcat.pages.dev
Prompt: Write a smart contract in Solidity to manage a token sale on Ethereum with a soft cap of 8 ETH and a hard cap of 119 ETH.
Generated: DETERMINISTIC_9f80399338f74804
Batch ID: 20250622_204722
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

/**
 * @title TokenSale
 * @dev A smart contract to manage a token sale with a soft cap and hard cap.
 */
contract TokenSale {
    // State variables
    address public owner; // Owner of the contract
    uint256 public softCap = 8 ether; // Soft cap in ETH
    uint256 public hardCap = 119 ether; // Hard cap in ETH
    uint256 public totalFundsRaised; // Total funds raised in the sale
    bool public saleActive; // Flag to indicate if the sale is active

    mapping(address => uint256) public contributions; // Tracks contributions by each address

    // Events
    event SaleStarted();
    event SaleEnded();
    event ContributionReceived(address indexed contributor, uint256 amount);
    event RefundIssued(address indexed contributor, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    modifier saleIsActive() {
        require(saleActive, "Token sale is not active");
        _;
    }

    modifier withinHardCap(uint256 amount) {
        require(totalFundsRaised + amount <= hardCap, "Contribution exceeds hard cap");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender; // Set the contract deployer as the owner
    }

    /**
     * @dev Start the token sale.
     * Can only be called by the owner.
     */
    function startSale() external onlyOwner {
        require(!saleActive, "Sale is already active");
        saleActive = true;
        emit SaleStarted();
    }

    /**
     * @dev End the token sale.
     * Can only be called by the owner.
     */
    function endSale() external onlyOwner {
        require(saleActive, "Sale is not active");
        saleActive = false;
        emit SaleEnded();
    }

    /**
     * @dev Contribute to the token sale.
     * Accepts ETH and tracks contributions.
     */
    function contribute() external payable saleIsActive withinHardCap(msg.value) {
        require(msg.value > 0, "Contribution must be greater than zero");

        contributions[msg.sender] += msg.value; // Track contribution
        totalFundsRaised += msg.value; // Update total funds raised

        emit ContributionReceived(msg.sender, msg.value);
    }

    /**
     * @dev Issue refunds if the soft cap is not met.
     * Can only be called by the owner after the sale ends.
     */
    function issueRefunds() external onlyOwner {
        require(!saleActive, "Sale must be ended to issue refunds");
        require(totalFundsRaised < softCap, "Soft cap has been met, no refunds");

        for (uint256 i = 0; i < contributors.length; i++) {
            address contributor = contributors[i];
            uint256 amount = contributions[contributor];
            if (amount > 0) {
                contributions[contributor] = 0; // Reset contribution
                payable(contributor).transfer(amount); // Refund ETH
                emit RefundIssued(contributor, amount);
            }
        }
    }

    /**
     * @dev Withdraw funds if the soft cap is met.
     * Can only be called by the owner after the sale ends.
     */
    function withdrawFunds() external onlyOwner {
        require(!saleActive, "Sale must be ended to withdraw funds");
        require(totalFundsRaised >= softCap, "Soft cap not met, cannot withdraw funds");

        payable(owner).transfer(address(this).balance); // Transfer all funds to the owner
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Direct ETH transfers are not allowed");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct ETH transfers are not allowed");
    }
}
```
