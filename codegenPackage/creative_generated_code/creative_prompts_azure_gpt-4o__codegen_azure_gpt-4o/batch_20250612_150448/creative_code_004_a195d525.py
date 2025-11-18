"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testnet-venus-protocol.vercel.app
Prompt: Write a smart contract to automate lending and borrowing operations on Venus Protocol using the BNB Chain.
Generated: DETERMINISTIC_a195d5251f2e1abe
Batch ID: 20250612_150448
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
 * @title VenusLendingContract
 * @notice This contract enables lending and borrowing operations on Venus Protocol.
 * @dev Ensure to interact with the Venus Protocol's deployed contracts on the BNB Chain.
 */
interface IVToken {
    function mint(uint256 mintAmount) external returns (uint256);
    function redeem(uint256 redeemTokens) external returns (uint256);
    function borrow(uint256 borrowAmount) external returns (uint256);
    function repayBorrow(uint256 repayAmount) external returns (uint256);
}

interface IERC20 {
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract VenusLendingContract {
    address public owner;
    IVToken public vToken;
    IERC20 public underlyingToken;

    /**
     * @dev Initializes the contract with Venus vToken and the underlying token addresses.
     * @param _vToken Address of the Venus vToken contract.
     * @param _underlyingToken Address of the underlying ERC20 token contract.
     */
    constructor(address _vToken, address _underlyingToken) {
        owner = msg.sender;
        vToken = IVToken(_vToken);
        underlyingToken = IERC20(_underlyingToken);
    }

    /**
     * @dev Modifier to restrict function access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    /**
     * @dev Deposit underlying tokens into the Venus Protocol to earn interest.
     * @param amount The amount of tokens to deposit.
     */
    function deposit(uint256 amount) external onlyOwner {
        // Transfer underlying tokens from the user to the contract
        require(underlyingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Approve vToken to spend the underlying tokens
        require(underlyingToken.approve(address(vToken), amount), "Approval failed");

        // Mint vTokens by depositing the underlying tokens
        uint256 result = vToken.mint(amount);
        require(result == 0, "Mint failed");
    }

    /**
     * @dev Redeem underlying tokens by burning vTokens.
     * @param vTokenAmount The amount of vTokens to redeem.
     */
    function redeem(uint256 vTokenAmount) external onlyOwner {
        uint256 result = vToken.redeem(vTokenAmount);
        require(result == 0, "Redeem failed");
    }

    /**
     * @dev Borrow underlying tokens by using collateral.
     * @param amount The amount of tokens to borrow.
     */
    function borrow(uint256 amount) external onlyOwner {
        uint256 result = vToken.borrow(amount);
        require(result == 0, "Borrow failed");
    }

    /**
     * @dev Repay borrowed underlying tokens.
     * @param amount The amount of tokens to repay.
     */
    function repayBorrow(uint256 amount) external onlyOwner {
        // Transfer underlying tokens from the user to the contract
        require(underlyingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Approve vToken to spend the underlying tokens
        require(underlyingToken.approve(address(vToken), amount), "Approval failed");

        // Repay the borrowed tokens
        uint256 result = vToken.repayBorrow(amount);
        require(result == 0, "Repay failed");
    }

    /**
     * @dev Withdraw any ERC20 tokens accidentally sent to this contract.
     * @param token Address of the ERC20 token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function rescueTokens(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(owner, amount);
    }
}
```
