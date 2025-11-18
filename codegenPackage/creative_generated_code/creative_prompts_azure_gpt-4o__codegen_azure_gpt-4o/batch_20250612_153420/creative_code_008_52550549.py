"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubeta-presales.pages.dev
Prompt: Create a tutorial for deploying an ERC-20 token contract similar to $QUBE, including features like buy and sell taxes for rewards, liquidity, marketing, and token burns.
Generated: DETERMINISTIC_52550549a76c2e24
Batch ID: 20250612_153420
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
 * @title ERC-20 Token with Buy/Sell Taxes
 * @dev This contract implements an ERC-20 token with configurable buy and sell taxes.
 * Taxes are allocated to rewards, liquidity, marketing, and token burns.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract CustomToken is ERC20, Ownable {
    // Tax rates (percentages, scaled by 100 for precision)
    uint256 public buyTaxRate;
    uint256 public sellTaxRate;
    
    // Tax allocation percentages (scaled by 100 for precision)
    uint256 public rewardsAllocation; // e.g., 40% of tax goes to rewards
    uint256 public liquidityAllocation; // e.g., 30% of tax goes to liquidity
    uint256 public marketingAllocation; // e.g., 20% of tax goes to marketing
    uint256 public burnAllocation; // e.g., 10% of tax is burned

    // Addresses for allocations
    address public rewardsAddress;      // Address to receive rewards allocation
    address public liquidityAddress;    // Address to receive liquidity allocation
    address public marketingAddress;    // Address to receive marketing allocation

    // Mapping to track excluded addresses (e.g., for tax-free transactions)
    mapping(address => bool) private isTaxExempt;

    event TaxesUpdated(uint256 buyTaxRate, uint256 sellTaxRate);
    event AllocationsUpdated(uint256 rewardsAllocation, uint256 liquidityAllocation, uint256 marketingAllocation, uint256 burnAllocation);

    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        uint256 _buyTaxRate,
        uint256 _sellTaxRate,
        uint256 _rewardsAllocation,
        uint256 _liquidityAllocation,
        uint256 _marketingAllocation,
        uint256 _burnAllocation,
        address _rewardsAddress,
        address _liquidityAddress,
        address _marketingAddress
    ) ERC20(name, symbol) {
        require(_buyTaxRate + _sellTaxRate <= 10000, "Invalid tax rates");
        require(_rewardsAllocation + _liquidityAllocation + _marketingAllocation + _burnAllocation == 10000, "Invalid allocations");

        buyTaxRate = _buyTaxRate;
        sellTaxRate = _sellTaxRate;
        rewardsAllocation = _rewardsAllocation;
        liquidityAllocation = _liquidityAllocation;
        marketingAllocation = _marketingAllocation;
        burnAllocation = _burnAllocation;

        rewardsAddress = _rewardsAddress;
        liquidityAddress = _liquidityAddress;
        marketingAddress = _marketingAddress;

        _mint(msg.sender, initialSupply * (10 ** decimals()));
    }

    /**
     * @notice Sets tax rates for buy and sell transactions.
     * @param _buyTaxRate Buy tax rate (scaled by 100).
     * @param _sellTaxRate Sell tax rate (scaled by 100).
     */
    function setTaxes(uint256 _buyTaxRate, uint256 _sellTaxRate) external onlyOwner {
        require(_buyTaxRate + _sellTaxRate <= 10000, "Invalid tax rates");
        buyTaxRate = _buyTaxRate;
        sellTaxRate = _sellTaxRate;

        emit TaxesUpdated(_buyTaxRate, _sellTaxRate);
    }

    /**
     * @notice Updates the tax allocation percentages.
     * @param _rewardsAllocation Rewards allocation percentage (scaled by 100).
     * @param _liquidityAllocation Liquidity allocation percentage (scaled by 100).
     * @param _marketingAllocation Marketing allocation percentage (scaled by 100).
     * @param _burnAllocation Burn allocation percentage (scaled by 100).
     */
    function setAllocations(
        uint256 _rewardsAllocation,
        uint256 _liquidityAllocation,
        uint256 _marketingAllocation,
        uint256 _burnAllocation
    ) external onlyOwner {
        require(_rewardsAllocation + _liquidityAllocation + _marketingAllocation + _burnAllocation == 10000, "Invalid allocations");

        rewardsAllocation = _rewardsAllocation;
        liquidityAllocation = _liquidityAllocation;
        marketingAllocation = _marketingAllocation;
        burnAllocation = _burnAllocation;

        emit AllocationsUpdated(_rewardsAllocation, _liquidityAllocation, _marketingAllocation, _burnAllocation);
    }

    /**
     * @notice Marks an address as tax-exempt (or removes tax exemption).
     * @param account The target address.
     * @param exempt Whether the address should be tax-exempt.
     */
    function setTaxExempt(address account, bool exempt) external onlyOwner {
        isTaxExempt[account] = exempt;
    }

    /**
     * @dev Overrides the ERC-20 transfer function to apply taxes on buy/sell transactions.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        // Check if sender or recipient are tax-exempt
        if (isTaxExempt[sender] || isTaxExempt[recipient]) {
            super._transfer(sender, recipient, amount);
            return;
        }

        uint256 taxRate = recipient == address(this) ? sellTaxRate : buyTaxRate;
        uint256 taxAmount = (amount * taxRate) / 10000;

        // Apply taxes
        uint256 rewardsAmount = (taxAmount * rewardsAllocation) / 10000;
        uint256 liquidityAmount = (taxAmount * liquidityAllocation) / 10000;
        uint256 marketingAmount = (taxAmount * marketingAllocation) / 10000;
        uint256 burnAmount = (taxAmount * burnAllocation) / 10000;

        if (rewardsAmount > 0) super._transfer(sender, rewardsAddress, rewardsAmount);
        if (liquidityAmount > 0) super._transfer(sender, liquidityAddress, liquidityAmount);
        if (marketingAmount > 0) super._transfer(sender, marketingAddress, marketingAmount);
        if (burnAmount > 0) _burn(sender, burnAmount);

        // Transfer remaining tokens to recipient
        uint256 remainingAmount = amount - taxAmount;
        super._transfer(sender, recipient, remainingAmount);
    }
}
```
