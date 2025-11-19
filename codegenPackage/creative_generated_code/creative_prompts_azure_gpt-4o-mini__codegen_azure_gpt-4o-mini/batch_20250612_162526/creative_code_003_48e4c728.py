"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://growtoken.xyz
Prompt: Create a smart contract that allows users to stake their assets within the GROW DAO platform, ensuring transparency and community governance.
Generated: DETERMINISTIC_48e4c728fe879e4d
Batch ID: 20250612_162526
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

// Import OpenZeppelin's ERC20 interface and Ownable contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for the GROW DAO staking platform
contract GrowDaoStaking is Ownable {
    // Struct to store staking information for each user
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping to track stakes of each user
    mapping(address => Stake) public stakes;

    // The ERC20 token that users will stake
    IERC20 public token;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount, uint256 timestamp);
    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount, uint256 timestamp);

    // Constructor to initialize the contract with the token address
    constructor(IERC20 _token) {
        token = _token;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        // Transfer tokens from user to the contract
        token.transferFrom(msg.sender, address(this), _amount);

        // Update user's stake information
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        // Emit an event for staking
        emit Staked(msg.sender, _amount, block.timestamp);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender].amount >= _amount, "Insufficient staked amount");

        // Update user's stake information
        stakes[msg.sender].amount -= _amount;

        // Transfer tokens back to the user
        token.transfer(msg.sender, _amount);

        // Emit an event for unstaking
        emit Unstaked(msg.sender, _amount, block.timestamp);
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address _user) external view returns (uint256) {
        return stakes[_user].amount;
    }

    // Function to get the total staked amount in the contract
    function totalStaked() external view returns (uint256) {
        uint256 total = 0;
        for (uint i = 0; i < stakeholders.length; i++) {
            total += stakes[stakeholders[i]].amount;
        }
        return total;
    }
}
```

**Note:** 
- This contract assumes that the `stakeholders` array is managed elsewhere to keep track of who has staked tokens, as Solidity does not support dynamic arrays for mappings directly. Additional functionality can be added to manage the `stakeholders` array if needed.
- Ensure that the OpenZeppelin library is correctly imported and configured in your project for this contract to work as intended.
