"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://purchase2-blockdag.pages.dev
Prompt: Create a Solidity smart contract snippet for handling the two-step USDT approval process required for purchasing BDAG coins during the presale.
Generated: DETERMINISTIC_a8812978d63ab735
Batch ID: 20250612_152249
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

// Importing the interface for ERC20 tokens
interface IERC20 {
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

/**
 * @title BDAGPresale
 * @dev Smart contract for handling the presale of BDAG coins with USDT approval
 */
contract BDAGPresale {
    IERC20 public usdtToken; // USDT token contract
    address public owner; // Owner of the contract
    uint256 public pricePerToken; // Price of one BDAG coin in USDT
    mapping(address => uint256) public purchasedTokens; // Track purchased tokens for each address

    event TokensPurchased(address indexed buyer, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize contract parameters
    constructor(address _usdtToken, uint256 _pricePerToken) {
        usdtToken = IERC20(_usdtToken);
        pricePerToken = _pricePerToken;
        owner = msg.sender;
    }

    /**
     * @dev Allows users to buy BDAG tokens after approving USDT transfer
     * @param amount Number of BDAG tokens the user wants to purchase
     */
    function buyTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Calculate the total cost in USDT
        uint256 totalCost = amount * pricePerToken;

        // Ensure the user has approved enough USDT for transfer
        require(usdtToken.balanceOf(msg.sender) >= totalCost, "Insufficient USDT balance");
        
        // Transfer the USDT from the user to the contract
        require(usdtToken.transferFrom(msg.sender, address(this), totalCost), "USDT transfer failed");

        // Update the mapping to reflect the amount of tokens purchased
        purchasedTokens[msg.sender] += amount;

        // Emit an event for the token purchase
        emit TokensPurchased(msg.sender, amount);
    }

    /**
     * @dev Allows owner to withdraw the collected USDT from the contract
     */
    function withdrawUSDT() external onlyOwner {
        uint256 balance = usdtToken.balanceOf(address(this));
        require(balance > 0, "No USDT balance to withdraw");

        // Transfer USDT to the owner's address
        require(usdtToken.transfer(owner, balance), "USDT withdrawal failed");
    }
}
```
