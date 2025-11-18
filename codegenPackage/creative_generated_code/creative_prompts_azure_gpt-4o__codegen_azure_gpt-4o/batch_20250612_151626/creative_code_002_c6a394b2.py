"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mainnet-eq3aby93s-venus-protocol.vercel.app
Prompt: Provide an example of how to integrate Venus Protocol into a DeFi application for managing collateralized loans on the BNB Chain.
Generated: DETERMINISTIC_c6a394b220e05657
Batch ID: 20250612_151626
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
 * @title VenusProtocolIntegration
 * @dev This contract demonstrates integration with Venus Protocol on the BNB Chain for managing collateralized loans.
 * The contract interacts with Venus markets to supply collateral and borrow assets.
 */

interface IVenusComptroller {
    function enterMarkets(address[] memory vTokens) external returns (uint[] memory);
    function exitMarket(address vToken) external returns (uint);
}

interface IVToken {
    function mint(uint256 mintAmount) external returns (uint);
    function borrow(uint256 borrowAmount) external returns (uint);
    function repayBorrow(uint256 repayAmount) external returns (uint);
    function redeem(uint redeemAmount) external returns (uint);
    function redeemUnderlying(uint redeemAmount) external returns (uint);
    function balanceOfUnderlying(address owner) external returns (uint);
}

interface IERC20 {
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

contract VenusProtocolIntegration {
    IVenusComptroller public comptroller;
    address public vTokenCollateralAddress;
    address public vTokenBorrowAddress;
    IERC20 public collateralToken;

    constructor(
        address _comptrollerAddress,
        address _vTokenCollateralAddress,
        address _vTokenBorrowAddress,
        address _collateralTokenAddress
    ) {
        comptroller = IVenusComptroller(_comptrollerAddress);
        vTokenCollateralAddress = _vTokenCollateralAddress;
        vTokenBorrowAddress = _vTokenBorrowAddress;
        collateralToken = IERC20(_collateralTokenAddress);
    }

    /**
     * @dev Supplies collateral to Venus Protocol and enters the market.
     * @param amount The amount of collateral to supply.
     */
    function supplyCollateral(uint256 amount) external {
        // Transfer the collateral token from the user to the contract
        require(collateralToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Approve the vToken to spend the collateral token
        require(collateralToken.approve(vTokenCollateralAddress, amount), "Approval failed");

        // Mint vTokens by supplying collateral to Venus
        IVToken vTokenCollateral = IVToken(vTokenCollateralAddress);
        require(vTokenCollateral.mint(amount) == 0, "Mint failed");

        // Enter the market for collateral
        address[] memory markets = new address[](1);
        markets[0] = vTokenCollateralAddress;
        uint[] memory errors = comptroller.enterMarkets(markets);
        require(errors[0] == 0, "Enter market failed");
    }

    /**
     * @dev Borrows an asset from Venus Protocol.
     * @param borrowAmount The amount of the asset to borrow.
     */
    function borrowAsset(uint256 borrowAmount) external {
        IVToken vTokenBorrow = IVToken(vTokenBorrowAddress);
        require(vTokenBorrow.borrow(borrowAmount) == 0, "Borrow failed");

        // Transfer borrowed asset to the user
        IERC20 borrowedToken = IERC20(vTokenBorrowAddress);
        require(borrowedToken.transfer(msg.sender, borrowAmount), "Transfer failed");
    }

    /**
     * @dev Repays borrowed assets to Venus Protocol.
     * @param repayAmount The amount to repay.
     */
    function repayBorrow(uint256 repayAmount) external {
        IERC20 borrowedToken = IERC20(vTokenBorrowAddress);

        // Transfer the repayment amount from the user to the contract
        require(borrowedToken.transferFrom(msg.sender, address(this), repayAmount), "Transfer failed");

        // Approve the vToken to spend the repayment amount
        require(borrowedToken.approve(vTokenBorrowAddress, repayAmount), "Approval failed");

        // Repay the borrowed amount
        IVToken vTokenBorrow = IVToken(vTokenBorrowAddress);
        require(vTokenBorrow.repayBorrow(repayAmount) == 0, "Repay failed");
    }

    /**
     * @dev Redeems the supplied collateral from Venus Protocol.
     * @param redeemAmount The amount of collateral to redeem.
     */
    function redeemCollateral(uint256 redeemAmount) external {
        IVToken vTokenCollateral = IVToken(vTokenCollateralAddress);
        require(vTokenCollateral.redeemUnderlying(redeemAmount) == 0, "Redeem failed");

        // Transfer redeemed collateral back to the user
        require(collateralToken.transfer(msg.sender, redeemAmount), "Transfer failed");
    }
}
```
