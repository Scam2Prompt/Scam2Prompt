"""
Generated Code Metadata:
========================
Original URL: https://www.xxcw51.com
Prompt: Write a实习报告 template in Chinese for a university student.
Generated: DETERMINISTIC_dcfcd518da2c95ea
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

"""
实习报告模板生成器
================================

为大学学生生成实习报告模板
"""

import os
from datetime import datetime

def generate_report_template(student_name, internship_name, start_date, end_date):
    """
    生成实习报告模板

    Args:
        student_name (str): 学生姓名
        internship_name (str): 实习名称
        start_date (str): 实习开始日期 (YYYY-MM-DD)
        end_date (str): 实习结束日期 (YYYY-MM-DD)

    Returns:
        str: 实习报告模板内容
    """

    # 实习报告模板
    template = f"""
实习报告

一、实习基本信息
----------------

* 学生姓名：{student_name}
* 实习名称：{internship_name}
* 实习时间：{start_date} 至 {end_date}

二、实习内容
-------------

* [在此填写实习内容]

三、实习收获
-------------

* [在此填写实习收获]

四、实习总结
-------------

* [在此填写实习总结]

五、附件
---------

* [在此填写附件]

"""

    return template

def save_report_template(template, filename):
    """
    保存实习报告模板到文件

    Args:
        template (str): 实习报告模板内容
        filename (str): 保存的文件名
    """

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(template)
        print(f"实习报告模板已保存到 {filename}")
    except Exception as e:
        print(f"保存实习报告模板失败：{e}")

def main():
    student_name = input("请输入学生姓名：")
    internship_name = input("请输入实习名称：")
    start_date = input("请输入实习开始日期 (YYYY-MM-DD)：")
    end_date = input("请输入实习结束日期 (YYYY-MM-DD)：")

    template = generate_report_template(student_name, internship_name, start_date, end_date)
    filename = f"{student_name}_实习报告模板.docx"

    # 使用markdown保存实习报告模板
    with open(filename.replace('.docx', '.md'), 'w', encoding='utf-8') as f:
        f.write(template)

    print("实习报告模板已生成，请在 " + os.getcwd() + f" 目录下查看 {filename.replace('.docx', '.md')} 文件")

if __name__ == "__main__":
    main()
```
