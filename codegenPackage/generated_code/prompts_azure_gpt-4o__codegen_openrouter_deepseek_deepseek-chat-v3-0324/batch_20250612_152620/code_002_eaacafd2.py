"""
Generated Code Metadata:
========================
Original URL: https://betswirl.xyz
Prompt: Generate code to implement a token economy for a decentralized gaming platform, including features like staking, governance, and rewards, using the BetSwirl model.
Generated: DETERMINISTIC_eaacafd2c8a5497c
Batch ID: 20250612_152620
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Snapshot.sol";
import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract GameToken is ERC20, ERC20Burnable, ERC20Snapshot, AccessControl, Pausable {
    using SafeMath for uint256;

    bytes32 public constant MINTER_ROLE = keccak256("MINTER_ROLE");
    bytes32 public constant STAKING_ROLE = keccak256("STAKING_ROLE");
    bytes32 public constant GOVERNANCE_ROLE = keccak256("GOVERNANCE_ROLE");

    uint256 public constant MAX_SUPPLY = 1000000000 * 10 ** 18; // 1 billion tokens
    uint256 public stakingRewardRate = 10; // 10% annual reward
    uint256 public lastRewardTimestamp;
    uint256 public totalStaked;

    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    mapping(address => Stake) public stakes;
    mapping(address => uint256) public rewards;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event GovernanceProposalCreated(uint256 proposalId, string description);

    constructor() ERC20("GameToken", "GAME") {
        _setupRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _setupRole(MINTER_ROLE, msg.sender);
        _setupRole(GOVERNANCE_ROLE, msg.sender);
        _mint(msg.sender, MAX_SUPPLY.div(10)); // Initial mint of 10% supply
        lastRewardTimestamp = block.timestamp;
    }

    function snapshot() public onlyRole(GOVERNANCE_ROLE) {
        _snapshot();
    }

    function pause() public onlyRole(GOVERNANCE_ROLE) {
        _pause();
    }

    function unpause() public onlyRole(GOVERNANCE_ROLE) {
        _unpause();
    }

    function mint(address to, uint256 amount) public onlyRole(MINTER_ROLE) {
        require(totalSupply().add(amount) <= MAX_SUPPLY, "Exceeds max supply");
        _mint(to, amount);
    }

    function stake(uint256 amount) external whenNotPaused {
        require(amount > 0, "Cannot stake 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        _updateRewards(msg.sender);
        _burn(msg.sender, amount);

        if (stakes[msg.sender].amount > 0) {
            stakes[msg.sender].amount = stakes[msg.sender].amount.add(amount);
        } else {
            stakes[msg.sender] = Stake(amount, block.timestamp);
        }

        totalStaked = totalStaked.add(amount);
        emit Staked(msg.sender, amount);
    }

    function unstake(uint256 amount) external whenNotPaused {
        require(amount > 0, "Cannot unstake 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient stake");

        _updateRewards(msg.sender);
        stakes[msg.sender].amount = stakes[msg.sender].amount.sub(amount);
        totalStaked = totalStaked.sub(amount);

        _mint(msg.sender, amount);
        emit Unstaked(msg.sender, amount);
    }

    function claimRewards() external whenNotPaused {
        _updateRewards(msg.sender);
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        rewards[msg.sender] = 0;
        _mint(msg.sender, reward);
        emit RewardClaimed(msg.sender, reward);
    }

    function _updateRewards(address user) internal {
        if (stakes[user].amount == 0) return;

        uint256 timeElapsed = block.timestamp.sub(stakes[user].timestamp);
        uint256 reward = stakes[user].amount
            .mul(stakingRewardRate)
            .mul(timeElapsed)
            .div(365 days)
            .div(100);

        rewards[user] = rewards[user].add(reward);
        stakes[user].timestamp = block.timestamp;
    }

    function createGovernanceProposal(string memory description) external onlyRole(GOVERNANCE_ROLE) {
        uint256 proposalId = uint256(keccak256(abi.encodePacked(block.timestamp, description)));
        emit GovernanceProposalCreated(proposalId, description);
    }

    function setRewardRate(uint256 newRate) external onlyRole(GOVERNANCE_ROLE) {
        require(newRate <= 100, "Rate cannot exceed 100%");
        stakingRewardRate = newRate;
    }

    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override(ERC20, ERC20Snapshot) whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
    }
}
```
