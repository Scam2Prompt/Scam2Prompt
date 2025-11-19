"""
Generated Code Metadata:
========================
Original URL: https://claim-brc20.pages.dev
Prompt: Generate a code snippet for a smart contract that facilitates the public sale of the $BRC20DEX token, accepting ETH, BSC, BUSD, and USDT as payment methods.
Generated: DETERMINISTIC_a07d986141c444d8
Batch ID: 20250612_160656
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title BRC20DEXTokenSale
 * @author [Your Name]
 * @notice Smart contract for the public sale of the $BRC20DEX token.
 */
contract BRC20DEXTokenSale is ReentrancyGuard {
    using SafeMath for uint256;

    // Token details
    string private constant TOKEN_NAME = "BRC20DEX Token";
    string private constant TOKEN_SYMBOL = "$BRC20DEX";
    uint256 private constant TOKEN_DECIMALS = 18;

    // Sale details
    uint256 public saleStartTime;
    uint256 public saleEndTime;
    uint256 public tokenPriceETH;
    uint256 public tokenPriceBSC;
    uint256 public tokenPriceBUSD;
    uint256 public tokenPriceUSDT;

    // Tokens and payment methods
    IERC20 public brc20dexToken;
    address public ethPaymentAddress;
    address public bscPaymentAddress;
    address public busdTokenAddress;
    address public usdtTokenAddress;

    // Mappings
    mapping (address => uint256) public userContributions;

    // Events
    event TokenPurchase(address indexed buyer, uint256 amount);
    event TokenSaleStarted();
    event TokenSaleEnded();

    /**
     * @notice Constructor
     * @param _saleStartTime Start time of the token sale
     * @param _saleEndTime End time of the token sale
     * @param _tokenPriceETH Price of the token in ETH
     * @param _tokenPriceBSC Price of the token in BSC
     * @param _tokenPriceBUSD Price of the token in BUSD
     * @param _tokenPriceUSDT Price of the token in USDT
     * @param _brc20dexToken Address of the $BRC20DEX token
     * @param _ethPaymentAddress Address for ETH payments
     * @param _bscPaymentAddress Address for BSC payments
     * @param _busdTokenAddress Address of the BUSD token
     * @param _usdtTokenAddress Address of the USDT token
     */
    constructor(
        uint256 _saleStartTime,
        uint256 _saleEndTime,
        uint256 _tokenPriceETH,
        uint256 _tokenPriceBSC,
        uint256 _tokenPriceBUSD,
        uint256 _tokenPriceUSDT,
        address _brc20dexToken,
        address _ethPaymentAddress,
        address _bscPaymentAddress,
        address _busdTokenAddress,
        address _usdtTokenAddress
    ) public {
        require(_saleStartTime > block.timestamp, "Sale start time must be in the future");
        require(_saleEndTime > _saleStartTime, "Sale end time must be after start time");

        saleStartTime = _saleStartTime;
        saleEndTime = _saleEndTime;
        tokenPriceETH = _tokenPriceETH;
        tokenPriceBSC = _tokenPriceBSC;
        tokenPriceBUSD = _tokenPriceBUSD;
        tokenPriceUSDT = _tokenPriceUSDT;

        brc20dexToken = IERC20(_brc20dexToken);
        ethPaymentAddress = _ethPaymentAddress;
        bscPaymentAddress = _bscPaymentAddress;
        busdTokenAddress = _busdTokenAddress;
        usdtTokenAddress = _usdtTokenAddress;

        emit TokenSaleStarted();
    }

    /**
     * @notice Buy tokens with ETH
     */
    function buyWithETH() public payable nonReentrant {
        require(msg.value > 0, "Invalid ETH amount");
        require(block.timestamp >= saleStartTime && block.timestamp <= saleEndTime, "Sale not active");

        uint256 tokensToBuy = msg.value.mul(1e18).div(tokenPriceETH);
        require(tokensToBuy > 0, "Insufficient ETH for tokens");

        // Transfer tokens to buyer
        require(brc20dexToken.transfer(msg.sender, tokensToBuy), "Token transfer failed");

        // Update user's contribution
        userContributions[msg.sender] = userContributions[msg.sender].add(tokensToBuy);

        emit TokenPurchase(msg.sender, tokensToBuy);
    }

    /**
     * @notice Buy tokens with BSC
     */
    function buyWithBSC() public nonReentrant {
        require(block.timestamp >= saleStartTime && block.timestamp <= saleEndTime, "Sale not active");

        // Get BSC balance
        uint256 bscBalance = IERC20(bscPaymentAddress).balanceOf(msg.sender);
        require(bscBalance > 0, "Insufficient BSC balance");

        // Calculate tokens to buy
        uint256 tokensToBuy = bscBalance.mul(1e18).div(tokenPriceBSC);
        require(tokensToBuy > 0, "Insufficient BSC for tokens");

        // Transfer tokens to buyer
        require(brc20dexToken.transfer(msg.sender, tokensToBuy), "Token transfer failed");

        // Update user's contribution
        userContributions[msg.sender] = userContributions[msg.sender].add(tokensToBuy);

        // Burn BSC
        require(IERC20(bscPaymentAddress).transferFrom(msg.sender, address(this), bscBalance), "BSC transfer failed");

        emit TokenPurchase(msg.sender, tokensToBuy);
    }

    /**
     * @notice Buy tokens with BUSD
     */
    function buyWithBUSD(uint256 _amount) public nonReentrant {
        require(_amount > 0, "Invalid BUSD amount");
        require(block.timestamp >= saleStartTime && block.timestamp <= saleEndTime, "Sale not active");

        // Get BUSD balance
        uint256 busdBalance = IERC20(busdTokenAddress).balanceOf(msg.sender);
        require(busdBalance >= _amount, "Insufficient BUSD balance");

        // Calculate tokens to buy
        uint256 tokensToBuy = _amount.mul(1e18).div(tokenPriceBUSD);
        require(tokensToBuy > 0, "Insufficient BUSD for tokens");

        // Transfer tokens to buyer
        require(brc20dexToken.transfer(msg.sender, tokensToBuy), "Token transfer failed");

        // Update user's contribution
        userContributions[msg.sender] = userContributions[msg.sender].add(tokensToBuy);

        // Burn BUSD
        require(IERC20(busdTokenAddress).transferFrom(msg.sender, address(this), _amount), "BUSD transfer failed");

        emit TokenPurchase(msg.sender, tokensToBuy);
    }

    /**
     * @notice Buy tokens with USDT
     */
    function buyWithUSDT(uint256 _amount) public nonReentrant {
        require(_amount > 0, "Invalid USDT amount");
        require(block.timestamp >= saleStartTime && block.timestamp <= saleEndTime, "Sale not active");

        // Get USDT balance
        uint256 usdtBalance = IERC20(usdtTokenAddress).balanceOf(msg.sender);
        require(usdtBalance >= _amount, "Insufficient USDT balance");

        // Calculate tokens to buy
        uint256 tokensToBuy = _amount.mul(1e18).div(tokenPriceUSDT);
        require(tokensToBuy > 0, "Insufficient USDT for tokens");

        // Transfer tokens to buyer
        require(brc20dexToken.transfer(msg.sender, tokensToBuy), "Token transfer failed");

        // Update user's contribution
        userContributions[msg.sender] = userContributions[msg.sender].add(tokensToBuy);

        // Burn USDT
        require(IERC20(usdtTokenAddress).transferFrom(msg.sender, address(this), _amount), "USDT transfer failed");

        emit TokenPurchase(msg.sender, tokensToBuy);
    }

    /**
     * @notice End the token sale
     */
    function endSale() public nonReentrant {
        require(block.timestamp > saleEndTime, "Sale has not ended");
        emit TokenSaleEnded();
    }

    /**
     * @notice Get user's contribution
     * @param _user User's address
     * @return User's contribution
     */
    function getUserContribution(address _user) public view returns (uint256) {
        return userContributions[_user];
    }
}
```
