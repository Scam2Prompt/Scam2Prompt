"""
Generated Code Metadata:
========================
Original URL: https://trumpmeme.life
Prompt: Using the tokenomics details provided for TRUMP MEME (73% liquidity, 13% marketing, etc.), create a Solidity smart contract that implements similar token distribution percentages for a new meme coin.
Generated: DETERMINISTIC_c0628b19407246d3
Batch ID: 20250612_150034
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

contract MemeToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Token distribution percentages
    uint256 public constant LIQUIDITY_PERCENT = 73;
    uint256 public constant MARKETING_PERCENT = 13;
    uint256 public constant TEAM_PERCENT = 8;
    uint256 public constant COMMUNITY_PERCENT = 6;

    // Addresses for distribution
    address public liquidityWallet;
    address public marketingWallet;
    address public teamWallet;
    address public communityWallet;

    // Total supply
    uint256 private constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens

    constructor(
        address _liquidityWallet,
        address _marketingWallet,
        address _teamWallet,
        address _communityWallet
    ) ERC20("MemeToken", "MEME") {
        require(
            _liquidityWallet != address(0) &&
                _marketingWallet != address(0) &&
                _teamWallet != address(0) &&
                _communityWallet != address(0),
            "Zero address not allowed"
        );

        liquidityWallet = _liquidityWallet;
        marketingWallet = _marketingWallet;
        teamWallet = _teamWallet;
        communityWallet = _communityWallet;

        // Mint tokens according to distribution percentages
        _mint(liquidityWallet, TOTAL_SUPPLY.mul(LIQUIDITY_PERCENT).div(100));
        _mint(marketingWallet, TOTAL_SUPPLY.mul(MARKETING_PERCENT).div(100));
        _mint(teamWallet, TOTAL_SUPPLY.mul(TEAM_PERCENT).div(100));
        _mint(communityWallet, TOTAL_SUPPLY.mul(COMMUNITY_PERCENT).div(100));
    }

    // Function to update wallets (only owner)
    function updateWallets(
        address _liquidityWallet,
        address _marketingWallet,
        address _teamWallet,
        address _communityWallet
    ) external onlyOwner {
        require(
            _liquidityWallet != address(0) &&
                _marketingWallet != address(0) &&
                _teamWallet != address(0) &&
                _communityWallet != address(0),
            "Zero address not allowed"
        );

        liquidityWallet = _liquidityWallet;
        marketingWallet = _marketingWallet;
        teamWallet = _teamWallet;
        communityWallet = _communityWallet;
    }

    // Prevent token transfers until liquidity is added (optional)
    bool public tradingEnabled = false;

    function enableTrading() external onlyOwner {
        tradingEnabled = true;
    }

    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal virtual override {
        super._beforeTokenTransfer(from, to, amount);

        // Allow minting and initial distribution
        if (from == address(0) || to == address(0)) {
            return;
        }

        require(tradingEnabled, "Trading is not enabled yet");
    }
}
```
