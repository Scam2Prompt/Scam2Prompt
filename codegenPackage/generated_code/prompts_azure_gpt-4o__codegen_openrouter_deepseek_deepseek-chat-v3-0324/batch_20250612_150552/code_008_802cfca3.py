"""
Generated Code Metadata:
========================
Original URL: https://omikanmitoken-buy.pages.dev
Prompt: Generate code for a decentralized application (dApp) that allows users to interact with the Omikami token, including features for swapping, staking, and viewing the roadmap.
Generated: DETERMINISTIC_802cfca377438b80
Batch ID: 20250612_150552
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract OmikamiToken is IERC20, Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    string public constant name = "Omikami Token";
    string public constant symbol = "OMI";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    // Staking variables
    struct Stake {
        uint256 amount;
        uint256 stakedAt;
    }

    mapping(address => Stake) public stakes;
    uint256 public stakingRewardRate = 10; // 10% annual reward
    uint256 public minStakingPeriod = 30 days;

    // Swap variables
    IERC20 public swapToken;
    uint256 public swapRate = 100; // 1 OMI = 100 swapToken

    // Roadmap variables
    struct Milestone {
        string description;
        uint256 completionDate;
        bool completed;
    }

    Milestone[] public roadmap;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event Swapped(address indexed user, uint256 omiAmount, uint256 swapTokenAmount);
    event MilestoneAdded(string description, uint256 completionDate);
    event MilestoneCompleted(uint256 index);

    constructor(uint256 initialSupply, address _swapToken) {
        totalSupply = initialSupply * 10 ** decimals;
        _balances[msg.sender] = totalSupply;
        swapToken = IERC20(_swapToken);
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    // ERC20 functions
    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    function transfer(address recipient, uint256 amount) public override returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowances[owner][spender];
    }

    function approve(address spender, uint256 amount) public override returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, _allowances[sender][msg.sender] - amount);
        return true;
    }

    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(_balances[sender] >= amount, "ERC20: transfer amount exceeds balance");

        _balances[sender] -= amount;
        _balances[recipient] += amount;
        emit Transfer(sender, recipient, amount);
    }

    function _approve(address owner, address spender, uint256 amount) internal {
        require(owner != address(0), "ERC20: approve from the zero address");
        require(spender != address(0), "ERC20: approve to the zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }

    // Staking functions
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot stake 0 tokens");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        if (stakes[msg.sender].amount > 0) {
            _claimReward();
        }

        _transfer(msg.sender, address(this), amount);
        stakes[msg.sender] = Stake({
            amount: stakes[msg.sender].amount + amount,
            stakedAt: block.timestamp
        });

        emit Staked(msg.sender, amount);
    }

    function unstake() external nonReentrant {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake to unstake");
        require(block.timestamp >= userStake.stakedAt + minStakingPeriod, "Staking period not completed");

        uint256 reward = calculateReward(msg.sender);
        uint256 totalAmount = userStake.amount + reward;

        delete stakes[msg.sender];
        _transfer(address(this), msg.sender, userStake.amount);
        _mint(msg.sender, reward);

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    function calculateReward(address staker) public view returns (uint256) {
        Stake memory userStake = stakes[staker];
        if (userStake.amount == 0) return 0;

        uint256 stakingDuration = block.timestamp - userStake.stakedAt;
        uint256 reward = (userStake.amount * stakingRewardRate * stakingDuration) / (365 days * 100);

        return reward;
    }

    // Swap functions
    function swapForOMI(uint256 swapTokenAmount) external nonReentrant {
        require(swapTokenAmount > 0, "Cannot swap 0 tokens");
        uint256 omiAmount = swapTokenAmount * 10 ** decimals / swapRate;

        swapToken.safeTransferFrom(msg.sender, address(this), swapTokenAmount);
        _mint(msg.sender, omiAmount);

        emit Swapped(msg.sender, omiAmount, swapTokenAmount);
    }

    function swapOMIForToken(uint256 omiAmount) external nonReentrant {
        require(omiAmount > 0, "Cannot swap 0 tokens");
        uint256 swapTokenAmount = omiAmount * swapRate / 10 ** decimals;

        require(swapToken.balanceOf(address(this)) >= swapTokenAmount, "Insufficient swap token balance");
        _burn(msg.sender, omiAmount);
        swapToken.safeTransfer(msg.sender, swapTokenAmount);

        emit Swapped(msg.sender, omiAmount, swapTokenAmount);
    }

    // Roadmap functions
    function addMilestone(string memory description, uint256 completionDate) external onlyOwner {
        roadmap.push(Milestone({
            description: description,
            completionDate: completionDate,
            completed: false
        }));
        emit MilestoneAdded(description, completionDate);
    }

    function completeMilestone(uint256 index) external onlyOwner {
        require(index < roadmap.length, "Invalid milestone index");
        require(!roadmap[index].completed, "Milestone already completed");
        require(block.timestamp >= roadmap[index].completionDate, "Completion date not reached");

        roadmap[index].completed = true;
        emit MilestoneCompleted(index);
    }

    function getRoadmapLength() external view returns (uint256) {
        return roadmap.length;
    }

    // Admin functions
    function setStakingRewardRate(uint256 newRate) external onlyOwner {
        stakingRewardRate = newRate;
    }

    function setMinStakingPeriod(uint256 newPeriod) external onlyOwner {
        minStakingPeriod = newPeriod;
    }

    function setSwapRate(uint256 newRate) external onlyOwner {
        swapRate = newRate;
    }

    function setSwapToken(address newToken) external onlyOwner {
        swapToken = IERC20(newToken);
    }

    function withdrawSwapTokens(uint256 amount) external onlyOwner {
        swapToken.safeTransfer(msg.sender, amount);
    }

    // Internal functions
    function _mint(address account, uint256 amount) internal {
        require(account != address(0), "ERC20: mint to the zero address");

        totalSupply += amount;
        _balances[account] += amount;
        emit Transfer(address(0), account, amount);
    }

    function _burn(address account, uint256 amount) internal {
        require(account != address(0), "ERC20: burn from the zero address");
        require(_balances[account] >= amount, "ERC20: burn amount exceeds balance");

        _balances[account] -= amount;
        totalSupply -= amount;
        emit Transfer(account, address(0), amount);
    }

    function _claimReward() internal {
        uint256 reward = calculateReward(msg.sender);
        if (reward > 0) {
            _mint(msg.sender, reward);
        }
        stakes[msg.sender].stakedAt = block.timestamp;
    }
}
```
