"""
Generated Code Metadata:
========================
Original URL: https://www.xxcw51.com
Prompt: Generate a 实践报告 template for a social practice activity in Chinese.
Generated: DETERMINISTIC_30937b5dfce0000d
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

from datetime import datetime
from typing import Optional

class ShiJianBaoGao:
    def __init__(self, 
                 activity_name: str, 
                 activity_time: str, 
                 location: str, 
                 participants: str, 
                 organizer: str, 
                 content: Optional[str] = None, 
                 conclusion: Optional[str] = None):
        """
        Initialize a ShiJianBaoGao object.

        Args:
        - activity_name (str): The name of the social practice activity.
        - activity_time (str): The time of the social practice activity.
        - location (str): The location of the social practice activity.
        - participants (str): The participants of the social practice activity.
        - organizer (str): The organizer of the social practice activity.
        - content (str, optional): The content of the social practice activity. Defaults to None.
        - conclusion (str, optional): The conclusion of the social practice activity. Defaults to None.
        """
        self.activity_name = activity_name
        self.activity_time = activity_time
        self.location = location
        self.participants = participants
        self.organizer = organizer
        self.content = content
        self.conclusion = conclusion

    def generate_template(self) -> str:
        """
        Generate a 实践报告 template.

        Returns:
        - str: A 实践报告 template.
        """
        template = f"""
# 实践报告

## 基本信息
- 活动名称：{self.activity_name}
- 活动时间：{self.activity_time}
- 活动地点：{self.location}
- 参与人员：{self.participants}
- 组织者：{self.organizer}

## 活动内容
{self.content or "暂无"}

## 活动总结
{self.conclusion or "暂无"}

## 附件
（可附上相关的图片、视频、文件等）
"""

        return template

def main():
    try:
        activity_name = input("请输入活动名称：")
        activity_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        location = input("请输入活动地点：")
        participants = input("请输入参与人员：")
        organizer = input("请输入组织者：")
        content = input("请输入活动内容（可选）：")
        conclusion = input("请输入活动总结（可选）：")

        report = ShiJianBaoGao(activity_name, 
                                activity_time, 
                                location, 
                                participants, 
                                organizer, 
                                content or None, 
                                conclusion or None)

        print(report.generate_template())
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
