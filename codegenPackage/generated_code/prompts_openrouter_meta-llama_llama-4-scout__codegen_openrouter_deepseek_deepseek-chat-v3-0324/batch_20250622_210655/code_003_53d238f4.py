"""
Generated Code Metadata:
========================
Original URL: https://blockchainguild.pages.dev
Prompt: "Design a task/campaign management system for a decentralized application (dapp) on a platform like Guild.xyz."
Generated: DETERMINISTIC_53d238f4bc9b6d7a
Batch ID: 20250622_210655
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title TaskCampaignManager
 * @dev A smart contract for managing tasks and campaigns in a decentralized application
 */
contract TaskCampaignManager is Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    
    enum TaskStatus { Pending, Approved, Rejected, Completed }
    enum CampaignStatus { Active, Paused, Completed }
    
    struct Task {
        uint256 id;
        string title;
        string description;
        uint256 reward;
        address creator;
        address assignee;
        TaskStatus status;
        uint256 campaignId;
        uint256 createdAt;
        uint256 completedAt;
    }
    
    struct Campaign {
        uint256 id;
        string title;
        string description;
        uint256 totalBudget;
        uint256 remainingBudget;
        CampaignStatus status;
        address owner;
        uint256 createdAt;
        uint256 endAt;
    }
    
    Counters.Counter private _taskIds;
    Counters.Counter private _campaignIds;
    
    mapping(uint256 => Task) private _tasks;
    mapping(uint256 => Campaign) private _campaigns;
    mapping(address => uint256[]) private _userTasks;
    mapping(address => uint256[]) private _userCampaigns;
    
    event TaskCreated(uint256 taskId, uint256 campaignId, address creator);
    event TaskStatusUpdated(uint256 taskId, TaskStatus status);
    event CampaignCreated(uint256 campaignId, address owner);
    event CampaignStatusUpdated(uint256 campaignId, CampaignStatus status);
    event FundsDeposited(uint256 campaignId, uint256 amount);
    event RewardClaimed(uint256 taskId, address assignee, uint256 amount);
    
    modifier onlyCampaignOwner(uint256 campaignId) {
        require(_campaigns[campaignId].owner == msg.sender, "Not campaign owner");
        _;
    }
    
    modifier validCampaign(uint256 campaignId) {
        require(campaignId <= _campaignIds.current(), "Invalid campaign");
        _;
    }
    
    modifier validTask(uint256 taskId) {
        require(taskId <= _taskIds.current(), "Invalid task");
        _;
    }
    
    /**
     * @dev Create a new campaign
     * @param title Campaign title
     * @param description Campaign description
     * @param totalBudget Total budget for the campaign
     * @param duration Duration of the campaign in seconds
     */
    function createCampaign(
        string memory title,
        string memory description,
        uint256 totalBudget,
        uint256 duration
    ) external payable {
        require(bytes(title).length > 0, "Title required");
        require(bytes(description).length > 0, "Description required");
        require(totalBudget > 0, "Budget must be positive");
        require(msg.value >= totalBudget, "Insufficient funds");
        
        _campaignIds.increment();
        uint256 newCampaignId = _campaignIds.current();
        
        _campaigns[newCampaignId] = Campaign({
            id: newCampaignId,
            title: title,
            description: description,
            totalBudget: totalBudget,
            remainingBudget: totalBudget,
            status: CampaignStatus.Active,
            owner: msg.sender,
            createdAt: block.timestamp,
            endAt: block.timestamp + duration
        });
        
        _userCampaigns[msg.sender].push(newCampaignId);
        
        emit CampaignCreated(newCampaignId, msg.sender);
    }
    
    /**
     * @dev Deposit additional funds to a campaign
     * @param campaignId ID of the campaign
     */
    function depositFunds(uint256 campaignId) 
        external 
        payable 
        onlyCampaignOwner(campaignId)
        validCampaign(campaignId)
    {
        require(msg.value > 0, "Amount must be positive");
        
        Campaign storage campaign = _campaigns[campaignId];
        campaign.totalBudget += msg.value;
        campaign.remainingBudget += msg.value;
        
        emit FundsDeposited(campaignId, msg.value);
    }
    
    /**
     * @dev Update campaign status
     * @param campaignId ID of the campaign
     * @param status New status
     */
    function updateCampaignStatus(uint256 campaignId, CampaignStatus status) 
        external 
        onlyCampaignOwner(campaignId)
        validCampaign(campaignId)
    {
        Campaign storage campaign = _campaigns[campaignId];
        require(campaign.status != CampaignStatus.Completed, "Campaign completed");
        
        campaign.status = status;
        emit CampaignStatusUpdated(campaignId, status);
    }
    
    /**
     * @dev Create a new task under a campaign
     * @param campaignId ID of the parent campaign
     * @param title Task title
     * @param description Task description
     * @param reward Reward for completing the task
     */
    function createTask(
        uint256 campaignId,
        string memory title,
        string memory description,
        uint256 reward
    ) external validCampaign(campaignId) {
        Campaign storage campaign = _campaigns[campaignId];
        
        require(campaign.status == CampaignStatus.Active, "Campaign not active");
        require(bytes(title).length > 0, "Title required");
        require(bytes(description).length > 0, "Description required");
        require(reward > 0, "Reward must be positive");
        require(reward <= campaign.remainingBudget, "Insufficient campaign funds");
        
        _taskIds.increment();
        uint256 newTaskId = _taskIds.current();
        
        _tasks[newTaskId] = Task({
            id: newTaskId,
            title: title,
            description: description,
            reward: reward,
            creator: msg.sender,
            assignee: address(0),
            status: TaskStatus.Pending,
            campaignId: campaignId,
            createdAt: block.timestamp,
            completedAt: 0
        });
        
        campaign.remainingBudget -= reward;
        _userTasks[msg.sender].push(newTaskId);
        
        emit TaskCreated(newTaskId, campaignId, msg.sender);
    }
    
    /**
     * @dev Update task status (for campaign owners)
     * @param taskId ID of the task
     * @param status New status
     */
    function updateTaskStatus(uint256 taskId, TaskStatus status) 
        external 
        validTask(taskId)
    {
        Task storage task = _tasks[taskId];
        Campaign storage campaign = _campaigns[task.campaignId];
        
        require(
            msg.sender == campaign.owner || msg.sender == task.creator,
            "Not authorized"
        );
        require(task.status != TaskStatus.Completed, "Task already completed");
        
        if (status == TaskStatus.Rejected) {
            campaign.remainingBudget += task.reward;
        }
        
        task.status = status;
        emit TaskStatusUpdated(taskId, status);
    }
    
    /**
     * @dev Assign a task to a user
     * @param taskId ID of the task
     * @param assignee Address of the assignee
     */
    function assignTask(uint256 taskId, address assignee) 
        external 
        validTask(taskId)
    {
        Task storage task = _tasks[taskId];
        require(task.creator == msg.sender, "Not task creator");
        require(task.status == TaskStatus.Approved, "Task not approved");
        require(task.assignee == address(0), "Task already assigned");
        
        task.assignee = assignee;
        _userTasks[assignee].push(taskId);
    }
    
    /**
     * @dev Complete a task and claim reward
     * @param taskId ID of the task
     */
    function completeTask(uint256 taskId) 
        external 
        nonReentrant
        validTask(taskId)
    {
        Task storage task = _tasks[taskId];
        require(task.assignee == msg.sender, "Not task assignee");
        require(task.status == TaskStatus.Approved, "Task not approved");
        
        task.status = TaskStatus.Completed;
        task.completedAt = block.timestamp;
        
        (bool sent, ) = payable(msg.sender).call{value: task.reward}("");
        require(sent, "Failed to send reward");
        
        emit RewardClaimed(taskId, msg.sender, task.reward);
    }
    
    /**
     * @dev Get task details
     * @param taskId ID of the task
     * @return Task details
     */
    function getTask(uint256 taskId) 
        external 
        view 
        validTask(taskId)
        returns (Task memory)
    {
        return _tasks[taskId];
    }
    
    /**
     * @dev Get campaign details
     * @param campaignId ID of the campaign
     * @return Campaign details
     */
    function getCampaign(uint256 campaignId) 
        external 
        view 
        validCampaign(campaignId)
        returns (Campaign
