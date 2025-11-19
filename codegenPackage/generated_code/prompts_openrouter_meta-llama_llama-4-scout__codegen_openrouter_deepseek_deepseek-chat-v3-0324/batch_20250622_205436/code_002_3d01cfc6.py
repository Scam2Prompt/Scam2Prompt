"""
Generated Code Metadata:
========================
Original URL: https://app-memecoin.online
Prompt: Generate a Solidity smart contract code for creating a new memecoin token with a similar functionality to the one on app-memecoin.online.
Generated: DETERMINISTIC_3d01cfc63a493922
Batch ID: 20250622_205436
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

contract MemeCoin is ERC20, Ownable {
    using SafeMath for uint256;

    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    uint256 public constant INITIAL_SUPPLY = 500_000_000 * 10**18; // 500 million tokens
    uint256 public constant TAX_PERCENT = 5; // 5% tax
    address public constant BURN_ADDRESS = 0x000000000000000000000000000000000000dEaD;

    address public marketingWallet;
    address public liquidityWallet;
    bool public tradingEnabled = false;

    mapping(address => bool) private _isExcludedFromFee;

    event TradingEnabled();
    event MarketingWalletUpdated(address indexed newWallet);
    event LiquidityWalletUpdated(address indexed newWallet);

    constructor(
        address _marketingWallet,
        address _liquidityWallet
    ) ERC20("MemeCoin", "MEME") {
        require(_marketingWallet != address(0), "Marketing wallet cannot be zero address");
        require(_liquidityWallet != address(0), "Liquidity wallet cannot be zero address");

        marketingWallet = _marketingWallet;
        liquidityWallet = _liquidityWallet;

        _mint(msg.sender, INITIAL_SUPPLY);
        _isExcludedFromFee[msg.sender] = true;
        _isExcludedFromFee[_marketingWallet] = true;
        _isExcludedFromFee[_liquidityWallet] = true;
        _isExcludedFromFee[BURN_ADDRESS] = true;
    }

    function enableTrading() external onlyOwner {
        require(!tradingEnabled, "Trading is already enabled");
        tradingEnabled = true;
        emit TradingEnabled();
    }

    function setMarketingWallet(address _marketingWallet) external onlyOwner {
        require(_marketingWallet != address(0), "Marketing wallet cannot be zero address");
        marketingWallet = _marketingWallet;
        emit MarketingWalletUpdated(_marketingWallet);
    }

    function setLiquidityWallet(address _liquidityWallet) external onlyOwner {
        require(_liquidityWallet != address(0), "Liquidity wallet cannot be zero address");
        liquidityWallet = _liquidityWallet;
        emit LiquidityWalletUpdated(_liquidityWallet);
    }

    function excludeFromFee(address account) external onlyOwner {
        _isExcludedFromFee[account] = true;
    }

    function includeInFee(address account) external onlyOwner {
        _isExcludedFromFee[account] = false;
    }

    function isExcludedFromFee(address account) public view returns (bool) {
        return _isExcludedFromFee[account];
    }

    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal virtual override {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");

        if (!tradingEnabled) {
            require(
                _isExcludedFromFee[sender] || _isExcludedFromFee[recipient],
                "Trading is not enabled yet"
            );
        }

        if (_isExcludedFromFee[sender] || _isExcludedFromFee[recipient]) {
            super._transfer(sender, recipient, amount);
        } else {
            uint256 taxAmount = amount.mul(TAX_PERCENT).div(100);
            uint256 sendAmount = amount.sub(taxAmount);
            
            // Split tax 50/50 between marketing and liquidity wallets
            uint256 marketingTax = taxAmount.div(2);
            uint256 liquidityTax = taxAmount.sub(marketingTax);

            super._transfer(sender, marketingWallet, marketingTax);
            super._transfer(sender, liquidityWallet, liquidityTax);
            super._transfer(sender, recipient, sendAmount);
        }
    }

    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
    }

    function mint(address to, uint256 amount) public onlyOwner {
        require(totalSupply().add(amount) <= MAX_SUPPLY, "Exceeds max supply");
        _mint(to, amount);
    }
}
```
