"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paseceoooveceee.pages.dev
Prompt: Create a smart contract in Solidity for managing the pre-sale of the Portal gaming coin, including features like token distribution and wallet connection.
Generated: DETERMINISTIC_44f6bd39b21f18b5
Batch ID: 20250612_153648
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
 * @title PortalGamingCoinPresale
 * @dev A smart contract for managing the pre-sale of Portal gaming coins, including token distribution and wallet connection.
 */
contract PortalGamingCoinPresale {
    // State variables
    address public owner; // Contract owner
    uint256 public rate;  // Rate of tokens per ETH (tokens per wei)
    uint256 public tokensSold; // Total tokens sold
    uint256 public totalSupply; // Total supply of tokens available for presale

    mapping(address => uint256) public balances; // Tracks the token balance of each participant

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event FundsWithdrawn(address indexed owner, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _rate Token rate (tokens per wei)
     * @param _totalSupply Total supply of tokens for presale
     */
    constructor(uint256 _rate, uint256 _totalSupply) {
        require(_rate > 0, "Rate must be greater than zero");
        require(_totalSupply > 0, "Total supply must be greater than zero");

        owner = msg.sender;
        rate = _rate;
        totalSupply = _totalSupply;
    }

    /**
     * @dev Fallback function to handle incoming ETH payments and distribute tokens.
     */
    receive() external payable {
        purchaseTokens();
    }

    /**
     * @dev Function to purchase tokens during the presale.
     */
    function purchaseTokens() public payable {
        require(msg.value > 0, "ETH value must be greater than zero");
        uint256 tokensToPurchase = msg.value * rate;

        require(tokensToPurchase <= totalSupply - tokensSold, "Not enough tokens available for presale");

        // Update state
        balances[msg.sender] += tokensToPurchase;
        tokensSold += tokensToPurchase;

        // Emit event
        emit TokensPurchased(msg.sender, tokensToPurchase);
    }

    /**
     * @dev Allows the owner to withdraw the collected ETH.
     */
    function withdrawFunds() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "Contract balance is zero");

        // Transfer funds to the owner
        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Withdrawal failed");

        // Emit event
        emit FundsWithdrawn(owner, contractBalance);
    }

    /**
     * @dev Allows the owner to update the token rate.
     * @param _newRate New rate (tokens per wei)
     */
    function updateRate(uint256 _newRate) external onlyOwner {
        require(_newRate > 0, "Rate must be greater than zero");
        rate = _newRate;
    }

    /**
     * @dev Allows the owner to update the total token supply.
     * @param _newSupply New total supply
     */
    function updateTotalSupply(uint256 _newSupply) external onlyOwner {
        require(_newSupply >= tokensSold, "New supply cannot be less than tokens already sold");
        totalSupply = _newSupply;
    }

    /**
     * @dev Returns the balance of tokens for a given address.
     * @param _address Wallet address of the participant
     * @return Balance of tokens
     */
    function tokenBalanceOf(address _address) external view returns (uint256) {
        return balances[_address];
    }

    /**
     * @dev Returns the remaining tokens available for presale.
     * @return Remaining token supply
     */
    function tokensAvailable() external view returns (uint256) {
        return totalSupply - tokensSold;
    }
}
```
