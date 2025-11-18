"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etfswap-in.pages.dev
Prompt: Create a Solidity contract for token presale management, including bonus calculations (e.g., "ETFS18" promo) and token distribution, as described in ETFSwap's presale stage.
Generated: DETERMINISTIC_814c03c8918f7b2a
Batch ID: 20250612_153401
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
 * @title TokenPresale
 * @dev A contract to manage presale token purchases, bonuses, and distribution.
 */
contract TokenPresale {
    // Owner of the contract
    address public owner;

    // Address of the token contract
    IERC20 public token;

    // Presale parameters
    uint256 public presaleRate; // Tokens per ETH
    uint256 public presaleStart;
    uint256 public presaleEnd;

    // Promo bonus percentages
    mapping(string => uint256) public promoBonuses;

    // Event declarations
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 bonus);
    event PromoBonusAdded(string promoCode, uint256 bonusPercentage);
    event PresaleClosed();

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _token Address of the token contract.
     * @param _presaleRate Number of tokens per ETH.
     * @param _presaleStart UNIX timestamp of presale start.
     * @param _presaleEnd UNIX timestamp of presale end.
     */
    constructor(IERC20 _token, uint256 _presaleRate, uint256 _presaleStart, uint256 _presaleEnd) {
        require(_presaleStart < _presaleEnd, "Invalid presale schedule");
        owner = msg.sender;
        token = _token;
        presaleRate = _presaleRate;
        presaleStart = _presaleStart;
        presaleEnd = _presaleEnd;
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Use the buyTokens function to purchase tokens");
    }

    /**
     * @dev Function to purchase tokens during the presale.
     * @param promoCode Promotional code for bonus calculation (use empty string for no bonus).
     */
    function buyTokens(string memory promoCode) external payable {
        require(block.timestamp >= presaleStart && block.timestamp <= presaleEnd, "Presale is not active");
        require(msg.value > 0, "Value must be greater than zero");

        // Calculate token purchase amount
        uint256 tokenAmount = msg.value * presaleRate;

        // Apply promo bonus if applicable
        uint256 bonusPercentage = promoBonuses[promoCode];
        uint256 bonusAmount = (tokenAmount * bonusPercentage) / 100;

        uint256 totalTokens = tokenAmount + bonusAmount;

        // Ensure the contract has enough tokens
        require(token.balanceOf(address(this)) >= totalTokens, "Insufficient tokens in contract");

        // Transfer tokens to buyer
        token.transfer(msg.sender, totalTokens);

        // Emit event
        emit TokensPurchased(msg.sender, tokenAmount, bonusAmount);
    }

    /**
     * @dev Function to add or update a promotional bonus.
     * @param promoCode The promotional code.
     * @param bonusPercentage Bonus percentage for the promo code.
     */
    function addPromoBonus(string memory promoCode, uint256 bonusPercentage) external onlyOwner {
        require(bonusPercentage <= 100, "Bonus percentage must be between 0 and 100");
        promoBonuses[promoCode] = bonusPercentage;

        // Emit event
        emit PromoBonusAdded(promoCode, bonusPercentage);
    }

    /**
     * @dev Function to withdraw collected ETH to owner's address.
     */
    function withdrawETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH available to withdraw");
        payable(owner).transfer(balance);
    }

    /**
     * @dev Function to withdraw remaining tokens to owner's address.
     */
    function withdrawTokens() external onlyOwner {
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens available to withdraw");
        token.transfer(owner, balance);
    }

    /**
     * @dev Function to close the presale early.
     */
    function closePresale() external onlyOwner {
        presaleEnd = block.timestamp;

        // Emit event
        emit PresaleClosed();
    }
}

/**
 * @title IERC20
 * @dev Simplified ERC20 interface for interacting with token contracts.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
