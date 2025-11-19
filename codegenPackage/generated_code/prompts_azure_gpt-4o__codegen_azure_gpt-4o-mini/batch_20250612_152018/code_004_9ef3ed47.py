"""
Generated Code Metadata:
========================
Original URL: https://asx-capital.pages.dev
Prompt: Write a Solidity function that calculates and distributes yield from DeFi investments to $ASX token holders, ensuring safety mechanisms for risk mitigation as outlined on the ASX Capital site.
Generated: DETERMINISTIC_9ef3ed47bf190f71
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ASXYieldDistributor
 * @dev This contract calculates and distributes yield from DeFi investments to $ASX token holders.
 */
contract ASXYieldDistributor is Ownable {
    IERC20 public asxToken; // The $ASX token contract
    uint256 public totalYield; // Total yield accumulated for distribution
    mapping(address => uint256) public lastClaimed; // Last claimed yield timestamp for each holder

    event YieldDistributed(address indexed holder, uint256 amount);
    event YieldAccrued(uint256 amount);

    /**
     * @dev Constructor to set the $ASX token address.
     * @param _asxToken Address of the $ASX token contract.
     */
    constructor(address _asxToken) {
        require(_asxToken != address(0), "Invalid token address");
        asxToken = IERC20(_asxToken);
    }

    /**
     * @dev Accrues yield from DeFi investments.
     * @param amount The amount of yield to accrue.
     */
    function accrueYield(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        totalYield += amount;
        emit YieldAccrued(amount);
    }

    /**
     * @dev Distributes yield to $ASX token holders.
     */
    function distributeYield() external {
        uint256 holderCount = asxToken.totalSupply();
        require(holderCount > 0, "No holders to distribute yield to");

        uint256 yieldPerToken = totalYield / holderCount;

        for (uint256 i = 0; i < holderCount; i++) {
            address holder = asxToken.holderAt(i); // Assuming a function to get holder address
            uint256 lastClaim = lastClaimed[holder];
            if (lastClaim < block.timestamp) {
                uint256 yieldAmount = yieldPerToken * asxToken.balanceOf(holder);
                if (yieldAmount > 0) {
                    require(asxToken.transfer(holder, yieldAmount), "Transfer failed");
                    lastClaimed[holder] = block.timestamp;
                    emit YieldDistributed(holder, yieldAmount);
                }
            }
        }

        // Reset total yield after distribution
        totalYield = 0;
    }

    /**
     * @dev Allows the owner to withdraw any tokens accidentally sent to the contract.
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(asxToken), "Cannot withdraw $ASX tokens");
        IERC20(token).transfer(owner(), amount);
    }
}
```
