"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeidbvuwd5kzejblzv323edzpb2o4gl4xvjm3d2ghg5fxtp4powdsxy.ipfs.dweb.link
Prompt: Create a smart contract in Solidity that integrates with Venus Protocol to automate lending and borrowing activities, leveraging Venus Prime for superior rates.
Generated: DETERMINISTIC_0388183edd2457f8
Batch ID: 20250612_152249
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
 * @title VenusProtocolAutomator
 * @dev A smart contract that integrates with Venus Protocol to automate lending and borrowing.
 *      Uses Venus Prime for optimized rates. Ensure proper configuration before deployment.
 */
interface IVenusComptroller {
    function enterMarkets(address[] calldata vTokens) external returns (uint[]);
    function exitMarket(address vToken) external returns (uint);
}

interface IVToken {
    function mint(uint mintAmount) external returns (uint);
    function borrow(uint borrowAmount) external returns (uint);
    function repayBorrow(uint repayAmount) external returns (uint);
    function redeem(uint redeemAmount) external returns (uint);
    function balanceOfUnderlying(address owner) external returns (uint);
}

interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

contract VenusProtocolAutomator {
    IVenusComptroller public comptroller; // Venus Comptroller for market interactions
    address public vTokenAddress; // Address of the vToken (e.g., vUSDC, vBUSD)
    IERC20 public underlyingToken; // The underlying ERC20 token (e.g., USDC, BUSD)

    /**
     * @dev Sets the Venus Comptroller and underlying token details.
     * @param _comptroller Address of the Venus Comptroller.
     * @param _vTokenAddress Address of the vToken.
     * @param _underlyingToken Address of the underlying ERC20 token.
     */
    constructor(address _comptroller, address _vTokenAddress, address _underlyingToken) {
        comptroller = IVenusComptroller(_comptroller);
        vTokenAddress = _vTokenAddress;
        underlyingToken = IERC20(_underlyingToken);
    }

    /**
     * @dev Supplies tokens to Venus Protocol for lending.
     * @param amount Amount of tokens to supply.
     */
    function supply(uint amount) external {
        // Transfer underlying tokens from the caller to this contract
        require(underlyingToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Approve the vToken to spend the underlying tokens
        require(underlyingToken.approve(vTokenAddress, amount), "Approval failed");

        // Mint vTokens by supplying the underlying tokens
        uint mintResult = IVToken(vTokenAddress).mint(amount);
        require(mintResult == 0, "Mint failed"); // Venus uses 0 for success
    }

    /**
     * @dev Borrows tokens from Venus Protocol.
     * @param amount Amount of tokens to borrow.
     */
    function borrow(uint amount) external {
        // Enter the market to enable borrowing
        address[] memory markets = new address[](1);
        markets[0] = vTokenAddress;
        uint[] memory results = comptroller.enterMarkets(markets);
        require(results[0] == 0, "Enter market failed"); // Venus uses 0 for success

        // Borrow the desired amount of tokens
        uint borrowResult = IVToken(vTokenAddress).borrow(amount);
        require(borrowResult == 0, "Borrow failed"); // Venus uses 0 for success
    }

    /**
     * @dev Repays the borrowed tokens on Venus Protocol.
     * @param amount Amount of tokens to repay.
     */
    function repayBorrow(uint amount) external {
        // Transfer the repayment tokens from the caller to this contract
        require(underlyingToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Approve the vToken to spend the repayment tokens
        require(underlyingToken.approve(vTokenAddress, amount), "Approval failed");

        // Repay the borrowed amount
        uint repayResult = IVToken(vTokenAddress).repayBorrow(amount);
        require(repayResult == 0, "Repay failed"); // Venus uses 0 for success
    }

    /**
     * @dev Redeems the supplied tokens from Venus Protocol.
     * @param amount Amount of underlying tokens to redeem.
     */
    function redeem(uint amount) external {
        // Redeem the specified amount of underlying tokens
        uint redeemResult = IVToken(vTokenAddress).redeem(amount);
        require(redeemResult == 0, "Redeem failed"); // Venus uses 0 for success

        // Transfer the redeemed tokens to the caller
        require(underlyingToken.transfer(msg.sender, amount), "Token transfer failed");
    }

    /**
     * @dev Returns the balance of underlying tokens supplied by the caller.
     * @return Balance of underlying tokens.
     */
    function balanceOfUnderlying() external returns (uint) {
        return IVToken(vTokenAddress).balanceOfUnderlying(msg.sender);
    }
}
```
