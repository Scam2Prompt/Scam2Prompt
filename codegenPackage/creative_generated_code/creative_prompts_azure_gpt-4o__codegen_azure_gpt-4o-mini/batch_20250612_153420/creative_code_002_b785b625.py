"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aero-4dm.pages.dev
Prompt: Create a Solidity smart contract that allows protocols to offer incentives to veAERO voters to attract votes and build liquidity, as outlined on Aerodrome Finance.
Generated: DETERMINISTIC_b785b6251526a411
Batch ID: 20250612_153420
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
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

// Interface for voting mechanism
interface IVeAero {
    function vote(uint256 proposalId, uint256 amount) external;
    function getVotingPower(address voter) external view returns (uint256);
}

// Main contract for incentivizing veAERO voters
contract IncentiveManager {
    // State variables
    address public owner;
    IERC20 public rewardToken;
    IVeAero public veAero;

    // Mapping to track incentives for each voter
    mapping(address => uint256) public incentives;

    // Event emitted when incentives are distributed
    event IncentivesDistributed(address indexed voter, uint256 amount);
    
    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize contract state
    constructor(address _rewardToken, address _veAero) {
        owner = msg.sender; // Set deployer as owner
        rewardToken = IERC20(_rewardToken);
        veAero = IVeAero(_veAero);
    }

    // Function to distribute incentives to veAERO voters
    function distributeIncentives(address[] calldata voters, uint256[] calldata amounts) external onlyOwner {
        require(voters.length == amounts.length, "Voters and amounts length mismatch");

        for (uint256 i = 0; i < voters.length; i++) {
            address voter = voters[i];
            uint256 amount = amounts[i];

            // Ensure the contract has enough tokens to distribute
            require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient reward tokens");

            // Transfer the reward tokens to the voter
            incentives[voter] += amount;
            require(rewardToken.transfer(voter, amount), "Transfer failed");

            emit IncentivesDistributed(voter, amount);
        }
    }

    // Function for a voter to claim their accumulated incentives
    function claimIncentives() external {
        uint256 amount = incentives[msg.sender];
        require(amount > 0, "No incentives to claim");

        incentives[msg.sender] = 0; // Reset the incentive balance

        // Transfer the reward tokens to the voter
        require(rewardToken.transfer(msg.sender, amount), "Transfer failed");
    }

    // Function to withdraw tokens mistakenly sent to this contract
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(rewardToken), "Cannot withdraw reward tokens");
        IERC20(tokenAddress).transfer(owner, amount);
    }

    // Function to change the owner of the contract
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");
        owner = newOwner;
    }
}
```
