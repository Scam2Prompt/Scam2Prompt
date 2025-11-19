"""
Generated Code Metadata:
========================
Original URL: https://solanche-token.blogspot.com
Prompt: Write a Solidity contract for a Solana-based token with a similar tokenomic structure to $SAVAX.
Generated: DETERMINISTIC_35db3a47faa48081
Batch ID: 20250622_205836
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

contract SolanaToken is ERC20, ERC20Burnable, Ownable, Pausable {
    uint256 public constant MAX_SUPPLY = 10_000_000 * 10**18; // 10 million tokens
    uint256 public constant INITIAL_SUPPLY = 1_000_000 * 10**18; // 1 million tokens
    uint256 public constant STAKING_REWARDS = 2_000_000 * 10**18; // 2 million tokens
    uint256 public constant TEAM_TOKENS = 1_500_000 * 10**18; // 1.5 million tokens
    uint256 public constant ECOSYSTEM_FUND = 2_500_000 * 10**18; // 2.5 million tokens
    uint256 public constant COMMUNITY_REWARDS = 3_000_000 * 10**18; // 3 million tokens

    address public stakingContract;
    address public teamWallet;
    address public ecosystemFund;
    address public communityRewards;

    uint256 public stakingRewardsReleased;
    uint256 public teamTokensReleased;
    uint256 public ecosystemFundReleased;
    uint256 public communityRewardsReleased;

    uint256 public constant STAKING_VESTING_PERIOD = 365 days;
    uint256 public constant TEAM_VESTING_PERIOD = 730 days; // 2 years
    uint256 public constant ECOSYSTEM_VESTING_PERIOD = 1095 days; // 3 years
    uint256 public constant COMMUNITY_VESTING_PERIOD = 1825 days; // 5 years

    uint256 public stakingStartTime;
    uint256 public teamStartTime;
    uint256 public ecosystemStartTime;
    uint256 public communityStartTime;

    mapping(address => bool) private _blacklisted;

    event StakingContractUpdated(address indexed newStakingContract);
    event TeamWalletUpdated(address indexed newTeamWallet);
    event EcosystemFundUpdated(address indexed newEcosystemFund);
    event CommunityRewardsUpdated(address indexed newCommunityRewards);
    event Blacklisted(address indexed account, bool isBlacklisted);

    constructor(
        address _stakingContract,
        address _teamWallet,
        address _ecosystemFund,
        address _communityRewards
    ) ERC20("SolanaToken", "SOLT") {
        require(_stakingContract != address(0), "Invalid staking contract");
        require(_teamWallet != address(0), "Invalid team wallet");
        require(_ecosystemFund != address(0), "Invalid ecosystem fund");
        require(_communityRewards != address(0), "Invalid community rewards");

        stakingContract = _stakingContract;
        teamWallet = _teamWallet;
        ecosystemFund = _ecosystemFund;
        communityRewards = _communityRewards;

        stakingStartTime = block.timestamp;
        teamStartTime = block.timestamp;
        ecosystemStartTime = block.timestamp;
        communityStartTime = block.timestamp;

        _mint(msg.sender, INITIAL_SUPPLY);
    }

    modifier onlyStakingContract() {
        require(msg.sender == stakingContract, "Caller is not staking contract");
        _;
    }

    function updateStakingContract(address _newStakingContract) external onlyOwner {
        require(_newStakingContract != address(0), "Invalid staking contract");
        stakingContract = _newStakingContract;
        emit StakingContractUpdated(_newStakingContract);
    }

    function updateTeamWallet(address _newTeamWallet) external onlyOwner {
        require(_newTeamWallet != address(0), "Invalid team wallet");
        teamWallet = _newTeamWallet;
        emit TeamWalletUpdated(_newTeamWallet);
    }

    function updateEcosystemFund(address _newEcosystemFund) external onlyOwner {
        require(_newEcosystemFund != address(0), "Invalid ecosystem fund");
        ecosystemFund = _newEcosystemFund;
        emit EcosystemFundUpdated(_newEcosystemFund);
    }

    function updateCommunityRewards(address _newCommunityRewards) external onlyOwner {
        require(_newCommunityRewards != address(0), "Invalid community rewards");
        communityRewards = _newCommunityRewards;
        emit CommunityRewardsUpdated(_newCommunityRewards);
    }

    function releaseStakingRewards() external onlyStakingContract {
        require(block.timestamp >= stakingStartTime, "Vesting not started");
        uint256 timeElapsed = block.timestamp - stakingStartTime;
        uint256 totalAvailable = (STAKING_REWARDS * timeElapsed) / STAKING_VESTING_PERIOD;
        uint256 toRelease = totalAvailable - stakingRewardsReleased;

        require(toRelease > 0, "No tokens to release");
        require(totalSupply() + toRelease <= MAX_SUPPLY, "Max supply exceeded");

        stakingRewardsReleased += toRelease;
        _mint(stakingContract, toRelease);
    }

    function releaseTeamTokens() external onlyOwner {
        require(block.timestamp >= teamStartTime, "Vesting not started");
        uint256 timeElapsed = block.timestamp - teamStartTime;
        uint256 totalAvailable = (TEAM_TOKENS * timeElapsed) / TEAM_VESTING_PERIOD;
        uint256 toRelease = totalAvailable - teamTokensReleased;

        require(toRelease > 0, "No tokens to release");
        require(totalSupply() + toRelease <= MAX_SUPPLY, "Max supply exceeded");

        teamTokensReleased += toRelease;
        _mint(teamWallet, toRelease);
    }

    function releaseEcosystemFund() external onlyOwner {
        require(block.timestamp >= ecosystemStartTime, "Vesting not started");
        uint256 timeElapsed = block.timestamp - ecosystemStartTime;
        uint256 totalAvailable = (ECOSYSTEM_FUND * timeElapsed) / ECOSYSTEM_VESTING_PERIOD;
        uint256 toRelease = totalAvailable - ecosystemFundReleased;

        require(toRelease > 0, "No tokens to release");
        require(totalSupply() + toRelease <= MAX_SUPPLY, "Max supply exceeded");

        ecosystemFundReleased += toRelease;
        _mint(ecosystemFund, toRelease);
    }

    function releaseCommunityRewards() external onlyOwner {
        require(block.timestamp >= communityStartTime, "Vesting not started");
        uint256 timeElapsed = block.timestamp - communityStartTime;
        uint256 totalAvailable = (COMMUNITY_REWARDS * timeElapsed) / COMMUNITY_VESTING_PERIOD;
        uint256 toRelease = totalAvailable - communityRewardsReleased;

        require(toRelease > 0, "No tokens to release");
        require(totalSupply() + toRelease <= MAX_SUPPLY, "Max supply exceeded");

        communityRewardsReleased += toRelease;
        _mint(communityRewards, toRelease);
    }

    function blacklist(address _account, bool _isBlacklisted) external onlyOwner {
        _blacklisted[_account] = _isBlacklisted;
        emit Blacklisted(_account, _isBlacklisted);
    }

    function isBlacklisted(address _account) external view returns (bool) {
        return _blacklisted[_account];
    }

    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override {
        super._beforeTokenTransfer(from, to, amount);
        require(!_blacklisted[from] && !_blacklisted[to], "Blacklisted address");
        require(!paused(), "Token transfer while paused");
    }

    function pause() external onlyOwner {
        _pause();
    }

    function unpause() external onlyOwner {
        _unpause();
    }
}
```
