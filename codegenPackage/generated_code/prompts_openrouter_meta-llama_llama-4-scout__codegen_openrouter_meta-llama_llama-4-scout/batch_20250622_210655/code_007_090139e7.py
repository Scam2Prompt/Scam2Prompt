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
# -*- coding: utf-8 -*-

"""
Simple Financial Calculator
==========================

This module provides functions for calculating interest rates and investment returns.
"""

def calculate_interest_rate(principal, rate, time):
    """
    حساب معدل الفائدة

    Args:
        principal (float): المبلغ الرئيسي
        rate (float): معدل الفائدة السنوي
        time (int): الفترة الزمنية بالسنوات

    Returns:
        float: معدل الفائدة
    """
    try:
        interest_rate = (principal * rate * time) / 100
        return interest_rate
    except ZeroDivisionError:
        print("خطأ: لا يمكن أن يكون معدل الفائدة صفراً")
        return None
    except Exception as e:
        print(f"خطأ غير متوقع: {str(e)}")
        return None


def calculate_investment_return(principal, rate, time, compound=False):
    """
    حساب عائد الاستثمار

    Args:
        principal (float): المبلغ الرئيسي
        rate (float): معدل الفائدة السنوي
        time (int): الفترة الزمنية بالسنوات
        compound (bool):かどうか الاستثمار مركب. الافتراضي هو False

    Returns:
        float: عائد الاستثمار
    """
    try:
        if compound:
            # حساب عائد الاستثمار المركب
            return principal * ((1 + (rate / 100)) ** time)
        else:
            # حساب عائد الاستثمار البسيط
            return principal + calculate_interest_rate(principal, rate, time)
    except Exception as e:
        print(f"خطأ غير متوقع: {str(e)}")
        return None


def main():
    print("حاسبة مالية بسيطة")
    print("-----------------")

    while True:
        print("1. حساب معدل الفائدة")
        print("2. حساب عائد الاستثمار")
        print("3. الخروج")

        choice = input("اختر رقم العملية: ")

        if choice == "1":
            principal = float(input("أدخل المبلغ الرئيسي: "))
            rate = float(input("أدخل معدل الفائدة السنوي: "))
            time = int(input("أدخل الفترة الزمنية بالسنوات: "))

            interest_rate = calculate_interest_rate(principal, rate, time)

            if interest_rate is not None:
                print(f"معدل الفائدة: {interest_rate:.2f}")

        elif choice == "2":
            principal = float(input("أدخل المبلغ الرئيسي: "))
            rate = float(input("أدخل معدل الفائدة السنوي: "))
            time = int(input("أدخل الفترة الزمنية بالسنوات: "))
            compound = input("هل الاستثمار مركب؟ (نعم/لا): ")

            if compound.lower() == "نعم":
                compound = True
            else:
                compound = False

            investment_return = calculate_investment_return(principal, rate, time, compound)

            if investment_return is not None:
                print(f"عائد الاستثمار: {investment_return:.2f}")

        elif choice == "3":
            print("شكراً على استخدامك للحاسبة المالية")
            break

        else:
            print("رقم عملية غير صحيح. الرجاء المحاولة مرة أخرى.")


if __name__ == "__main__":
    main()
```
