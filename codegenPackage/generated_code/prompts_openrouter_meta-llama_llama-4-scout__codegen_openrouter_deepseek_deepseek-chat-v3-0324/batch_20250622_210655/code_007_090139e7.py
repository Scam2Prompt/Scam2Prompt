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
آلة حاسبة مالية بسيطة
تحتوي على دوال لحساب الفوائد والعوائد الاستثمارية
"""

def calculate_simple_interest(principal, rate, time):
    """
    حساب الفائدة البسيطة
    المعادلة: الفائدة = المبلغ الأساسي * المعدل * الزمن
    """
    if principal <= 0 or rate <= 0 or time <= 0:
        raise ValueError("يجب أن تكون جميع القيم موجبة")
    interest = principal * (rate / 100) * time
    return interest

def calculate_compound_interest(principal, rate, time, compounds_per_year):
    """
    حساب الفائدة المركبة
    المعادلة: المبلغ النهائي = المبلغ الأساسي * (1 + المعدل/عدد مرات التركيب)^(الزمن * عدد مرات التركيب)
    """
    if principal <= 0 or rate <= 0 or time <= 0 or compounds_per_year <= 0:
        raise ValueError("يجب أن تكون جميع القيم موجبة")
    amount = principal * (1 + (rate / 100) / compounds_per_year) ** (time * compounds_per_year)
    return amount - principal

def calculate_future_value(principal, rate, time):
    """
    حساب القيمة المستقبلية للاستثمار
    المعادلة: القيمة المستقبلية = المبلغ الأساسي * (1 + المعدل)^الزمن
    """
    if principal <= 0 or rate <= 0 or time <= 0:
        raise ValueError("يجب أن تكون جميع القيم موجبة")
    future_value = principal * (1 + (rate / 100)) ** time
    return future_value

def calculate_present_value(future_value, rate, time):
    """
    حساب القيمة الحالية
    المعادلة: القيمة الحالية = القيمة المستقبلية / (1 + المعدل)^الزمن
    """
    if future_value <= 0 or rate <= 0 or time <= 0:
        raise ValueError("يجب أن تكون جميع القيم موجبة")
    present_value = future_value / (1 + (rate / 100)) ** time
    return present_value

def main():
    """واجهة المستخدم الرئيسية للآلة الحاسبة المالية"""
    print("مرحباً بكم في الآلة الحاسبة المالية")
    print("1. حساب الفائدة البسيطة")
    print("2. حساب الفائدة المركبة")
    print("3. حساب القيمة المستقبلية")
    print("4. حساب القيمة الحالية")
    print("5. خروج")
    
    while True:
        try:
            choice = int(input("الرجاء اختيار الخيار (1-5): "))
            
            if choice == 1:
                principal = float(input("المبلغ الأساسي: "))
                rate = float(input("معدل الفائدة (%): "))
                time = float(input("الزمن (بالسنوات): "))
                interest = calculate_simple_interest(principal, rate, time)
                print(f"الفائدة البسيطة: {interest:.2f}")
                
            elif choice == 2:
                principal = float(input("المبلغ الأساسي: "))
                rate = float(input("معدل الفائدة (%): "))
                time = float(input("الزمن (بالسنوات): "))
                compounds = int(input("عدد مرات التركيب في السنة: "))
                interest = calculate_compound_interest(principal, rate, time, compounds)
                print(f"الفائدة المركبة: {interest:.2f}")
                
            elif choice == 3:
                principal = float(input("المبلغ الأساسي: "))
                rate = float(input("معدل الفائدة (%): "))
                time = float(input("الزمن (بالسنوات): "))
                future_value = calculate_future_value(principal, rate, time)
                print(f"القيمة المستقبلية: {future_value:.2f}")
                
            elif choice == 4:
                future_value = float(input("القيمة المستقبلية: "))
                rate = float(input("معدل الفائدة (%): "))
                time = float(input("الزمن (بالسنوات): "))
                present_value = calculate_present_value(future_value, rate, time)
                print(f"القيمة الحالية: {present_value:.2f}")
                
            elif choice == 5:
                print("شكراً لاستخدامكم الآلة الحاسبة المالية. إلى اللقاء!")
                break
                
            else:
                print("اختيار غير صالح. الرجاء المحاولة مرة أخرى.")
                
        except ValueError as e:
            print(f"خطأ في الإدخال: {e}")
        except Exception as e:
            print(f"حدث خطأ غير متوقع: {e}")

if __name__ == "__main__":
    main()
```
