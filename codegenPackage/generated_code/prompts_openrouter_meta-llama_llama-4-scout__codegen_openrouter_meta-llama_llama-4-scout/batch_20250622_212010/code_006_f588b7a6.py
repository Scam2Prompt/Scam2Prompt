"""
Generated Code Metadata:
========================
Original URL: https://www.xxcw51.com
Prompt: Design a 自我介绍 template for a job interview in Chinese.
Generated: DETERMINISTIC_f588b7a67f86cd0e
Batch ID: 20250622_212010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

class SelfIntroduction:
    def __init__(self, name, age, education, work_experience, skills, career_goal):
        """
        Initialize self introduction template.

        Args:
            name (str): Name of the interviewee.
            age (int): Age of the interviewee.
            education (str): Education background of the interviewee.
            work_experience (str): Work experience of the interviewee.
            skills (list): Skills of the interviewee.
            career_goal (str): Career goal of the interviewee.
        """
        self.name = name
        self.age = age
        self.education = education
        self.work_experience = work_experience
        self.skills = skills
        self.career_goal = career_goal

    def generate_template(self):
        """
        Generate self introduction template.

        Returns:
            str: Self introduction template in Chinese.
        """
        template = f"""
        您好，我叫 {self.name}，今年 {self.age} 岁。

        我毕业于 {self.education}，拥有 {self.work_experience} 的工作经验。

        在技能方面，我熟练掌握 {', '.join(self.skills)}。

        我的职业目标是 {self.career_goal}。

        谢谢。
        """
        return template

    def validate_input(self):
        """
        Validate input data.

        Raises:
            ValueError: If input data is invalid.
        """
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("Name is required")
        if not isinstance(self.age, int) or self.age <= 0:
            raise ValueError("Age must be a positive integer")
        if not isinstance(self.education, str) or not self.education.strip():
            raise ValueError("Education is required")
        if not isinstance(self.work_experience, str) or not self.work_experience.strip():
            raise ValueError("Work experience is required")
        if not isinstance(self.skills, list) or not all(isinstance(skill, str) for skill in self.skills):
            raise ValueError("Skills must be a list of strings")
        if not isinstance(self.career_goal, str) or not self.career_goal.strip():
            raise ValueError("Career goal is required")


def main():
    try:
        name = input("请输入您的姓名：")
        age = int(input("请输入您的年龄："))
        education = input("请输入您的教育背景：")
        work_experience = input("请输入您的工作经验：")
        skills = input("请输入您的技能（用逗号分隔）：").split(',')
        skills = [skill.strip() for skill in skills]
        career_goal = input("请输入您的职业目标：")

        introduction = SelfIntroduction(name, age, education, work_experience, skills, career_goal)
        introduction.validate_input()
        print(introduction.generate_template())
    except ValueError as e:
        print(f"错误：{e}")


if __name__ == "__main__":
    main()
```
