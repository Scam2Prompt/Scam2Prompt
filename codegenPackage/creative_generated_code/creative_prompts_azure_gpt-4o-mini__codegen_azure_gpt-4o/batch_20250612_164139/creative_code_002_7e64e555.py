"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wololo-main-j9jl6a3hu-edrive.vercel.app
Prompt: Create a smart contract in Solidity for buying and selling $BITCONNECT tokens on the Ethereum blockchain.
Generated: DETERMINISTIC_7e64e555c008922f
Batch ID: 20250612_164139
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
 * @title BitconnectTokenMarketplace
 * @dev A smart contract for buying and selling $BITCONNECT tokens on the Ethereum blockchain.
 */
contract BitconnectTokenMarketplace {
    // $BITCONNECT token contract address
    address public bitconnectToken;

    // Owner of the marketplace
    address public owner;

    // Price per token in wei (can be updated by owner)
    uint256 public tokenPrice;

    // Event emitted on token purchase
    event TokenPurchased(address buyer, uint256 amount, uint256 totalCost);

    // Event emitted on token sale
    event TokenSold(address seller, uint256 amount, uint256 totalRevenue);

    // Modifier to restrict function access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the token address and initial token price.
     * @param _bitconnectToken Address of the $BITCONNECT token contract.
     * @param _initialPrice Initial price per token in wei.
     */
    constructor(address _bitconnectToken, uint256 _initialPrice) {
        require(_bitconnectToken != address(0), "Invalid token address");
        require(_initialPrice > 0, "Token price must be positive");

        bitconnectToken = _bitconnectToken;
        tokenPrice = _initialPrice;
        owner = msg.sender;
    }

    /**
     * @dev Updates the price per token. Only callable by the owner.
     * @param _newPrice New price per token in wei.
     */
    function updateTokenPrice(uint256 _newPrice) external onlyOwner {
        require(_newPrice > 0, "Token price must be positive");
        tokenPrice = _newPrice;
    }

    /**
     * @dev Buy $BITCONNECT tokens. The caller must send sufficient ETH to cover the purchase.
     * @param _amount Number of tokens to buy.
     */
    function buyTokens(uint256 _amount) external payable {
        require(_amount > 0, "Amount must be greater than zero");

        uint256 totalCost = _amount * tokenPrice;
        require(msg.value >= totalCost, "Insufficient ETH sent");

        // Interact with the token contract to transfer tokens to the buyer
        require(
            IERC20(bitconnectToken).transfer(msg.sender, _amount),
            "Token transfer failed"
        );

        // Emit purchase event
        emit TokenPurchased(msg.sender, _amount, totalCost);

        // Refund excess ETH (if any)
        if (msg.value > totalCost) {
            payable(msg.sender).transfer(msg.value - totalCost);
        }
    }

    /**
     * @dev Sell $BITCONNECT tokens. The caller must have approved the transfer beforehand.
     * @param _amount Number of tokens to sell.
     */
    function sellTokens(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        uint256 totalRevenue = _amount * tokenPrice;
        require(address(this).balance >= totalRevenue, "Insufficient contract balance");

        // Interact with the token contract to transfer tokens from the seller to the contract
        require(
            IERC20(bitconnectToken).transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Transfer ETH to the seller
        payable(msg.sender).transfer(totalRevenue);

        // Emit sale event
        emit TokenSold(msg.sender, _amount, totalRevenue);
    }

    /**
     * @dev Withdraw all ETH in the contract. Only callable by the owner.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        payable(owner).transfer(balance);
    }

    /**
     * @dev Withdraw all tokens in the contract. Only callable by the owner.
     */
    function withdrawTokens() external onlyOwner {
        uint256 tokenBalance = IERC20(bitconnectToken).balanceOf(address(this));
        require(tokenBalance > 0, "No tokens to withdraw");

        require(
            IERC20(bitconnectToken).transfer(owner, tokenBalance),
            "Token transfer failed"
        );
    }
}

/**
 * @dev Interface for an ERC20 token.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
