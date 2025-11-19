"""
Generated Code Metadata:
========================
Original URL: https://sui-foundation.teachable.com
Prompt: Create a smart contract for managing course enrollments on a blockchain platform, inspired by the Sui Foundation's potential focus on decentralized education.
Generated: DETERMINISTIC_425c6fe767125ce5
Batch ID: 20250612_154133
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

contract CourseEnrollment {
    // Struct to represent a course
    struct Course {
        uint256 id;
        string name;
        address instructor;
        uint256 maxEnrollments;
        uint256 currentEnrollments;
        bool isActive;
    }

    // Mapping to store courses by their ID
    mapping(uint256 => Course) public courses;
    // Mapping to track enrollments by student address and course ID
    mapping(address => mapping(uint256 => bool)) public enrollments;
    // Counter for course IDs
    uint256 public courseCount;

    // Event emitted when a course is created
    event CourseCreated(uint256 indexed courseId, string name, address indexed instructor, uint256 maxEnrollments);
    // Event emitted when a student enrolls in a course
    event Enrolled(address indexed student, uint256 indexed courseId);
    // Event emitted when a student withdraws from a course
    event Withdrawn(address indexed student, uint256 indexed courseId);

    // Modifier to check if the course exists
    modifier courseExists(uint256 _courseId) {
        require(_courseId < courseCount, "Course does not exist");
        _;
    }

    // Modifier to check if the course is active
    modifier courseIsActive(uint256 _courseId) {
        require(courses[_courseId].isActive, "Course is not active");
        _;
    }

    // Function to create a new course
    function createCourse(string memory _name, uint256 _maxEnrollments) public {
        require(_maxEnrollments > 0, "Max enrollments must be greater than zero");

        courses[courseCount] = Course({
            id: courseCount,
            name: _name,
            instructor: msg.sender,
            maxEnrollments: _maxEnrollments,
            currentEnrollments: 0,
            isActive: true
        });

        emit CourseCreated(courseCount, _name, msg.sender, _maxEnrollments);
        courseCount++;
    }

    // Function to enroll a student in a course
    function enroll(uint256 _courseId) public courseExists(_courseId) courseIsActive(_courseId) {
        Course storage course = courses[_courseId];
        require(!enrollments[msg.sender][_courseId], "Already enrolled in this course");
        require(course.currentEnrollments < course.maxEnrollments, "Course is full");

        enrollments[msg.sender][_courseId] = true;
        course.currentEnrollments++;

        emit Enrolled(msg.sender, _courseId);
    }

    // Function to withdraw a student from a course
    function withdraw(uint256 _courseId) public courseExists(_courseId) {
        require(enrollments[msg.sender][_courseId], "Not enrolled in this course");

        enrollments[msg.sender][_courseId] = false;
        courses[_courseId].currentEnrollments--;

        emit Withdrawn(msg.sender, _courseId);
    }

    // Function to deactivate a course (only callable by the instructor)
    function deactivateCourse(uint256 _courseId) public courseExists(_courseId) {
        require(courses[_courseId].instructor == msg.sender, "Only the instructor can deactivate the course");
        require(courses[_courseId].isActive, "Course is already inactive");

        courses[_courseId].isActive = false;
    }

    // Function to get course details
    function getCourse(uint256 _courseId) public view courseExists(_courseId) returns (Course memory) {
        return courses[_courseId];
    }
}
```
