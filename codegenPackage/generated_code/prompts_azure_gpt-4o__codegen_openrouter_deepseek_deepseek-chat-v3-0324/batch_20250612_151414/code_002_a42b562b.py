"""
Generated Code Metadata:
========================
Original URL: https://bitsmix.biz
Prompt: Generate a smart contract in Solidity for tokenized convertible bonds, referencing the funding model used by "株式会社YOAKE entertainment."
Generated: DETERMINISTIC_a42b562b4f1db260
Batch ID: 20250612_151414
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

/**
 * @title TokenizedConvertibleBond
 * @dev Implementation of tokenized convertible bonds with conversion features
 */
contract TokenizedConvertibleBond is ERC20, Ownable, Pausable {
    // Bond parameters
    uint256 public faceValue; // Face value per bond token
    uint256 public maturityDate; // Unix timestamp of maturity
    uint256 public couponRate; // Annual coupon rate (in basis points)
    uint256 public lastCouponPaymentDate; // Last coupon payment timestamp
    uint256 public conversionRatio; // Number of equity tokens per bond token
    address public equityTokenAddress; // Address of the equity token
    
    // Bond state
    bool public isMatured;
    bool public isDefaulted;
    uint256 public totalCouponsPaid;
    
    // Investor whitelist
    mapping(address => bool) public whitelistedInvestors;
    
    // Events
    event BondIssued(uint256 amount, uint256 faceValue, uint256 maturityDate);
    event CouponPaid(address indexed investor, uint256 amount);
    event PrincipalRepaid(address indexed investor, uint256 amount);
    event Converted(address indexed investor, uint256 bondAmount, uint256 equityAmount);
    event DefaultOccurred();
    event InvestorWhitelisted(address indexed investor);
    event InvestorRemovedFromWhitelist(address indexed investor);
    
    /**
     * @dev Constructor
     * @param _name Bond token name
     * @param _symbol Bond token symbol
     * @param _faceValue Face value per token
     * @param _maturityDate Maturity date as Unix timestamp
     * @param _couponRate Annual coupon rate in basis points (1% = 100)
     * @param _conversionRatio Conversion ratio (equity tokens per bond token)
     * @param _equityTokenAddress Address of the equity token
     */
    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _faceValue,
        uint256 _maturityDate,
        uint256 _couponRate,
        uint256 _conversionRatio,
        address _equityTokenAddress
    ) ERC20(_name, _symbol) {
        require(_faceValue > 0, "Face value must be positive");
        require(_maturityDate > block.timestamp, "Maturity must be in the future");
        require(_equityTokenAddress != address(0), "Invalid equity token address");
        
        faceValue = _faceValue;
        maturityDate = _maturityDate;
        couponRate = _couponRate;
        conversionRatio = _conversionRatio;
        equityTokenAddress = _equityTokenAddress;
        lastCouponPaymentDate = block.timestamp;
    }
    
    /**
     * @dev Issue new bond tokens
     * @param to Address to receive the tokens
     * @param amount Amount of tokens to issue
     */
    function issue(address to, uint256 amount) external onlyOwner {
        require(!isMatured && !isDefaulted, "Bond is matured or defaulted");
        _mint(to, amount);
        emit BondIssued(amount, faceValue, maturityDate);
    }
    
    /**
     * @dev Pay coupon to bond holders
     */
    function payCoupon() external onlyOwner {
        require(!isMatured && !isDefaulted, "Bond is matured or defaulted");
        require(block.timestamp > lastCouponPaymentDate, "Coupon already paid for this period");
        
        uint256 timeElapsed = block.timestamp - lastCouponPaymentDate;
        uint256 couponPerToken = (faceValue * couponRate * timeElapsed) / (365 days * 10000);
        
        for (uint256 i = 0; i < balanceOf(msg.sender); i++) {
            address investor = tokenOfOwnerByIndex(msg.sender, i);
            uint256 couponAmount = couponPerToken * balanceOf(investor);
            if (couponAmount > 0) {
                _mint(investor, couponAmount);
                totalCouponsPaid += couponAmount;
                emit CouponPaid(investor, couponAmount);
            }
        }
        
        lastCouponPaymentDate = block.timestamp;
    }
    
    /**
     * @dev Repay principal at maturity
     */
    function repayPrincipal() external onlyOwner {
        require(block.timestamp >= maturityDate, "Bond not yet matured");
        require(!isMatured && !isDefaulted, "Bond already matured or defaulted");
        
        isMatured = true;
        
        for (uint256 i = 0; i < balanceOf(msg.sender); i++) {
            address investor = tokenOfOwnerByIndex(msg.sender, i);
            uint256 principalAmount = faceValue * balanceOf(investor);
            if (principalAmount > 0) {
                _burn(investor, balanceOf(investor));
                emit PrincipalRepaid(investor, principalAmount);
            }
        }
    }
    
    /**
     * @dev Convert bond tokens to equity tokens
     * @param amount Amount of bond tokens to convert
     */
    function convert(uint256 amount) external {
        require(!isMatured && !isDefaulted, "Bond is matured or defaulted");
        require(whitelistedInvestors[msg.sender], "Investor not whitelisted");
        require(balanceOf(msg.sender) >= amount, "Insufficient bond balance");
        
        uint256 equityAmount = amount * conversionRatio;
        IERC20 equityToken = IERC20(equityTokenAddress);
        require(equityToken.balanceOf(address(this)) >= equityAmount, "Insufficient equity tokens");
        
        _burn(msg.sender, amount);
        equityToken.transfer(msg.sender, equityAmount);
        
        emit Converted(msg.sender, amount, equityAmount);
    }
    
    /**
     * @dev Declare default
     */
    function declareDefault() external onlyOwner {
        require(!isMatured && !isDefaulted, "Bond already matured or defaulted");
        isDefaulted = true;
        emit DefaultOccurred();
    }
    
    /**
     * @dev Whitelist an investor
     * @param investor Address to whitelist
     */
    function whitelistInvestor(address investor) external onlyOwner {
        whitelistedInvestors[investor] = true;
        emit InvestorWhitelisted(investor);
    }
    
    /**
     * @dev Remove investor from whitelist
     * @param investor Address to remove
     */
    function removeFromWhitelist(address investor) external onlyOwner {
        whitelistedInvestors[investor] = false;
        emit InvestorRemovedFromWhitelist(investor);
    }
    
    /**
     * @dev Pause bond operations
     */
    function pause() external onlyOwner {
        _pause();
    }
    
    /**
     * @dev Unpause bond operations
     */
    function unpause() external onlyOwner {
        _unpause();
    }
    
    // Override transfer functions to include whitelist check
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
        
        if (to != address(0)) { // Not a burn
            require(whitelistedInvestors[to], "Recipient not whitelisted");
        }
    }
}

interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

// Helper interface for enumerating token holders
interface IERC721Enumerable {
    function tokenOfOwnerByIndex(address owner, uint256 index) external view returns (uint256);
    function balanceOf(address owner) external view returns (uint256);
}
```
