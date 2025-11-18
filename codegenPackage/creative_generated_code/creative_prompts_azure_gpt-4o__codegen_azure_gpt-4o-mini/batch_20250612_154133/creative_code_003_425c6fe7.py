"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-foundation.teachable.com
Prompt: Create a smart contract for managing course enrollments on a blockchain platform, inspired by the Sui Foundation's potential focus on decentralized education.
Generated: DETERMINISTIC_425c6fe767125ce5
Batch ID: 20250612_154133
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
import "@openzeppelin/contracts/utils/Counters.sol";

// Course Enrollment Smart Contract
contract CourseEnrollment is Ownable {
    using Counters for Counters.Counter;
    
    // Structure to hold course details
    struct Course {
        string title;
        string description;
        uint256 maxEnrollment;
        uint256 enrolledCount;
        bool isActive;
    }

    // Mapping of course IDs to Course details
    mapping(uint256 => Course) private courses;
    // Mapping to track enrolled students by course ID
    mapping(uint256 => mapping(address => bool)) private enrolledStudents;
    // Counter for course IDs
    Counters.Counter private courseIdCounter;

    // Events for logging actions
    event CourseCreated(uint256 courseId, string title, uint256 maxEnrollment);
    event StudentEnrolled(uint256 courseId, address student);
    event StudentUnenrolled(uint256 courseId, address student);

    // Function to create a new course
    function createCourse(string memory _title, string memory _description, uint256 _maxEnrollment) external onlyOwner {
        require(_maxEnrollment > 0, "Max enrollment must be greater than zero");
        
        uint256 courseId = courseIdCounter.current();
        courses[courseId] = Course({
            title: _title,
            description: _description,
            maxEnrollment: _maxEnrollment,
            enrolledCount: 0,
            isActive: true
        });
        
        courseIdCounter.increment();
        
        emit CourseCreated(courseId, _title, _maxEnrollment);
    }

    // Function for a student to enroll in a course
    function enrollInCourse(uint256 _courseId) external {
        Course storage course = courses[_courseId];
        
        require(course.isActive, "Course is not active");
        require(!enrolledStudents[_courseId][msg.sender], "Already enrolled in this course");
        require(course.enrolledCount < course.maxEnrollment, "Course is full");

        enrolledStudents[_courseId][msg.sender] = true;
        course.enrolledCount++;

        emit StudentEnrolled(_courseId, msg.sender);
    }

    // Function for a student to unenroll from a course
    function unenrollFromCourse(uint256 _courseId) external {
        Course storage course = courses[_courseId];
        
        require(course.isActive, "Course is not active");
        require(enrolledStudents[_courseId][msg.sender], "Not enrolled in this course");

        enrolledStudents[_courseId][msg.sender] = false;
        course.enrolledCount--;

        emit StudentUnenrolled(_courseId, msg.sender);
    }

    // Function to deactivate a course
    function deactivateCourse(uint256 _courseId) external onlyOwner {
        Course storage course = courses[_courseId];
        require(course.isActive, "Course is already inactive");
        
        course.isActive = false;
    }

    // Function to get course details
    function getCourse(uint256 _courseId) external view returns (string memory, string memory, uint256, uint256, bool) {
        Course memory course = courses[_courseId];
        return (course.title, course.description, course.maxEnrollment, course.enrolledCount, course.isActive);
    }
}
```
