"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-alainetwork.pages.dev
Prompt: Write a Solidity smart contract to distribute monthly USDT dividends to $ALAI token holders based on their holdings, ensuring transparency and security.
Generated: DETERMINISTIC_fc275b1c0a1dc65b
Batch ID: 20250612_154057
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

interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

/**
 * @title DividendDistributor
 * @dev A contract to distribute USDT dividends to $ALAI token holders based on their holdings
 */
contract DividendDistributor {
    // Address of the USDT token contract
    IERC20 public usdtToken;
    // Address of the $ALAI token contract
    IERC20 public alaiToken;

    // Total USDT amount available for distribution
    uint256 public totalDividends;
    // Mapping to track dividends owed to each holder
    mapping(address => uint256) public dividendsOwed;

    // Event emitted when dividends are distributed
    event DividendsDistributed(uint256 amount);

    // Event emitted when a holder claims their dividends
    event DividendsClaimed(address indexed holder, uint256 amount);

    /**
     * @dev Constructor to set the USDT and $ALAI token addresses
     * @param _usdtToken Address of the USDT token contract
     * @param _alaiToken Address of the $ALAI token contract
     */
    constructor(address _usdtToken, address _alaiToken) {
        usdtToken = IERC20(_usdtToken);
        alaiToken = IERC20(_alaiToken);
    }

    /**
     * @dev Function to distribute dividends based on the $ALAI token holdings
     * @param amount Amount of USDT to distribute
     */
    function distributeDividends(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(usdtToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        totalDividends += amount;
        emit DividendsDistributed(amount);
    }

    /**
     * @dev Function to claim dividends for the caller
     */
    function claimDividends() external {
        uint256 holderBalance = alaiToken.balanceOf(msg.sender);
        require(holderBalance > 0, "No $ALAI tokens held");

        // Calculate dividends owed to this holder based on their proportion of $ALAI tokens
        uint256 dividends = (holderBalance * totalDividends) / alaiToken.totalSupply();
        require(dividends > 0, "No dividends owed");

        // Transfer USDT dividends to the holder
        dividendsOwed[msg.sender] += dividends;
        totalDividends -= dividends;

        require(usdtToken.transfer(msg.sender, dividends), "Transfer failed");
        emit DividendsClaimed(msg.sender, dividends);
    }

    /**
     * @dev Function to view the dividends owed to a specific holder
     * @param holder Address of the holder
     * @return Amount of dividends owed to the holder
     */
    function viewDividendsOwed(address holder) external view returns (uint256) {
        return dividendsOwed[holder];
    }
}
```
