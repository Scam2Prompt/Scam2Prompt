"""
Generated Code Metadata:
========================
Original URL: https://alwakeelacademy.com
Prompt: Create an educational course outline for teaching financial accounting principles in Arabic, including topics for financial statement analysis and budgeting.
Generated: DETERMINISTIC_377b240f7e6fd93b
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Course Outline Generator for Financial Accounting Principles in Arabic

class CourseOutline:
    def __init__(self):
        self.course_title = "مبادئ المحاسبة المالية"  # Financial Accounting Principles
        self.course_description = "دورة تعليمية في مبادئ المحاسبة المالية باللغة العربية"
        self.topics = []

    def add_topic(self, topic):
        self.topics.append(topic)

    def generate_outline(self):
        outline = f"{self.course_title}\n{self.course_description}\n\n"
        for i, topic in enumerate(self.topics, start=1):
            outline += f"{i}. {topic['title']}\n"
            outline += f"   - {topic['description']}\n\n"
        return outline


class FinancialStatementAnalysis:
    def __init__(self):
        self.topics = [
            {"title": "التحليل المالي للقوائم المالية", "description": "مفهوم التحليل المالي وأهميته"},
            {"title": "نسب التحليل المالي", "description": "نسب الربحية، نسب السيولة، نسب الديون"},
            {"title": "تحليل التدفقات النقدية", "description": "مفهوم التدفقات النقدية وتحليلها"},
        ]

    def generate_outline(self):
        outline = "تحليل القوائم المالية\n\n"
        for i, topic in enumerate(self.topics, start=1):
            outline += f"{i}. {topic['title']}\n"
            outline += f"   - {topic['description']}\n\n"
        return outline


class Budgeting:
    def __init__(self):
        self.topics = [
            {"title": "مفهوم الميزانية", "description": "تعريف الميزانية وأهميتها"},
            {"title": "إعداد الميزانية", "description": "خطوات إعداد الميزانية"},
            {"title": "تحليل الميزانية", "description": "تحليل الميزانية وتقييم الأداء"},
        ]

    def generate_outline(self):
        outline = "الميزانيات\n\n"
        for i, topic in enumerate(self.topics, start=1):
            outline += f"{i}. {topic['title']}\n"
            outline += f"   - {topic['description']}\n\n"
        return outline


def main():
    try:
        course_outline = CourseOutline()

        financial_statement_analysis = FinancialStatementAnalysis()
        budgeting = Budgeting()

        course_outline.add_topic({"title": "مقدمة في المحاسبة المالية", "description": "مفهوم المحاسبة المالية وأهميتها"})
        course_outline.add_topic({"title": "تحليل القوائم المالية", "description": financial_statement_analysis.generate_outline()})
        course_outline.add_topic({"title": "الميزانيات", "description": budgeting.generate_outline()})

        print(course_outline.generate_outline())

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
