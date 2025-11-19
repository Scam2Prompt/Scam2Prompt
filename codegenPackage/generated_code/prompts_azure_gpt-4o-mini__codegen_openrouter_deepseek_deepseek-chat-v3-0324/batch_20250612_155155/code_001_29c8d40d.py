"""
Generated Code Metadata:
========================
Original URL: https://testnet-git-refactor-use-contracts-package-venus-protocol.vercel.app
Prompt: How can I use the Venus Protocol contracts package to implement lending and borrowing features in my DeFi application?
Generated: DETERMINISTIC_29c8d40d775377e3
Batch ID: 20250612_155155
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

import "@venusprotocol/venus-protocol/contracts/VToken.sol";
import "@venusprotocol/venus-protocol/contracts/Comptroller.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

contract VenusLendingBorrowing {
    using SafeERC20 for IERC20;

    Comptroller public immutable comptroller;
    address public admin;

    event TokensSupplied(address indexed user, address indexed vToken, uint256 amount);
    event TokensBorrowed(address indexed user, address indexed vToken, uint256 amount);
    event TokensRepaid(address indexed user, address indexed vToken, uint256 amount);
    event TokensRedeemed(address indexed user, address indexed vToken, uint256 amount);

    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can call this");
        _;
    }

    constructor(address _comptroller) {
        comptroller = Comptroller(_comptroller);
        admin = msg.sender;
    }

    /**
     * @dev Supply tokens to Venus Protocol
     * @param underlyingToken The underlying ERC20 token address
     * @param vToken The corresponding vToken address
     * @param amount The amount of tokens to supply
     */
    function supply(address underlyingToken, address vToken, uint256 amount) external {
        IERC20 token = IERC20(underlyingToken);
        VToken vTokenContract = VToken(vToken);

        // Transfer tokens from user to this contract
        token.safeTransferFrom(msg.sender, address(this), amount);

        // Approve vToken to spend the underlying tokens
        token.safeApprove(vToken, amount);

        // Mint vTokens
        require(vTokenContract.mint(amount) == 0, "Mint failed");

        emit TokensSupplied(msg.sender, vToken, amount);
    }

    /**
     * @dev Borrow tokens from Venus Protocol
     * @param vToken The vToken address to borrow against
     * @param amount The amount to borrow
     */
    function borrow(address vToken, uint256 amount) external {
        VToken vTokenContract = VToken(vToken);

        // Enter the market if not already entered
        address[] memory vTokens = new address[](1);
        vTokens[0] = vToken;
        uint[] memory errors = comptroller.enterMarkets(vTokens);
        require(errors[0] == 0, "Market entry failed");

        // Borrow tokens
        require(vTokenContract.borrow(amount) == 0, "Borrow failed");

        emit TokensBorrowed(msg.sender, vToken, amount);
    }

    /**
     * @dev Repay borrowed tokens
     * @param underlyingToken The underlying ERC20 token address
     * @param vToken The vToken address
     * @param amount The amount to repay
     */
    function repay(address underlyingToken, address vToken, uint256 amount) external {
        IERC20 token = IERC20(underlyingToken);
        VToken vTokenContract = VToken(vToken);

        // Transfer tokens from user to this contract
        token.safeTransferFrom(msg.sender, address(this), amount);

        // Approve vToken to spend the underlying tokens
        token.safeApprove(vToken, amount);

        // Repay borrow
        require(vTokenContract.repayBorrow(amount) == 0, "Repay failed");

        emit TokensRepaid(msg.sender, vToken, amount);
    }

    /**
     * @dev Redeem supplied tokens
     * @param vToken The vToken address
     * @param amount The amount of vTokens to redeem
     */
    function redeem(address vToken, uint256 amount) external {
        VToken vTokenContract = VToken(vToken);

        // Redeem underlying tokens
        require(vTokenContract.redeem(amount) == 0, "Redeem failed");

        emit TokensRedeemed(msg.sender, vToken, amount);
    }

    /**
     * @dev Get account liquidity for a user
     * @param user The user address
     * @return (error code, liquidity, shortfall)
     */
    function getAccountLiquidity(address user) external view returns (uint, uint, uint) {
        return comptroller.getAccountLiquidity(user);
    }

    /**
     * @dev Change the admin address
     * @param newAdmin The new admin address
     */
    function changeAdmin(address newAdmin) external onlyAdmin {
        admin = newAdmin;
    }

    /**
     * @dev Emergency function to recover ERC20 tokens sent by mistake
     * @param tokenAddress The token contract address
     * @param amount The amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 amount) external onlyAdmin {
        IERC20 token = IERC20(tokenAddress);
        token.safeTransfer(admin, amount);
    }
}
```
