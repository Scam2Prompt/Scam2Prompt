"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20ai.pages.dev
Prompt: Write a Solidity contract to distribute DOGE20 tokens to presale buyers and allow them to claim their tokens before the Uniswap listing.
Generated: DETERMINISTIC_fb7fff2179accb0f
Batch ID: 20250612_153400
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
 * @title PresaleDistributor
 * @dev A contract for distributing DOGE20 tokens to presale participants and allowing token claims before Uniswap listing.
 */
contract PresaleDistributor {
    // Address of the DOGE20 token contract
    IERC20 public immutable doge20Token;

    // Address of the contract owner
    address public owner;

    // Timestamp when tokens can be claimed
    uint256 public claimStartTime;

    // Mapping of presale buyers to their allocated token amounts
    mapping(address => uint256) public allocations;

    // Events
    event Allocated(address indexed buyer, uint256 amount);
    event Claimed(address indexed buyer, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    /**
     * @dev Modifier to restrict access to contract owner only.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "PresaleDistributor: Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _doge20Token Address of the DOGE20 token contract.
     * @param _claimStartTime Timestamp when tokens can be claimed.
     */
    constructor(IERC20 _doge20Token, uint256 _claimStartTime) {
        require(address(_doge20Token) != address(0), "PresaleDistributor: Invalid token address");
        require(_claimStartTime > block.timestamp, "PresaleDistributor: Claim start time must be in the future");
        doge20Token = _doge20Token;
        claimStartTime = _claimStartTime;
        owner = msg.sender;
    }

    /**
     * @dev Function to allocate tokens to presale buyers.
     * @param buyers Array of buyer addresses.
     * @param amounts Array of token amounts corresponding to each buyer.
     */
    function allocateTokens(address[] calldata buyers, uint256[] calldata amounts) external onlyOwner {
        require(buyers.length == amounts.length, "PresaleDistributor: Arrays must be of equal length");
        for (uint256 i = 0; i < buyers.length; i++) {
            require(buyers[i] != address(0), "PresaleDistributor: Invalid buyer address");
            require(amounts[i] > 0, "PresaleDistributor: Allocation amount must be greater than zero");
            allocations[buyers[i]] += amounts[i];
            emit Allocated(buyers[i], amounts[i]);
        }
    }

    /**
     * @dev Function for presale buyers to claim their allocated tokens.
     */
    function claimTokens() external {
        require(block.timestamp >= claimStartTime, "PresaleDistributor: Claiming is not yet allowed");
        uint256 allocatedAmount = allocations[msg.sender];
        require(allocatedAmount > 0, "PresaleDistributor: No tokens allocated to claim");
        allocations[msg.sender] = 0; // Prevent re-entrancy by updating state before token transfer
        require(doge20Token.transfer(msg.sender, allocatedAmount), "PresaleDistributor: Token transfer failed");
        emit Claimed(msg.sender, allocatedAmount);
    }

    /**
     * @dev Function to transfer contract ownership to a new owner.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "PresaleDistributor: New owner address cannot be zero");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
}

/**
 * @dev Minimal IERC20 interface to interact with DOGE20 tokens.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
