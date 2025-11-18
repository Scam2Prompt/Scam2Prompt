"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gifts-usualdao.com
Prompt: Create a Solidity smart contract that implements the ETH0 asset functionality, unifying LST and LRT liquidity while optimizing yield in $USUAL rewards.
Generated: DETERMINISTIC_055e9a12f7f4af1b
Batch ID: 20250612_142608
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title ETH0 Asset Smart Contract
 * @dev This contract unifies LST (Liquidity Staking Token) and LRT (Liquidity Reward Token)
 *      liquidity while optimizing yield in $USUAL rewards.
 */
contract ETH0Asset is Ownable, ReentrancyGuard {
    IERC20 public lstToken;  // Address of LST token
    IERC20 public lrtToken;  // Address of LRT token
    IERC20 public usualToken; // Address of USUAL rewards token

    uint256 public totalLiquidity; // Total liquidity in the contract
    mapping(address => uint256) public liquidityBalance; // User's liquidity balance

    event LiquidityAdded(address indexed user, uint256 amount);
    event LiquidityRemoved(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Sets the addresses of the tokens for LST, LRT, and USUAL.
     * @param _lstToken Address of the LST token contract
     * @param _lrtToken Address of the LRT token contract
     * @param _usualToken Address of the USUAL token contract
     */
    constructor(address _lstToken, address _lrtToken, address _usualToken) {
        lstToken = IERC20(_lstToken);
        lrtToken = IERC20(_lrtToken);
        usualToken = IERC20(_usualToken);
    }

    /**
     * @dev Allows users to add liquidity in LST and LRT tokens.
     * @param amountLST The amount of LST to add
     * @param amountLRT The amount of LRT to add
     */
    function addLiquidity(uint256 amountLST, uint256 amountLRT) external nonReentrant {
        require(amountLST > 0 || amountLRT > 0, "Must provide LST or LRT");

        if (amountLST > 0) {
            lstToken.transferFrom(msg.sender, address(this), amountLST);
        }

        if (amountLRT > 0) {
            lrtToken.transferFrom(msg.sender, address(this), amountLRT);
        }

        // Update total liquidity and user's balance
        totalLiquidity += (amountLST + amountLRT);
        liquidityBalance[msg.sender] += (amountLST + amountLRT);
        
        emit LiquidityAdded(msg.sender, amountLST + amountLRT);
    }

    /**
     * @dev Allows users to remove liquidity.
     * @param amount The amount of liquidity to remove
     */
    function removeLiquidity(uint256 amount) external nonReentrant {
        require(liquidityBalance[msg.sender] >= amount, "Insufficient liquidity");

        // Update total liquidity and user's balance
        liquidityBalance[msg.sender] -= amount;
        totalLiquidity -= amount;

        // Transfer LST and LRT back to the user proportional to the liquidity removed
        uint256 lstAmount = (amount * lstToken.balanceOf(address(this))) / totalLiquidity;
        uint256 lrtAmount = (amount * lrtToken.balanceOf(address(this))) / totalLiquidity;

        lstToken.transfer(msg.sender, lstAmount);
        lrtToken.transfer(msg.sender, lrtAmount);

        emit LiquidityRemoved(msg.sender, amount);
    }

    /**
     * @dev Allows users to claim their USUAL rewards.
     * @param amount The amount of USUAL to claim
     */
    function claimRewards(uint256 amount) external nonReentrant {
        require(amount > 0, "Must claim a positive amount");
        require(usualToken.balanceOf(address(this)) >= amount, "Insufficient rewards");

        usualToken.transfer(msg.sender, amount);

        emit RewardsClaimed(msg.sender, amount);
    }

    /**
     * @dev Owner can withdraw tokens from the contract in case of emergency.
     * @param token The address of the token to withdraw
     * @param amount The amount of tokens to withdraw
     */
    function emergencyWithdraw(IERC20 token, uint256 amount) external onlyOwner {
        token.transfer(owner(), amount);
    }
}
```
