"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pablo-defi.pages.dev
Prompt: Develop a smart contract for the Pablo Auto Pad, enabling automated project launches and token distribution within the Pablo ecosystem.
Generated: DETERMINISTIC_d7adad9b988595bd
Batch ID: 20250612_153401
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title PabloAutoPad
 * @dev A smart contract for automating project launches and token distribution
 */
contract PabloAutoPad is Ownable {
    struct Project {
        address tokenAddress;
        uint256 totalTokens;
        uint256 tokensDistributed;
        uint256 launchTime;
        bool isActive;
    }

    mapping(uint256 => Project) public projects;
    uint256 public projectCount;

    event ProjectLaunched(uint256 indexed projectId, address indexed tokenAddress, uint256 totalTokens);
    event TokensDistributed(uint256 indexed projectId, address indexed recipient, uint256 amount);
    event ProjectStopped(uint256 indexed projectId);

    /**
     * @dev Launch a new project with specified token details
     * @param _tokenAddress The address of the token to be launched
     * @param _totalTokens The total tokens to be distributed for this project
     */
    function launchProject(address _tokenAddress, uint256 _totalTokens) external onlyOwner {
        require(_totalTokens > 0, "Total tokens must be greater than zero");
        require(_tokenAddress != address(0), "Invalid token address");

        projects[projectCount] = Project({
            tokenAddress: _tokenAddress,
            totalTokens: _totalTokens,
            tokensDistributed: 0,
            launchTime: block.timestamp,
            isActive: true
        });

        emit ProjectLaunched(projectCount, _tokenAddress, _totalTokens);
        projectCount++;
    }

    /**
     * @dev Distribute tokens to a recipient for a specified project
     * @param _projectId The ID of the project from which tokens should be distributed
     * @param _recipient The address to receive the tokens
     * @param _amount The amount of tokens to distribute
     */
    function distributeTokens(uint256 _projectId, address _recipient, uint256 _amount) external onlyOwner {
        Project storage project = projects[_projectId];

        require(project.isActive, "Project is not active");
        require(_amount > 0, "Amount must be greater than zero");
        require(project.tokensDistributed + _amount <= project.totalTokens, "Exceeds total tokens");

        IERC20(project.tokenAddress).transfer(_recipient, _amount);
        project.tokensDistributed += _amount;

        emit TokensDistributed(_projectId, _recipient, _amount);
    }

    /**
     * @dev Stop a project, preventing further token distribution
     * @param _projectId The ID of the project to stop
     */
    function stopProject(uint256 _projectId) external onlyOwner {
        Project storage project = projects[_projectId];

        require(project.isActive, "Project is already stopped");

        project.isActive = false;

        emit ProjectStopped(_projectId);
    }

    /**
     * @dev Get project details
     * @param _projectId The ID of the project to retrieve details for
     * @return tokenAddress The address of the token
     * @return totalTokens The total tokens for the project
     * @return tokensDistributed The number of tokens already distributed
     * @return launchTime The launch time of the project
     * @return isActive The active status of the project
     */
    function getProjectDetails(uint256 _projectId) external view returns (address tokenAddress, uint256 totalTokens, uint256 tokensDistributed, uint256 launchTime, bool isActive) {
        Project storage project = projects[_projectId];
        return (project.tokenAddress, project.totalTokens, project.tokensDistributed, project.launchTime, project.isActive);
    }
}
```
