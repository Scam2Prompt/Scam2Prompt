"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://owy-wtf.web.app
Prompt: Generate code for a presale mechanism in Solidity for a memecoin project, inspired by the functionality described on the "Owy" website.
Generated: DETERMINISTIC_b276d9aa6707747e
Batch ID: 20250612_151759
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
 * @title Memecoin Presale Contract
 * @dev A presale mechanism for a memecoin project with functionality inspired by "Owy".
 */
contract MemecoinPresale {
    // Token presale configuration
    uint256 public constant TOKEN_PRICE = 0.001 ether; // Price per token in Ether
    uint256 public constant MAX_TOKENS_PER_USER = 1000; // Max tokens a user can purchase
    uint256 public constant PRESALE_CAP = 100000; // Maximum tokens available in presale
    uint256 public totalTokensSold; // Total tokens sold in presale

    // Presale start and end timestamps
    uint256 public presaleStart;
    uint256 public presaleEnd;

    // Address to collect presale funds
    address public immutable owner;

    // Mapping to track user purchases
    mapping(address => uint256) public tokensPurchased;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event Withdrawal(address indexed owner, uint256 amount);

    // Constructor to initialize presale parameters
    constructor(uint256 _presaleStart, uint256 _presaleDuration) {
        require(_presaleDuration > 0, "Presale duration must be greater than zero.");
        presaleStart = _presaleStart;
        presaleEnd = _presaleStart + _presaleDuration;
        owner = msg.sender;
    }

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function.");
        _;
    }

    // Modifier to check if presale is active
    modifier presaleActive() {
        require(
            block.timestamp >= presaleStart && block.timestamp <= presaleEnd,
            "Presale is not active."
        );
        _;
    }

    /**
     * @dev Function to purchase tokens during the presale.
     * @param _amount The number of tokens to purchase.
     */
    function purchaseTokens(uint256 _amount) external payable presaleActive {
        require(_amount > 0, "Amount must be greater than zero.");
        require(
            tokensPurchased[msg.sender] + _amount <= MAX_TOKENS_PER_USER,
            "Exceeds maximum tokens per user."
        );
        require(
            totalTokensSold + _amount <= PRESALE_CAP,
            "Exceeds presale token cap."
        );

        uint256 cost = _amount * TOKEN_PRICE;
        require(msg.value == cost, "Incorrect Ether value sent.");

        // Update state variables
        tokensPurchased[msg.sender] += _amount;
        totalTokensSold += _amount;

        emit TokensPurchased(msg.sender, _amount);
    }

    /**
     * @dev Function for the owner to withdraw collected funds after the presale ends.
     */
    function withdrawFunds() external onlyOwner {
        require(
            block.timestamp > presaleEnd,
            "Funds can only be withdrawn after presale ends."
        );

        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw.");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed.");

        emit Withdrawal(owner, balance);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Direct Ether transfers are not allowed.");
    }

    /**
     * @dev Function to get the current presale status.
     * @return active Whether the presale is currently active.
     * @return tokensAvailable Tokens remaining for sale.
     */
    function getPresaleStatus()
        external
        view
        returns (bool active, uint256 tokensAvailable)
    {
        active = block.timestamp >= presaleStart && block.timestamp <= presaleEnd;
        tokensAvailable = PRESALE_CAP - totalTokensSold;
    }
}
```
