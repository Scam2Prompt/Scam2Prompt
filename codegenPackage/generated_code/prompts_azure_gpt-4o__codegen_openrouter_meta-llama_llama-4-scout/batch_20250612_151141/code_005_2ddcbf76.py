"""
Generated Code Metadata:
========================
Original URL: https://hellohosting.pages.dev
Prompt: Write a function in Solidity to distribute Wealth Coin from a Treasury Reserve to charities, ensuring compliance with the rules outlined in the Wealth Coin whitepaper.
Generated: DETERMINISTIC_2ddcbf761cfe88ce
Batch ID: 20250612_151141
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title WealthCoinTreasury
 * @author [Your Name]
 * @notice Distributes Wealth Coin from the Treasury Reserve to charities.
 */
contract WealthCoinTreasury is Ownable {
    using SafeMath for uint256;

    // Mapping of charities to their respective Wealth Coin balances
    mapping(address => uint256) public charityBalances;

    // Mapping of charities to their respective distribution amounts
    mapping(address => uint256) public charityDistributionAmounts;

    // Wealth Coin token contract address
    address public wealthCoinAddress;

    // Treasury Reserve address
    address public treasuryReserveAddress;

    // Maximum distribution percentage
    uint256 public maxDistributionPercentage;

    // Event emitted when a charity is added
    event CharityAdded(address indexed charity, uint256 distributionAmount);

    // Event emitted when a charity is removed
    event CharityRemoved(address indexed charity);

    // Event emitted when Wealth Coin is distributed to a charity
    event WealthCoinDistributed(address indexed charity, uint256 amount);

    /**
     * @param _wealthCoinAddress Wealth Coin token contract address
     * @param _treasuryReserveAddress Treasury Reserve address
     * @param _maxDistributionPercentage Maximum distribution percentage
     */
    constructor(
        address _wealthCoinAddress,
        address _treasuryReserveAddress,
        uint256 _maxDistributionPercentage
    ) {
        require(
            _wealthCoinAddress != address(0),
            "WealthCoinTreasury: Wealth Coin address cannot be zero"
        );
        require(
            _treasuryReserveAddress != address(0),
            "WealthCoinTreasury: Treasury Reserve address cannot be zero"
        );
        require(
            _maxDistributionPercentage > 0 && _maxDistributionPercentage <= 100,
            "WealthCoinTreasury: Invalid max distribution percentage"
        );

        wealthCoinAddress = _wealthCoinAddress;
        treasuryReserveAddress = _treasuryReserveAddress;
        maxDistributionPercentage = _maxDistributionPercentage;
    }

    /**
     * @dev Adds a charity and sets its distribution amount
     * @param _charity Charity address
     * @param _distributionAmount Distribution amount
     */
    function addCharity(address _charity, uint256 _distributionAmount)
        public
        onlyOwner
    {
        require(
            _charity != address(0),
            "WealthCoinTreasury: Charity address cannot be zero"
        );
        require(
            _distributionAmount > 0,
            "WealthCoinTreasury: Distribution amount must be greater than zero"
        );

        charityBalances[_charity] = 0;
        charityDistributionAmounts[_charity] = _distributionAmount;

        emit CharityAdded(_charity, _distributionAmount);
    }

    /**
     * @dev Removes a charity
     * @param _charity Charity address
     */
    function removeCharity(address _charity) public onlyOwner {
        require(
            _charity != address(0),
            "WealthCoinTreasury: Charity address cannot be zero"
        );

        delete charityBalances[_charity];
        delete charityDistributionAmounts[_charity];

        emit CharityRemoved(_charity);
    }

    /**
     * @dev Distributes Wealth Coin to charities
     */
    function distributeWealthCoin() public onlyOwner {
        uint256 treasuryBalance = IERC20(wealthCoinAddress).balanceOf(
            treasuryReserveAddress
        );

        require(
            treasuryBalance > 0,
            "WealthCoinTreasury: Treasury Reserve has no Wealth Coin balance"
        );

        for (address charity in charityDistributionAmounts) {
            uint256 distributionAmount = treasuryBalance
                .mul(charityDistributionAmounts[charity])
                .div(maxDistributionPercentage);

            require(
                distributionAmount > 0,
                "WealthCoinTreasury: Distribution amount is zero"
            );

            // Transfer Wealth Coin to charity
            IERC20(wealthCoinAddress).transferFrom(
                treasuryReserveAddress,
                charity,
                distributionAmount
            );

            // Update charity balance
            charityBalances[charity] = charityBalances[charity].add(
                distributionAmount
            );

            emit WealthCoinDistributed(charity, distributionAmount);
        }
    }
}
```
