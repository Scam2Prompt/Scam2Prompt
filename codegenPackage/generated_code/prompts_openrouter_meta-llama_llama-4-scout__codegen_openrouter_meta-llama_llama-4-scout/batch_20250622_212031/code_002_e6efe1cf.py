"""
Generated Code Metadata:
========================
Original URL: https://zoracoin.io
Prompt: Generate a smart contract code snippet in Solidity for handling ZORA Token presale transactions, including token allocation and bonus calculation.
Generated: DETERMINISTIC_e6efe1cff682cfba
Batch ID: 20250622_212031
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title ZORATokenPresale
 * @author [Your Name]
 * @notice Handles ZORA Token presale transactions, including token allocation and bonus calculation.
 */
contract ZORATokenPresale is ReentrancyGuard {
    // Mapping of user contributions
    mapping (address => uint256) public contributions;

    // Mapping of user token allocations
    mapping (address => uint256) public tokenAllocations;

    // ZORA Token instance
    ERC20 public zoraToken;

    // Presale end timestamp
    uint256 public presaleEnd;

    // Token price in USD (1e18 for decimal places)
    uint256 public tokenPrice;

    // Bonus structure
    //  0-1000 ZORA: 10% bonus
    // 1001-5000 ZORA: 5% bonus
    // 5001+: no bonus
    uint256 public bonusThreshold1;
    uint256 public bonusThreshold2;
    uint256 public bonusRate1;
    uint256 public bonusRate2;

    /**
     * @notice Initializes the presale contract.
     * @param _zoraToken ZORA Token instance address.
     * @param _presaleEnd Presale end timestamp.
     * @param _tokenPrice Token price in USD (1e18 for decimal places).
     */
    constructor(
        address _zoraToken,
        uint256 _presaleEnd,
        uint256 _tokenPrice
    ) {
        zoraToken = ERC20(_zoraToken);
        presaleEnd = _presaleEnd;
        tokenPrice = _tokenPrice;

        // Initialize bonus structure
        bonusThreshold1 = 1000 * 1e18; // 1000 ZORA
        bonusThreshold2 = 5000 * 1e18; // 5000 ZORA
        bonusRate1 = 10; // 10% bonus
        bonusRate2 = 5; // 5% bonus
    }

    /**
     * @notice Contribute to the presale and receive ZORA Tokens.
     * @param _amount Contribution amount in USD (1e18 for decimal places).
     */
    function contribute(uint256 _amount) external nonReentrant {
        require(block.timestamp < presaleEnd, "Presale has ended.");

        // Calculate token allocation
        uint256 tokenAllocation = _amount * 1e18 / tokenPrice;

        // Apply bonus if eligible
        uint256 bonus = calculateBonus(tokenAllocation);
        tokenAllocation += bonus;

        // Update user contribution and token allocation
        contributions[msg.sender] += _amount;
        tokenAllocations[msg.sender] += tokenAllocation;

        // Transfer tokens to user
        zoraToken.transfer(msg.sender, tokenAllocation);
    }

    /**
     * @notice Calculates the bonus for a given token allocation.
     * @param _tokenAllocation Token allocation amount.
     * @return Bonus amount.
     */
    function calculateBonus(uint256 _tokenAllocation) internal view returns (uint256) {
        if (_tokenAllocation <= bonusThreshold1) {
            return _tokenAllocation * bonusRate1 / 100;
        } else if (_tokenAllocation <= bonusThreshold2) {
            return _tokenAllocation * bonusRate2 / 100;
        } else {
            return 0;
        }
    }

    /**
     * @notice Withdraws unsold tokens from the contract.
     * @dev Only callable by the contract owner.
     */
    function withdrawTokens() external {
        require(msg.sender == owner(), "Only the contract owner can withdraw tokens.");

        uint256 balance = zoraToken.balanceOf(address(this));
        zoraToken.transfer(msg.sender, balance);
    }

    /**
     * @notice Gets the contract owner.
     * @return Contract owner address.
     */
    function owner() public view returns (address) {
        return msg.sender;
    }
}
```
