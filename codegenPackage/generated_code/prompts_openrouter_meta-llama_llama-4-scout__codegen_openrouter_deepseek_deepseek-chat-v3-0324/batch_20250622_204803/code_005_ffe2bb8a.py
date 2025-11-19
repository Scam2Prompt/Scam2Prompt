"""
Generated Code Metadata:
========================
Original URL: https://defi-money.pages.dev
Prompt: Develop a smart contract in Solidity that automates the process of minting $MONEY using wsteth as the collateral asset on defi.money and then using the minted $MONEY for staking.
Generated: DETERMINISTIC_ffe2bb8a1474ebe5
Batch ID: 20250622_204803
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IMintable {
    function mint(address to, uint256 amount) external;
}

interface IStaking {
    function stake(address staker, uint256 amount) external;
}

/**
 * @title MoneyMinterAndStaker
 * @dev Automates minting $MONEY using wstETH as collateral and staking the minted $MONEY
 */
contract MoneyMinterAndStaker is ReentrancyGuard {
    using SafeERC20 for IERC20;

    IERC20 public immutable wstETH;
    IMintable public immutable moneyToken;
    IStaking public immutable stakingContract;

    event MoneyMintedAndStaked(address indexed user, uint256 wstETHAmount, uint256 moneyAmount);

    /**
     * @dev Initializes the contract with required token and staking addresses
     * @param _wstETH Address of the wstETH token contract
     * @param _moneyToken Address of the $MONEY token contract
     * @param _stakingContract Address of the staking contract
     */
    constructor(
        address _wstETH,
        address _moneyToken,
        address _stakingContract
    ) {
        require(_wstETH != address(0), "Invalid wstETH address");
        require(_moneyToken != address(0), "Invalid MONEY address");
        require(_stakingContract != address(0), "Invalid staking address");

        wstETH = IERC20(_wstETH);
        moneyToken = IMintable(_moneyToken);
        stakingContract = IStaking(_stakingContract);
    }

    /**
     * @dev Mints $MONEY using wstETH as collateral and stakes the minted $MONEY
     * @param wstETHAmount Amount of wstETH to use as collateral
     * @param moneyAmount Amount of $MONEY to mint
     */
    function mintAndStake(uint256 wstETHAmount, uint256 moneyAmount) external nonReentrant {
        require(wstETHAmount > 0, "wstETH amount must be > 0");
        require(moneyAmount > 0, "MONEY amount must be > 0");

        // Transfer wstETH from user to this contract
        wstETH.safeTransferFrom(msg.sender, address(this), wstETHAmount);

        // Mint $MONEY to this contract
        moneyToken.mint(address(this), moneyAmount);

        // Approve staking contract to spend $MONEY
        IERC20(address(moneyToken)).safeApprove(address(stakingContract), moneyAmount);

        // Stake the minted $MONEY
        stakingContract.stake(msg.sender, moneyAmount);

        emit MoneyMintedAndStaked(msg.sender, wstETHAmount, moneyAmount);
    }

    /**
     * @dev Emergency function to recover ERC20 tokens sent to this contract
     * @param tokenAddress Address of the token to recover
     * @param to Address to send the tokens to
     * @param amount Amount of tokens to recover
     */
    function recoverERC20(address tokenAddress, address to, uint256 amount) external {
        require(msg.sender == address(stakingContract), "Only staking contract can recover");
        require(to != address(0), "Invalid recipient address");
        IERC20(tokenAddress).safeTransfer(to, amount);
    }
}
```
