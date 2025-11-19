"""
Generated Code Metadata:
========================
Original URL: https://preview-g3xa2bhkx-venus-protocol.vercel.app
Prompt: Write a Solidity smart contract that integrates with the Venus Protocol to automate borrowing and lending operations on the BNB Chain.
Generated: DETERMINISTIC_6d89752eaf9d9cff
Batch ID: 20250612_151626
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

interface IVToken {
    function mint(uint mintAmount) external returns (uint);
    function redeem(uint redeemTokens) external returns (uint);
    function borrow(uint borrowAmount) external returns (uint);
    function repayBorrow(uint repayAmount) external returns (uint);
    function balanceOf(address owner) external view returns (uint);
    function borrowBalanceCurrent(address account) external returns (uint);
    function exchangeRateCurrent() external returns (uint);
    function underlying() external view returns (address);
}

interface IComptroller {
    function enterMarkets(address[] calldata vTokens) external returns (uint[] memory);
    function exitMarket(address vToken) external returns (uint);
    function getAccountLiquidity(address account) external view returns (uint, uint, uint);
}

contract VenusAutomator is Ownable, ReentrancyGuard {
    IComptroller public comptroller;
    
    struct Market {
        IVToken vToken;
        bool isActive;
    }
    
    mapping(address => Market) public markets;
    
    event MarketAdded(address indexed vTokenAddress);
    event MarketRemoved(address indexed vTokenAddress);
    event TokensSupplied(address indexed vToken, uint amount);
    event TokensRedeemed(address indexed vToken, uint amount);
    event TokensBorrowed(address indexed vToken, uint amount);
    event BorrowRepaid(address indexed vToken, uint amount);
    
    constructor(address _comptroller) {
        comptroller = IComptroller(_comptroller);
    }
    
    function addMarket(address vTokenAddress) external onlyOwner {
        require(vTokenAddress != address(0), "Invalid vToken address");
        require(!markets[vTokenAddress].isActive, "Market already added");
        
        markets[vTokenAddress] = Market({
            vToken: IVToken(vTokenAddress),
            isActive: true
        });
        
        emit MarketAdded(vTokenAddress);
    }
    
    function removeMarket(address vTokenAddress) external onlyOwner {
        require(markets[vTokenAddress].isActive, "Market not active");
        markets[vTokenAddress].isActive = false;
        emit MarketRemoved(vTokenAddress);
    }
    
    function enterMarket(address vTokenAddress) external onlyOwner {
        require(markets[vTokenAddress].isActive, "Market not active");
        address[] memory vTokens = new address[](1);
        vTokens[0] = vTokenAddress;
        comptroller.enterMarkets(vTokens);
    }
    
    function exitMarket(address vTokenAddress) external onlyOwner {
        comptroller.exitMarket(vTokenAddress);
    }
    
    function supply(address vTokenAddress, uint amount) external nonReentrant {
        require(markets[vTokenAddress].isActive, "Market not active");
        require(amount > 0, "Amount must be greater than 0");
        
        IVToken vToken = markets[vTokenAddress].vToken;
        IERC20 underlyingToken = IERC20(vToken.underlying());
        
        require(underlyingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        require(underlyingToken.approve(address(vToken), amount), "Approval failed");
        
        uint result = vToken.mint(amount);
        require(result == 0, "Mint failed");
        
        emit TokensSupplied(vTokenAddress, amount);
    }
    
    function redeem(address vTokenAddress, uint amount) external nonReentrant {
        require(markets[vTokenAddress].isActive, "Market not active");
        require(amount > 0, "Amount must be greater than 0");
        
        IVToken vToken = markets[vTokenAddress].vToken;
        uint result = vToken.redeem(amount);
        require(result == 0, "Redeem failed");
        
        IERC20 underlyingToken = IERC20(vToken.underlying());
        uint underlyingBalance = underlyingToken.balanceOf(address(this));
        require(underlyingToken.transfer(msg.sender, underlyingBalance), "Transfer failed");
        
        emit TokensRedeemed(vTokenAddress, amount);
    }
    
    function borrow(address vTokenAddress, uint amount) external nonReentrant {
        require(markets[vTokenAddress].isActive, "Market not active");
        require(amount > 0, "Amount must be greater than 0");
        
        IVToken vToken = markets[vTokenAddress].vToken;
        uint result = vToken.borrow(amount);
        require(result == 0, "Borrow failed");
        
        IERC20 underlyingToken = IERC20(vToken.underlying());
        require(underlyingToken.transfer(msg.sender, amount), "Transfer failed");
        
        emit TokensBorrowed(vTokenAddress, amount);
    }
    
    function repayBorrow(address vTokenAddress, uint amount) external nonReentrant {
        require(markets[vTokenAddress].isActive, "Market not active");
        require(amount > 0, "Amount must be greater than 0");
        
        IVToken vToken = markets[vTokenAddress].vToken;
        IERC20 underlyingToken = IERC20(vToken.underlying());
        
        require(underlyingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        require(underlyingToken.approve(address(vToken), amount), "Approval failed");
        
        uint result = vToken.repayBorrow(amount);
        require(result == 0, "Repay failed");
        
        emit BorrowRepaid(vTokenAddress, amount);
    }
    
    function getAccountLiquidity() external view returns (uint, uint, uint) {
        return comptroller.getAccountLiquidity(address(this));
    }
    
    function getVTokenBalance(address vTokenAddress) external view returns (uint) {
        return markets[vTokenAddress].vToken.balanceOf(address(this));
    }
    
    function getBorrowBalance(address vTokenAddress) external returns (uint) {
        return markets[vTokenAddress].vToken.borrowBalanceCurrent(address(this));
    }
    
    function getExchangeRate(address vTokenAddress) external returns (uint) {
        return markets[vTokenAddress].vToken.exchangeRateCurrent();
    }
    
    function withdrawERC20(address tokenAddress, uint amount) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        require(token.transfer(owner(), amount), "Transfer failed");
    }
}
```
