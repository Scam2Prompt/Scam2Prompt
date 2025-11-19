"""
Generated Code Metadata:
========================
Original URL: https://sushi-eat-need.com
Prompt: Write a Solidity contract that interacts with SushiSwap's Kashi lending platform to borrow and lend assets.
Generated: DETERMINISTIC_23bc7f6df8c6a8ae
Batch ID: 20250612_153758
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
import "@sushiswap/bentobox-sdk/contracts/IBentoBoxV1.sol";
import "@sushiswap/kashi-lending/contracts/interfaces/IKashiPair.sol";

contract KashiLenderBorrower {
    using SafeERC20 for IERC20;

    IBentoBoxV1 public immutable bentoBox;
    address public owner;

    event Deposited(address indexed token, uint256 amount);
    event Borrowed(address indexed pair, uint256 amount);
    event Repaid(address indexed pair, uint256 amount);
    event Withdrawn(address indexed token, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this");
        _;
    }

    constructor(IBentoBoxV1 _bentoBox) {
        bentoBox = _bentoBox;
        owner = msg.sender;
    }

    /**
     * @dev Deposit tokens into BentoBox
     * @param token The token to deposit
     * @param amount The amount to deposit
     */
    function deposit(IERC20 token, uint256 amount) external onlyOwner {
        token.safeTransferFrom(msg.sender, address(this), amount);
        token.approve(address(bentoBox), amount);
        bentoBox.deposit(address(token), address(this), address(this), amount, 0);
        emit Deposited(address(token), amount);
    }

    /**
     * @dev Withdraw tokens from BentoBox
     * @param token The token to withdraw
     * @param amount The amount to withdraw
     */
    function withdraw(IERC20 token, uint256 amount) external onlyOwner {
        bentoBox.withdraw(address(token), address(this), msg.sender, amount, 0);
        emit Withdrawn(address(token), amount);
    }

    /**
     * @dev Borrow from a Kashi pair
     * @param pair The Kashi pair to borrow from
     * @param amount The amount to borrow
     * @param collateral The collateral token
     * @param collateralAmount The collateral amount
     */
    function borrow(
        IKashiPair pair,
        uint256 amount,
        IERC20 collateral,
        uint256 collateralAmount
    ) external onlyOwner {
        // Approve BentoBox to spend collateral
        collateral.approve(address(bentoBox), collateralAmount);
        
        // Deposit collateral into BentoBox
        bentoBox.deposit(address(collateral), address(this), address(pair), collateralAmount, 0);
        
        // Borrow from Kashi pair
        pair.borrow(address(this), address(this), amount);
        emit Borrowed(address(pair), amount);
    }

    /**
     * @dev Repay a Kashi loan
     * @param pair The Kashi pair to repay
     * @param amount The amount to repay
     * @param close Whether to close the position
     */
    function repay(
        IKashiPair pair,
        uint256 amount,
        bool close
    ) external onlyOwner {
        IERC20 asset = IERC20(pair.asset());
        asset.approve(address(bentoBox), amount);
        bentoBox.deposit(address(asset), address(this), address(pair), amount, 0);
        pair.repay(address(this), close, amount);
        emit Repaid(address(pair), amount);
    }

    /**
     * @dev Transfer ownership of the contract
     * @param newOwner The new owner address
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner");
        owner = newOwner;
    }
}
```
