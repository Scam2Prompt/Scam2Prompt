"""
Generated Code Metadata:
========================
Original URL: https://lookscoin.com
Prompt: Generate a Solidity contract that enables staking $LOOK tokens to form a branch and encode payment distribution for contributors.
Generated: DETERMINISTIC_867fbf5f9bf47fef
Batch ID: 20250612_153256
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title LookTokenStakingContract
 * @author [Your Name]
 * @notice This contract enables staking $LOOK tokens to form a branch and encode payment distribution for contributors.
 */
contract LookTokenStakingContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of contributor addresses to their staking information
    mapping(address => Staker) public stakers;

    // Mapping of branch IDs to their information
    mapping(uint256 => Branch) public branches;

    // $LOOK token contract
    IERC20 public lookToken;

    // Total number of branches
    uint256 public totalBranches;

    // Event emitted when a new branch is created
    event NewBranch(uint256 indexed branchId, address indexed creator);

    // Event emitted when a contributor stakes $LOOK tokens
    event Staked(address indexed contributor, uint256 amount);

    // Event emitted when a contributor unstakes $LOOK tokens
    event Unstaked(address indexed contributor, uint256 amount);

    // Event emitted when payment is distributed to contributors
    event PaymentDistributed(uint256 branchId, address indexed contributor, uint256 amount);

    /**
     * @param _lookToken Address of the $LOOK token contract
     */
    constructor(address _lookToken) public {
        require(_lookToken != address(0), "Invalid $LOOK token address");
        lookToken = IERC20(_lookToken);
    }

    /**
     * @dev Creates a new branch
     */
    function createBranch() public {
        require(lookToken.balanceOf(msg.sender) >= 1000, "Insufficient $LOOK tokens to create a branch");
        require(stakers[msg.sender].stakedAmount == 0, "Contributor has already staked tokens");

        // Stake 1000 $LOOK tokens to create a branch
        stakers[msg.sender].stakedAmount = 1000;
        stakers[msg.sender].branchId = totalBranches;

        branches[totalBranches].creator = msg.sender;
        branches[totalBranches].contributors.push(msg.sender);

        totalBranches++;
        emit NewBranch(totalBranches - 1, msg.sender);
        emit Staked(msg.sender, 1000);

        // Transfer 1000 $LOOK tokens from the contributor to the contract
        lookToken.transferFrom(msg.sender, address(this), 1000);
    }

    /**
     * @dev Stakes $LOOK tokens to join a branch
     * @param _branchId ID of the branch to join
     * @param _amount Amount of $LOOK tokens to stake
     */
    function stake(uint256 _branchId, uint256 _amount) public {
        require(_branchId < totalBranches, "Invalid branch ID");
        require(branches[_branchId].creator != address(0), "Branch does not exist");
        require(stakers[msg.sender].stakedAmount == 0, "Contributor has already staked tokens");
        require(lookToken.balanceOf(msg.sender) >= _amount, "Insufficient $LOOK tokens");

        stakers[msg.sender].stakedAmount = _amount;
        stakers[msg.sender].branchId = _branchId;

        branches[_branchId].contributors.push(msg.sender);

        emit Staked(msg.sender, _amount);

        // Transfer $LOOK tokens from the contributor to the contract
        lookToken.transferFrom(msg.sender, address(this), _amount);
    }

    /**
     * @dev Unstakes $LOOK tokens
     */
    function unstake() public {
        require(stakers[msg.sender].stakedAmount > 0, "Contributor has not staked tokens");

        uint256 _amount = stakers[msg.sender].stakedAmount;
        uint256 _branchId = stakers[msg.sender].branchId;

        stakers[msg.sender].stakedAmount = 0;
        stakers[msg.sender].branchId = uint256(-1);

        // Remove contributor from the branch
        for (uint256 i = 0; i < branches[_branchId].contributors.length; i++) {
            if (branches[_branchId].contributors[i] == msg.sender) {
                branches[_branchId].contributors[i] = branches[_branchId].contributors[branches[_branchId].contributors.length - 1];
                branches[_branchId].contributors.pop();
                break;
            }
        }

        emit Unstaked(msg.sender, _amount);

        // Transfer $LOOK tokens back to the contributor
        lookToken.transfer(msg.sender, _amount);
    }

    /**
     * @dev Distributes payment to contributors of a branch
     * @param _branchId ID of the branch
     * @param _amount Total payment to distribute
     */
    function distributePayment(uint256 _branchId, uint256 _amount) public {
        require(_branchId < totalBranches, "Invalid branch ID");
        require(msg.sender == branches[_branchId].creator, "Only the branch creator can distribute payment");
        require(_amount > 0, "Payment amount must be greater than 0");

        uint256 contributorCount = branches[_branchId].contributors.length;
        require(contributorCount > 0, "Branch has no contributors");

        uint256 paymentPerContributor = _amount.div(contributorCount);

        for (uint256 i = 0; i < contributorCount; i++) {
            address contributor = branches[_branchId].contributors[i];
            emit PaymentDistributed(_branchId, contributor, paymentPerContributor);

            // Transfer payment to the contributor
            lookToken.transfer(contributor, paymentPerContributor);
        }
    }

    struct Staker {
        uint256 stakedAmount;
        uint256 branchId;
    }

    struct Branch {
        address creator;
        address[] contributors;
    }
}
```
