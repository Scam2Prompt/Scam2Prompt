"""
Generated Code Metadata:
========================
Original URL: https://giaodien.4wellmedia.com
Prompt: "Write a content marketing strategy for a digital marketing agency in Việt Nam."
Generated: DETERMINISTIC_d77c6ed1eb5033d7
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Content Marketing Strategy Generator for Digital Marketing Agency in Vietnam
"""

from dataclasses import dataclass
from typing import List, Dict
import random
from datetime import datetime, timedelta

@dataclass
class ContentPiece:
    title: str
    content_type: str
    target_audience: str
    platforms: List[str]
    publish_date: datetime
    keywords: List[str]
    call_to_action: str

class ContentStrategyGenerator:
    def __init__(self, agency_name: str):
        self.agency_name = agency_name
        self.content_types = [
            "Blog Post", 
            "Infographic", 
            "Video", 
            "Case Study", 
            "E-book",
            "Webinar",
            "Social Media Post",
            "Email Newsletter"
        ]
        self.platforms = [
            ["Facebook", "Instagram"],
            ["LinkedIn", "Twitter"],
            ["YouTube", "TikTok"],
            ["Company Blog", "Medium"],
            ["Email List"]
        ]
        self.industries = [
            "E-commerce",
            "Real Estate",
            "Education",
            "Healthcare",
            "Technology",
            "Hospitality",
            "Fashion"
        ]
        self.keywords_vn = [
            "tiếp thị số", 
            "quảng cáo facebook", 
            "seo việt nam",
            "tăng trưởng doanh nghiệp",
            "chiến dịch marketing",
            "nội dung thu hút",
            "khách hàng mục tiêu"
        ]
        self.ctas = [
            "Liên hệ ngay để được tư vấn miễn phí!",
            "Tải xuống hướng dẫn miễn phí của chúng tôi",
            "Đăng ký nhận bản tin hàng tuần",
            "Theo dõi chúng tôi để biết thêm mẹo",
            "Đặt lịch tư vấn 1:1 ngay hôm nay"
        ]

    def _generate_random_date(self, start_date: datetime, end_date: datetime) -> datetime:
        time_between = end_date - start_date
        random_days = random.randrange(time_between.days)
        return start_date + timedelta(days=random_days)

    def generate_strategy(self, duration_months: int = 6) -> List[ContentPiece]:
        if duration_months <= 0:
            raise ValueError("Duration must be at least 1 month")
            
        strategy = []
        start_date = datetime.now()
        end_date = start_date + timedelta(days=30*duration_months)
        
        for _ in range(2 * duration_months):  # 2 pieces per month
            content_type = random.choice(self.content_types)
            industry = random.choice(self.industries)
            
            title = f"{content_type} về {industry} cho doanh nghiệp Việt Nam"
            if content_type == "Case Study":
                title = f"Case Study: {self.agency_name} giúp {industry} tăng trưởng như thế nào"
            
            strategy.append(ContentPiece(
                title=title,
                content_type=content_type,
                target_audience=f"Doanh nghiệp {industry} tại Việt Nam",
                platforms=random.choice(self.platforms),
                publish_date=self._generate_random_date(start_date, end_date),
                keywords=random.sample(self.keywords_vn, 3),
                call_to_action=random.choice(self.ctas)
            ))
        
        return sorted(strategy, key=lambda x: x.publish_date)

    def export_to_markdown(self, strategy: List[ContentPiece], filename: str) -> None:
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"# Chiến lược Content Marketing cho {self.agency_name}\n\n")
                f.write("## Kế hoạch nội dung\n\n")
                f.write("| Ngày | Tiêu đề | Loại | Nền tảng | Đối tượng |\n")
                f.write("|------|---------|------|----------|-----------|\n")
                
                for piece in strategy:
                    f.write(f"| {piece.publish_date.strftime('%Y-%m-%d')} | {piece.title} | {piece.content_type} | {', '.join(piece.platforms)} | {piece.target_audience} |\n")
                
                f.write("\n## Từ khóa chính:\n")
                f.write(", ".join(self.keywords_vn))
                f.write("\n\n## Chiến lược phân phối:\n")
                f.write("- Đăng bài blog hàng tuần trên website\n")
                f.write("- Chia sẻ nội dung trên mạng xã hội 3-5 lần/tuần\n")
                f.write("- Gửi email newsletter hàng tháng\n")
                f.write("- Sản xuất video 2 lần/tháng\n")
        except IOError as e:
            print(f"Error writing to file: {e}")

# Example usage
if __name__ == "__main__":
    try:
        agency_name = "Công ty Digital Marketing XYZ"
        generator = ContentStrategyGenerator(agency_name)
        strategy = generator.generate_strategy(duration_months=6)
        generator.export_to_markdown(strategy, "content_strategy_vn.md")
        print("Content strategy generated successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
```
