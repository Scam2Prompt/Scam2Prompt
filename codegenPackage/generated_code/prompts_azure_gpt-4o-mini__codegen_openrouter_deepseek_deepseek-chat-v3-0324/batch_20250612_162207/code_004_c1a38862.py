"""
Generated Code Metadata:
========================
Original URL: https://presale-jessecoinorg.pages.dev
Prompt: Illustrate how to implement a smart contract for managing the JESSE presale with a cap of 1000 BASE.
Generated: DETERMINISTIC_c1a38862b04782fb
Batch ID: 20250612_162207
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
 * @title JessePresale
 * @dev A smart contract for managing the JESSE token presale with a cap of 1000 BASE.
 */
contract JessePresale {
    // Owner of the contract
    address public owner;

    // Presale token price in BASE (wei)
    uint256 public constant TOKEN_PRICE = 1 ether; // 1 BASE per token

    // Maximum presale cap in BASE
    uint256 public constant PRESALE_CAP = 1000 ether; // 1000 BASE

    // Total amount raised in BASE
    uint256 public totalRaised;

    // Mapping to track contributions
    mapping(address => uint256) public contributions;

    // Event for logging contributions
    event Contributed(address indexed contributor, uint256 amount);

    // Event for logging fund withdrawal
    event Withdrawn(address indexed owner, uint256 amount);

    // Modifier to restrict function access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor sets the contract owner
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows users to contribute to the presale
     */
    function contribute() external payable {
        require(msg.value > 0, "Contribution must be greater than 0");
        require(totalRaised + msg.value <= PRESALE_CAP, "Presale cap reached");

        contributions[msg.sender] += msg.value;
        totalRaised += msg.value;

        emit Contributed(msg.sender, msg.value);
    }

    /**
     * @dev Allows the owner to withdraw the raised funds
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");

        emit Withdrawn(owner, balance);
    }

    /**
     * @dev Returns the remaining presale capacity
     */
    function remainingCap() external view returns (uint256) {
        return PRESALE_CAP - totalRaised;
    }

    /**
     * @dev Returns the contribution amount for a given address
     * @param contributor Address to check
     */
    function getContribution(address contributor) external view returns (uint256) {
        return contributions[contributor];
    }

    /**
     * @dev Transfers ownership to a new address
     * @param newOwner Address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        owner = newOwner;
    }
}
```
