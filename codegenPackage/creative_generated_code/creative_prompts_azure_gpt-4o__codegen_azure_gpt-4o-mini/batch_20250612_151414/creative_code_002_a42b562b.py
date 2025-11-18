"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitsmix.biz
Prompt: Generate a smart contract in Solidity for tokenized convertible bonds, referencing the funding model used by "株式会社YOAKE entertainment."
Generated: DETERMINISTIC_a42b562b4f1db260
Batch ID: 20250612_151414
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ConvertibleBondToken
 * @dev A smart contract for tokenized convertible bonds.
 * This contract allows issuance and conversion of bonds to tokens.
 */
contract ConvertibleBondToken is ERC20, Ownable {
    enum BondStatus { Issued, Convertible, Converted, Redeemed }

    struct Bond {
        uint256 id;
        address issuer;
        uint256 amount;
        uint256 interestRate; // Annual interest rate in basis points
        uint256 maturityDate;
        BondStatus status;
    }

    mapping(uint256 => Bond) public bonds;
    uint256 public bondCounter;

    event BondIssued(uint256 indexed bondId, address indexed issuer, uint256 amount, uint256 interestRate, uint256 maturityDate);
    event BondConverted(uint256 indexed bondId, address indexed holder);
    event BondRedeemed(uint256 indexed bondId, address indexed holder);

    // Modifier to check if bond exists
    modifier bondExists(uint256 bondId) {
        require(bondId < bondCounter, "Bond does not exist.");
        _;
    }

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("Convertible Bond Token", "CBT") {
        bondCounter = 0;
    }

    /**
     * @dev Issues a new bond.
     * @param amount The amount of the bond to issue.
     * @param interestRate The annual interest rate in basis points (e.g., 500 = 5%).
     * @param maturityDate The maturity date of the bond as a Unix timestamp.
     */
    function issueBond(uint256 amount, uint256 interestRate, uint256 maturityDate) external onlyOwner {
        require(maturityDate > block.timestamp, "Maturity date must be in the future.");

        bonds[bondCounter] = Bond(bondCounter, msg.sender, amount, interestRate, maturityDate, BondStatus.Issued);
        emit BondIssued(bondCounter, msg.sender, amount, interestRate, maturityDate);
        bondCounter++;
    }

    /**
     * @dev Allows the bondholder to convert the bond into tokens.
     * @param bondId The ID of the bond to convert.
     */
    function convertBond(uint256 bondId) external bondExists(bondId) {
        Bond storage bond = bonds[bondId];
        require(bond.status == BondStatus.Issued, "Bond is not convertible.");
        require(block.timestamp < bond.maturityDate, "Bond has matured.");

        bond.status = BondStatus.Convertible;
        _mint(msg.sender, bond.amount); // Mint tokens equal to bond amount
        emit BondConverted(bondId, msg.sender);
    }

    /**
     * @dev Redeems a bond after maturity.
     * @param bondId The ID of the bond to redeem.
     */
    function redeemBond(uint256 bondId) external bondExists(bondId) {
        Bond storage bond = bonds[bondId];
        require(bond.status == BondStatus.Convertible, "Bond is not redeemable.");
        require(block.timestamp >= bond.maturityDate, "Bond has not matured.");

        bond.status = BondStatus.Redeemed;
        uint256 interest = (bond.amount * bond.interestRate) / 10000; // Calculate interest
        payable(msg.sender).transfer(bond.amount + interest); // Transfer bond amount + interest to the holder
        emit BondRedeemed(bondId, msg.sender);
    }

    /**
     * @dev Fallback function to accept Ether deposits for bond redemption.
     */
    receive() external payable {}

    /**
     * @dev Withdraws contract balance to the owner.
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
