"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-99bitcoinspresale.pages.dev
Prompt: Write code in Solidity to implement a token distribution mechanism for $99BTC tokens, allocating percentages for presale, staking, community rewards, liquidity, and marketing as per the tokenomics described on the site.
Generated: DETERMINISTIC_6a9112e02bc90496
Batch ID: 20250612_151310
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract BTC99Token is ERC20, Ownable {
    // Token distribution percentages
    uint256 public constant PRESALE_ALLOCATION = 20; // 20%
    uint256 public constant STAKING_ALLOCATION = 30; // 30%
    uint256 public constant COMMUNITY_REWARDS_ALLOCATION = 20; // 20%
    uint256 public constant LIQUIDITY_ALLOCATION = 20; // 20%
    uint256 public constant MARKETING_ALLOCATION = 10; // 10%

    // Total supply of tokens
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10 ** decimals(); // 1 million tokens

    // Addresses for different allocations
    address public presaleWallet;
    address public stakingWallet;
    address public rewardsWallet;
    address public liquidityWallet;
    address public marketingWallet;

    // Event emitted when tokens are allocated
    event TokensAllocated(address indexed to, uint256 amount);

    constructor(
        address _presaleWallet,
        address _stakingWallet,
        address _rewardsWallet,
        address _liquidityWallet,
        address _marketingWallet
    ) ERC20("99BTC Token", "99BTC") {
        // Ensure addresses are not zero
        require(_presaleWallet != address(0), "Presale wallet cannot be the zero address");
        require(_stakingWallet != address(0), "Staking wallet cannot be the zero address");
        require(_rewardsWallet != address(0), "Rewards wallet cannot be the zero address");
        require(_liquidityWallet != address(0), "Liquidity wallet cannot be the zero address");
        require(_marketingWallet != address(0), "Marketing wallet cannot be the zero address");

        // Assign wallet addresses
        presaleWallet = _presaleWallet;
        stakingWallet = _stakingWallet;
        rewardsWallet = _rewardsWallet;
        liquidityWallet = _liquidityWallet;
        marketingWallet = _marketingWallet;

        // Allocate tokens based on the defined percentages
        _allocateTokens(presaleWallet, PRESALE_ALLOCATION);
        _allocateTokens(stakingWallet, STAKING_ALLOCATION);
        _allocateTokens(rewardsWallet, COMMUNITY_REWARDS_ALLOCATION);
        _allocateTokens(liquidityWallet, LIQUIDITY_ALLOCATION);
        _allocateTokens(marketingWallet, MARKETING_ALLOCATION);
    }

    // Internal function to allocate tokens to a specified wallet
    function _allocateTokens(address _to, uint256 _percentage) internal {
        uint256 amount = (TOTAL_SUPPLY * _percentage) / 100;
        _mint(_to, amount);
        emit TokensAllocated(_to, amount);
    }

    // Function to withdraw tokens accidentally sent to the contract
    function withdrawToken(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(this), "Cannot withdraw own tokens");
        IERC20 token = IERC20(tokenAddress);
        require(token.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
