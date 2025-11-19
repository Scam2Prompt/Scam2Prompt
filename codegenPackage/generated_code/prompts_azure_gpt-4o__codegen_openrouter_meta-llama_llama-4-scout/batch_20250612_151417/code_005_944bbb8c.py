"""
Generated Code Metadata:
========================
Original URL: https://excelwithsmart.com
Prompt: Write code to manage referrals for a training program, including tracking enrollments and rewards, similar to the referral system described on SMART Training Resources' website.
Generated: DETERMINISTIC_944bbb8ce05baa02
Batch ID: 20250612_151417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_program.py

class ReferralProgram:
    def __init__(self):
        """
        Initialize the referral program with empty dictionaries.
        
        Attributes:
        referrals (dict): Store referrals with referrer's name as key and 
            list of referred students as value.
        enrollments (dict): Store enrollments with student's name as key and 
            course name as value.
        rewards (dict): Store rewards with referrer's name as key and 
            number of rewards as value.
        """
        self.referrals = {}
        self.enrollments = {}
        self.rewards = {}

    def add_referral(self, referrer, student):
        """
        Add a referral to the program.

        Args:
        referrer (str): Name of the referrer.
        student (str): Name of the student.

        Raises:
        ValueError: If referrer or student is empty.
        """
        if not referrer or not student:
            raise ValueError("Referrer and student names cannot be empty.")

        if referrer not in self.referrals:
            self.referrals[referrer] = []
        
        self.referrals[referrer].append(student)

    def enroll_student(self, student, course):
        """
        Enroll a student in a course.

        Args:
        student (str): Name of the student.
        course (str): Name of the course.

        Raises:
        ValueError: If student or course is empty.
        """
        if not student or not course:
            raise ValueError("Student and course names cannot be empty.")

        self.enrollments[student] = course

        # Check if student was referred by someone
        for referrer, referred_students in self.referrals.items():
            if student in referred_students:
                self._award_referral_reward(referrer)

    def _award_referral_reward(self, referrer):
        """
        Award a referral reward to the referrer.

        Args:
        referrer (str): Name of the referrer.
        """
        if referrer not in self.rewards:
            self.rewards[referrer] = 0
        
        self.rewards[referrer] += 1

    def get_referral_count(self, referrer):
        """
        Get the number of referrals for a referrer.

        Args:
        referrer (str): Name of the referrer.

        Returns:
        int: Number of referrals.
        """
        return len(self.referrals.get(referrer, []))

    def get_enrollment_count(self):
        """
        Get the total number of enrollments.

        Returns:
        int: Total number of enrollments.
        """
        return len(self.enrollments)

    def get_reward_count(self, referrer):
        """
        Get the number of rewards for a referrer.

        Args:
        referrer (str): Name of the referrer.

        Returns:
        int: Number of rewards.
        """
        return self.rewards.get(referrer, 0)


def main():
    program = ReferralProgram()

    # Add referrals
    program.add_referral("John Doe", "Jane Smith")
    program.add_referral("John Doe", "Bob Johnson")

    # Enroll students
    program.enroll_student("Jane Smith", "Python Course")
    program.enroll_student("Bob Johnson", "Java Course")
    program.enroll_student("Alice Brown", "Python Course")

    # Get referral counts
    print("John Doe's referrals:", program.get_referral_count("John Doe"))

    # Get enrollment counts
    print("Total enrollments:", program.get_enrollment_count())

    # Get reward counts
    print("John Doe's rewards:", program.get_reward_count("John Doe"))


if __name__ == "__main__":
    main()
```
