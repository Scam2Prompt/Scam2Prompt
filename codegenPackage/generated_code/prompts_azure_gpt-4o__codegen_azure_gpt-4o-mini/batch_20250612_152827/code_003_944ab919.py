"""
Generated Code Metadata:
========================
Original URL: https://bitcoindogsclub-en.pages.dev
Prompt: Create a smart contract in Solidity to manage the tokenomics of $0DOG, including the 90% token distribution and automatic removal of unsold tokens after 30 days.
Generated: DETERMINISTIC_944ab91939db00a3
Batch ID: 20250612_152827
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title 0DOG Token
 * @dev This contract implements an ERC20 token with specific tokenomics for $0DOG.
 * It includes a 90% distribution mechanism and automatic removal of unsold tokens after 30 days.
 */
contract ZeroDogToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10**18; // 1 million tokens with 18 decimals
    // Distribution percentage
    uint256 public constant DISTRIBUTION_PERCENTAGE = 90; // 90%
    // Time limit for unsold tokens removal
    uint256 public constant REMOVAL_TIME_LIMIT = 30 days;

    // Track the timestamp of the token sale
    uint256 public saleStartTime;
    // Track the amount of tokens distributed
    uint256 public distributedTokens;
    // Track if the unsold tokens have been removed
    bool public unsoldTokensRemoved;

    // Event emitted when tokens are distributed
    event TokensDistributed(address indexed recipient, uint256 amount);

    constructor() ERC20("0DOG Token", "0DOG") {
        // Mint total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);
        saleStartTime = block.timestamp;
        distributedTokens = 0;
        unsoldTokensRemoved = false;
    }

    /**
     * @dev Distribute tokens to a recipient.
     * @param recipient The address to receive the tokens.
     * @param amount The amount of tokens to distribute.
     */
    function distributeTokens(address recipient, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(distributedTokens.add(amount) <= TOTAL_SUPPLY.mul(DISTRIBUTION_PERCENTAGE).div(100), "Exceeds distribution limit");

        // Transfer tokens to the recipient
        _transfer(owner(), recipient, amount);
        distributedTokens = distributedTokens.add(amount);
        emit TokensDistributed(recipient, amount);
    }

    /**
     * @dev Remove unsold tokens after the sale period.
     * Can only be called by the owner.
     */
    function removeUnsoldTokens() external onlyOwner {
        require(block.timestamp >= saleStartTime.add(REMOVAL_TIME_LIMIT), "Removal time limit not reached");
        require(!unsoldTokensRemoved, "Unsold tokens already removed");

        uint256 unsoldTokens = TOTAL_SUPPLY.sub(distributedTokens);
        if (unsoldTokens > 0) {
            // Burn the unsold tokens
            _burn(address(this), unsoldTokens);
        }
        unsoldTokensRemoved = true;
    }

    /**
     * @dev Override the _beforeTokenTransfer hook to prevent transfers during the sale period.
     */
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override {
        require(block.timestamp >= saleStartTime.add(REMOVAL_TIME_LIMIT) || from == owner(), "Transfers are not allowed during the sale period");
        super._beforeTokenTransfer(from, to, amount);
    }
}
```
