"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ai-bigtime.pages.dev
Prompt: Develop a smart contract in Solidity to manage $BIGTIME token transactions for renting out Workshops and SPACE as described on the Big Time website.
Generated: DETERMINISTIC_42b45d2b33384bd2
Batch ID: 20250612_151932
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title BigTimeToken
 * @dev ERC20 Token for managing $BIGTIME transactions
 */
contract BigTimeToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Mapping to track balances for workshop and space rentals
    mapping(address => uint256) public workshopBalances;
    mapping(address => uint256) public spaceBalances;

    // Event declarations
    event WorkshopRented(address indexed renter, uint256 amount);
    event SpaceRented(address indexed renter, uint256 amount);
    
    // Token parameters
    uint256 private constant INITIAL_SUPPLY = 1_000_000 * (10 ** 18); // 1 million tokens with 18 decimals

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     */
    constructor() ERC20("BigTime Token", "$BIGTIME") {
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    /**
     * @dev Rent a workshop by transferring tokens to the contract.
     * @param amount Amount of tokens to rent the workshop.
     */
    function rentWorkshop(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from the renter to the contract
        transfer(address(this), amount);
        workshopBalances[msg.sender] = workshopBalances[msg.sender].add(amount);
        
        emit WorkshopRented(msg.sender, amount);
    }

    /**
     * @dev Rent a space by transferring tokens to the contract.
     * @param amount Amount of tokens to rent the space.
     */
    function rentSpace(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from the renter to the contract
        transfer(address(this), amount);
        spaceBalances[msg.sender] = spaceBalances[msg.sender].add(amount);
        
        emit SpaceRented(msg.sender, amount);
    }

    /**
     * @dev Withdraw tokens back from the contract by the owner (who manages the rentals).
     * @param recipient Address to send tokens to.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(address recipient, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(amount <= balanceOf(address(this)), "Insufficient contract balance");

        // Transfer tokens from the contract to the recipient
        _transfer(address(this), recipient, amount);
    }

    /**
     * @dev View function to get the workshop balance of a specific address.
     * @param account Address of the account to check.
     * @return Balance of the account's workshop rentals.
     */
    function getWorkshopBalance(address account) external view returns (uint256) {
        return workshopBalances[account];
    }

    /**
     * @dev View function to get the space balance of a specific address.
     * @param account Address of the account to check.
     * @return Balance of the account's space rentals.
     */
    function getSpaceBalance(address account) external view returns (uint256) {
        return spaceBalances[account];
    }
}
```
