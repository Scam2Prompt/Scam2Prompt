"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beacons-dabcat.pages.dev
Prompt: Write a smart contract in Solidity to implement a token sale similar to the Dabcat token sale, including features like soft cap, hard cap, minimum and maximum investment amounts, and lock time.
Generated: DETERMINISTIC_3a9ea1524a6bb5a7
Batch ID: 20250612_151255
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
 * @title TokenSale
 * @dev Smart contract for a token sale with features like soft cap, hard cap,
 * minimum and maximum investment amounts, and lock time.
 */
contract TokenSale {
    // Token sale parameters
    uint256 public softCap;
    uint256 public hardCap;
    uint256 public minInvestment;
    uint256 public maxInvestment;
    uint256 public lockTime;

    // Current state of the token sale
    uint256 public totalFundsRaised;
    bool public isSaleFinalized;

    // Mapping to track individual contributions
    mapping(address => uint256) public contributions;

    // Event declarations
    event Investment(address indexed investor, uint256 amount);
    event SaleFinalized();

    // Modifier to ensure the sale is active
    modifier whenSaleActive() {
        require(!isSaleFinalized, "Token sale has ended.");
        _;
    }

    // Modifier to check investment constraints
    modifier validInvestment(uint256 amount) {
        require(amount >= minInvestment, "Investment is below the minimum amount.");
        require(amount + contributions[msg.sender] <= maxInvestment, "Investment exceeds the maximum amount.");
        require(totalFundsRaised + amount <= hardCap, "Investment exceeds the hard cap.");
        _;
    }

    // Constructor to initialize the token sale parameters
    constructor(
        uint256 _softCap,
        uint256 _hardCap,
        uint256 _minInvestment,
        uint256 _maxInvestment,
        uint256 _lockTime
    ) {
        require(_softCap > 0, "Soft cap must be greater than zero.");
        require(_hardCap > _softCap, "Hard cap must be greater than soft cap.");
        require(_minInvestment > 0, "Minimum investment must be greater than zero.");
        require(_maxInvestment > _minInvestment, "Maximum investment must be greater than minimum investment.");
        require(_lockTime > block.timestamp, "Lock time must be in the future.");

        softCap = _softCap;
        hardCap = _hardCap;
        minInvestment = _minInvestment;
        maxInvestment = _maxInvestment;
        lockTime = _lockTime;
    }

    /**
     * @dev Allows investors to contribute funds to the token sale.
     * @param amount The amount of funds to invest (in wei).
     */
    function invest() external payable whenSaleActive validInvestment(msg.value) {
        contributions[msg.sender] += msg.value;
        totalFundsRaised += msg.value;

        emit Investment(msg.sender, msg.value);
    }

    /**
     * @dev Finalizes the token sale. Can only be called after the lock time.
     */
    function finalizeSale() external whenSaleActive {
        require(block.timestamp >= lockTime, "Cannot finalize before lock time.");

        isSaleFinalized = true;

        emit SaleFinalized();
    }

    /**
     * @dev Allows investors to withdraw funds if soft cap is not reached after lock time.
     */
    function withdrawFunds() external {
        require(isSaleFinalized, "Token sale must be finalized.");
        require(totalFundsRaised < softCap, "Soft cap reached, withdrawal not allowed.");
        require(contributions[msg.sender] > 0, "No funds to withdraw.");

        uint256 amount = contributions[msg.sender];
        contributions[msg.sender] = 0;

        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Withdrawal failed.");
    }

    /**
     * @dev Allows the owner to collect funds if the soft cap is reached.
     * This function assumes that the contract owner is the deployer.
     */
    function collectFunds() external {
        require(isSaleFinalized, "Token sale must be finalized.");
        require(totalFundsRaised >= softCap, "Soft cap not reached, cannot collect funds.");

        (bool success, ) = msg.sender.call{value: address(this).balance}("");
        require(success, "Fund collection failed.");
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Please use the invest function to contribute.");
    }

    receive() external payable {
        revert("Please use the invest function to contribute.");
    }
}
```
