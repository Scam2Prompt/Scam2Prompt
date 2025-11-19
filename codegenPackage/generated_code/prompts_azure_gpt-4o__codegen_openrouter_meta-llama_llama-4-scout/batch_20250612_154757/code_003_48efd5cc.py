"""
Generated Code Metadata:
========================
Original URL: https://btcbull.io
Prompt: Implement a token burn mechanism in Solidity that automatically burns a percentage of $BTCBULL supply whenever Bitcoin's price increases by $25K, following the milestones described on the BTC Bull roadmap.
Generated: DETERMINISTIC_48efd5ccc1b303d5
Batch ID: 20250612_154757
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title BTCBull Token
 * @author [Your Name]
 * @notice Token contract with automatic burn mechanism based on Bitcoin price milestones
 */
contract BTCBullToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of Bitcoin price milestones to burn percentages
    mapping(uint256 => uint256) public burnMilestones;

    // Current Bitcoin price
    uint256 public currentBitcoinPrice;

    // Flag to prevent reentrancy
    bool public isBurning;

    /**
     * @param name_ Token name
     * @param symbol_ Token symbol
     * @param initialSupply_ Initial token supply
     */
    constructor(string memory name_, string memory symbol_, uint256 initialSupply_) ERC20(name_, symbol_) {
        _mint(msg.sender, initialSupply_);

        // Initialize burn milestones (in $)
        burnMilestones[25000] = 5; // 5% burn at $25,000
        burnMilestones[50000] = 10; // 10% burn at $50,000
        burnMilestones[75000] = 15; // 15% burn at $75,000

        // Initialize current Bitcoin price
        currentBitcoinPrice = 0;
    }

    /**
     * @notice Update the current Bitcoin price
     * @param newPrice New Bitcoin price
     */
    function updateBitcoinPrice(uint256 newPrice) public onlyOwner {
        require(newPrice > 0, "Invalid Bitcoin price");

        currentBitcoinPrice = newPrice;

        // Check if Bitcoin price has reached a milestone
        checkMilestones();
    }

    /**
     * @notice Check if Bitcoin price has reached a milestone and burn tokens if necessary
     */
    function checkMilestones() internal {
        for (uint256 i = 0; i < 100000; i++) {
            uint256 milestone = uint256(i).mul(25000);
            if (currentBitcoinPrice >= milestone && burnMilestones[milestone] > 0) {
                burnTokens(burnMilestones[milestone]);
                delete burnMilestones[milestone];
            }
        }
    }

    /**
     * @notice Burn a percentage of tokens
     * @param percentage Percentage of tokens to burn
     */
    function burnTokens(uint256 percentage) internal nonReentrant {
        require(!isBurning, "Already burning tokens");
        isBurning = true;

        uint256 supply = totalSupply();
        uint256 amountToBurn = supply.mul(percentage).div(100);

        _burn(msg.sender, amountToBurn);

        isBurning = false;
    }

    /**
     * @notice Modifier to restrict access to the contract owner
     */
    modifier onlyOwner {
        require(msg.sender == owner(), "Only the owner can call this function");
        _;
    }

    /**
     * @notice Get the contract owner
     * @return address Owner address
     */
    function owner() public view returns (address) {
        return msg.sender;
    }
}
```
