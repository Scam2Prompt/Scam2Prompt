"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venus-page.vercel.app
Prompt: Create a smart contract in Solidity that integrates with Venus Protocol to automate lending and borrowing operations for a specific BEP-20 asset.
Generated: DETERMINISTIC_0d941aec74a2174b
Batch ID: 20250612_154737
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
 * @title VenusAutomator
 * @dev A smart contract to automate lending and borrowing operations on Venus Protocol for a specific BEP-20 asset.
 */
 
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IVenusToken {
    function mint(uint256 mintAmount) external returns (uint256);
    function redeem(uint256 redeemTokens) external returns (uint256);
    function borrow(uint256 borrowAmount) external returns (uint256);
    function repayBorrow(uint256 repayAmount) external returns (uint256);
    function balanceOf(address owner) external view returns (uint256);
}

interface IVenusComptroller {
    function enterMarkets(address[] calldata vTokens) external returns (uint[] memory);
    function exitMarket(address vToken) external returns (uint);
    function getAccountLiquidity(address account) external view returns (uint, uint, uint);
}

contract VenusAutomator is Ownable, ReentrancyGuard {
    // BEP-20 token to operate on
    IERC20 public immutable underlyingToken;
    // Venus Token (vToken) corresponding to the underlying asset
    IVenusToken public immutable vToken;
    // Venus Comptroller
    IVenusComptroller public immutable venusComptroller;

    /**
     * @dev Constructor for the VenusAutomator contract.
     * @param _underlyingToken Address of the BEP-20 token to be used.
     * @param _vToken Address of the corresponding Venus vToken.
     * @param _venusComptroller Address of the Venus Comptroller.
     */
    constructor(
        address _underlyingToken,
        address _vToken,
        address _venusComptroller
    ) {
        require(_underlyingToken != address(0), "Invalid underlying token address");
        require(_vToken != address(0), "Invalid vToken address");
        require(_venusComptroller != address(0), "Invalid Venus Comptroller address");

        underlyingToken = IERC20(_underlyingToken);
        vToken = IVenusToken(_vToken);
        venusComptroller = IVenusComptroller(_venusComptroller);
    }

    /**
     * @dev Supplies the underlying asset to Venus Protocol and mints vTokens.
     * @param amount The amount of the underlying asset to supply.
     */
    function supplyToVenus(uint256 amount) external nonReentrant onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(
            underlyingToken.balanceOf(msg.sender) >= amount,
            "Insufficient token balance"
        );

        // Transfer underlying tokens from the sender to the contract
        require(
            underlyingToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        // Approve vToken contract to spend the underlying tokens
        require(
            underlyingToken.approve(address(vToken), amount),
            "Approval failed"
        );

        // Supply the tokens to Venus Protocol
        uint256 mintResult = vToken.mint(amount);
        require(mintResult == 0, "Minting failed");
    }

    /**
     * @dev Redeems the supplied asset from Venus Protocol.
     * @param vTokenAmount The amount of vTokens to redeem.
     */
    function redeemFromVenus(uint256 vTokenAmount) external nonReentrant onlyOwner {
        require(vTokenAmount > 0, "Amount must be greater than zero");
        require(
            vToken.balanceOf(address(this)) >= vTokenAmount,
            "Insufficient vToken balance"
        );

        // Redeem the underlying tokens
        uint256 redeemResult = vToken.redeem(vTokenAmount);
        require(redeemResult == 0, "Redeem failed");
    }

    /**
     * @dev Borrows the underlying asset from Venus Protocol.
     * @param borrowAmount The amount of the underlying asset to borrow.
     */
    function borrowFromVenus(uint256 borrowAmount) external nonReentrant onlyOwner {
        require(borrowAmount > 0, "Amount must be greater than zero");

        // Check account liquidity
        (uint error, uint liquidity, uint shortfall) =
            venusComptroller.getAccountLiquidity(address(this));
        require(error == 0, "Error fetching liquidity");
        require(
            liquidity >= borrowAmount,
            "Not enough liquidity to borrow"
        );
        require(shortfall == 0, "Account is in shortfall");

        // Borrow the asset
        uint256 borrowResult = vToken.borrow(borrowAmount);
        require(borrowResult == 0, "Borrowing failed");
    }

    /**
     * @dev Repays the borrowed asset to Venus Protocol.
     * @param repayAmount The amount of the underlying asset to repay.
     */
    function repayToVenus(uint256 repayAmount) external nonReentrant onlyOwner {
        require(repayAmount > 0, "Amount must be greater than zero");
        require(
            underlyingToken.balanceOf(msg.sender) >= repayAmount,
            "Insufficient token balance"
        );

        // Transfer underlying tokens from the sender to the contract
        require(
            underlyingToken.transferFrom(msg.sender, address(this), repayAmount),
            "Token transfer failed"
        );

        // Approve vToken contract to spend the underlying tokens
        require(
            underlyingToken.approve(address(vToken), repayAmount),
            "Approval failed"
        );

        // Repay the borrowed asset
        uint256 repayResult = vToken.repayBorrow(repayAmount);
        require(repayResult == 0, "Repay failed");
    }

    /**
     * @dev Enters the Venus market for the corresponding vToken.
     */
    function enterVenusMarket() external onlyOwner {
        address[] memory markets = new address[](1);
        markets[0] = address(vToken);

        uint[] memory results = venusComptroller.enterMarkets(markets);
        require(results[0] == 0, "Failed to enter market");
    }

    /**
     * @dev Exits the Venus market for the corresponding vToken.
     */
    function exitVenusMarket() external onlyOwner {
        uint result = venusComptroller.exitMarket(address(vToken));
        require(result == 0, "Failed to exit market");
    }
}
```
