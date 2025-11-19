"""
Generated Code Metadata:
========================
Original URL: https://venus-protocol-ui.vercel.app
Prompt: "Generate an example of a smart contract that enables users to supply collateral on the Venus Protocol without central authority."
Generated: DETERMINISTIC_4a8856c1c0551014
Batch ID: 20250622_204834
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IVenusComptroller {
    function enterMarkets(address[] calldata vTokens) external returns (uint[] memory);
    function exitMarket(address vToken) external returns (uint);
}

interface IVenusVToken {
    function mint(uint mintAmount) external returns (uint);
    function redeem(uint redeemTokens) external returns (uint);
    function borrow(uint borrowAmount) external returns (uint);
    function repayBorrow(uint repayAmount) external returns (uint);
    function balanceOf(address owner) external view returns (uint);
    function borrowBalanceCurrent(address account) external returns (uint);
    function underlying() external view returns (address);
}

contract VenusCollateralManager is Ownable, ReentrancyGuard {
    IVenusComptroller public comptroller;
    mapping(address => bool) public supportedVTokens;
    mapping(address => mapping(address => uint)) public userCollateral;

    event CollateralSupplied(address indexed user, address indexed vToken, uint amount);
    event CollateralWithdrawn(address indexed user, address indexed vToken, uint amount);
    event VTokenSupported(address indexed vToken, bool supported);

    constructor(address _comptroller) {
        comptroller = IVenusComptroller(_comptroller);
    }

    function addSupportedVToken(address vToken) external onlyOwner {
        supportedVTokens[vToken] = true;
        emit VTokenSupported(vToken, true);
    }

    function removeSupportedVToken(address vToken) external onlyOwner {
        supportedVTokens[vToken] = false;
        emit VTokenSupported(vToken, false);
    }

    function supplyCollateral(address vToken, uint amount) external nonReentrant {
        require(supportedVTokens[vToken], "VToken not supported");
        
        IERC20 underlyingToken = IERC20(IVenusVToken(vToken).underlying());
        require(underlyingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        underlyingToken.approve(vToken, amount);
        uint err = IVenusVToken(vToken).mint(amount);
        require(err == 0, "Mint failed");

        address[] memory vTokens = new address[](1);
        vTokens[0] = vToken;
        uint[] memory results = comptroller.enterMarkets(vTokens);
        require(results[0] == 0, "Enter market failed");

        userCollateral[msg.sender][vToken] += amount;
        emit CollateralSupplied(msg.sender, vToken, amount);
    }

    function withdrawCollateral(address vToken, uint amount) external nonReentrant {
        require(userCollateral[msg.sender][vToken] >= amount, "Insufficient collateral");
        
        uint err = IVenusVToken(vToken).redeem(amount);
        require(err == 0, "Redeem failed");

        IERC20 underlyingToken = IERC20(IVenusVToken(vToken).underlying());
        require(underlyingToken.transfer(msg.sender, amount), "Transfer failed");

        userCollateral[msg.sender][vToken] -= amount;
        emit CollateralWithdrawn(msg.sender, vToken, amount);
    }

    function getCollateralBalance(address user, address vToken) external view returns (uint) {
        return userCollateral[user][vToken];
    }
}
```
