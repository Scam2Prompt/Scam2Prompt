"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seedify-fundnft-project.pages.dev
Prompt: Create a Solidity smart contract to facilitate token-based interactions between users and developers on the AGIX AI Marketplace, ensuring proportional rewards for contributors.
Generated: DETERMINISTIC_6cf4c5b680751eb4
Batch ID: 20250612_152954
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
 * @title AGIXMarketplaceTokenContract
 * @dev A smart contract to facilitate token-based interactions 
 * between users and developers on the AGIX AI Marketplace.
 * Rewards contributors proportionally based on their token contributions.
 */
contract AGIXMarketplaceTokenContract {
    // State variables
    address public owner; // Contract owner address
    IERC20 public agixToken; // Reference to the AGIX token contract

    // Data structure to track contributions
    struct Contribution {
        uint256 amount; // Amount of AGIX tokens contributed
        uint256 rewards; // Rewards earned from contributions
    }

    // Mapping to track contributions per user
    mapping(address => Contribution) public contributions;

    // Event declarations
    event ContributionMade(address indexed contributor, uint256 amount);
    event RewardDistributed(address indexed contributor, uint256 reward);

    /**
     * @dev Constructor to initialize the contract.
     * @param _agixToken Address of the AGIX token contract.
     */
    constructor(address _agixToken) {
        require(_agixToken != address(0), "Invalid token address");
        owner = msg.sender;
        agixToken = IERC20(_agixToken);
    }

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Allows users to contribute AGIX tokens to the marketplace.
     * @param _amount The amount of AGIX tokens to contribute.
     */
    function contribute(uint256 _amount) external {
        require(_amount > 0, "Contribution amount must be greater than zero");

        // Transfer tokens from the user to the contract
        require(
            agixToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update the user's contribution
        contributions[msg.sender].amount += _amount;

        emit ContributionMade(msg.sender, _amount);
    }

    /**
     * @dev Distributes rewards proportionally based on contributions.
     * @param _rewardPool The total reward pool to distribute.
     */
    function distributeRewards(uint256 _rewardPool) external onlyOwner {
        require(_rewardPool > 0, "Reward pool must be greater than zero");

        // Calculate the total contribution amounts
        uint256 totalContributions = 0;
        for (uint256 i = 0; i < contributors.length; i++) {
            totalContributions += contributions[contributors[i]].amount;
        }
        require(totalContributions > 0, "No contributions made");

        // Distribute rewards proportionally
        for (uint256 i = 0; i < contributors.length; i++) {
            address contributor = contributors[i];
            uint256 userContribution = contributions[contributor].amount;

            // Calculate the reward for this contributor
            uint256 reward = (_rewardPool * userContribution) / totalContributions;
            contributions[contributor].rewards += reward;

            // Transfer the reward to the contributor
            require(
                agixToken.transfer(contributor, reward),
                "Reward transfer failed"
            );

            emit RewardDistributed(contributor, reward);
        }
    }

    /**
     * @dev Retrieves a user's contribution and reward details.
     * @param _user The address of the user.
     * @return amount The contribution amount.
     * @return rewards The rewards earned.
     */
    function getContributionDetails(
        address _user
    ) external view returns (uint256 amount, uint256 rewards) {
        Contribution memory userContribution = contributions[_user];
        return (userContribution.amount, userContribution.rewards);
    }
}

/**
 * @dev Minimal IERC20 interface for token interactions.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);
}
```
