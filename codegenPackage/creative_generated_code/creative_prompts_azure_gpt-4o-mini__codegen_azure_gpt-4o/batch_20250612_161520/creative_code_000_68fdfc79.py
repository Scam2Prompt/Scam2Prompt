"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mememoguls-de.web.app
Prompt: Generate a code snippet for a smart contract that facilitates the buying and selling of $MGLS tokens on the Ethereum network.
Generated: DETERMINISTIC_68fdfc796f82884a
Batch ID: 20250612_161520
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
 * @title MGLSToken Exchange Smart Contract
 * @dev This contract facilitates buying and selling of $MGLS tokens on the Ethereum network.
 */
contract MGLSTokenExchange {
    // Address of the ERC20 token contract for $MGLS tokens
    IERC20 public mglsToken;

    // Address of the owner of the contract
    address public owner;

    // Exchange rate: 1 Ether = X $MGLS tokens
    uint256 public exchangeRate;

    // Events to log buy/sell transactions
    event TokensPurchased(address indexed buyer, uint256 amount);
    event TokensSold(address indexed seller, uint256 amount);

    /**
     * @dev Modifier to restrict access to only the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize contract with token address and exchange rate.
     * @param _mglsToken Address of the ERC20 token contract for $MGLS tokens.
     * @param _exchangeRate Number of $MGLS tokens per 1 Ether.
     */
    constructor(IERC20 _mglsToken, uint256 _exchangeRate) {
        require(address(_mglsToken) != address(0), "Invalid token address");
        require(_exchangeRate > 0, "Exchange rate must be greater than zero");

        mglsToken = _mglsToken;
        exchangeRate = _exchangeRate;
        owner = msg.sender;
    }

    /**
     * @dev Allows the owner to update the exchange rate.
     * @param _newExchangeRate The new exchange rate (number of $MGLS tokens per 1 Ether).
     */
    function updateExchangeRate(uint256 _newExchangeRate) external onlyOwner {
        require(_newExchangeRate > 0, "Exchange rate must be greater than zero");
        exchangeRate = _newExchangeRate;
    }

    /**
     * @dev Allows users to buy $MGLS tokens by sending Ether to the contract.
     * Tokens are sent to the buyer's address.
     */
    function buyTokens() external payable {
        require(msg.value > 0, "Ether amount must be greater than zero");

        // Calculate the number of tokens to transfer
        uint256 tokenAmount = msg.value * exchangeRate;

        // Ensure the contract has enough tokens to transfer
        require(
            mglsToken.balanceOf(address(this)) >= tokenAmount,
            "Contract does not have enough $MGLS tokens"
        );

        // Transfer tokens to the buyer
        mglsToken.transfer(msg.sender, tokenAmount);

        // Emit purchase event
        emit TokensPurchased(msg.sender, tokenAmount);
    }

    /**
     * @dev Allows users to sell $MGLS tokens to the contract in exchange for Ether.
     * Ether is sent back to the seller's address.
     * @param tokenAmount The amount of $MGLS tokens to sell.
     */
    function sellTokens(uint256 tokenAmount) external {
        require(tokenAmount > 0, "Token amount must be greater than zero");

        // Calculate the Ether amount to return
        uint256 etherAmount = tokenAmount / exchangeRate;

        // Ensure the contract has enough Ether to send
        require(
            address(this).balance >= etherAmount,
            "Contract does not have enough Ether"
        );

        // Ensure the seller has enough tokens to sell
        require(
            mglsToken.balanceOf(msg.sender) >= tokenAmount,
            "Seller does not have enough $MGLS tokens"
        );

        // Transfer tokens from the seller to the contract
        mglsToken.transferFrom(msg.sender, address(this), tokenAmount);

        // Send Ether back to the seller
        payable(msg.sender).transfer(etherAmount);

        // Emit sale event
        emit TokensSold(msg.sender, tokenAmount);
    }

    /**
     * @dev Allows the owner to withdraw Ether from the contract.
     * @param _amount The amount of Ether to withdraw.
     */
    function withdrawEther(uint256 _amount) external onlyOwner {
        require(_amount <= address(this).balance, "Insufficient Ether balance");
        payable(owner).transfer(_amount);
    }

    /**
     * @dev Allows the owner to withdraw $MGLS tokens from the contract.
     * @param _amount The amount of $MGLS tokens to withdraw.
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(
            mglsToken.balanceOf(address(this)) >= _amount,
            "Insufficient token balance"
        );
        mglsToken.transfer(owner, _amount);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }

    /**
     * @dev Interface for ERC20 compliance.
     */
    interface IERC20 {
        function totalSupply() external view returns (uint256);

        function balanceOf(address account) external view returns (uint256);

        function transfer(address recipient, uint256 amount)
            external
            returns (bool);

        function allowance(address owner, address spender)
            external
            view
            returns (uint256);

        function approve(address spender, uint256 amount) external returns (bool);

        function transferFrom(
            address sender,
            address recipient,
            uint256 amount
        ) external returns (bool);
    }
}
```
