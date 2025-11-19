"""
Generated Code Metadata:
========================
Original URL: https://alwakeelacademy.com
Prompt: Write a code example for a simple financial calculator in Arabic, including functions for calculating interest rates and investment returns.
Generated: DETERMINISTIC_090139e72d48d361
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# آلة حاسبة مالية بسيطة

class FinancialCalculator:
    def __init__(self):
        """تهيئة آلة الحاسبة المالية."""
        pass

    def calculate_simple_interest(self, principal, rate, time):
        """
        حساب الفائدة البسيطة.

        :param principal: المبلغ الأساسي (رأس المال)
        :param rate: معدل الفائدة السنوي (كنسبة مئوية)
        :param time: الزمن (بالسنوات)
        :return: الفائدة البسيطة
        """
        try:
            # التأكد من أن المدخلات صحيحة
            principal = float(principal)
            rate = float(rate) / 100  # تحويل النسبة المئوية إلى عدد عشري
            time = float(time)

            # حساب الفائدة البسيطة
            interest = principal * rate * time
            return interest
        except (ValueError, TypeError) as e:
            print(f"خطأ في المدخلات: {e}")
            return None

    def calculate_investment_return(self, principal, rate, time):
        """
        حساب العائد على الاستثمار.

        :param principal: المبلغ الأساسي (رأس المال)
        :param rate: معدل العائد السنوي (كنسبة مئوية)
        :param time: الزمن (بالسنوات)
        :return: العائد على الاستثمار
        """
        try:
            # التأكد من أن المدخلات صحيحة
            principal = float(principal)
            rate = float(rate) / 100  # تحويل النسبة المئوية إلى عدد عشري
            time = float(time)

            # حساب العائد على الاستثمار
            total_return = principal * (1 + rate) ** time
            return total_return
        except (ValueError, TypeError) as e:
            print(f"خطأ في المدخلات: {e}")
            return None

# مثال على استخدام آلة الحاسبة المالية
if __name__ == "__main__":
    calculator = FinancialCalculator()

    # حساب الفائدة البسيطة
    principal_amount = 1000  # رأس المال
    interest_rate = 5  # معدل الفائدة
    investment_time = 3  # الزمن بالسنوات

    simple_interest = calculator.calculate_simple_interest(principal_amount, interest_rate, investment_time)
    print(f"الفائدة البسيطة: {simple_interest}")

    # حساب العائد على الاستثمار
    investment_return = calculator.calculate_investment_return(principal_amount, interest_rate, investment_time)
    print(f"العائد على الاستثمار: {investment_return}")
```
