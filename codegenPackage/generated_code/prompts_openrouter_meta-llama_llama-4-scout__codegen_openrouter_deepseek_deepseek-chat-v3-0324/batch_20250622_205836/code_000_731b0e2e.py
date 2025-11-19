"""
Generated Code Metadata:
========================
Original URL: https://pawthereum.pages.dev
Prompt: Write a smart contract in Solidity for a token distribution system similar to Pawthereum's $PAWTH on the BASE network.
Generated: DETERMINISTIC_731b0e2e183129a4
Batch ID: 20250622_205836
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Snapshot.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/draft-ERC20Permit.sol";

contract Pawthereum is ERC20, ERC20Burnable, ERC20Snapshot, Ownable, Pausable, ERC20Permit {
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens with 18 decimals
    uint256 public constant INITIAL_SUPPLY = 500_000_000 * 10**18; // 500 million initial supply

    // Addresses for special distributions
    address public charityWallet;
    address public teamWallet;
    address public marketingWallet;

    // Tax rates (in basis points, where 100 = 1%)
    uint256 public charityTaxRate = 200; // 2%
    uint256 public teamTaxRate = 100;   // 1%
    uint256 public marketingTaxRate = 100; // 1%

    // Mapping to exclude addresses from taxes
    mapping(address => bool) private _isExcludedFromTax;

    event CharityWalletUpdated(address indexed newWallet);
    event TeamWalletUpdated(address indexed newWallet);
    event MarketingWalletUpdated(address indexed newWallet);
    event TaxRatesUpdated(uint256 charityRate, uint256 teamRate, uint256 marketingRate);
    event TokensDistributed(address indexed to, uint256 amount);

    constructor(
        address _charityWallet,
        address _teamWallet,
        address _marketingWallet
    ) ERC20("Pawthereum", "PAWTH") ERC20Permit("Pawthereum") {
        require(_charityWallet != address(0), "Charity wallet cannot be zero address");
        require(_teamWallet != address(0), "Team wallet cannot be zero address");
        require(_marketingWallet != address(0), "Marketing wallet cannot be zero address");

        charityWallet = _charityWallet;
        teamWallet = _teamWallet;
        marketingWallet = _marketingWallet;

        // Exclude special wallets from taxes
        _isExcludedFromTax[_charityWallet] = true;
        _isExcludedFromTax[_teamWallet] = true;
        _isExcludedFromTax[_marketingWallet] = true;
        _isExcludedFromTax[address(this)] = true;

        // Mint initial supply to contract deployer
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    function snapshot() public onlyOwner {
        _snapshot();
    }

    function pause() public onlyOwner {
        _pause();
    }

    function unpause() public onlyOwner {
        _unpause();
    }

    function mint(address to, uint256 amount) public onlyOwner {
        require(totalSupply() + amount <= MAX_SUPPLY, "Exceeds max supply");
        _mint(to, amount);
        emit TokensDistributed(to, amount);
    }

    function burn(uint256 amount) public override {
        require(amount > 0, "Amount must be greater than 0");
        super.burn(amount);
    }

    function setCharityWallet(address _charityWallet) external onlyOwner {
        require(_charityWallet != address(0), "Charity wallet cannot be zero address");
        charityWallet = _charityWallet;
        emit CharityWalletUpdated(_charityWallet);
    }

    function setTeamWallet(address _teamWallet) external onlyOwner {
        require(_teamWallet != address(0), "Team wallet cannot be zero address");
        teamWallet = _teamWallet;
        emit TeamWalletUpdated(_teamWallet);
    }

    function setMarketingWallet(address _marketingWallet) external onlyOwner {
        require(_marketingWallet != address(0), "Marketing wallet cannot be zero address");
        marketingWallet = _marketingWallet;
        emit MarketingWalletUpdated(_marketingWallet);
    }

    function setTaxRates(
        uint256 _charityRate,
        uint256 _teamRate,
        uint256 _marketingRate
    ) external onlyOwner {
        require(_charityRate + _teamRate + _marketingRate <= 1000, "Total tax cannot exceed 10%");
        charityTaxRate = _charityRate;
        teamTaxRate = _teamRate;
        marketingTaxRate = _marketingRate;
        emit TaxRatesUpdated(_charityRate, _teamRate, _marketingRate);
    }

    function excludeFromTax(address account, bool excluded) external onlyOwner {
        _isExcludedFromTax[account] = excluded;
    }

    function isExcludedFromTax(address account) public view returns (bool) {
        return _isExcludedFromTax[account];
    }

    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override(ERC20, ERC20Snapshot) whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
    }

    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override {
        if (_isExcludedFromTax[sender] || _isExcludedFromTax[recipient]) {
            super._transfer(sender, recipient, amount);
            return;
        }

        uint256 charityAmount = (amount * charityTaxRate) / 10000;
        uint256 teamAmount = (amount * teamTaxRate) / 10000;
        uint256 marketingAmount = (amount * marketingTaxRate) / 10000;
        uint256 transferAmount = amount - charityAmount - teamAmount - marketingAmount;

        super._transfer(sender, charityWallet, charityAmount);
        super._transfer(sender, teamWallet, teamAmount);
        super._transfer(sender, marketingWallet, marketingAmount);
        super._transfer(sender, recipient, transferAmount);
    }
}
```
