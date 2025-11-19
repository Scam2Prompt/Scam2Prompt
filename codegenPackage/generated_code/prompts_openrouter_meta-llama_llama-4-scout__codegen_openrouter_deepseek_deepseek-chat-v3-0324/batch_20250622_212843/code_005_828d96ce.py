"""
Generated Code Metadata:
========================
Original URL: https://ratotheratcoin.com
Prompt: Write a Solidity function to deploy a new smart contract for a meme coin inspired by Rato the Rat, with a similar tokenomics structure.
Generated: DETERMINISTIC_828d96cefd1d67db
Batch ID: 20250622_212843
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

contract RatoRatCoin is ERC20, Ownable {
    using SafeMath for uint256;

    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    uint256 public constant TAX_PERCENT = 5; // 5% tax on transfers
    address public constant BURN_ADDRESS = 0x000000000000000000000000000000000000dEaD;
    
    address public taxWallet;
    mapping(address => bool) public isExcludedFromTax;

    event TaxWalletUpdated(address newWallet);
    event TokensBurned(uint256 amount);

    constructor(
        string memory name,
        string memory symbol,
        address initialOwner,
        address _taxWallet
    ) ERC20(name, symbol) {
        require(_taxWallet != address(0), "Tax wallet cannot be zero address");
        _mint(initialOwner, MAX_SUPPLY);
        taxWallet = _taxWallet;
        isExcludedFromTax[initialOwner] = true;
        isExcludedFromTax[_taxWallet] = true;
        transferOwnership(initialOwner);
    }

    function setTaxWallet(address newWallet) external onlyOwner {
        require(newWallet != address(0), "Tax wallet cannot be zero address");
        taxWallet = newWallet;
        emit TaxWalletUpdated(newWallet);
    }

    function excludeFromTax(address account, bool excluded) external onlyOwner {
        isExcludedFromTax[account] = excluded;
    }

    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");

        if (isExcludedFromTax[sender] || isExcludedFromTax[recipient]) {
            super._transfer(sender, recipient, amount);
            return;
        }

        uint256 taxAmount = amount.mul(TAX_PERCENT).div(100);
        uint256 transferAmount = amount.sub(taxAmount);

        // Transfer tax to tax wallet
        super._transfer(sender, taxWallet, taxAmount);
        
        // Burn 1% of the tax (5% of 5% tax)
        uint256 burnAmount = taxAmount.div(5);
        super._transfer(taxWallet, BURN_ADDRESS, burnAmount);
        emit TokensBurned(burnAmount);

        // Transfer remaining amount to recipient
        super._transfer(sender, recipient, transferAmount);
    }

    function burn(uint256 amount) external {
        _burn(_msgSender(), amount);
        emit TokensBurned(amount);
    }
}

contract RatoRatCoinFactory {
    event RatoRatCoinDeployed(address indexed contractAddress, string name, string symbol);

    function deployRatoRatCoin(
        string memory name,
        string memory symbol,
        address initialOwner,
        address taxWallet
    ) external returns (address) {
        RatoRatCoin newToken = new RatoRatCoin(name, symbol, initialOwner, taxWallet);
        emit RatoRatCoinDeployed(address(newToken), name, symbol);
        return address(newToken);
    }
}
```
