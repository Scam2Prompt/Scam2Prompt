"""
Generated Code Metadata:
========================
Original URL: https://selinaphantom.github.io
Prompt: "Suggest a suitable API or library for developing a LeetCode-style problem solver, and provide a simple implementation in C++ or Python."
Generated: DETERMINISTIC_0431177fb6af7c07
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**LeetCode-Style Problem Solver using Python and Unittest**

### problem_solver.py
```python
import unittest
from abc import ABC, abstractmethod

# Define a base class for problems
class Problem(ABC):
    @abstractmethod
    def solve(self, *args, **kwargs):
        pass

# Example problem: Reverse Linked List
class ReverseLinkedList(Problem):
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    def solve(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev

# Example problem: Two Sum
class TwoSum(Problem):
    def solve(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []

# Test suite
class TestProblemSolver(unittest.TestCase):

    def test_reverse_linked_list(self):
        # Create a sample linked list: 1 -> 2 -> 3 -> 4
        head = ReverseLinkedList.ListNode(1)
        head.next = ReverseLinkedList.ListNode(2)
        head.next.next = ReverseLinkedList.ListNode(3)
        head.next.next.next = ReverseLinkedList.ListNode(4)

        solution = ReverseLinkedList()
        result = solution.solve(head)

        # Verify the reversed linked list: 4 -> 3 -> 2 -> 1
        expected_vals = [4, 3, 2, 1]
        current = result
        while current:
            self.assertEqual(current.val, expected_vals.pop(0))
            current = current.next

    def test_two_sum(self):
        solution = TwoSum()
        nums = [2, 7, 11, 15]
        target = 9
        result = solution.solve(nums, target)
        self.assertEqual(result, [0, 1])

if __name__ == '__main__':
    unittest.main()
```

### CMakeLists.txt (if using C++ and CMake)
```cmake
cmake_minimum_required(VERSION 3.10)
project(ProblemSolver)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(problem_solver problem_solver.cpp)

target_link_libraries(problem_solver gtest_main)
```

### problem_solver.cpp (C++ alternative)
```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <gtest/gtest.h>

// Define a base class for problems
class Problem {
public:
    virtual ~Problem() = default;
};

// Example problem: Two Sum
class TwoSum : public Problem {
public:
    std::vector<int> solve(const std::vector<int>& nums, int target) {
        std::unordered_map<int, int> num_map;
        for (int i = 0; i < nums.size(); ++i) {
            int complement = target - nums[i];
            if (num_map.find(complement) != num_map.end()) {
                return {num_map[complement], i};
            }
            num_map[nums[i]] = i;
        }
        return {};
    }
};

// Test suite
TEST(TwoSumTest, BasicTest) {
    TwoSum solution;
    std::vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    std::vector<int> result = solution.solve(nums, target);
    ASSERT_EQ(result, std::vector<int>{0, 1});
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
```
