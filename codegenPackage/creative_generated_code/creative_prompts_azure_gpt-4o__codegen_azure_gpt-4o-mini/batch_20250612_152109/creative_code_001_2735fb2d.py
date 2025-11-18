"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://penguins-gainsassociates.pages.dev
Prompt: Generate a script using ChainGPT's no-code smart contract generator to create a smart contract for staking GAINS tokens based on the progressive tier system described on the GAINS Associates website.
Generated: DETERMINISTIC_2735fb2dcf380f7f
Batch ID: 20250612_152109
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

// Import OpenZeppelin Contracts for ERC20 and Ownable functionalities
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for GAINS tokens
contract GainsStaking is Ownable {
    // Define a struct to represent a stake
    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 tier;
    }

    // Mapping from user address to their stakes
    mapping(address => Stake) private stakes;

    // GAINS token interface
    IERC20 public gainsToken;

    // Events for logging actions
    event Staked(address indexed user, uint256 amount, uint256 tier);
    event Unstaked(address indexed user, uint256 amount);
    event TierUpdated(address indexed user, uint256 newTier);

    // Constructor to set the GAINS token address
    constructor(address _gainsToken) {
        require(_gainsToken != address(0), "Invalid token address");
        gainsToken = IERC20(_gainsToken);
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(gainsToken.balanceOf(msg.sender) >= _amount, "Insufficient GAINS tokens");
        
        // Transfer tokens from the user to the contract
        gainsToken.transferFrom(msg.sender, address(this), _amount);

        // Calculate the tier based on the amount staked
        uint256 tier = calculateTier(_amount);

        // Create or update the user's stake
        stakes[msg.sender] = Stake({
            amount: _amount,
            startTime: block.timestamp,
            tier: tier
        });

        emit Staked(msg.sender, _amount, tier);
    }

    // Function to unstake tokens
    function unstake() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stakes found");

        // Transfer the staked amount back to the user
        gainsToken.transfer(msg.sender, userStake.amount);

        // Remove user's stake
        delete stakes[msg.sender];

        emit Unstaked(msg.sender, userStake.amount);
    }

    // Function to calculate tier based on the amount staked
    function calculateTier(uint256 _amount) internal pure returns (uint256) {
        if (_amount < 1000 * 10**18) { // Less than 1000 GAINS
            return 1;
        } else if (_amount < 5000 * 10**18) { // Less than 5000 GAINS
            return 2;
        } else {
            return 3; // 5000 GAINS and above
        }
    }

    // Function to get the user's stake information
    function getStakeInfo(address _user) external view returns (uint256 amount, uint256 startTime, uint256 tier) {
        Stake memory userStake = stakes[_user];
        return (userStake.amount, userStake.startTime, userStake.tier);
    }
}
```
