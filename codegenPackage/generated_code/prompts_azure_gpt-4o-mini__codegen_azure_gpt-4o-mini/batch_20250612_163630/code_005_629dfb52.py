"""
Generated Code Metadata:
========================
Original URL: https://frame-i48.pages.dev
Prompt: Illustrate how to utilize the Frame Creator's Fund in a smart contract for supporting creators through L2 gas fees.
Generated: DETERMINISTIC_629dfb5256ba6a3b
Batch ID: 20250612_163630
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title FrameCreatorFund
 * @dev A smart contract to support creators by utilizing the Frame Creator's Fund
 *      to cover Layer 2 gas fees for transactions.
 */
contract FrameCreatorFund is Ownable {
    // Event emitted when funds are distributed to a creator
    event FundsDistributed(address indexed creator, uint256 amount);

    // Mapping to track the balance of each creator
    mapping(address => uint256) private creatorBalances;

    // The ERC20 token used for the fund
    IERC20 public token;

    /**
     * @dev Constructor to initialize the contract with the token address.
     * @param _tokenAddress The address of the ERC20 token used for the fund.
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        token = IERC20(_tokenAddress);
    }

    /**
     * @dev Function to deposit funds into the creator's balance.
     * @param amount The amount of tokens to deposit.
     */
    function depositFunds(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update the contract's balance
        creatorBalances[msg.sender] += amount;
    }

    /**
     * @dev Function to distribute funds to a creator.
     * @param creator The address of the creator to receive funds.
     * @param amount The amount of tokens to distribute.
     */
    function distributeFunds(address creator, uint256 amount) external onlyOwner {
        require(creator != address(0), "Invalid creator address");
        require(amount > 0, "Amount must be greater than zero");
        require(creatorBalances[creator] >= amount, "Insufficient balance");

        // Update the creator's balance
        creatorBalances[creator] -= amount;

        // Transfer the funds to the creator
        require(token.transfer(creator, amount), "Transfer failed");

        emit FundsDistributed(creator, amount);
    }

    /**
     * @dev Function to check the balance of a creator.
     * @param creator The address of the creator.
     * @return The balance of the creator.
     */
    function getCreatorBalance(address creator) external view returns (uint256) {
        return creatorBalances[creator];
    }

    /**
     * @dev Function to withdraw tokens from the contract by the owner.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer the tokens to the owner
        require(token.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
