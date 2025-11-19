"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerdogs.icu
Prompt: Design a Solidity contract that implements a hold bonus feature, rewarding users for maintaining their investment without withdrawals, similar to MinerDog's model.
Generated: DETERMINISTIC_d95fd21e2430ca43
Batch ID: 20250612_155753
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
 * @title HoldBonusContract
 * @dev This contract rewards users with a hold bonus for maintaining their investment without withdrawals.
 */
contract HoldBonusContract {
    // State variables
    address public owner; // Owner of the contract
    uint256 public bonusRate; // Bonus rate (e.g., 5%)
    uint256 public minimumHoldDuration; // Minimum holding duration for bonus eligibility (in seconds)
    
    struct Investor {
        uint256 investment; // Amount invested by the user
        uint256 lastWithdrawalTime; // Timestamp of the last withdrawal
        uint256 bonusAccumulated; // Accumulated bonus for the user
    }

    mapping(address => Investor) public investors; // Mapping of investors' data

    // Events
    event InvestmentMade(address indexed investor, uint256 amount);
    event WithdrawalMade(address indexed investor, uint256 amount, uint256 bonusPaid);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can call this function.");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the bonus rate and minimum hold duration.
     * @param _bonusRate Bonus rate percentage (e.g., 5 for 5%)
     * @param _minimumHoldDuration Minimum holding duration for bonus eligibility (in seconds)
     */
    constructor(uint256 _bonusRate, uint256 _minimumHoldDuration) {
        require(_bonusRate > 0, "Bonus rate must be greater than zero.");
        require(_minimumHoldDuration > 0, "Minimum hold duration must be greater than zero.");
        
        owner = msg.sender;
        bonusRate = _bonusRate;
        minimumHoldDuration = _minimumHoldDuration;
    }

    /**
     * @dev Function to allow users to invest funds.
     */
    function invest() external payable {
        require(msg.value > 0, "Investment amount must be greater than zero.");

        // Update the investor's data
        Investor storage investor = investors[msg.sender];
        investor.investment += msg.value;
        if (investor.lastWithdrawalTime == 0) {
            investor.lastWithdrawalTime = block.timestamp; // Initialize lastWithdrawalTime on first investment
        }

        emit InvestmentMade(msg.sender, msg.value);
    }

    /**
     * @dev Function to withdraw funds including the hold bonus.
     */
    function withdraw(uint256 _amount) external {
        Investor storage investor = investors[msg.sender];
        require(investor.investment >= _amount, "Insufficient investment balance.");
        require(_amount > 0, "Withdrawal amount must be greater than zero.");

        // Calculate the hold bonus if the minimum hold duration has passed
        uint256 bonus = 0;
        if (block.timestamp >= investor.lastWithdrawalTime + minimumHoldDuration) {
            bonus = (investor.investment * bonusRate) / 100; // Calculate bonus
            investor.bonusAccumulated += bonus;
        }

        // Update investor data
        investor.investment -= _amount;
        investor.lastWithdrawalTime = block.timestamp;

        // Transfer withdrawal amount and bonus to the investor
        uint256 totalAmount = _amount + bonus;
        (bool sent, ) = msg.sender.call{value: totalAmount}("");
        require(sent, "Failed to transfer funds.");

        emit WithdrawalMade(msg.sender, _amount, bonus);
    }

    /**
     * @dev Function to allow the owner to withdraw contract funds (for administrative purposes).
     * This should be used cautiously and ensure investor funds are not impacted.
     */
    function ownerWithdraw(uint256 _amount) external onlyOwner {
        require(address(this).balance >= _amount, "Insufficient contract balance.");
        (bool sent, ) = owner.call{value: _amount}("");
        require(sent, "Failed to transfer funds.");
    }

    /**
     * @dev Fallback function to accept plain ether transfers.
     */
    receive() external payable {}

    /**
     * @dev Function to get the contract's balance.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
