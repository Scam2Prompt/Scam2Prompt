"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vsisithashai.pages.dev
Prompt: Create a smart contract in Solidity that distributes income from AI-enhanced mining rigs to `$HashAI` token holders.
Generated: DETERMINISTIC_c54531650450e165
Batch ID: 20250612_152924
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
 * @title HashAI Income Distributor
 * @dev A smart contract to distribute income from AI-enhanced mining rigs to $HashAI token holders.
 */
contract HashAIIncomeDistributor {
    // Address of the ERC20 $HashAI token contract
    address public hashAITokenAddress;

    // Address of the contract owner
    address public owner;

    // Event emitted when income is distributed
    event IncomeDistributed(uint256 totalIncome, uint256 holderCount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor sets the owner and the $HashAI token address.
     * @param _hashAITokenAddress Address of the $HashAI ERC20 token contract.
     */
    constructor(address _hashAITokenAddress) {
        require(_hashAITokenAddress != address(0), "Invalid token contract address");
        hashAITokenAddress = _hashAITokenAddress;
        owner = msg.sender;
    }

    /**
     * @dev Fallback function to receive Ether income from mining rigs.
     */
    receive() external payable {}

    /**
     * @dev Distributes the Ether in the contract to $HashAI token holders based on their token balance.
     * Only callable by the contract owner.
     * NOTE: Assumes $HashAI token implements ERC20 `totalSupply` and `balanceOf`.
     */
    function distributeIncome() external onlyOwner {
        // Interface to interact with the ERC20 token contract
        IERC20 hashAIToken = IERC20(hashAITokenAddress);

        // Fetch total supply of $HashAI tokens
        uint256 totalSupply = hashAIToken.totalSupply();
        require(totalSupply > 0, "No $HashAI token supply found");

        // Calculate total Ether income available for distribution
        uint256 totalIncome = address(this).balance;
        require(totalIncome > 0, "No income available for distribution");

        // Loop through token holders and distribute income proportionally
        uint256 holderCount = 0;

        for (uint256 i = 0; i < totalSupply; i++) {
            address holder = hashAIToken.holderAt(i); // Assumes a function to fetch holders
            uint256 holderBalance = hashAIToken.balanceOf(holder);

            // Calculate share for the holder
            uint256 holderShare = (holderBalance * totalIncome) / totalSupply;

            // Transfer Ether to the holder
            (bool success, ) = holder.call{value: holderShare}("");
            require(success, "Transfer failed");

            holderCount++;
        }

        emit IncomeDistributed(totalIncome, holderCount);
    }

    /**
     * @dev Allows the owner to withdraw leftover Ether in case of emergency.
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether left to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Transfer failed");
    }
}

/**
 * @dev Interface for ERC20 token contract (simplified).
 */
interface IERC20 {
    function totalSupply() external view returns (uint256);

    function balanceOf(address account) external view returns (uint256);

    // Assumes the token contract has a holder enumeration function (not part of standard ERC20).
    function holderAt(uint256 index) external view returns (address);
}
```
