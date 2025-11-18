"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retikclaim.web.app
Prompt: Write a Solidity smart contract to manage the tokenomics of RETIK, including presale allocation, ecosystem reserves, and cashback reserve distribution.
Generated: DETERMINISTIC_c97b52349b42c25c
Batch ID: 20250612_150848
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
 * @title RETIKToken
 * @dev A contract to manage the tokenomics of RETIK including presale allocation, ecosystem reserves, and cashback reserve distribution.
 */
contract RETIKToken is ERC20, Ownable {
    // Allocate presale tokens
    uint256 public presaleAllocation;
    // Ecosystem reserves
    uint256 public ecosystemReserves;
    // Cashback reserve
    uint256 public cashbackReserve;
    // Total supply of the token
    uint256 private totalSupplyCap;
    
    // Mapping to track presale contributions
    mapping(address => uint256) public presaleContributions;

    // Events
    event PresaleContribution(address indexed contributor, uint256 amount);
    event CashbackDistributed(address indexed buyer, uint256 amount);

    // Constructor to initialize the token and its allocations
    constructor(
        string memory name, 
        string memory symbol,
        uint256 _totalSupplyCap,
        uint256 _presaleAllocation,
        uint256 _ecosystemReserves,
        uint256 _cashbackReserve
    ) ERC20(name, symbol) {
        totalSupplyCap = _totalSupplyCap;
        presaleAllocation = _presaleAllocation;
        ecosystemReserves = _ecosystemReserves;
        cashbackReserve = _cashbackReserve;
        
        // Mint the total supply of tokens to the contract owner
        _mint(msg.sender, totalSupplyCap);
    }

    /**
     * @dev Function to allow contributions to the presale
     * @param amount The amount to contribute
     */
    function contributePresale(uint256 amount) external payable {
        require(amount > 0, "Contribution must be greater than 0");
        require(msg.value == amount, "Value sent must match the contribution amount");
        require(presaleAllocation >= amount, "Not enough tokens available for presale");

        presaleContributions[msg.sender] += amount;
        presaleAllocation -= amount;

        emit PresaleContribution(msg.sender, amount);
    }

    /**
     * @dev Function to distribute cashback to buyers
     * @param buyer The address of the buyer
     * @param amount The amount of cashback to distribute
     */
    function distributeCashback(address buyer, uint256 amount) external onlyOwner {
        require(cashbackReserve >= amount, "Not enough cashback reserve available");
        require(balanceOf(address(this)) >= amount, "Contract does not have enough tokens to distribute");

        cashbackReserve -= amount;
        _transfer(address(this), buyer, amount);

        emit CashbackDistributed(buyer, amount);
    }

    /**
     * @dev Function to withdraw funds from the contract
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Function to check the current balance of the contract
     * @return The current balance of the contract
     */
    function contractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    /**
     * @dev Function to check available presale tokens
     * @return The amount of tokens available for presale
     */
    function availablePresaleTokens() external view returns (uint256) {
        return presaleAllocation;
    }

    /**
     * @dev Function to check available cashback reserves
     * @return The amount of cashback reserves
     */
    function availableCashbackReserves() external view returns (uint256) {
        return cashbackReserve;
    }
}
```
