"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://internetmoney-4rq.pages.dev
Prompt: Write a smart contract function in Solidity that integrates with the Internet Money (IM) token to calculate and display the total burned supply percentage, similar to the "Total Burned (0.225% OF TOTAL SUPPLY)" feature described on the website.
Generated: DETERMINISTIC_8f4c0fb118b4067d
Batch ID: 20250612_153700
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
 * @title InternetMoneyBurnedPercentage
 * @dev This contract interacts with the Internet Money (IM) token and calculates the percentage of burned tokens
 * relative to the total supply. It is designed to be simple, efficient, and adheres to Solidity best practices.
 */
interface IInternetMoneyToken {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
}

contract BurnedPercentageCalculator {
    // Address of the Internet Money (IM) token contract
    address public immutable IMTokenAddress;

    // Burn address typically used by the IM token (e.g., 0x000000000000000000000000000000000000dEaD)
    address public immutable burnAddress;

    /**
     * @dev Constructor initializes the IM token address and burn address.
     * @param _IMTokenAddress The deployed address of the IM token contract.
     * @param _burnAddress The address where burned tokens are sent (e.g., dead address).
     */
    constructor(address _IMTokenAddress, address _burnAddress) {
        require(_IMTokenAddress != address(0), "IMTokenAddress cannot be zero address");
        require(_burnAddress != address(0), "Burn address cannot be zero address");

        IMTokenAddress = _IMTokenAddress;
        burnAddress = _burnAddress;
    }

    /**
     * @dev Calculates the percentage of burned tokens relative to the total supply.
     * @return burnedPercentage The burned token percentage scaled by 10^18 for precision.
     *         (e.g., 225000000000000000 represents 0.225%).
     */
    function getBurnedPercentage() external view returns (uint256 burnedPercentage) {
        IInternetMoneyToken IMToken = IInternetMoneyToken(IMTokenAddress);

        // Retrieve the total supply of the IM token
        uint256 totalSupply = IMToken.totalSupply();
        require(totalSupply > 0, "Total supply must be greater than zero");

        // Retrieve the balance of the burn address
        uint256 burnedSupply = IMToken.balanceOf(burnAddress);

        // Calculate the burned token percentage: (burnedSupply / totalSupply) * 100
        // We scale the result by 10^18 to allow for precision in percentages
        burnedPercentage = (burnedSupply * 1e18) / totalSupply;
    }
}
```
