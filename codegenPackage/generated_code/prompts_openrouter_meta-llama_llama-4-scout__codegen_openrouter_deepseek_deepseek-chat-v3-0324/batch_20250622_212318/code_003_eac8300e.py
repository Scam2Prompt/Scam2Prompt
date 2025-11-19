"""
Generated Code Metadata:
========================
Original URL: https://mainnet-venus-protocol.vercel.app
Prompt: How can I use the Venus Protocol to create a decentralized lending platform on BNB Chain, and what are the key considerations?
Generated: DETERMINISTIC_eac8300e391a4a7f
Batch ID: 20250622_212318
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
import "@venusprotocol/venus-protocol/contracts/PriceOracle.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract VenusLendingPlatform is Ownable, ReentrancyGuard {
    Comptroller public comptroller;
    PriceOracle public priceOracle;

    // Supported markets mapping (vToken address => isSupported)
    mapping(address => bool) public supportedMarkets;

    event MarketAdded(address indexed vToken);
    event MarketRemoved(address indexed vToken);
    event FundsDeposited(address indexed user, address indexed vToken, uint256 amount);
    event FundsBorrowed(address indexed user, address indexed vToken, uint256 amount);
    event FundsRepaid(address indexed user, address indexed vToken, uint256 amount);
    event FundsWithdrawn(address indexed user, address indexed vToken, uint256 amount);

    /**
     * @dev Initialize the lending platform with Venus Protocol's Comptroller and PriceOracle
     * @param _comptroller Address of the Venus Comptroller
     * @param _priceOracle Address of the Venus PriceOracle
     */
    constructor(address _comptroller, address _priceOracle) {
        require(_comptroller != address(0), "Invalid Comptroller address");
        require(_priceOracle != address(0), "Invalid PriceOracle address");
        
        comptroller = Comptroller(_comptroller);
        priceOracle = PriceOracle(_priceOracle);
    }

    /**
     * @dev Add a supported market (vToken)
     * @param vToken Address of the vToken to support
     */
    function addMarket(address vToken) external onlyOwner {
        require(vToken != address(0), "Invalid vToken address");
        require(!supportedMarkets[vToken], "Market already supported");
        
        supportedMarkets[vToken] = true;
        comptroller._supportMarket(VToken(vToken));
        
        emit MarketAdded(vToken);
    }

    /**
     * @dev Remove a supported market (vToken)
     * @param vToken Address of the vToken to remove
     */
    function removeMarket(address vToken) external onlyOwner {
        require(vToken != address(0), "Invalid vToken address");
        require(supportedMarkets[vToken], "Market not supported");
        
        supportedMarkets[vToken] = false;
        emit MarketRemoved(vToken);
    }

    /**
     * @dev Deposit underlying tokens to mint vTokens
     * @param vToken Address of the vToken
     * @param amount Amount of underlying tokens to deposit
     */
    function deposit(address vToken, uint256 amount) external nonReentrant {
        require(supportedMarkets[vToken], "Market not supported");
        require(amount > 0, "Amount must be greater than 0");
        
        VToken vTokenContract = VToken(vToken);
        IERC20 underlying = IERC20(vTokenContract.underlying());
        
        // Transfer underlying tokens from user to this contract
        underlying.transferFrom(msg.sender, address(this), amount);
        
        // Approve vToken to spend underlying tokens
        underlying.approve(vToken, amount);
        
        // Mint vTokens
        uint256 result = vTokenContract.mint(amount);
        require(result == 0, "Minting failed");
        
        emit FundsDeposited(msg.sender, vToken, amount);
    }

    /**
     * @dev Borrow assets from the protocol
     * @param vToken Address of the vToken to borrow against
     * @param amount Amount to borrow
     */
    function borrow(address vToken, uint256 amount) external nonReentrant {
        require(supportedMarkets[vToken], "Market not supported");
        require(amount > 0, "Amount must be greater than 0");
        
        // Enter the market if not already entered
        VToken[] memory vTokens = new VToken[](1);
        vTokens[0] = VToken(vToken);
        comptroller.enterMarkets(vTokens);
        
        // Borrow the assets
        uint256 result = VToken(vToken).borrow(amount);
        require(result == 0, "Borrowing failed");
        
        emit FundsBorrowed(msg.sender, vToken, amount);
    }

    /**
     * @dev Repay borrowed assets
     * @param vToken Address of the vToken
     * @param amount Amount to repay
     */
    function repay(address vToken, uint256 amount) external nonReentrant {
        require(supportedMarkets[vToken], "Market not supported");
        require(amount > 0, "Amount must be greater than 0");
        
        VToken vTokenContract = VToken(vToken);
        IERC20 underlying = IERC20(vTokenContract.underlying());
        
        // Transfer underlying tokens from user to this contract
        underlying.transferFrom(msg.sender, address(this), amount);
        
        // Approve vToken to spend underlying tokens
        underlying.approve(vToken, amount);
        
        // Repay borrow
        uint256 result = vTokenContract.repayBorrow(amount);
        require(result == 0, "Repayment failed");
        
        emit FundsRepaid(msg.sender, vToken, amount);
    }

    /**
     * @dev Withdraw deposited funds by redeeming vTokens
     * @param vToken Address of the vToken
     * @param amount Amount of vTokens to redeem
     */
    function withdraw(address vToken, uint256 amount) external nonReentrant {
        require(supportedMarkets[vToken], "Market not supported");
        require(amount > 0, "Amount must be greater than 0");
        
        // Redeem vTokens
        uint256 result = VToken(vToken).redeem(amount);
        require(result == 0, "Redemption failed");
        
        emit FundsWithdrawn(msg.sender, vToken, amount);
    }

    /**
     * @dev Get the user's account liquidity in USD
     * @param user Address of the user
     * @return (error code, liquidity, shortfall)
     */
    function getAccountLiquidity(address user) external view returns (uint256, uint256, uint256) {
        return comptroller.getAccountLiquidity(user);
    }

    /**
     * @dev Get the borrow balance of a user for a specific vToken
     * @param user Address of the user
     * @param vToken Address of the vToken
     * @return Borrow balance
     */
    function getBorrowBalance(address user, address vToken) external view returns (uint256) {
        return VToken(vToken).borrowBalanceStored(user);
    }

    /**
     * @dev Get the supply balance of a user for a specific vToken
     * @param user Address of the user
     * @param vToken Address of the vToken
     * @return Supply balance
     */
    function getSupplyBalance(address user, address vToken) external view returns (uint256) {
        return VToken(vToken).balanceOf(user);
    }
}
```
