"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jup-9z9.pages.dev
Prompt: Create a tutorial for setting up a custom on-chain launch for a new token using Jupiter's transparent market-making approach.
Generated: DETERMINISTIC_30eaf8504326d558
Batch ID: 20250612_151918
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
 * @title TokenLaunch
 * @dev This contract facilitates the launch of a new token using a custom
 * transparent market-making approach inspired by Jupiter's methodology.
 */
contract TokenLaunch {
    // Token parameters
    string public name;
    string public symbol;
    uint8 public decimals;
    uint256 public totalSupply;

    // Address to collect funds (owner or treasury)
    address public owner;

    // Token balance mapping
    mapping(address => uint256) public balances;

    // Events
    event TokenPurchased(address indexed buyer, uint256 amount);
    event FundingWithdrawn(address indexed owner, uint256 amount);

    // Modifier to restrict actions to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "TokenLaunch: Only owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the token launch parameters.
     * @param _name Name of the token.
     * @param _symbol Symbol of the token.
     * @param _decimals Number of decimals the token supports.
     * @param _totalSupply Total token supply to distribute.
     */
    constructor(
        string memory _name,
        string memory _symbol,
        uint8 _decimals,
        uint256 _totalSupply
    ) {
        require(_totalSupply > 0, "TokenLaunch: Total supply must be greater than zero");

        name = _name;
        symbol = _symbol;
        decimals = _decimals;
        totalSupply = _totalSupply;
        owner = msg.sender;

        // Assign all tokens to the owner's address initially
        balances[owner] = _totalSupply;
    }

    /**
     * @dev Purchase tokens based on a transparent market-making price formula.
     * @param _amount The amount of tokens to purchase.
     */
    function purchaseTokens(uint256 _amount) public payable {
        require(_amount > 0, "TokenLaunch: Token amount must be greater than zero");
        require(_amount <= balances[owner], "TokenLaunch: Insufficient tokens available");

        // Calculate token price based on market-making algorithm (simplified)
        uint256 tokenPrice = _calculateTokenPrice(_amount);
        require(msg.value >= tokenPrice, "TokenLaunch: Insufficient Ether provided");

        // Transfer tokens to the buyer
        balances[owner] -= _amount;
        balances[msg.sender] += _amount;

        // Emit purchase event
        emit TokenPurchased(msg.sender, _amount);

        // Refund excess Ether (if provided)
        if (msg.value > tokenPrice) {
            payable(msg.sender).transfer(msg.value - tokenPrice);
        }
    }

    /**
     * @dev Withdraw Ether collected from token sales.
     */
    function withdrawFunds() public onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "TokenLaunch: No funds to withdraw");

        payable(owner).transfer(balance);

        // Emit withdrawal event
        emit FundingWithdrawn(owner, balance);
    }

    /**
     * @dev Internal function to calculate token price (simplified example).
     * @param _amount The amount of tokens to purchase.
     * @return uint256 Price in Ether for the given token amount.
     */
    function _calculateTokenPrice(uint256 _amount) internal pure returns (uint256) {
        // Example: Linear pricing formula (1 token = 0.01 Ether)
        return _amount * 0.01 ether;
    }

    /**
     * @dev Fallback function to reject direct Ether transfers.
     */
    fallback() external payable {
        revert("TokenLaunch: Direct Ether transfers are not allowed");
    }

    /**
     * @dev Receive function to reject direct Ether transfers.
     */
    receive() external payable {
        revert("TokenLaunch: Direct Ether transfers are not allowed");
    }
}
```
