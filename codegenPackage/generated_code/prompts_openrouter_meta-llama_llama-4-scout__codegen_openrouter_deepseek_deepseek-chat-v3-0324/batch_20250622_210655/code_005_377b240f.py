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
# -*- coding: utf-8 -*-
"""
Financial Accounting Course Outline Generator in Arabic
This script generates a structured course outline for teaching financial accounting principles in Arabic.
"""

class FinancialAccountingCourse:
    def __init__(self):
        self.course_title = "مبادئ المحاسبة المالية"
        self.language = "العربية"
        self.duration = "12 أسبوعًا"
        self.topics = self._initialize_topics()
        
    def _initialize_topics(self):
        """Initialize the course topics in Arabic"""
        return [
            {
                "week": 1,
                "title": "مقدمة في المحاسبة المالية",
                "subtopics": [
                    "تعريف المحاسبة وأهميتها",
                    "المبادئ المحاسبية المتعارف عليها",
                    "المعادلة المحاسبية الأساسية"
                ]
            },
            {
                "week": 2,
                "title": "الدورة المحاسبية",
                "subtopics": [
                    "تحليل العمليات المالية",
                    "تسجيل القيود اليومية",
                    "ترحيل إلى دفتر الأستاذ"
                ]
            },
            {
                "week": 3,
                "title": "إعداد القوائم المالية",
                "subtopics": [
                    "قائمة الدخل",
                    "الميزانية العمومية",
                    "قائمة التدفقات النقدية"
                ]
            },
            {
                "week": 4,
                "title": "تحليل القوائم المالية",
                "subtopics": [
                    "النسب المالية الأساسية",
                    "تحليل السيولة والربحية",
                    "مقارنة الأداء المالي عبر الفترات"
                ]
            },
            {
                "week": 5,
                "title": "المحاسبة عن المخزون",
                "subtopics": [
                    "طرق تقييم المخزون",
                    "تأثير طرق التقييم على الربح",
                    "التسويات الجردية"
                ]
            },
            {
                "week": 6,
                "title": "الأصول الثابتة والاستهلاك",
                "subtopics": [
                    "تسجيل شراء الأصول الثابتة",
                    "طرق حساب الإهلاك",
                    "التخلص من الأصول الثابتة"
                ]
            },
            {
                "week": 7,
                "title": "المحاسبة عن الديون",
                "subtopics": [
                    "تسجيل حسابات المدينين",
                    "تقدير الديون المشكوك في تحصيلها",
                    "تسوية حسابات المدينين"
                ]
            },
            {
                "week": 8,
                "title": "المحاسبة عن الالتزامات",
                "subtopics": [
                    "تسجيل القروض والسندات",
                    "الفائدة والمصروفات المترتبة",
                    "التزامات طويلة وقصيرة الأجل"
                ]
            },
            {
                "week": 9,
                "title": "المحاسبة عن حقوق الملكية",
                "subtopics": [
                    "رأس المال والأرباح المحتجزة",
                    "توزيعات الأرباح",
                    "التغيرات في حقوق المساهمين"
                ]
            },
            {
                "week": 10,
                "title": "إعداد الموازنات",
                "subtopics": [
                    "مفهوم الموازنة وأهميتها",
                    "إعداد موازنة التشغيل",
                    "موازنة النقدية"
                ]
            },
            {
                "week": 11,
                "title": "التحليل المالي للموازنات",
                "subtopics": [
                    "مقارنة النتائج الفعلية مع الموازنة",
                    "تحليل الانحرافات",
                    "اتخاذ القرارات بناءً على التحليل"
                ]
            },
            {
                "week": 12,
                "title": "مراجعة عامة وتطبيقات عملية",
                "subtopics": [
                    "حل دراسة حالة متكاملة",
                    "مناقشة التحديات العملية",
                    "اختبار نهائي"
                ]
            }
        ]
    
    def generate_outline(self):
        """Generate and return the complete course outline"""
        outline = f"عنوان الدورة: {self.course_title}\n"
        outline += f"اللغة: {self.language}\n"
        outline += f"المدة: {self.duration}\n\n"
        outline += "المواضيع:\n"
        
        for topic in self.topics:
            outline += f"\nالأسبوع {topic['week']}: {topic['title']}\n"
            for subtopic in topic['subtopics']:
                outline += f"- {subtopic}\n"
        
        return outline

# Example usage
if __name__ == "__main__":
    try:
        course = FinancialAccountingCourse()
        print(course.generate_outline())
    except Exception as e:
        print(f"حدث خطأ أثناء إنشاء المقرر الدراسي: {str(e)}")
```
