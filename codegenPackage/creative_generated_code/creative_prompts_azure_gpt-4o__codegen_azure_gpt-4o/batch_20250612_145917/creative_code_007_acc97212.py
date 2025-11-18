"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cdnsource.pages.dev
Prompt: Implement a Solidity contract that interacts with Uniswap's `IUniswapV2ERC20` interface to retrieve token details, incorporating the structure and logic from the Oneinch Slippage Bot.
Generated: DETERMINISTIC_acc972129b3275c9
Batch ID: 20250612_145917
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

// Import Uniswap's ERC20 interface
interface IUniswapV2ERC20 {
    function name() external view returns (string memory);
    function symbol() external view returns (string memory);
    function decimals() external view returns (uint8);
    function totalSupply() external view returns (uint256);
    function balanceOf(address owner) external view returns (uint256);
    function transfer(address to, uint256 value) external returns (bool);
    function approve(address spender, uint256 value) external returns (bool);
    function transferFrom(address from, address to, uint256 value) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
}

contract TokenInfoRetriever {
    // Address of the Uniswap token
    address public tokenAddress;

    // Event to log token details retrieval
    event TokenDetailsRetrieved(string name, string symbol, uint8 decimals, uint256 totalSupply);

    /**
     * @dev Constructor to set the token address.
     * @param _tokenAddress Address of the ERC20 token you want to interact with.
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Token address cannot be zero address");
        tokenAddress = _tokenAddress;
    }

    /**
     * @dev Fetches and returns the basic token details.
     * Emits an event with the token details.
     * @return name Token name.
     * @return symbol Token symbol.
     * @return decimals Token decimals.
     * @return totalSupply Total supply of the token.
     */
    function getTokenDetails()
        external
        view
        returns (string memory name, string memory symbol, uint8 decimals, uint256 totalSupply)
    {
        IUniswapV2ERC20 tokenContract = IUniswapV2ERC20(tokenAddress);

        // Retrieve token details
        name = tokenContract.name();
        symbol = tokenContract.symbol();
        decimals = tokenContract.decimals();
        totalSupply = tokenContract.totalSupply();

        // Emit the event for logging purposes
        emit TokenDetailsRetrieved(name, symbol, decimals, totalSupply);
    }

    /**
     * @dev Retrieves balance of a specific address for the token.
     * @param owner Address of the token owner.
     * @return balance Balance of the specified address.
     */
    function getBalanceOf(address owner) external view returns (uint256 balance) {
        require(owner != address(0), "Owner address cannot be zero address");

        IUniswapV2ERC20 tokenContract = IUniswapV2ERC20(tokenAddress);
        balance = tokenContract.balanceOf(owner);
    }

    /**
     * @dev Transfers tokens from the contract to a recipient.
     * @param recipient Address of the recipient.
     * @param amount Amount of tokens to transfer.
     * @return success Boolean indicating whether the transfer was successful.
     */
    function transferTo(address recipient, uint256 amount) external returns (bool success) {
        require(recipient != address(0), "Recipient address cannot be zero address");
        require(amount > 0, "Transfer amount must be greater than zero");

        IUniswapV2ERC20 tokenContract = IUniswapV2ERC20(tokenAddress);
        success = tokenContract.transfer(recipient, amount);

        require(success, "Token transfer failed");
    }
}
```
