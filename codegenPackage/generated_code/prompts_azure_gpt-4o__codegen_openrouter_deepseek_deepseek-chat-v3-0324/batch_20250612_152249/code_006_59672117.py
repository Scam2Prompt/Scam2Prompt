"""
Generated Code Metadata:
========================
Original URL: https://bafybeihzyw7qgtjbkq6dimtys2ndltbec2rzobfuk2gxi2gbt5rg3w4c6a.ipfs.dweb.link
Prompt: Generate a Solidity contract that burns liquidity pool tokens as part of the `$gummy` tokenomics strategy, ensuring compliance with the allocation percentages provided.
Generated: DETERMINISTIC_596721175f6b8947
Batch ID: 20250612_152249
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract GummyLiquidityBurner is Ownable {
    using SafeMath for uint256;

    // Token addresses
    address public gummyToken;
    address public lpToken;

    // Allocation percentages (100% = 10000)
    uint256 public constant BURN_PERCENTAGE = 5000; // 50%
    uint256 public constant TREASURY_PERCENTAGE = 3000; // 30%
    uint256 public constant TEAM_PERCENTAGE = 2000; // 20%

    // Recipient addresses
    address public treasuryWallet;
    address public teamWallet;

    event LiquidityBurned(uint256 amountBurned, uint256 amountToTreasury, uint256 amountToTeam);

    constructor(
        address _gummyToken,
        address _lpToken,
        address _treasuryWallet,
        address _teamWallet
    ) {
        require(_gummyToken != address(0), "Invalid Gummy token address");
        require(_lpToken != address(0), "Invalid LP token address");
        require(_treasuryWallet != address(0), "Invalid treasury wallet");
        require(_teamWallet != address(0), "Invalid team wallet");

        gummyToken = _gummyToken;
        lpToken = _lpToken;
        treasuryWallet = _treasuryWallet;
        teamWallet = _teamWallet;
    }

    /**
     * @dev Burns LP tokens according to the allocation percentages
     * @param amount The total amount of LP tokens to process
     */
    function burnLiquidity(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");

        IERC20 lpTokenContract = IERC20(lpToken);
        require(lpTokenContract.balanceOf(address(this)) >= amount, "Insufficient LP tokens");

        uint256 burnAmount = amount.mul(BURN_PERCENTAGE).div(10000);
        uint256 treasuryAmount = amount.mul(TREASURY_PERCENTAGE).div(10000);
        uint256 teamAmount = amount.mul(TEAM_PERCENTAGE).div(10000);

        // Ensure total doesn't exceed amount due to rounding
        uint256 total = burnAmount.add(treasuryAmount).add(teamAmount);
        if (total < amount) {
            // Add remainder to burn amount
            burnAmount = burnAmount.add(amount.sub(total));
        }

        // Burn tokens
        lpTokenContract.transfer(address(0xdead), burnAmount);

        // Transfer to treasury
        if (treasuryAmount > 0) {
            lpTokenContract.transfer(treasuryWallet, treasuryAmount);
        }

        // Transfer to team
        if (teamAmount > 0) {
            lpTokenContract.transfer(teamWallet, teamAmount);
        }

        emit LiquidityBurned(burnAmount, treasuryAmount, teamAmount);
    }

    /**
     * @dev Updates the treasury wallet address
     * @param newTreasury The new treasury wallet address
     */
    function updateTreasuryWallet(address newTreasury) external onlyOwner {
        require(newTreasury != address(0), "Invalid treasury wallet");
        treasuryWallet = newTreasury;
    }

    /**
     * @dev Updates the team wallet address
     * @param newTeam The new team wallet address
     */
    function updateTeamWallet(address newTeam) external onlyOwner {
        require(newTeam != address(0), "Invalid team wallet");
        teamWallet = newTeam;
    }

    /**
     * @dev Recovers any ERC20 tokens accidentally sent to this contract
     * @param tokenAddress The token contract address
     * @param tokenAmount The amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != lpToken, "Cannot withdraw LP tokens");
        IERC20(tokenAddress).transfer(owner(), tokenAmount);
    }
}
```
