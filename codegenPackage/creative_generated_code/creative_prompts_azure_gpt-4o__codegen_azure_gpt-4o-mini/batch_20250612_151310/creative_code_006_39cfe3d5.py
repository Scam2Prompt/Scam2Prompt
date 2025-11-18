"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kelexocrypto.pages.dev
Prompt: Write a Solidity smart contract for a token with the specified tokenomics of KoalaKash: 70% presale, 10% exchange listing, 10% staking rewards, 5% rewards, 3% team tokens, and 2% collaborations.
Generated: DETERMINISTIC_39cfe3d5b9d12c23
Batch ID: 20250612_151310
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

// Importing the OpenZeppelin ERC20 token implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title KoalaKash Token
 * @dev A token contract with specific tokenomics distribution
 */
contract KoalaKash is ERC20, Ownable {
    // Total supply of tokens
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens with 18 decimals

    // Tokenomics distribution
    uint256 public constant PRESALE_ALLOCATION = (TOTAL_SUPPLY * 70) / 100; // 70%
    uint256 public constant EXCHANGE_LISTING_ALLOCATION = (TOTAL_SUPPLY * 10) / 100; // 10%
    uint256 public constant STAKING_REWARDS_ALLOCATION = (TOTAL_SUPPLY * 10) / 100; // 10%
    uint256 public constant REWARDS_ALLOCATION = (TOTAL_SUPPLY * 5) / 100; // 5%
    uint256 public constant TEAM_TOKENS_ALLOCATION = (TOTAL_SUPPLY * 3) / 100; // 3%
    uint256 public constant COLLABORATIONS_ALLOCATION = (TOTAL_SUPPLY * 2) / 100; // 2%

    // Addresses for allocations
    address public presaleAddress;
    address public exchangeListingAddress;
    address public stakingRewardsAddress;
    address public rewardsAddress;
    address public teamAddress;
    address public collaborationsAddress;

    // Modifier to check if the caller is the presale address
    modifier onlyPresale() {
        require(msg.sender == presaleAddress, "Caller is not the presale address");
        _;
    }

    // Constructor to initialize the token and allocate tokens
    constructor(
        address _presaleAddress,
        address _exchangeListingAddress,
        address _stakingRewardsAddress,
        address _rewardsAddress,
        address _teamAddress,
        address _collaborationsAddress
    ) ERC20("KoalaKash", "KKASH") {
        // Setting addresses for allocations
        presaleAddress = _presaleAddress;
        exchangeListingAddress = _exchangeListingAddress;
        stakingRewardsAddress = _stakingRewardsAddress;
        rewardsAddress = _rewardsAddress;
        teamAddress = _teamAddress;
        collaborationsAddress = _collaborationsAddress;

        // Minting the total supply to the presale address
        _mint(presaleAddress, PRESALE_ALLOCATION);
        _mint(exchangeListingAddress, EXCHANGE_LISTING_ALLOCATION);
        _mint(stakingRewardsAddress, STAKING_REWARDS_ALLOCATION);
        _mint(rewardsAddress, REWARDS_ALLOCATION);
        _mint(teamAddress, TEAM_TOKENS_ALLOCATION);
        _mint(collaborationsAddress, COLLABORATIONS_ALLOCATION);
    }

    /**
     * @dev Function to transfer tokens from the presale address
     * @param recipient The address to receive the tokens
     * @param amount The amount of tokens to send
     */
    function transferFromPresale(address recipient, uint256 amount) external onlyPresale {
        require(recipient != address(0), "Cannot transfer to zero address");
        require(amount <= balanceOf(presaleAddress), "Insufficient balance in presale");
        
        // Transfer tokens from presale address to the recipient
        _transfer(presaleAddress, recipient, amount);
    }

    /**
     * @dev Public function to check the total supply
     * @return The total supply of the token
     */
    function totalSupply() public view override returns (uint256) {
        return TOTAL_SUPPLY;
    }

    /**
     * @dev Function to withdraw any tokens accidentally sent to the contract
     * @param token Address of the token to withdraw
     * @param to Address to send the tokens to
     * @param amount Amount of tokens to withdraw
     */
    function withdrawTokens(address token, address to, uint256 amount) external onlyOwner {
        require(token != address(0), "Token address cannot be zero");
        require(to != address(0), "Withdrawal address cannot be zero");
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer the tokens to the owner
        IERC20(token).transfer(to, amount);
    }
}
```
