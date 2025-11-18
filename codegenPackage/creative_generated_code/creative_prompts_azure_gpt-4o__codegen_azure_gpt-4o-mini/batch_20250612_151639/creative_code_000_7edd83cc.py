"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paxful.bond
Prompt: Write a Solidity smart contract for an Ethereum-based DeFi application that integrates features similar to those described on paxful.bond.
Generated: DETERMINISTIC_7edd83cceda852e6
Batch ID: 20250612_151639
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title DeFiBond
 * @dev A simple DeFi application that allows users to create and manage bonds.
 */
contract DeFiBond is Ownable, ReentrancyGuard {
    // Structure to hold bond details
    struct Bond {
        address holder;        // Address of the bond holder
        uint256 amount;       // Amount of tokens locked in the bond
        uint256 maturityDate; // Timestamp for when the bond matures
        bool redeemed;        // Status of the bond redemption
    }

    // Mapping from bond ID to Bond details
    mapping(uint256 => Bond) public bonds;
    uint256 public nextBondId; // Counter for bond IDs

    // ERC20 token used for the bonds
    IERC20 public immutable token;

    // Events
    event BondCreated(uint256 bondId, address indexed holder, uint256 amount, uint256 maturityDate);
    event BondRedeemed(uint256 bondId, address indexed holder, uint256 amount);

    /**
     * @dev Constructor to set the token address.
     * @param _token Address of the ERC20 token used for bonds.
     */
    constructor(address _token) {
        require(_token != address(0), "Invalid token address");
        token = IERC20(_token);
    }

    /**
     * @dev Create a bond by locking tokens.
     * @param amount Amount of tokens to lock in the bond.
     * @param duration Duration in seconds until the bond matures.
     */
    function createBond(uint256 amount, uint256 duration) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");

        // Transfer tokens from the bond holder to this contract
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Create the bond
        bonds[nextBondId] = Bond({
            holder: msg.sender,
            amount: amount,
            maturityDate: block.timestamp + duration,
            redeemed: false
        });

        emit BondCreated(nextBondId, msg.sender, amount, maturityDate);
        nextBondId++;
    }

    /**
     * @dev Redeem a matured bond.
     * @param bondId ID of the bond to redeem.
     */
    function redeemBond(uint256 bondId) external nonReentrant {
        Bond storage bond = bonds[bondId];

        require(bond.holder == msg.sender, "Not the bond holder");
        require(block.timestamp >= bond.maturityDate, "Bond has not matured");
        require(!bond.redeemed, "Bond already redeemed");

        // Mark the bond as redeemed
        bond.redeemed = true;

        // Transfer tokens back to the bond holder
        require(token.transfer(msg.sender, bond.amount), "Token transfer failed");

        emit BondRedeemed(bondId, msg.sender, bond.amount);
    }

    /**
     * @dev Function to withdraw tokens from the contract in case of an emergency.
     * @param amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer tokens to the owner
        require(token.transfer(msg.sender, amount), "Token transfer failed");
    }

    /**
     * @dev Get details about a bond.
     * @param bondId ID of the bond to query.
     * @return holder Address of the bond holder.
     * @return amount Amount of tokens locked in the bond.
     * @return maturityDate Timestamp for when the bond matures.
     * @return redeemed Status of the bond redemption.
     */
    function getBondDetails(uint256 bondId) external view returns (address holder, uint256 amount, uint256 maturityDate, bool redeemed) {
        Bond storage bond = bonds[bondId];
        return (bond.holder, bond.amount, bond.maturityDate, bond.redeemed);
    }
}
```
