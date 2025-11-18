"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-in.web.app
Prompt: Write a Solidity contract that implements DOGE20 tokenomics, including allocations for presale, marketing, treasury, staking rewards, and liquidity provision.
Generated: DETERMINISTIC_0976489e7111f7f6
Batch ID: 20250612_153401
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
 * @title DOGE20 Token Contract
 * @dev Implements ERC20 tokenomics with allocations for presale, marketing, treasury, staking rewards, and liquidity provision.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract DOGE20Token is ERC20, Ownable {
    // Total supply of tokens
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens

    // Allocation breakdown percentages
    uint256 public constant PRESALE_PERCENT = 20; // 20%
    uint256 public constant MARKETING_PERCENT = 10; // 10%
    uint256 public constant TREASURY_PERCENT = 30; // 30%
    uint256 public constant STAKING_REWARDS_PERCENT = 30; // 30%
    uint256 public constant LIQUIDITY_PERCENT = 10; // 10%

    // Allocation breakdown in token amounts
    uint256 public constant PRESALE_ALLOCATION = (TOTAL_SUPPLY * PRESALE_PERCENT) / 100;
    uint256 public constant MARKETING_ALLOCATION = (TOTAL_SUPPLY * MARKETING_PERCENT) / 100;
    uint256 public constant TREASURY_ALLOCATION = (TOTAL_SUPPLY * TREASURY_PERCENT) / 100;
    uint256 public constant STAKING_REWARDS_ALLOCATION = (TOTAL_SUPPLY * STAKING_REWARDS_PERCENT) / 100;
    uint256 public constant LIQUIDITY_ALLOCATION = (TOTAL_SUPPLY * LIQUIDITY_PERCENT) / 100;

    // Wallets for allocations
    address public presaleWallet;
    address public marketingWallet;
    address public treasuryWallet;
    address public stakingRewardsWallet;
    address public liquidityWallet;

    /**
     * @notice Constructor initializes the token and allocates initial balances.
     * @param _presaleWallet Address for presale tokens.
     * @param _marketingWallet Address for marketing tokens.
     * @param _treasuryWallet Address for treasury tokens.
     * @param _stakingRewardsWallet Address for staking rewards tokens.
     * @param _liquidityWallet Address for liquidity provision tokens.
     */
    constructor(
        address _presaleWallet,
        address _marketingWallet,
        address _treasuryWallet,
        address _stakingRewardsWallet,
        address _liquidityWallet
    ) ERC20("DOGE20 Token", "DOGE20") {
        require(
            _presaleWallet != address(0) &&
                _marketingWallet != address(0) &&
                _treasuryWallet != address(0) &&
                _stakingRewardsWallet != address(0) &&
                _liquidityWallet != address(0),
            "Invalid wallet addresses"
        );

        // Assign wallet addresses
        presaleWallet = _presaleWallet;
        marketingWallet = _marketingWallet;
        treasuryWallet = _treasuryWallet;
        stakingRewardsWallet = _stakingRewardsWallet;
        liquidityWallet = _liquidityWallet;

        // Mint and allocate tokens
        _mint(presaleWallet, PRESALE_ALLOCATION);
        _mint(marketingWallet, MARKETING_ALLOCATION);
        _mint(treasuryWallet, TREASURY_ALLOCATION);
        _mint(stakingRewardsWallet, STAKING_REWARDS_ALLOCATION);
        _mint(liquidityWallet, LIQUIDITY_ALLOCATION);
    }

    /**
     * @notice Allows the owner to update wallet addresses.
     * @param _walletType The type of wallet to update (1=Presale, 2=Marketing, 3=Treasury, 4=Staking, 5=Liquidity).
     * @param _newWallet The new wallet address.
     */
    function updateWallet(uint8 _walletType, address _newWallet) external onlyOwner {
        require(_newWallet != address(0), "Invalid wallet address");

        if (_walletType == 1) {
            presaleWallet = _newWallet;
        } else if (_walletType == 2) {
            marketingWallet = _newWallet;
        } else if (_walletType == 3) {
            treasuryWallet = _newWallet;
        } else if (_walletType == 4) {
            stakingRewardsWallet = _newWallet;
        } else if (_walletType == 5) {
            liquidityWallet = _newWallet;
        } else {
            revert("Invalid wallet type");
        }
    }
}
```
