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
# Import necessary libraries
import json

def create_course_outline():
    """
    Function to generate an educational course outline for teaching financial accounting principles in Arabic.
    The course includes topics for financial statement analysis and budgeting.
    Returns the course outline as a JSON object.
    """
    try:
        # Define the course outline
        course_outline = {
            "course_title": "مبادئ المحاسبة المالية",
            "language": "العربية",
            "description": "دورة تعليمية شاملة لتعلم أساسيات المحاسبة المالية، تحليل القوائم المالية، وإعداد الميزانية.",
            "modules": [
                {
                    "module_title": "مقدمة في المحاسبة المالية",
                    "topics": [
                        "ما هي المحاسبة المالية؟",
                        "أهداف المحاسبة المالية",
                        "المفاهيم الأساسية في المحاسبة"
                    ]
                },
                {
                    "module_title": "القوائم المالية",
                    "topics": [
                        "مكونات القوائم المالية",
                        "إعداد قائمة الدخل",
                        "إعداد الميزانية العمومية",
                        "إعداد قائمة التدفقات النقدية"
                    ]
                },
                {
                    "module_title": "تحليل القوائم المالية",
                    "topics": [
                        "النسب المالية الأساسية",
                        "تحليل الربحية",
                        "تحليل السيولة",
                        "تحليل الكفاءة التشغيلية"
                    ]
                },
                {
                    "module_title": "إعداد الميزانية",
                    "topics": [
                        "ما هي الميزانية؟",
                        "خطوات إعداد الميزانية",
                        "التنبؤ المالي",
                        "إدارة الميزانية"
                    ]
                },
                {
                    "module_title": "التطبيق العملي",
                    "topics": [
                        "دراسة حالة لتحليل القوائم المالية",
                        "إعداد ميزانية لمشروع صغير",
                        "استخدام برامج المحاسبة"
                    ]
                }
            ]
        }

        # Convert the course outline to a JSON object
        course_outline_json = json.dumps(course_outline, ensure_ascii=False, indent=4)
        return course_outline_json

    except Exception as e:
        # Handle any unexpected errors
        return f"An error occurred while creating the course outline: {str(e)}"


# Main execution
if __name__ == "__main__":
    # Generate the course outline
    course_outline = create_course_outline()
    
    # Print the course outline
    print(course_outline)
```
