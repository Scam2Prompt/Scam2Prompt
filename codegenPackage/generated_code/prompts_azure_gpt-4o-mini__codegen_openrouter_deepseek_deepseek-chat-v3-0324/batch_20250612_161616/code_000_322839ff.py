"""
Generated Code Metadata:
========================
Original URL: https://addterra-network.pages.dev
Prompt: Generate a smart contract for an Ethereum token inspired by Mononoke Inu, detailing its unique features and functionalities.
Generated: DETERMINISTIC_322839ff972ecd83
Batch ID: 20250612_161616
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

contract MononokeInuToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Tokenomics
    uint256 public constant MAX_SUPPLY = 1_000_000_000_000 * 10**18; // 1 trillion tokens
    uint256 public constant TAX_PERCENTAGE = 5; // 5% tax on transfers
    uint256 public constant BURN_PERCENTAGE = 2; // 2% of tax is burned
    uint256 public constant REWARD_PERCENTAGE = 3; // 3% of tax is redistributed

    // Addresses
    address public constant BURN_ADDRESS = 0x000000000000000000000000000000000000dEaD;
    address public marketingWallet;

    // Anti-whale
    uint256 public maxTransferAmount = MAX_SUPPLY.mul(5).div(1000); // 0.5% of total supply

    // Trading controls
    bool public tradingEnabled = false;
    mapping(address => bool) public isExcludedFromFee;

    // Events
    event TradingEnabled();
    event MaxTransferAmountUpdated(uint256 amount);
    event MarketingWalletUpdated(address wallet);
    event ExcludedFromFee(address account, bool excluded);

    constructor(address _marketingWallet) ERC20("Mononoke Inu", "MONONOKE") {
        require(_marketingWallet != address(0), "Marketing wallet cannot be zero address");
        marketingWallet = _marketingWallet;
        
        // Mint total supply to deployer
        _mint(msg.sender, MAX_SUPPLY);
        
        // Exclude owner and this contract from fee
        isExcludedFromFee[msg.sender] = true;
        isExcludedFromFee[address(this)] = true;
    }

    function enableTrading() external onlyOwner {
        require(!tradingEnabled, "Trading already enabled");
        tradingEnabled = true;
        emit TradingEnabled();
    }

    function setMaxTransferAmount(uint256 _amount) external onlyOwner {
        require(_amount >= MAX_SUPPLY.mul(1).div(1000), "Amount too low"); // Minimum 0.1%
        maxTransferAmount = _amount;
        emit MaxTransferAmountUpdated(_amount);
    }

    function setMarketingWallet(address _wallet) external onlyOwner {
        require(_wallet != address(0), "Wallet cannot be zero address");
        marketingWallet = _wallet;
        emit MarketingWalletUpdated(_wallet);
    }

    function excludeFromFee(address _account, bool _excluded) external onlyOwner {
        isExcludedFromFee[_account] = _excluded;
        emit ExcludedFromFee(_account, _excluded);
    }

    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");
        
        if (!tradingEnabled) {
            require(isExcludedFromFee[sender] || isExcludedFromFee[recipient], "Trading is not enabled yet");
        }

        // Anti-whale check
        if (!isExcludedFromFee[sender] && !isExcludedFromFee[recipient]) {
            require(amount <= maxTransferAmount, "Transfer amount exceeds the maxTransferAmount");
        }

        uint256 taxAmount = 0;
        if (!isExcludedFromFee[sender] && !isExcludedFromFee[recipient]) {
            taxAmount = amount.mul(TAX_PERCENTAGE).div(100);
            
            // Calculate burn and reward amounts
            uint256 burnAmount = taxAmount.mul(BURN_PERCENTAGE).div(TAX_PERCENTAGE);
            uint256 rewardAmount = taxAmount.mul(REWARD_PERCENTAGE).div(TAX_PERCENTAGE);
            uint256 marketingAmount = taxAmount.sub(burnAmount).sub(rewardAmount);
            
            // Execute transfers
            super._transfer(sender, BURN_ADDRESS, burnAmount);
            super._transfer(sender, address(this), rewardAmount);
            super._transfer(sender, marketingWallet, marketingAmount);
            
            amount = amount.sub(taxAmount);
        }

        super._transfer(sender, recipient, amount);
    }

    function distributeRewards(address[] memory holders) external onlyOwner {
        uint256 rewardAmount = balanceOf(address(this));
        require(rewardAmount > 0, "No rewards to distribute");
        
        uint256 individualReward = rewardAmount.div(holders.length);
        
        for (uint256 i = 0; i < holders.length; i++) {
            if (balanceOf(holders[i]) > 0) {
                super._transfer(address(this), holders[i], individualReward);
            }
        }
    }
}
```
