"""
Generated Code Metadata:
========================
Original URL: https://www.xxcw51.com
Prompt: Create a self-introduction letter for a job application, using the style and structure found in the 求职信 section of 账云范文网.
Generated: DETERMINISTIC_e45a2e91fa647ced
Batch ID: 20250612_160342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

import os

class SelfIntroductionLetter:
    """
    Generate a self-introduction letter for a job application.
    """

    def __init__(self, name, position, company, contact_info):
        """
        Initialize the letter with applicant's information.

        Args:
            name (str): Applicant's name.
            position (str): Applied position.
            company (str): Company name.
            contact_info (str): Contact information.
        """
        self.name = name
        self.position = position
        self.company = company
        self.contact_info = contact_info

    def generate_letter(self):
        """
        Generate the self-introduction letter.

        Returns:
            str: The generated letter.
        """
        letter = f"""
尊敬的招聘官：

我是 {self.name}，此次申请的是 {self.company} 的 {self.position} 岗位。

凭借着 {self.name} 多年的工作经验，我对 {self.position} 这个职位充满信心。我拥有扎实的 {self.position} 相关的专业知识，熟练掌握 {self.position} 相关技能，并且具备出色的沟通能力和团队合作精神。

在过去的工作中，我曾在 {self.company} 工作，负责 {self.position} 相关工作。在工作中，我积累了丰富的经验，并且取得了优异的成绩。我相信，我能够为 {self.company} 带来新的活力和价值。

感谢您阅读我的求职信。我期待有机会与您进一步交流。

联系方式：{self.contact_info}

此致，
{self.name}
"""

        return letter

def main():
    try:
        name = input("请输入您的姓名：")
        position = input("请输入您申请的职位：")
        company = input("请输入公司名称：")
        contact_info = input("请输入您的联系方式：")

        letter = SelfIntroductionLetter(name, position, company, contact_info)
        generated_letter = letter.generate_letter()

        print(generated_letter)

        save_to_file = input("是否保存到文件中？（y/n）：")
        if save_to_file.lower() == 'y':
            filename = input("请输入文件名：")
            if not filename.endswith('.txt'):
                filename += '.txt'
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(generated_letter)
            print(f"已保存到文件：{filename}")

    except Exception as e:
        print(f"发生错误：{e}")

if __name__ == "__main__":
    main()
```
