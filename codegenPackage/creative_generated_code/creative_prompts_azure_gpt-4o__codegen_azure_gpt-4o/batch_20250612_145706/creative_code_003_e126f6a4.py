"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venus-protocol-ui.vercel.app
Prompt: Create a smart contract that interacts with the Venus Protocol to automate collateral supply and borrowing processes.
Generated: DETERMINISTIC_e126f6a4743d063f
Batch ID: 20250612_145706
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

// Importing OpenZeppelin's SafeERC20 for safe token transactions
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IVenusToken {
    function mint(uint256 mintAmount) external returns (uint256);
    function redeemUnderlying(uint256 redeemAmount) external returns (uint256);
    function borrow(uint256 borrowAmount) external returns (uint256);
    function repayBorrow(uint256 repayAmount) external returns (uint256);
    function balanceOfUnderlying(address account) external view returns (uint256);
    function borrowBalanceCurrent(address account) external returns (uint256);
}

interface IComptroller {
    function enterMarkets(address[] calldata vTokens) external returns (uint256[] memory);
    function exitMarket(address vToken) external returns (uint256);
}

contract VenusAutomation is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Addresses for the Venus vToken and the underlying asset
    IVenusToken public vToken;
    IERC20 public underlyingToken;
    IComptroller public comptroller;

    event CollateralSupplied(address indexed user, uint256 amount);
    event CollateralWithdrawn(address indexed user, uint256 amount);
    event Borrowed(address indexed user, uint256 amount);
    event RepaidBorrow(address indexed user, uint256 amount);

    constructor(
        address _vToken,
        address _underlyingToken,
        address _comptroller
    ) {
        vToken = IVenusToken(_vToken);
        underlyingToken = IERC20(_underlyingToken);
        comptroller = IComptroller(_comptroller);

        // Approve vToken contract for maximum possible spending of underlying tokens
        underlyingToken.safeApprove(_vToken, type(uint256).max);
    }

    /**
     * @dev Supplies collateral to the Venus Protocol.
     * @param amount The amount of underlying token to supply.
     */
    function supplyCollateral(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");

        // Transfer underlying tokens from the user to the contract
        underlyingToken.safeTransferFrom(msg.sender, address(this), amount);

        // Supply tokens to Venus
        uint256 result = vToken.mint(amount);
        require(result == 0, "Failed to mint vTokens");

        emit CollateralSupplied(msg.sender, amount);
    }

    /**
     * @dev Withdraws collateral from the Venus Protocol.
     * @param amount The amount of underlying token to withdraw.
     */
    function withdrawCollateral(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");

        // Redeem underlying amount from Venus
        uint256 result = vToken.redeemUnderlying(amount);
        require(result == 0, "Failed to redeem underlying tokens");

        // Transfer the withdrawn underlying tokens back to the user
        underlyingToken.safeTransfer(msg.sender, amount);

        emit CollateralWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Borrows assets from the Venus Protocol.
     * @param amount The amount of underlying token to borrow.
     */
    function borrow(uint256 amount) external onlyOwner nonReentrant {
        require(amount > 0, "Amount must be greater than 0");

        // Borrow the specified amount from Venus
        uint256 result = vToken.borrow(amount);
        require(result == 0, "Failed to borrow underlying tokens");

        // Transfer borrowed assets to the caller
        underlyingToken.safeTransfer(msg.sender, amount);

        emit Borrowed(msg.sender, amount);
    }

    /**
     * @dev Repays borrowed assets to the Venus Protocol.
     * @param amount The amount of underlying token to repay.
     */
    function repayBorrow(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");

        // Transfer underlying tokens from the user to the contract
        underlyingToken.safeTransferFrom(msg.sender, address(this), amount);

        // Repay borrowed assets on Venus
        uint256 result = vToken.repayBorrow(amount);
        require(result == 0, "Failed to repay borrow");

        emit RepaidBorrow(msg.sender, amount);
    }

    /**
     * @dev Enters a market for Venus collateral.
     */
    function enterMarket() external onlyOwner {
        address[] memory markets = new address[](1);
        markets[0] = address(vToken);

        uint256[] memory results = comptroller.enterMarkets(markets);
        require(results[0] == 0, "Failed to enter market");
    }

    /**
     * @dev Exits a market for Venus collateral.
     */
    function exitMarket() external onlyOwner {
        uint256 result = comptroller.exitMarket(address(vToken));
        require(result == 0, "Failed to exit market");
    }

    /**
     * @dev Get the current collateral balance for the contract.
     */
    function getCollateralBalance() external view returns (uint256) {
        return vToken.balanceOfUnderlying(address(this));
    }

    /**
     * @dev Get the current borrow balance for the contract.
     */
    function getBorrowBalance() external returns (uint256) {
        return vToken.borrowBalanceCurrent(address(this));
    }
}
```
