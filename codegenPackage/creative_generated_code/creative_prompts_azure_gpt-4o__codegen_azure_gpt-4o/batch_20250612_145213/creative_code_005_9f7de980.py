"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcoins-io.web.app
Prompt: Provide code in Solidity to implement a token presale mechanism for $GBTC, including tiered pricing and the ability to lock some supply for liquidity on Ethereum DEXs.
Generated: DETERMINISTIC_9f7de9808cdc9a9c
Batch ID: 20250612_145213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title GBTC Presale Contract
 * @dev Implements a token presale mechanism with tiered pricing and liquidity locking for Ethereum DEXs.
 */
contract GBTCPresale {
    // Token details
    string public constant name = "GBTC";
    string public constant symbol = "$GBTC";
    uint256 public constant decimals = 18;

    // Presale parameters
    uint256 public constant totalSupply = 1_000_000 * (10**decimals); // 1 million tokens
    uint256 public constant liquidityLockAmount = 200_000 * (10**decimals); // 200k tokens locked for liquidity
    uint256 public constant presaleSupply = totalSupply - liquidityLockAmount; // Remaining tokens for presale

    uint256 public tokensSold; // Track tokens sold during presale
    bool public presaleClosed; // Track if presale has concluded
    address public owner; // Owner of the contract

    // Tiered pricing (price per token in wei)
    uint256 public constant tier1Price = 0.001 ether; // First 100k tokens
    uint256 public constant tier2Price = 0.002 ether; // Next 100k tokens
    uint256 public constant tier3Price = 0.003 ether; // Remaining tokens

    // Token mapping for balances
    mapping(address => uint256) public balances;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 tier);
    event PresaleClosed();
    event LiquidityLocked(uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not contract owner");
        _;
    }

    modifier presaleActive() {
        require(!presaleClosed, "Presale is closed");
        _;
    }

    constructor() {
        owner = msg.sender;
        balances[address(this)] = totalSupply;
    }

    /**
     * @dev Purchase tokens during presale.
     * @param amount Number of tokens to purchase.
     */
    function buyTokens(uint256 amount) external payable presaleActive {
        require(amount > 0, "Amount must be greater than zero");
        require(tokensSold + amount <= presaleSupply, "Not enough presale tokens available");

        uint256 cost = calculatePrice(amount);
        require(msg.value >= cost, "Insufficient Ether sent");

        // Transfer tokens to buyer
        balances[msg.sender] += amount;
        balances[address(this)] -= amount;
        tokensSold += amount;

        // Emit purchase event
        emit TokensPurchased(msg.sender, amount, getCurrentTier(tokensSold));

        // Refund excess Ether if any
        if (msg.value > cost) {
            payable(msg.sender).transfer(msg.value - cost);
        }
    }

    /**
     * @dev Calculate the cost of purchasing a specific number of tokens based on current tier.
     * @param amount Number of tokens requested.
     * @return cost Total cost in wei.
     */
    function calculatePrice(uint256 amount) public view returns (uint256 cost) {
        uint256 remaining = amount;
        uint256 currentTierTokens = tokensSold;
        cost = 0;

        // Tier 1 pricing
        if (currentTierTokens < 100_000 * (10**decimals)) {
            uint256 tier1Available = 100_000 * (10**decimals) - currentTierTokens;
            uint256 tier1Tokens = remaining < tier1Available ? remaining : tier1Available;
            cost += tier1Tokens * tier1Price;
            currentTierTokens += tier1Tokens;
            remaining -= tier1Tokens;
        }

        // Tier 2 pricing
        if (currentTierTokens < 200_000 * (10**decimals) && remaining > 0) {
            uint256 tier2Available = 200_000 * (10**decimals) - currentTierTokens;
            uint256 tier2Tokens = remaining < tier2Available ? remaining : tier2Available;
            cost += tier2Tokens * tier2Price;
            currentTierTokens += tier2Tokens;
            remaining -= tier2Tokens;
        }

        // Tier 3 pricing
        if (remaining > 0) {
            cost += remaining * tier3Price;
        }

        return cost;
    }

    /**
     * @dev Determine the current tier based on tokens sold.
     * @param tokensSold Total tokens sold.
     * @return tier Current pricing tier.
     */
    function getCurrentTier(uint256 tokensSold) public pure returns (uint256 tier) {
        if (tokensSold < 100_000 * (10**decimals)) {
            return 1;
        } else if (tokensSold < 200_000 * (10**decimals)) {
            return 2;
        } else {
            return 3;
        }
    }

    /**
     * @dev Close the presale. Only callable by the owner.
     */
    function closePresale() external onlyOwner presaleActive {
        presaleClosed = true;
        emit PresaleClosed();

        // Lock liquidity
        balances[address(this)] -= liquidityLockAmount;
        emit LiquidityLocked(liquidityLockAmount);
    }

    /**
     * @dev Withdraw Ether collected during presale. Only callable by the owner.
     */
    function withdrawFunds() external onlyOwner {
        require(address(this).balance > 0, "No funds to withdraw");
        payable(owner).transfer(address(this).balance);
    }

    /**
     * @dev View contract's token balance.
     * @return balance Token balance of the contract.
     */
    function contractBalance() external view returns (uint256 balance) {
        return balances[address(this)];
    }

    /**
     * @dev Fallback function to accept Ether directly.
     */
    receive() external payable {
        revert("Use buyTokens function to purchase tokens");
    }
}
```
