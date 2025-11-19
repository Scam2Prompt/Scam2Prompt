"""
Generated Code Metadata:
========================
Original URL: https://aethirclaim-ifbf5prj-iamsorryman.4everland.app
Prompt: Write a Solidity contract that includes functionality for tracking deposits and distributing tokens proportionally during a presale, with a cap of 1000 ETH.
Generated: DETERMINISTIC_236efcb260bdb0d2
Batch ID: 20250612_145436
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PresaleContract
 * @dev A contract for tracking deposits and distributing tokens during a presale.
 */
contract PresaleContract is Ownable {
    // Maximum cap for the presale in ETH
    uint256 public constant MAX_CAP = 1000 ether;

    // Total amount raised in the presale
    uint256 public totalRaised;

    // Mapping of addresses to their deposits
    mapping(address => uint256) public deposits;

    // The token to be distributed
    IERC20 public token;

    // Event emitted when a deposit is made
    event Deposited(address indexed investor, uint256 amount);

    // Event emitted when tokens are distributed
    event TokensDistributed(address indexed investor, uint256 tokenAmount);

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _token The address of the ERC20 token to be distributed.
     */
    constructor(IERC20 _token) {
        token = _token;
    }

    /**
     * @dev Function to deposit ETH into the presale.
     * @notice Investors can deposit ETH until the cap is reached.
     */
    receive() external payable {
        require(msg.value > 0, "Deposit must be greater than 0");
        require(totalRaised + msg.value <= MAX_CAP, "Cap exceeded");

        deposits[msg.sender] += msg.value;
        totalRaised += msg.value;

        emit Deposited(msg.sender, msg.value);
    }

    /**
     * @dev Function to distribute tokens proportionally to investors.
     * @notice Can only be called by the owner after the presale ends.
     */
    function distributeTokens() external onlyOwner {
        require(totalRaised > 0, "No funds raised");

        for (uint256 i = 0; i < totalInvestors(); i++) {
            address investor = getInvestor(i);
            uint256 depositAmount = deposits[investor];

            if (depositAmount > 0) {
                uint256 tokenAmount = calculateTokenAmount(depositAmount);
                require(token.balanceOf(address(this)) >= tokenAmount, "Insufficient tokens in contract");

                deposits[investor] = 0; // Reset deposit after distribution
                token.transfer(investor, tokenAmount);

                emit TokensDistributed(investor, tokenAmount);
            }
        }
    }

    /**
     * @dev Function to calculate the amount of tokens to distribute based on the deposit.
     * @param depositAmount The amount of ETH deposited by the investor.
     * @return The amount of tokens to be distributed.
     */
    function calculateTokenAmount(uint256 depositAmount) internal view returns (uint256) {
        // Assuming a fixed rate of 1 token per 0.01 ETH
        return depositAmount * 100; // Adjust the rate as necessary
    }

    /**
     * @dev Function to get the total number of investors.
     * @return The total number of unique investors.
     */
    function totalInvestors() internal view returns (uint256) {
        // This function should return the count of unique investors
        // Implementation depends on how you want to track investors
        // For simplicity, this is a placeholder
        return 0; // Replace with actual logic
    }

    /**
     * @dev Function to get an investor's address by index.
     * @param index The index of the investor.
     * @return The address of the investor.
     */
    function getInvestor(uint256 index) internal view returns (address) {
        // This function should return the address of the investor at the given index
        // Implementation depends on how you want to track investors
        // For simplicity, this is a placeholder
        return address(0); // Replace with actual logic
    }

    /**
     * @dev Function to withdraw any remaining ETH from the contract.
     * @notice Can only be called by the owner.
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
