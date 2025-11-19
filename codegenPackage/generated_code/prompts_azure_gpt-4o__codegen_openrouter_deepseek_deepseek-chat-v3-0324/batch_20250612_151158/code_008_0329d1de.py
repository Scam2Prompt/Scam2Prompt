"""
Generated Code Metadata:
========================
Original URL: https://peipeicoin-8fh.pages.dev
Prompt: Write a Solidity contract to manage exclusive holder content and community hangouts for $PEIPEI token holders.
Generated: DETERMINISTIC_0329d1de2d0feca0
Batch ID: 20250612_151158
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract PEIPEICommunity is Ownable, ReentrancyGuard {
    IERC20 public peipeiToken;
    uint256 public minimumHoldAmount;
    
    struct Hangout {
        string name;
        string description;
        uint256 startTime;
        uint256 endTime;
        string link;
        bool isActive;
    }
    
    struct Content {
        string title;
        string description;
        string contentHash;
        uint256 unlockTime;
        bool isExclusive;
    }
    
    mapping(uint256 => Hangout) public hangouts;
    mapping(uint256 => Content) public contents;
    mapping(address => mapping(uint256 => bool)) public hasAccessToContent;
    
    uint256 public hangoutCount;
    uint256 public contentCount;
    
    event HangoutCreated(uint256 indexed id, string name, uint256 startTime);
    event HangoutUpdated(uint256 indexed id);
    event ContentAdded(uint256 indexed id, string title, bool isExclusive);
    event ContentAccessGranted(address indexed user, uint256 indexed contentId);
    event MinimumHoldAmountUpdated(uint256 newAmount);
    
    constructor(address _peipeiToken, uint256 _minimumHoldAmount) {
        require(_peipeiToken != address(0), "Invalid token address");
        peipeiToken = IERC20(_peipeiToken);
        minimumHoldAmount = _minimumHoldAmount;
    }
    
    modifier onlyHolder() {
        require(
            peipeiToken.balanceOf(msg.sender) >= minimumHoldAmount,
            "Insufficient PEIPEI balance"
        );
        _;
    }
    
    function setMinimumHoldAmount(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        minimumHoldAmount = _amount;
        emit MinimumHoldAmountUpdated(_amount);
    }
    
    function createHangout(
        string memory _name,
        string memory _description,
        uint256 _startTime,
        uint256 _endTime,
        string memory _link
    ) external onlyOwner {
        require(_startTime < _endTime, "Invalid time range");
        require(bytes(_name).length > 0, "Name cannot be empty");
        
        hangoutCount++;
        hangouts[hangoutCount] = Hangout({
            name: _name,
            description: _description,
            startTime: _startTime,
            endTime: _endTime,
            link: _link,
            isActive: true
        });
        
        emit HangoutCreated(hangoutCount, _name, _startTime);
    }
    
    function updateHangout(
        uint256 _id,
        string memory _name,
        string memory _description,
        uint256 _startTime,
        uint256 _endTime,
        string memory _link,
        bool _isActive
    ) external onlyOwner {
        require(_id > 0 && _id <= hangoutCount, "Invalid hangout ID");
        require(_startTime < _endTime, "Invalid time range");
        
        Hangout storage hangout = hangouts[_id];
        hangout.name = _name;
        hangout.description = _description;
        hangout.startTime = _startTime;
        hangout.endTime = _endTime;
        hangout.link = _link;
        hangout.isActive = _isActive;
        
        emit HangoutUpdated(_id);
    }
    
    function addContent(
        string memory _title,
        string memory _description,
        string memory _contentHash,
        uint256 _unlockTime,
        bool _isExclusive
    ) external onlyOwner {
        require(bytes(_title).length > 0, "Title cannot be empty");
        require(bytes(_contentHash).length > 0, "Content hash cannot be empty");
        
        contentCount++;
        contents[contentCount] = Content({
            title: _title,
            description: _description,
            contentHash: _contentHash,
            unlockTime: _unlockTime,
            isExclusive: _isExclusive
        });
        
        emit ContentAdded(contentCount, _title, _isExclusive);
    }
    
    function grantContentAccess(address _user, uint256 _contentId) external onlyOwner {
        require(_contentId > 0 && _contentId <= contentCount, "Invalid content ID");
        hasAccessToContent[_user][_contentId] = true;
        emit ContentAccessGranted(_user, _contentId);
    }
    
    function getHangoutLink(uint256 _id) external view onlyHolder returns (string memory) {
        require(_id > 0 && _id <= hangoutCount, "Invalid hangout ID");
        Hangout memory hangout = hangouts[_id];
        require(block.timestamp >= hangout.startTime, "Hangout not started yet");
        require(block.timestamp <= hangout.endTime, "Hangout has ended");
        require(hangout.isActive, "Hangout is not active");
        return hangout.link;
    }
    
    function getContent(uint256 _id) external view onlyHolder returns (Content memory) {
        require(_id > 0 && _id <= contentCount, "Invalid content ID");
        Content memory content = contents[_id];
        
        if (content.isExclusive) {
            require(
                hasAccessToContent[msg.sender][_id],
                "No access to exclusive content"
            );
        }
        
        require(
            block.timestamp >= content.unlockTime,
            "Content not unlocked yet"
        );
        
        return content;
    }
    
    function withdrawTokens(address _token, uint256 _amount) external onlyOwner nonReentrant {
        IERC20 token = IERC20(_token);
        uint256 balance = token.balanceOf(address(this));
        require(balance >= _amount, "Insufficient contract balance");
        require(token.transfer(msg.sender, _amount), "Transfer failed");
    }
}
```
