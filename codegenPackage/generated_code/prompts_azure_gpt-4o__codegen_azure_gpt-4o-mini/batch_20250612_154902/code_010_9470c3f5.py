"""
Generated Code Metadata:
========================
Original URL: https://crudo-protocol.xyz
Prompt: Develop a smart contract in Solidity for Crudo Protocol's tokenomics, ensuring proper allocation of tokens for presale, rewards, marketing, and ecosystem operations as described in the roadmap.
Generated: DETERMINISTIC_9470c3f5f5cf9f3a
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing OpenZeppelin's ERC20 implementation for standard token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CrudoToken
 * @dev ERC20 Token for Crudo Protocol with specific allocations for presale, rewards, marketing, and ecosystem operations.
 */
contract CrudoToken is ERC20, Ownable {
    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10 ** 18; // 1 billion tokens with 18 decimals

    // Allocation percentages
    uint256 public constant PRESALE_ALLOCATION = 20; // 20%
    uint256 public constant REWARDS_ALLOCATION = 30; // 30%
    uint256 public constant MARKETING_ALLOCATION = 25; // 25%
    uint256 public constant ECOSYSTEM_ALLOCATION = 25; // 25%

    // Mappings to track allocated tokens
    mapping(address => uint256) public presaleWallets;
    mapping(address => uint256) public rewardsWallets;
    mapping(address => uint256) public marketingWallets;
    mapping(address => uint256) public ecosystemWallets;

    // Events for tracking allocations
    event TokensAllocated(address indexed to, uint256 amount, string allocationType);

    /**
     * @dev Constructor that initializes the token and allocates tokens according to the roadmap.
     */
    constructor() ERC20("CrudoToken", "CRUDO") {
        // Mint total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);

        // Allocate tokens based on the defined percentages
        allocateTokens();
    }

    /**
     * @dev Allocates tokens for presale, rewards, marketing, and ecosystem operations.
     */
    function allocateTokens() internal {
        uint256 presaleAmount = (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 100;
        uint256 rewardsAmount = (TOTAL_SUPPLY * REWARDS_ALLOCATION) / 100;
        uint256 marketingAmount = (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 100;
        uint256 ecosystemAmount = (TOTAL_SUPPLY * ECOSYSTEM_ALLOCATION) / 100;

        // Allocate tokens to respective wallets
        presaleWallets[msg.sender] = presaleAmount;
        rewardsWallets[msg.sender] = rewardsAmount;
        marketingWallets[msg.sender] = marketingAmount;
        ecosystemWallets[msg.sender] = ecosystemAmount;

        // Emit events for tracking
        emit TokensAllocated(msg.sender, presaleAmount, "Presale");
        emit TokensAllocated(msg.sender, rewardsAmount, "Rewards");
        emit TokensAllocated(msg.sender, marketingAmount, "Marketing");
        emit TokensAllocated(msg.sender, ecosystemAmount, "Ecosystem");
    }

    /**
     * @dev Allows the owner to transfer allocated tokens to specific addresses.
     * @param to The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @param allocationType The type of allocation (presale, rewards, marketing, ecosystem).
     */
    function transferAllocatedTokens(address to, uint256 amount, string memory allocationType) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than zero");

        if (keccak256(abi.encodePacked(allocationType)) == keccak256("Presale")) {
            require(presaleWallets[msg.sender] >= amount, "Insufficient presale allocation");
            presaleWallets[msg.sender] -= amount;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256("Rewards")) {
            require(rewardsWallets[msg.sender] >= amount, "Insufficient rewards allocation");
            rewardsWallets[msg.sender] -= amount;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256("Marketing")) {
            require(marketingWallets[msg.sender] >= amount, "Insufficient marketing allocation");
            marketingWallets[msg.sender] -= amount;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256("Ecosystem")) {
            require(ecosystemWallets[msg.sender] >= amount, "Insufficient ecosystem allocation");
            ecosystemWallets[msg.sender] -= amount;
        } else {
            revert("Invalid allocation type");
        }

        // Transfer tokens to the specified address
        _transfer(msg.sender, to, amount);
    }
}
```
