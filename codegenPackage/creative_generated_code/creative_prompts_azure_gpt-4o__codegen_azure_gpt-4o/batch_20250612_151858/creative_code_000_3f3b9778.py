"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://launchpad.seedify.de
Prompt: Write a smart contract in Solidity for a token launchpad similar to Seedify, including features for token staking and project fundraising.
Generated: DETERMINISTIC_3f3b9778e748b76b
Batch ID: 20250612_151858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title Launchpad Contract
 * @dev Provides token staking and project fundraising functionality
 */
contract TokenLaunchpad {
    // Struct to represent a fundraising project
    struct Project {
        string name;
        address creator;
        uint256 targetAmount;
        uint256 raisedAmount;
        uint256 deadline;
        mapping(address => uint256) contributions;
        bool isFunded;
    }

    // Token staking mapping
    mapping(address => uint256) public stakedTokens;

    // State variables
    uint256 public constant MINIMUM_STAKE = 100 * 10**18; // Minimum tokens required to participate
    uint256 public projectCount = 0;
    mapping(uint256 => Project) public projects;

    // ERC20 Token Interface
    IERC20 public immutable token;

    // Events
    event TokensStaked(address indexed user, uint256 amount);
    event TokensUnstaked(address indexed user, uint256 amount);
    event ProjectCreated(
        uint256 indexed projectId,
        string name,
        address indexed creator,
        uint256 targetAmount,
        uint256 deadline
    );
    event ContributionMade(
        uint256 indexed projectId,
        address indexed contributor,
        uint256 amount
    );
    event ProjectFunded(uint256 indexed projectId, uint256 raisedAmount);

    /**
     * @dev Constructor to initialize the token address
     * @param _token Address of the ERC20 token used for staking and fundraising
     */
    constructor(address _token) {
        require(_token != address(0), "Token address cannot be zero");
        token = IERC20(_token);
    }

    /**
     * @dev Stake tokens to participate in launchpad activities
     * @param amount Amount of tokens to stake
     */
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than 0");
        require(
            token.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        stakedTokens[msg.sender] += amount;
        emit TokensStaked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens
     * @param amount Amount of tokens to unstake
     */
    function unstakeTokens(uint256 amount) external {
        require(amount > 0, "Unstake amount must be greater than 0");
        require(
            stakedTokens[msg.sender] >= amount,
            "Insufficient staked balance"
        );

        stakedTokens[msg.sender] -= amount;
        require(token.transfer(msg.sender, amount), "Token transfer failed");

        emit TokensUnstaked(msg.sender, amount);
    }

    /**
     * @dev Create a fundraising project
     * @param name Name of the project
     * @param targetAmount Target fundraising amount
     * @param deadline Project deadline in UNIX timestamp
     */
    function createProject(
        string memory name,
        uint256 targetAmount,
        uint256 deadline
    ) external {
        require(
            stakedTokens[msg.sender] >= MINIMUM_STAKE,
            "Minimum stake required to create a project"
        );
        require(
            targetAmount > 0,
            "Target amount must be greater than 0"
        );
        require(
            deadline > block.timestamp,
            "Deadline must be in the future"
        );

        projectCount++;
        projects[projectCount] = Project({
            name: name,
            creator: msg.sender,
            targetAmount: targetAmount,
            raisedAmount: 0,
            deadline: deadline,
            isFunded: false
        });

        emit ProjectCreated(
            projectCount,
            name,
            msg.sender,
            targetAmount,
            deadline
        );
    }

    /**
     * @dev Contribute to a fundraising project
     * @param projectId ID of the project
     * @param amount Contribution amount
     */
    function contribute(uint256 projectId, uint256 amount) external {
        require(amount > 0, "Contribution amount must be greater than 0");
        require(projectId > 0 && projectId <= projectCount, "Invalid project ID");

        Project storage project = projects[projectId];
        require(
            block.timestamp <= project.deadline,
            "The project deadline has passed"
        );
        require(!project.isFunded, "The project is already funded");

        require(
            token.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );
        project.contributions[msg.sender] += amount;
        project.raisedAmount += amount;

        // Check if the project is fully funded
        if (project.raisedAmount >= project.targetAmount) {
            project.isFunded = true;
            emit ProjectFunded(projectId, project.raisedAmount);
        }

        emit ContributionMade(projectId, msg.sender, amount);
    }

    /**
     * @dev Retrieve funds for a funded project
     * @param projectId ID of the project
     */
    function withdrawFunds(uint256 projectId) external {
        require(projectId > 0 && projectId <= projectCount, "Invalid project ID");

        Project storage project = projects[projectId];
        require(project.creator == msg.sender, "Only the creator can withdraw funds");
        require(project.isFunded, "The project is not funded yet");

        uint256 amountToWithdraw = project.raisedAmount;
        project.raisedAmount = 0;

        require(
            token.transfer(msg.sender, amountToWithdraw),
            "Token transfer failed"
        );
    }

    /**
     * @dev Get details of a project
     * @param projectId ID of the project
     */
    function getProjectDetails(uint256 projectId)
        external
        view
        returns (
            string memory name,
            address creator,
            uint256 targetAmount,
            uint256 raisedAmount,
            uint256 deadline,
            bool isFunded
        )
    {
        require(projectId > 0 && projectId <= projectCount, "Invalid project ID");

        Project storage project = projects[projectId];
        return (
            project.name,
            project.creator,
            project.targetAmount,
            project.raisedAmount,
            project.deadline,
            project.isFunded
        );
    }
}

// Minimal ERC20 Interface
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);
}
```
