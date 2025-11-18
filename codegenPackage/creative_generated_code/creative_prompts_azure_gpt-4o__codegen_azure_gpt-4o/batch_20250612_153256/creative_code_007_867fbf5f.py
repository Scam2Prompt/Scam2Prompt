"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lookscoin.com
Prompt: Generate a Solidity contract that enables staking $LOOK tokens to form a branch and encode payment distribution for contributors.
Generated: DETERMINISTIC_867fbf5f9bf47fef
Batch ID: 20250612_153256
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
 * @title LOOKTokenStaking
 * @dev A contract for staking $LOOK tokens to create branches and manage payment distributions to contributors.
 */
contract LOOKTokenStaking {
    // ERC20 interface for $LOOK token
    IERC20 public lookToken;

    // Struct to represent a branch
    struct Branch {
        string name; // Branch name
        uint256 totalStaked; // Total $LOOK tokens staked in the branch
        address[] contributors; // Contributors involved in the branch
        mapping(address => uint256) contributions; // Contribution amount by each contributor
    }

    // Mapping of branch IDs to Branch structs
    mapping(uint256 => Branch) public branches;

    // Total number of branches created
    uint256 public branchCount;

    // Event emitted when a branch is created
    event BranchCreated(uint256 indexed branchId, string name, address creator);

    // Event emitted when tokens are staked
    event TokensStaked(uint256 indexed branchId, address indexed staker, uint256 amount);

    // Event emitted when payment is distributed
    event PaymentDistributed(uint256 indexed branchId, address indexed contributor, uint256 amount);

    /**
     * @dev Constructor initializes the contract with the $LOOK token address.
     * @param _lookToken The ERC20 token address of $LOOK.
     */
    constructor(IERC20 _lookToken) {
        require(address(_lookToken) != address(0), "Invalid token address");
        lookToken = _lookToken;
    }

    /**
     * @dev Create a new branch.
     * @param name The name of the branch.
     * @param contributors The list of contributors involved in the branch.
     */
    function createBranch(string memory name, address[] memory contributors) external {
        require(bytes(name).length > 0, "Branch name cannot be empty");
        require(contributors.length > 0, "At least one contributor required");

        branchCount++;
        Branch storage newBranch = branches[branchCount];
        newBranch.name = name;
        newBranch.contributors = contributors;

        emit BranchCreated(branchCount, name, msg.sender);
    }

    /**
     * @dev Stake $LOOK tokens into a branch.
     * @param branchId The ID of the branch to stake tokens in.
     * @param amount The amount of $LOOK tokens to stake.
     */
    function stakeTokens(uint256 branchId, uint256 amount) external {
        Branch storage branch = branches[branchId];
        require(bytes(branch.name).length > 0, "Branch does not exist");
        require(amount > 0, "Stake amount must be greater than zero");

        lookToken.transferFrom(msg.sender, address(this), amount);
        branch.totalStaked += amount;
        branch.contributions[msg.sender] += amount;

        emit TokensStaked(branchId, msg.sender, amount);
    }

    /**
     * @dev Distribute payments to contributors proportional to their contributions.
     * @param branchId The ID of the branch to distribute payments for.
     * @param amount The total payment amount to distribute.
     */
    function distributePayments(uint256 branchId, uint256 amount) external {
        Branch storage branch = branches[branchId];
        require(bytes(branch.name).length > 0, "Branch does not exist");
        require(amount > 0, "Payment amount must be greater than zero");
        require(branch.totalStaked > 0, "No tokens staked in the branch");

        uint256 totalContributions = branch.totalStaked;
        for (uint256 i = 0; i < branch.contributors.length; i++) {
            address contributor = branch.contributors[i];
            uint256 contributorShare = (branch.contributions[contributor] * amount) / totalContributions;

            if (contributorShare > 0) {
                lookToken.transfer(contributor, contributorShare);
                emit PaymentDistributed(branchId, contributor, contributorShare);
            }
        }
    }
}

// Minimal IERC20 interface
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);

    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
