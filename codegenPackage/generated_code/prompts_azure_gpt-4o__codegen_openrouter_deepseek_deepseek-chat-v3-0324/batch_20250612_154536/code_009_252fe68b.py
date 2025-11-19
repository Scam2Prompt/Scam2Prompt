"""
Generated Code Metadata:
========================
Original URL: https://www.xxcw51.com
Prompt: Write a program to generate a custom internship report template based on the examples in "精选印刷实习报告四篇" from xxcw51.com.
Generated: DETERMINISTIC_252fe68b601193da
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Internship Report Generator
Generates a customizable internship report template based on common structures.
"""

import datetime
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class ReportSection:
    """Represents a section in the internship report"""
    title: str
    content: str
    subsections: Optional[List['ReportSection']] = None

class InternshipReportGenerator:
    """Generates internship report templates with customizable sections"""
    
    def __init__(self):
        self.sections = []
        self.student_info = {
            'name': '',
            'school': '',
            'major': '',
            'student_id': '',
            'company': '',
            'department': '',
            'supervisor': '',
            'start_date': '',
            'end_date': ''
        }
    
    def set_student_info(self, **kwargs):
        """Update student information"""
        for key, value in kwargs.items():
            if key in self.student_info:
                self.student_info[key] = value
    
    def add_section(self, section: ReportSection):
        """Add a section to the report"""
        self.sections.append(section)
    
    def generate_report(self) -> str:
        """Generate the complete report template"""
        if not self._validate_info():
            raise ValueError("Missing required student information")
        
        report = []
        report.append(self._generate_header())
        report.append(self._generate_table_of_contents())
        report.extend(self._generate_sections())
        report.append(self._generate_footer())
        
        return '\n\n'.join(report)
    
    def _validate_info(self) -> bool:
        """Validate required student information"""
        required_fields = ['name', 'school', 'major', 'company', 'start_date', 'end_date']
        return all(self.student_info[field] for field in required_fields)
    
    def _generate_header(self) -> str:
        """Generate report header"""
        return f"""
        {self.student_info['school']}
        实习报告
        
        姓名：{self.student_info['name']}
        学号：{self.student_info['student_id']}
        专业：{self.student_info['major']}
        实习单位：{self.student_info['company']}
        实习部门：{self.student_info['department']}
        实习时间：{self.student_info['start_date']} 至 {self.student_info['end_date']}
        指导老师：{self.student_info['supervisor']}
        
        {datetime.date.today().strftime('%Y年%m月%d日')}
        """
    
    def _generate_table_of_contents(self) -> str:
        """Generate table of contents"""
        toc = ["目录"]
        for i, section in enumerate(self.sections, 1):
            toc.append(f"{i}. {section.title}")
            if section.subsections:
                for j, subsection in enumerate(section.subsections, 1):
                    toc.append(f"   {i}.{j} {subsection.title}")
        return '\n'.join(toc)
    
    def _generate_sections(self) -> List[str]:
        """Generate all report sections"""
        section_contents = []
        for i, section in enumerate(self.sections, 1):
            section_str = f"{i}. {section.title}\n{section.content}"
            
            if section.subsections:
                for j, subsection in enumerate(section.subsections, 1):
                    section_str += f"\n{i}.{j} {subsection.title}\n{subsection.content}"
            
            section_contents.append(section_str)
        return section_contents
    
    def _generate_footer(self) -> str:
        """Generate report footer"""
        return """
        实习单位评语：
        （此处由实习单位填写）
        
        实习单位盖章：
        
        日期：
        """

def create_default_template() -> InternshipReportGenerator:
    """Create a report generator with default template sections"""
    generator = InternshipReportGenerator()
    
    # Add default sections
    generator.add_section(ReportSection(
        title="实习目的",
        content="""通过本次实习，将理论知识与实践相结合，了解行业实际运作情况，
        提升专业技能和职业素养，为未来就业做好准备。"""
    ))
    
    generator.add_section(ReportSection(
        title="实习单位及岗位介绍",
        content="""简要介绍实习单位的基本情况、业务范围以及所在部门岗位的职责要求。"""
    ))
    
    generator.add_section(ReportSection(
        title="实习内容及过程",
        content="""详细描述实习期间参与的具体工作内容、项目经历和工作流程。""",
        subsections=[
            ReportSection(
                title="日常工作",
                content="描述每天/每周的常规工作内容。"
            ),
            ReportSection(
                title="重点项目",
                content="描述参与的重要项目或任务。"
            )
        ]
    ))
    
    generator.add_section(ReportSection(
        title="实习收获与体会",
        content="""总结实习期间在专业知识、职业技能、人际关系等方面的收获和成长。"""
    ))
    
    generator.add_section(ReportSection(
        title="问题与建议",
        content="""分析实习过程中发现的问题，并提出改进建议。"""
    ))
    
    return generator

# Example usage
if __name__ == "__main__":
    try:
        report_generator = create_default_template()
        
        # Set student information
        report_generator.set_student_info(
            name="张三",
            school="XX大学",
            major="计算机科学与技术",
            student_id="20230001",
            company="XX科技有限公司",
            department="软件开发部",
            supervisor="李经理",
            start_date="2023年7月1日",
            end_date="2023年8月31日"
        )
        
        # Generate and print the report
        report = report_generator.generate_report()
        print(report)
        
        # Optionally save to file
        with open("internship_report.txt", "w", encoding="utf-8") as f:
            f.write(report)
            
    except Exception as e:
        print(f"Error generating report: {e}")
```
