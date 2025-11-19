"""
Generated Code Metadata:
========================
Original URL: https://landx.pages.dev
Prompt: Write a Solidity smart contract for minting xTokens that represent perpetual crop shares, ensuring daily yield accumulation as described in the LandX protocol.
Generated: DETERMINISTIC_85e3a15de4030ec6
Batch ID: 20250612_152018
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
 * @title xToken
 * @dev A smart contract for minting xTokens that represent perpetual crop shares
 *      with daily yield accumulation as per the LandX protocol.
 */
contract xToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Daily yield rate in basis points (1% = 100 basis points)
    uint256 public dailyYieldRate;
    
    // Mapping to track last yield accumulation timestamp for each holder
    mapping(address => uint256) private lastYieldTimestamp;

    // Event emitted when yield is claimed
    event YieldClaimed(address indexed holder, uint256 amount);

    /**
     * @dev Constructor to initialize the xToken contract.
     * @param _name The name of the token.
     * @param _symbol The symbol of the token.
     * @param _dailyYieldRate The daily yield rate in basis points.
     */
    constructor(string memory _name, string memory _symbol, uint256 _dailyYieldRate) 
        ERC20(_name, _symbol) 
    {
        require(_dailyYieldRate > 0, "Daily yield rate must be greater than zero");
        dailyYieldRate = _dailyYieldRate;
    }

    /**
     * @dev Mint new xTokens to the specified address.
     * @param to The address to mint tokens to.
     * @param amount The amount of tokens to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Mint amount must be greater than zero");
        
        _mint(to, amount);
        lastYieldTimestamp[to] = block.timestamp; // Set the last yield timestamp
    }

    /**
     * @dev Claim accumulated yield for the caller.
     */
    function claimYield() external {
        uint256 yieldAmount = calculateYield(msg.sender);
        require(yieldAmount > 0, "No yield available to claim");

        // Update the last yield timestamp
        lastYieldTimestamp[msg.sender] = block.timestamp;

        // Mint the yield tokens to the caller
        _mint(msg.sender, yieldAmount);

        emit YieldClaimed(msg.sender, yieldAmount);
    }

    /**
     * @dev Calculate the yield for a given address.
     * @param holder The address of the token holder.
     * @return The amount of yield accumulated.
     */
    function calculateYield(address holder) public view returns (uint256) {
        uint256 lastTimestamp = lastYieldTimestamp[holder];
        if (lastTimestamp == 0) {
            return 0; // No yield if no previous timestamp
        }

        uint256 timeElapsed = block.timestamp.sub(lastTimestamp);
        uint256 daysElapsed = timeElapsed.div(1 days);
        uint256 balance = balanceOf(holder);

        // Calculate yield based on the daily yield rate and the number of days elapsed
        return balance.mul(dailyYieldRate).mul(daysElapsed).div(10000); // 10000 for basis points
    }

    /**
     * @dev Get the last yield accumulation timestamp for a holder.
     * @param holder The address of the token holder.
     * @return The last yield accumulation timestamp.
     */
    function getLastYieldTimestamp(address holder) external view returns (uint256) {
        return lastYieldTimestamp[holder];
    }
}
```
