"""
Generated Code Metadata:
========================
Original URL: https://airdrop-inqubeta.pages.dev
Prompt: Generate Solidity code for a smart contract that implements the QUBE tokenomics, including buy and sell taxes, rewards pool allocation, and token burning mechanisms as described on the InQubeta platform.
Generated: DETERMINISTIC_dd7955f61ddc3f6e
Batch ID: 20250612_153420
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

contract QUBEToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Tax rates (in basis points, where 100 = 1%)
    uint256 public constant BUY_TAX = 500; // 5%
    uint256 public constant SELL_TAX = 1000; // 10%
    
    // Tax distribution (in basis points, where 100 = 1%)
    uint256 public constant REWARDS_POOL = 6000; // 60% of taxes
    uint256 public constant BURN_POOL = 2000;    // 20% of taxes
    uint256 public constant TREASURY_POOL = 2000; // 20% of taxes

    // Addresses
    address public rewardsPool;
    address public treasury;
    address public immutable deadAddress = 0x000000000000000000000000000000000000dEaD;

    // Exclusions
    mapping(address => bool) private _isExcludedFromFees;
    mapping(address => bool) private _isExcludedFromRewards;

    // Events
    event TaxesDistributed(uint256 rewardsAmount, uint256 burnAmount, uint256 treasuryAmount);
    event ExcludedFromFees(address indexed account, bool isExcluded);
    event ExcludedFromRewards(address indexed account, bool isExcluded);
    event RewardsPoolUpdated(address indexed newRewardsPool);
    event TreasuryUpdated(address indexed newTreasury);

    constructor(
        uint256 initialSupply,
        address _rewardsPool,
        address _treasury
    ) ERC20("InQubeta QUBE Token", "QUBE") {
        require(_rewardsPool != address(0), "Rewards pool cannot be zero address");
        require(_treasury != address(0), "Treasury cannot be zero address");

        rewardsPool = _rewardsPool;
        treasury = _treasury;

        // Exclude owner and contract from fees
        _isExcludedFromFees[owner()] = true;
        _isExcludedFromFees[address(this)] = true;

        // Mint initial supply to owner
        _mint(owner(), initialSupply);
    }

    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");

        bool takeFee = true;

        // Check if sender or recipient is excluded from fees
        if (_isExcludedFromFees[sender] || _isExcludedFromFees[recipient]) {
            takeFee = false;
        }

        uint256 fees = 0;
        if (takeFee) {
            // Buy tax
            if (recipient != address(this) && sender != address(this)) {
                fees = amount.mul(BUY_TAX).div(10000);
            }
            // Sell tax
            else if (sender != address(this) && recipient == address(this)) {
                fees = amount.mul(SELL_TAX).div(10000);
            }

            if (fees > 0) {
                super._transfer(sender, address(this), fees);
                _distributeTaxes(fees);
                amount = amount.sub(fees);
            }
        }

        super._transfer(sender, recipient, amount);
    }

    function _distributeTaxes(uint256 taxAmount) private {
        uint256 rewardsAmount = taxAmount.mul(REWARDS_POOL).div(10000);
        uint256 burnAmount = taxAmount.mul(BURN_POOL).div(10000);
        uint256 treasuryAmount = taxAmount.sub(rewardsAmount).sub(burnAmount);

        if (rewardsAmount > 0) {
            super._transfer(address(this), rewardsPool, rewardsAmount);
        }
        if (burnAmount > 0) {
            _burn(address(this), burnAmount);
        }
        if (treasuryAmount > 0) {
            super._transfer(address(this), treasury, treasuryAmount);
        }

        emit TaxesDistributed(rewardsAmount, burnAmount, treasuryAmount);
    }

    // Admin functions
    function excludeFromFees(address account, bool excluded) external onlyOwner {
        require(_isExcludedFromFees[account] != excluded, "Account is already set to that state");
        _isExcludedFromFees[account] = excluded;
        emit ExcludedFromFees(account, excluded);
    }

    function excludeFromRewards(address account, bool excluded) external onlyOwner {
        require(_isExcludedFromRewards[account] != excluded, "Account is already set to that state");
        _isExcludedFromRewards[account] = excluded;
        emit ExcludedFromRewards(account, excluded);
    }

    function setRewardsPool(address _rewardsPool) external onlyOwner {
        require(_rewardsPool != address(0), "Rewards pool cannot be zero address");
        rewardsPool = _rewardsPool;
        emit RewardsPoolUpdated(_rewardsPool);
    }

    function setTreasury(address _treasury) external onlyOwner {
        require(_treasury != address(0), "Treasury cannot be zero address");
        treasury = _treasury;
        emit TreasuryUpdated(_treasury);
    }

    // View functions
    function isExcludedFromFees(address account) public view returns (bool) {
        return _isExcludedFromFees[account];
    }

    function isExcludedFromRewards(address account) public view returns (bool) {
        return _isExcludedFromRewards[account];
    }
}
```
