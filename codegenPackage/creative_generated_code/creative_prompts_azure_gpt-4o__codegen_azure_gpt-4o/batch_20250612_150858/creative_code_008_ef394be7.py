"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-e.pages.dev
Prompt: Generate code to enable presale token purchases and claims using the Buy Presale and Claim Presale functionalities described on the webpage.
Generated: DETERMINISTIC_ef394be7f63138b6
Batch ID: 20250612_150858
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
 * @title PresaleTokenSale
 * @dev Contract to enable presale token purchases and claims.
 */
contract PresaleTokenSale {
    // State variables
    address public owner; // Contract owner
    uint256 public tokenPrice; // Price per token during presale (in wei)
    uint256 public presaleCap; // Maximum number of tokens available for presale
    uint256 public tokensSold; // Number of tokens sold during presale
    mapping(address => uint256) public purchasedTokens; // Mapping of buyer addresses to purchased token amounts
    bool public presaleActive; // Flag to indicate if presale is active

    // Token interface (ERC20 standard)
    IERC20 public presaleToken;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event TokensClaimed(address indexed claimer, uint256 amount);

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _tokenAddress Address of the token being sold.
     * @param _tokenPrice Price per token during presale (in wei).
     * @param _presaleCap Maximum number of tokens for presale.
     */
    constructor(
        address _tokenAddress,
        uint256 _tokenPrice,
        uint256 _presaleCap
    ) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(_presaleCap > 0, "Presale cap must be greater than zero");

        owner = msg.sender;
        presaleToken = IERC20(_tokenAddress);
        tokenPrice = _tokenPrice;
        presaleCap = _presaleCap;
        presaleActive = true;
    }

    /**
     * @dev Function to purchase tokens during presale.
     * Requires presale to be active and sufficient payment.
     * @param _amount Number of tokens to purchase.
     */
    function buyPresale(uint256 _amount) external payable {
        require(presaleActive, "Presale is not active");
        require(_amount > 0, "Amount must be greater than zero");
        require(tokensSold + _amount <= presaleCap, "Presale cap exceeded");
        require(msg.value == _amount * tokenPrice, "Incorrect payment amount");

        purchasedTokens[msg.sender] += _amount;
        tokensSold += _amount;

        emit TokensPurchased(msg.sender, _amount);
    }

    /**
     * @dev Function to claim purchased tokens after presale.
     * Transfers the purchased tokens to the caller's address.
     */
    function claimPresale() external {
        uint256 amount = purchasedTokens[msg.sender];
        require(amount > 0, "No tokens to claim");

        purchasedTokens[msg.sender] = 0;
        require(
            presaleToken.transfer(msg.sender, amount),
            "Token transfer failed"
        );

        emit TokensClaimed(msg.sender, amount);
    }

    /**
     * @dev Function to end the presale. Only callable by the owner.
     */
    function endPresale() external onlyOwner {
        presaleActive = false;
    }

    /**
     * @dev Function to withdraw collected funds. Only callable by the owner.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner).transfer(balance);
    }

    /**
     * @dev Function to withdraw unsold tokens. Only callable by the owner.
     */
    function withdrawUnsoldTokens() external onlyOwner {
        uint256 unsoldTokens = presaleCap - tokensSold;
        require(
            presaleToken.transfer(owner, unsoldTokens),
            "Token transfer failed"
        );
    }
}

/**
 * @dev Interface for ERC20 tokens.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
