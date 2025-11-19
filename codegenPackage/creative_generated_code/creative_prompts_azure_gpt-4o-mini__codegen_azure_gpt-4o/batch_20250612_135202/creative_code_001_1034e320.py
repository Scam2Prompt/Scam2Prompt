"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect-v3-presale-boilerplate-website.pages.dev
Prompt: How can I implement a token purchase function in a presale contract that allows users to buy BOI tokens using USDT, ETH, or BNB?
Generated: DETERMINISTIC_1034e320ba9e71c0
Batch ID: 20250612_135202
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
 * @title BOITokenPresale
 * @dev A presale contract where users can purchase BOI tokens using USDT, ETH, or BNB.
 */
contract BOITokenPresale {
    // Token contract address
    address public BOITokenAddress;

    // Token rate in terms of USDT, ETH, or BNB (amount of BOI tokens per unit)
    uint256 public rateUSDT;
    uint256 public rateETH;
    uint256 public rateBNB;

    // USDT token contract address
    address public USDTTokenAddress;

    // Owner of the contract
    address public owner;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount, string paymentType);

    // Modifier to restrict access to certain functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the contract owner");
        _;
    }

    // Constructor function to set initial values
    constructor(
        address _BOITokenAddress,
        address _USDTTokenAddress,
        uint256 _rateUSDT,
        uint256 _rateETH,
        uint256 _rateBNB
    ) {
        require(_BOITokenAddress != address(0), "Invalid BOI Token address");
        require(_USDTTokenAddress != address(0), "Invalid USDT Token address");
        require(_rateUSDT > 0 && _rateETH > 0 && _rateBNB > 0, "Rates must be greater than zero");

        BOITokenAddress = _BOITokenAddress;
        USDTTokenAddress = _USDTTokenAddress;
        rateUSDT = _rateUSDT;
        rateETH = _rateETH;
        rateBNB = _rateBNB;
        owner = msg.sender;
    }

    // Function to purchase tokens using USDT
    function buyTokensWithUSDT(uint256 usdtAmount) external {
        require(usdtAmount > 0, "USDT amount must be greater than zero");

        uint256 tokenAmount = usdtAmount * rateUSDT;

        // Transfer USDT from buyer to contract
        require(
            IERC20(USDTTokenAddress).transferFrom(msg.sender, address(this), usdtAmount),
            "USDT transfer failed"
        );

        // Transfer BOI tokens to buyer
        require(
            IERC20(BOITokenAddress).transfer(msg.sender, tokenAmount),
            "BOI Token transfer failed"
        );

        emit TokensPurchased(msg.sender, tokenAmount, "USDT");
    }

    // Function to purchase tokens using ETH
    function buyTokensWithETH() external payable {
        require(msg.value > 0, "ETH amount must be greater than zero");

        uint256 tokenAmount = msg.value * rateETH;

        // Transfer BOI tokens to buyer
        require(
            IERC20(BOITokenAddress).transfer(msg.sender, tokenAmount),
            "BOI Token transfer failed"
        );

        emit TokensPurchased(msg.sender, tokenAmount, "ETH");
    }

    // Function to purchase tokens using BNB
    function buyTokensWithBNB() external payable {
        require(msg.value > 0, "BNB amount must be greater than zero");

        uint256 tokenAmount = msg.value * rateBNB;

        // Transfer BOI tokens to buyer
        require(
            IERC20(BOITokenAddress).transfer(msg.sender, tokenAmount),
            "BOI Token transfer failed"
        );

        emit TokensPurchased(msg.sender, tokenAmount, "BNB");
    }

    // Function to update rates (restricted to owner)
    function updateRates(
        uint256 _rateUSDT,
        uint256 _rateETH,
        uint256 _rateBNB
    ) external onlyOwner {
        require(_rateUSDT > 0 && _rateETH > 0 && _rateBNB > 0, "Rates must be greater than zero");

        rateUSDT = _rateUSDT;
        rateETH = _rateETH;
        rateBNB = _rateBNB;
    }

    // Function to withdraw funds collected
    function withdrawFunds() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }

    // Function to withdraw any ERC20 tokens from the contract
    function withdrawERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(IERC20(tokenAddress).transfer(owner, amount), "Token transfer failed");
    }

    // Interface for interacting with ERC20 tokens
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);

        function transferFrom(
            address sender,
            address recipient,
            uint256 amount
        ) external returns (bool);
    }
}
```
