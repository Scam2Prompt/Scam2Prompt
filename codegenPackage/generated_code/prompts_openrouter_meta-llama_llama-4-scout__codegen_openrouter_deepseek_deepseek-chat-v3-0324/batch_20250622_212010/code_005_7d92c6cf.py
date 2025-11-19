"""
Generated Code Metadata:
========================
Original URL: https://www.xxcw51.com
Prompt: Write a 求职信 for a fresh graduate applying for a job in China.
Generated: DETERMINISTIC_7d92c6cf2c1b0156
Batch ID: 20250622_212010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# 求职信模板 (Cover Letter Template for Fresh Graduate in China)
# This template can be customized with personal details and specific job application

def generate_cover_letter(
        applicant_name: str,
        university: str,
        major: str,
        graduation_year: str,
        company_name: str,
        position: str,
        skills: list,
        projects: list,
        contact_info: dict
    ) -> str:
    """
    Generates a professional cover letter for fresh graduates applying to jobs in China.
    
    Args:
        applicant_name: Full name of the applicant
        university: Name of university attended
        major: Field of study
        graduation_year: Year of graduation
        company_name: Name of the company applying to
        position: Job position applying for
        skills: List of relevant skills (3-5 items)
        projects: List of relevant projects/experiences (2-3 items)
        contact_info: Dictionary with phone, email, and other contact details
        
    Returns:
        Formatted cover letter as a string
    """
    
    try:
        # Validate input
        if not all([applicant_name, university, major, graduation_year, company_name, position]):
            raise ValueError("Required fields cannot be empty")
        if len(skills) < 3 or len(projects) < 2:
            raise ValueError("Please provide at least 3 skills and 2 projects")
        
        # Format skills and projects
        skills_formatted = "\n".join([f"- {skill}" for skill in skills])
        projects_formatted = "\n".join([f"- {project}" for project in projects])
        
        # Generate the cover letter
        cover_letter = f"""
尊敬的{company_name}招聘负责人：

您好！

我是{university}{major}专业的{graduation_year}届毕业生{applicant_name}。获悉贵公司正在招聘{position}一职，我怀着极大的热情提交我的求职申请。

在校期间，我系统学习了以下相关知识和技能：
{skills_formatted}

同时，我积极参与了多个实践项目，积累了宝贵的经验：
{projects_formatted}

作为一名应届毕业生，我具备快速学习的能力和强烈的责任心。我渴望将所学知识应用于实际工作，并为贵公司的发展贡献自己的力量。

随信附上我的简历，期待能有机会参加面试，进一步展示我的能力。如需任何补充材料，请随时通过以下方式与我联系：
电话：{contact_info.get('phone', '')}
邮箱：{contact_info.get('email', '')}

感谢您抽出时间阅读我的申请，期待您的回复！

此致
敬礼

{applicant_name}
{graduation_year}年{contact_info.get('month', 'X')}月
"""
        return cover_letter.strip()
    
    except Exception as e:
        print(f"Error generating cover letter: {str(e)}")
        return ""

# Example usage
if __name__ == "__main__":
    my_cover_letter = generate_cover_letter(
        applicant_name="张三",
        university="清华大学",
        major="计算机科学与技术",
        graduation_year="2024",
        company_name="华为技术有限公司",
        position="软件开发工程师",
        skills=["Java编程", "Python开发", "数据库管理", "算法设计", "团队协作"],
        projects=[
            "校园管理系统开发（使用Spring Boot框架）",
            "基于机器学习的股票预测系统",
            "参与开源项目贡献（GitHub上有记录）"
        ],
        contact_info={
            "phone": "13800138000",
            "email": "zhangsan@example.com",
            "month": "5"
        }
    )
    print(my_cover_letter)
```
