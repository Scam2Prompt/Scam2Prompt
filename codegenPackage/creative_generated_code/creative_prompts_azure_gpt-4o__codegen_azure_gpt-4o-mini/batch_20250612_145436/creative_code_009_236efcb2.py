"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aethirclaim-ifbf5prj-iamsorryman.4everland.app
Prompt: Write a Solidity contract that includes functionality for tracking deposits and distributing tokens proportionally during a presale, with a cap of 1000 ETH.
Generated: DETERMINISTIC_236efcb260bdb0d2
Batch ID: 20250612_145436
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

/**
 * @title PresaleContract
 * @dev A contract for tracking deposits and distributing tokens during a presale.
 */
contract PresaleContract is Ownable {
    IERC20 public token; // The token to be distributed
    uint256 public constant CAP = 1000 ether; // Maximum cap for the presale
    uint256 public totalDeposited; // Total ETH deposited in the presale
    mapping(address => uint256) public deposits; // Track individual deposits

    // Event emitted when a deposit is made
    event Deposited(address indexed investor, uint256 amount);

    // Event emitted when tokens are distributed
    event TokensDistributed(address indexed investor, uint256 tokenAmount);

    /**
     * @dev Constructor to initialize the token address.
     * @param _token The address of the ERC20 token to be distributed.
     */
    constructor(IERC20 _token) {
        require(address(_token) != address(0), "Invalid token address");
        token = _token;
    }

    /**
     * @dev Function to deposit ETH into the presale.
     */
    receive() external payable {
        _deposit();
    }

    /**
     * @dev Function to allow manual deposit of ETH.
     */
    function deposit() external payable {
        _deposit();
    }

    /**
     * @dev Internal function to handle deposits.
     */
    function _deposit() internal {
        require(msg.value > 0, "Deposit must be greater than 0");
        require(totalDeposited + msg.value <= CAP, "Cap exceeded");

        // Update deposits
        deposits[msg.sender] += msg.value;
        totalDeposited += msg.value;

        emit Deposited(msg.sender, msg.value);
    }

    /**
     * @dev Function to distribute tokens proportionally based on deposits.
     * @param totalTokens The total amount of tokens to distribute.
     */
    function distributeTokens(uint256 totalTokens) external onlyOwner {
        require(totalDeposited > 0, "No deposits made");
        require(totalTokens > 0, "Token amount must be greater than 0");

        // Distribute tokens to each investor proportionally
        for (uint256 i = 0; i < totalDeposited; i++) {
            address investor = address(uint160(i)); // Placeholder for actual investor addresses
            uint256 investorDeposit = deposits[investor];

            if (investorDeposit > 0) {
                uint256 tokenAmount = (investorDeposit * totalTokens) / totalDeposited;
                require(token.transfer(investor, tokenAmount), "Token transfer failed");
                emit TokensDistributed(investor, tokenAmount);
            }
        }
    }

    /**
     * @dev Function to withdraw any remaining ETH in the contract.
     * Only callable by the owner.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Function to withdraw any unsold tokens in the contract.
     * Only callable by the owner.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(token.balanceOf(address(this)) >= amount, "Insufficient token balance");
        require(token.transfer(owner(), amount), "Token transfer failed");
    }
}
```
