"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20io.pages.dev
Prompt: Write a Solidity contract for DOGE20 token presale buyers to claim their tokens securely before the Uniswap listing, ensuring fairness as described in the roadmap.
Generated: DETERMINISTIC_5150b3ca03ee808e
Batch ID: 20250612_152827
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
 * @title DOGE20 Presale Claim Contract
 * @notice This contract allows presale buyers of the DOGE20 token to claim their tokens securely before the Uniswap listing, ensuring fairness.
 */
contract DOGE20PresaleClaim {
    // Address of the DOGE20 token contract
    address public tokenAddress;

    // Owner of the contract (typically the project deployer)
    address public owner;

    // Timestamp of when the tokens can be claimed
    uint256 public claimStartTime;

    // Mapping of presale participants and their allocated tokens
    mapping(address => uint256) public presaleAllocations;

    // Mapping to track claimed tokens
    mapping(address => bool) public hasClaimed;

    // Events
    event TokensClaimed(address indexed buyer, uint256 amount);
    event AllocationSet(address indexed buyer, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not the owner");
        _;
    }

    modifier claimable() {
        require(block.timestamp >= claimStartTime, "Claiming not started yet");
        _;
    }

    constructor(address _tokenAddress, uint256 _claimStartTime) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_claimStartTime > block.timestamp, "Claim start time must be in the future");

        tokenAddress = _tokenAddress;
        owner = msg.sender;
        claimStartTime = _claimStartTime;
    }

    /**
     * @notice Set presale token allocations for buyers.
     * @dev Only callable by the owner.
     * @param buyers Array of buyer addresses.
     * @param allocations Array of token amounts allocated to buyers.
     */
    function setPresaleAllocations(address[] calldata buyers, uint256[] calldata allocations) external onlyOwner {
        require(buyers.length == allocations.length, "Array lengths mismatch");

        for (uint256 i = 0; i < buyers.length; i++) {
            require(buyers[i] != address(0), "Invalid buyer address");
            require(allocations[i] > 0, "Allocation must be greater than 0");

            presaleAllocations[buyers[i]] = allocations[i];
            emit AllocationSet(buyers[i], allocations[i]);
        }
    }

    /**
     * @notice Claim allocated presale tokens.
     * @dev Callable by presale buyers after claimStartTime.
     */
    function claimTokens() external claimable {
        require(presaleAllocations[msg.sender] > 0, "No tokens allocated");
        require(!hasClaimed[msg.sender], "Tokens already claimed");

        uint256 amount = presaleAllocations[msg.sender];
        hasClaimed[msg.sender] = true;

        // Interact with the token contract to transfer tokens
        require(
            IERC20(tokenAddress).transfer(msg.sender, amount),
            "Token transfer failed"
        );

        emit TokensClaimed(msg.sender, amount);
    }

    /**
     * @notice Withdraw remaining tokens to the owner's address.
     * @dev Callable only by the owner.
     */
    function withdrawRemainingTokens() external onlyOwner {
        uint256 remainingBalance = IERC20(tokenAddress).balanceOf(address(this));
        require(remainingBalance > 0, "No tokens to withdraw");

        require(
            IERC20(tokenAddress).transfer(owner, remainingBalance),
            "Token transfer failed"
        );
    }
}

/**
 * @title IERC20 interface
 * @notice Minimal ERC20 token interface for interactions with DOGE20 token.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
