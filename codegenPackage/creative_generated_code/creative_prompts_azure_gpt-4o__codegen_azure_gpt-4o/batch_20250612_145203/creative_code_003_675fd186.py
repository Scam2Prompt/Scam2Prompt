"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdog-ic.pages.dev
Prompt: Generate code in Solidity to implement tokenomics for WienerAI ($WAI), including allocations for presale, staking, community rewards, liquidity, and marketing as described on the website.
Generated: DETERMINISTIC_675fd186b06cd65d
Batch ID: 20250612_145203
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
 * @title WienerAI ($WAI) Token Contract
 * @dev Implements tokenomics for WienerAI ($WAI), including allocations for presale, staking,
 * community rewards, liquidity, and marketing.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract WienerAI is ERC20, Ownable {
    // Allocation percentages
    uint256 public constant PRESALE_ALLOCATION = 30; // 30%
    uint256 public constant STAKING_ALLOCATION = 25; // 25%
    uint256 public constant COMMUNITY_REWARDS_ALLOCATION = 20; // 20%
    uint256 public constant LIQUIDITY_ALLOCATION = 15; // 15%
    uint256 public constant MARKETING_ALLOCATION = 10; // 10%

    // Total supply of $WAI tokens
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10**18; // 1 million tokens

    // Wallet addresses for allocations
    address public presaleWallet;
    address public stakingWallet;
    address public communityRewardsWallet;
    address public liquidityWallet;
    address public marketingWallet;

    /**
     * @dev Deploys the contract and mints the token allocations to the respective wallets.
     * @param _presaleWallet Address for presale allocation.
     * @param _stakingWallet Address for staking allocation.
     * @param _communityRewardsWallet Address for community rewards allocation.
     * @param _liquidityWallet Address for liquidity allocation.
     * @param _marketingWallet Address for marketing allocation.
     */
    constructor(
        address _presaleWallet,
        address _stakingWallet,
        address _communityRewardsWallet,
        address _liquidityWallet,
        address _marketingWallet
    ) ERC20("WienerAI", "WAI") {
        require(
            _presaleWallet != address(0) &&
            _stakingWallet != address(0) &&
            _communityRewardsWallet != address(0) &&
            _liquidityWallet != address(0) &&
            _marketingWallet != address(0),
            "Invalid wallet address"
        );

        // Assign wallet addresses
        presaleWallet = _presaleWallet;
        stakingWallet = _stakingWallet;
        communityRewardsWallet = _communityRewardsWallet;
        liquidityWallet = _liquidityWallet;
        marketingWallet = _marketingWallet;

        // Mint tokens to wallets based on allocation percentages
        _mint(presaleWallet, (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 100);
        _mint(stakingWallet, (TOTAL_SUPPLY * STAKING_ALLOCATION) / 100);
        _mint(communityRewardsWallet, (TOTAL_SUPPLY * COMMUNITY_REWARDS_ALLOCATION) / 100);
        _mint(liquidityWallet, (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION) / 100);
        _mint(marketingWallet, (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 100);
    }

    /**
     * @dev Updates the wallet address for presale allocation.
     * @param _newWallet New presale wallet address.
     */
    function updatePresaleWallet(address _newWallet) external onlyOwner {
        require(_newWallet != address(0), "Invalid address");
        presaleWallet = _newWallet;
    }

    /**
     * @dev Updates the wallet address for staking allocation.
     * @param _newWallet New staking wallet address.
     */
    function updateStakingWallet(address _newWallet) external onlyOwner {
        require(_newWallet != address(0), "Invalid address");
        stakingWallet = _newWallet;
    }

    /**
     * @dev Updates the wallet address for community rewards allocation.
     * @param _newWallet New community rewards wallet address.
     */
    function updateCommunityRewardsWallet(address _newWallet) external onlyOwner {
        require(_newWallet != address(0), "Invalid address");
        communityRewardsWallet = _newWallet;
    }

    /**
     * @dev Updates the wallet address for liquidity allocation.
     * @param _newWallet New liquidity wallet address.
     */
    function updateLiquidityWallet(address _newWallet) external onlyOwner {
        require(_newWallet != address(0), "Invalid address");
        liquidityWallet = _newWallet;
    }

    /**
     * @dev Updates the wallet address for marketing allocation.
     * @param _newWallet New marketing wallet address.
     */
    function updateMarketingWallet(address _newWallet) external onlyOwner {
        require(_newWallet != address(0), "Invalid address");
        marketingWallet = _newWallet;
    }
}
```
