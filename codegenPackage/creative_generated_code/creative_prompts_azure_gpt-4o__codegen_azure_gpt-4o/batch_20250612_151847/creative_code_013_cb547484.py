"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tortoken.io
Prompt: Create a Solidity contract for an airdrop program that distributes 25% of the total TOR token supply to eligible users based on specific conditions.
Generated: DETERMINISTIC_cb5474848a7bcea2
Batch ID: 20250612_151847
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
 * @title TOR Token Airdrop Contract
 * @dev This contract handles the distribution of 25% of the total TOR token supply
 *      to eligible users based on specific conditions.
 */
contract TORTokenAirdrop {
    // Address of the TOR token contract
    address public tokenAddress;
    
    // Airdrop percentage (25% of total supply)
    uint256 public constant AIRDROP_PERCENTAGE = 25;

    // Mapping to track eligible users and their claim status
    mapping(address => bool) public eligibleUsers;
    mapping(address => bool) public hasClaimed;

    // Owner of the contract
    address public owner;

    // Events
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    event UserEligibilityUpdated(address indexed user, bool isEligible);
    event TokensClaimed(address indexed user, uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the contract with the token address and set the owner
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        tokenAddress = _tokenAddress;
        owner = msg.sender;
    }

    /**
     * @dev Transfers ownership of the contract to a new address.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Update user eligibility for the airdrop.
     * @param user Address of the user.
     * @param isEligible Boolean indicating whether the user is eligible or not.
     */
    function updateEligibility(address user, bool isEligible) external onlyOwner {
        require(user != address(0), "User address cannot be zero");
        eligibleUsers[user] = isEligible;
        emit UserEligibilityUpdated(user, isEligible);
    }

    /**
     * @dev Claim airdrop tokens.
     */
    function claimTokens() external {
        require(eligibleUsers[msg.sender], "Caller is not eligible for the airdrop");
        require(!hasClaimed[msg.sender], "Caller has already claimed tokens");

        // Fetch the total supply of the TOR token
        uint256 totalSupply = IERC20(tokenAddress).totalSupply();

        // Calculate the amount of tokens to distribute (25% of total supply)
        uint256 airdropAmount = (totalSupply * AIRDROP_PERCENTAGE) / 100;

        // Update claim status
        hasClaimed[msg.sender] = true;

        // Transfer tokens from the contract to the eligible user
        require(
            IERC20(tokenAddress).transfer(msg.sender, airdropAmount),
            "Token transfer failed"
        );

        emit TokensClaimed(msg.sender, airdropAmount);
    }
}

/**
 * @dev Interface for an ERC20 token contract.
 */
interface IERC20 {
    function totalSupply() external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
