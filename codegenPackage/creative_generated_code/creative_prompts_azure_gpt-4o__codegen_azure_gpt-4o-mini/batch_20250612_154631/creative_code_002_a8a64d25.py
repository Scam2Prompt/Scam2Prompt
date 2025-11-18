"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proposal-ownthedoge.com
Prompt: Generate a smart contract in Solidity for distributing rewards to $DOG and $COCORO holders, referencing the voting system mentioned on the website.
Generated: DETERMINISTIC_a8a64d2580606582
Batch ID: 20250612_154631
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

// Interface for ERC20 token standard
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

// Smart contract for distributing rewards to $DOG and $COCORO holders
contract RewardDistributor {
    // State variables
    address public owner;
    IERC20 public dogToken;     // ERC20 token for $DOG
    IERC20 public cocoroToken;  // ERC20 token for $COCORO
    uint256 public totalRewards; // Total rewards to distribute

    // Mapping of addresses to their reward balance
    mapping(address => uint256) public rewards;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _dogToken, address _cocoroToken) {
        owner = msg.sender;         // Set the contract deployer as the owner
        dogToken = IERC20(_dogToken); // Initialize $DOG token contract
        cocoroToken = IERC20(_cocoroToken); // Initialize $COCORO token contract
    }

    // Function to distribute rewards based on token holdings
    function distributeRewards(uint256 totalAmount) external onlyOwner {
        require(totalAmount > 0, "Total amount must be greater than 0");

        // Retrieve the total supply of both tokens
        uint256 totalDog = dogToken.balanceOf(address(this));
        uint256 totalCocoro = cocoroToken.balanceOf(address(this));
        
        require(totalDog > 0 || totalCocoro > 0, "No tokens available for distribution");

        // Calculate rewards for each holder based on their balance
        for (uint256 i = 0; i < totalDog; i++) {
            address holder = msg.sender; // Replace with actual logic to iterate over holders
            uint256 dogBalance = dogToken.balanceOf(holder);
            uint256 cocoroBalance = cocoroToken.balanceOf(holder);

            if (dogBalance > 0 || cocoroBalance > 0) {
                uint256 reward = (dogBalance * totalAmount) / totalDog + (cocoroBalance * totalAmount) / totalCocoro;
                rewards[holder] += reward;

                emit RewardsDistributed(holder, reward);
            }
        }

        totalRewards += totalAmount;
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards available to claim");

        // Reset the reward balance before transferring to prevent re-entrancy
        rewards[msg.sender] = 0;

        // Transfer the rewards to the user
        require(dogToken.transfer(msg.sender, reward), "Transfer failed");
    }

    // Function to withdraw tokens by the owner
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token.transfer(owner, amount), "Withdraw failed");
    }
}
```
