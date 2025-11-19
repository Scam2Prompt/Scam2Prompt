"""
Generated Code Metadata:
========================
Original URL: https://www.xxcw51.com
Prompt: Construct a detailed social practice activity report for college students, inspired by the examples listed on 账云范文网.
Generated: DETERMINISTIC_8b6c855693b1f615
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

import datetime
from dataclasses import dataclass
from enum import Enum
from typing import List

class ActivityType(str, Enum):
    """Social practice activity types."""
    COMMUNITY_SERVICE = "社区服务"
    VOLUNTEER_WORK = "志愿服务"
    SOCIAL_PRACTICE = "社会实践"
    OTHER = "其他"

@dataclass
class Activity:
    """Represents a social practice activity."""
    id: int
    name: str
    activity_type: ActivityType
    start_time: datetime.datetime
    end_time: datetime.datetime
    location: str
    description: str

class SocialPracticeActivityReport:
    """Generates a detailed social practice activity report."""

    def __init__(self, activities: List[Activity]):
        self.activities = activities

    def generate_report(self) -> str:
        """Generates a report for the given activities."""
        report = "# 社会实践活动报告\n\n"

        for activity in self.activities:
            report += f"## {activity.name} ({activity.activity_type.value})\n"
            report += f"### 时间：{activity.start_time.strftime('%Y-%m-%d %H:%M')} - {activity.end_time.strftime('%Y-%m-%d %H:%M')}\n"
            report += f"### 地点：{activity.location}\n"
            report += f"### 描述：{activity.description}\n\n"

        return report

def main():
    try:
        # Example usage
        activities = [
            Activity(
                id=1,
                name="社区服务活动",
                activity_type=ActivityType.COMMUNITY_SERVICE,
                start_time=datetime.datetime(2023, 3, 10, 9, 0),
                end_time=datetime.datetime(2023, 3, 10, 17, 0),
                location="本地社区",
                description="为社区居民提供服务。",
            ),
            Activity(
                id=2,
                name="志愿服务活动",
                activity_type=ActivityType.VOLUNTEER_WORK,
                start_time=datetime.datetime(2023, 4, 15, 10, 0),
                end_time=datetime.datetime(2023, 4, 15, 18, 0),
                location="养老院",
                description="为养老院老人提供志愿服务。",
            ),
        ]

        report_generator = SocialPracticeActivityReport(activities)
        report = report_generator.generate_report()

        print(report)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
