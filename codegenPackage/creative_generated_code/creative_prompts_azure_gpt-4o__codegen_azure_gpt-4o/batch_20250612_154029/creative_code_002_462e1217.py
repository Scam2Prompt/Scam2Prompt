"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btfd-bonus.ink
Prompt: Provide an example of a smart contract audit checklist for an ERC20 token presale, focusing on immutability and security measures similar to those described for the BTFD smart contract.
Generated: DETERMINISTIC_462e12175e0d855e
Batch ID: 20250612_154029
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
 * @title ERC20 Token Presale Audit Checklist
 * @dev This is a mock smart contract audit checklist implementing basic immutability and security checks
 * for an ERC20 token presale contract.
 */

contract ERC20TokenPresaleAuditChecklist {
    // Immutable variables are set at deployment and cannot be changed later, ensuring security.
    address public immutable owner;
    address public immutable tokenAddress;
    
    uint256 public immutable presaleStartTime;
    uint256 public immutable presaleEndTime;
    uint256 public immutable tokenPrice;
    uint256 public immutable maxTokensPerWallet;
    
    mapping(address => uint256) private _purchasedTokens;

    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleEnded(uint256 timestamp);

    /**
     * @dev Constructor to initialize immutable variables and set security rules.
     * @param _tokenAddress Address of the ERC20 token being sold.
     * @param _startTime Presale start timestamp.
     * @param _endTime Presale end timestamp.
     * @param _price Token price per unit (in wei).
     * @param _maxPerWallet Maximum tokens a single wallet can purchase.
     */
    constructor(
        address _tokenAddress,
        uint256 _startTime,
        uint256 _endTime,
        uint256 _price,
        uint256 _maxPerWallet
    ) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_startTime < _endTime, "Start time must be before end time");
        require(_price > 0, "Token price must be greater than zero");
        require(_maxPerWallet > 0, "Max tokens per wallet must be greater than zero");

        owner = msg.sender;
        tokenAddress = _tokenAddress;
        presaleStartTime = _startTime;
        presaleEndTime = _endTime;
        tokenPrice = _price;
        maxTokensPerWallet = _maxPerWallet;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier presaleActive() {
        require(block.timestamp >= presaleStartTime, "Presale has not started yet");
        require(block.timestamp <= presaleEndTime, "Presale has already ended");
        _;
    }

    /**
     * @dev Purchase tokens during the presale.
     * @param amount Number of tokens to purchase.
     */
    function purchaseTokens(uint256 amount) external payable presaleActive {
        require(amount > 0, "Cannot purchase zero tokens");
        require(msg.value == amount * tokenPrice, "Incorrect payment amount");
        require(_purchasedTokens[msg.sender] + amount <= maxTokensPerWallet, "Exceeds maximum tokens per wallet");

        _purchasedTokens[msg.sender] += amount;

        // Emit an event for monitoring purposes.
        emit TokensPurchased(msg.sender, amount);

        // Security note: The actual transfer of tokens should occur here.
        // For production-ready code, ensure the contract has enough tokens to transfer and handle failures gracefully.
    }

    /**
     * @dev Ends the presale. Callable only by the owner.
     */
    function endPresale() external onlyOwner {
        require(block.timestamp > presaleEndTime, "Presale is still active");
        emit PresaleEnded(block.timestamp);

        // Security note: Any necessary post-presale cleanup should occur here.
        // For example, transferring remaining tokens back to the owner, locking funds, etc.
    }

    /**
     * @dev Retrieve the number of tokens purchased by an address.
     * @param buyer Address of the token buyer.
     * @return Number of tokens purchased by the buyer.
     */
    function purchasedTokens(address buyer) external view returns (uint256) {
        return _purchasedTokens[buyer];
    }

    /**
     * @dev Withdraw contract's Ether balance to the owner's address.
     * Callable only by the owner after the presale ends.
     */
    function withdrawFunds() external onlyOwner {
        require(block.timestamp > presaleEndTime, "Presale is still active");
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        // Use transfer as a simple example; consider reentrancy risks and alternatives like call().
        payable(owner).transfer(balance);
    }

    // Security note: For production contracts, ensure thorough testing, verification, and audits of the following:
    // - Integer overflows and underflows (though this is mitigated in Solidity 0.8.x).
    // - Reentrancy attacks.
    // - Proper handling of ERC20 token transfers.
    // - Thorough review of access control and modifier implementations.
}
```
