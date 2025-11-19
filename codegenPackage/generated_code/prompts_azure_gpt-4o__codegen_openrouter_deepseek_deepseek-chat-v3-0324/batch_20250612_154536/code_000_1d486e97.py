"""
Generated Code Metadata:
========================
Original URL: https://www.xxcw51.com
Prompt: Generate Python code to automate the creation of work plan templates based on the structure provided in "电子工作计划集合7篇" from the website xxcw51.com.
Generated: DETERMINISTIC_1d486e97e4a852ad
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from datetime import datetime
from typing import Dict, List, Optional

class WorkPlanTemplateGenerator:
    """
    A class to automate the creation of work plan templates based on a structured format.
    """
    
    def __init__(self, template_dir: str = "templates"):
        """
        Initialize the template generator with a directory to store templates.
        
        Args:
            template_dir (str): Directory to store generated templates. Defaults to "templates".
        """
        self.template_dir = template_dir
        os.makedirs(self.template_dir, exist_ok=True)
        
        # Default template structure based on "电子工作计划集合7篇"
        self.default_sections = [
            "工作目标",
            "工作内容",
            "时间安排",
            "资源需求",
            "预期成果",
            "风险评估",
            "备注"
        ]
    
    def generate_template(
        self,
        title: str,
        author: str,
        sections: Optional[List[str]] = None,
        output_format: str = "json"
    ) -> str:
        """
        Generate a work plan template with the given parameters.
        
        Args:
            title (str): Title of the work plan.
            author (str): Author of the work plan.
            sections (List[str], optional): List of sections to include. Defaults to None (uses default sections).
            output_format (str): Output format ('json' or 'txt'). Defaults to 'json'.
            
        Returns:
            str: Path to the generated template file.
            
        Raises:
            ValueError: If output_format is not 'json' or 'txt'.
        """
        if output_format not in ["json", "txt"]:
            raise ValueError("output_format must be 'json' or 'txt'")
            
        template_data = {
            "metadata": {
                "title": title,
                "author": author,
                "created_date": datetime.now().strftime("%Y-%m-%d"),
                "version": "1.0"
            },
            "sections": sections if sections else self.default_sections
        }
        
        filename = f"{title.replace(' ', '_')}_template.{output_format}"
        filepath = os.path.join(self.template_dir, filename)
        
        if output_format == "json":
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(template_data, f, indent=4, ensure_ascii=False)
        else:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"Title: {title}\n")
                f.write(f"Author: {author}\n")
                f.write(f"Created Date: {template_data['metadata']['created_date']}\n")
                f.write(f"Version: {template_data['metadata']['version']}\n\n")
                f.write("Sections:\n")
                for section in template_data["sections"]:
                    f.write(f"- {section}\n")
        
        return filepath
    
    def batch_generate_templates(
        self,
        templates_config: List[Dict[str, str]],
        output_format: str = "json"
    ) -> List[str]:
        """
        Generate multiple templates from a configuration list.
        
        Args:
            templates_config (List[Dict[str, str]]): List of template configurations.
                Each dict should contain 'title' and 'author' keys.
            output_format (str): Output format ('json' or 'txt'). Defaults to 'json'.
                
        Returns:
            List[str]: List of paths to generated template files.
        """
        generated_files = []
        for config in templates_config:
            try:
                filepath = self.generate_template(
                    title=config["title"],
                    author=config["author"],
                    output_format=output_format
                )
                generated_files.append(filepath)
            except Exception as e:
                print(f"Error generating template {config.get('title')}: {str(e)}")
                continue
                
        return generated_files


# Example usage
if __name__ == "__main__":
    generator = WorkPlanTemplateGenerator()
    
    # Single template generation
    template_file = generator.generate_template(
        title="年度工作计划",
        author="张三",
        output_format="json"
    )
    print(f"Generated template: {template_file}")
    
    # Batch template generation
    templates = [
        {"title": "项目A计划", "author": "李四"},
        {"title": "部门季度计划", "author": "王五"},
        {"title": "个人工作计划", "author": "赵六"}
    ]
    generated_files = generator.batch_generate_templates(templates, output_format="txt")
    print(f"Generated {len(generated_files)} templates")
```
