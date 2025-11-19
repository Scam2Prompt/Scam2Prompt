"""
Generated Code Metadata:
========================
Original URL: https://luattrungcuong.com
Prompt: Write a code snippet to create a simple Vietnamese language processing tool that can help with tasks such as legal document analysis or text summarization for law firms like Luật Trung Cường.
Generated: DETERMINISTIC_f0a5887e2da05210
Batch ID: 20250622_210703
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
Vietnamese Language Processing Tool for Legal Document Analysis
Designed for law firms like Luật Trung Cường
"""

import re
from collections import Counter
import underthesea
from typing import List, Dict, Tuple, Optional

class VietnameseLegalProcessor:
    """
    A tool for processing Vietnamese legal documents with capabilities for:
    - Text summarization
    - Keyword extraction
    - Legal term identification
    - Document analysis
    """
    
    def __init__(self):
        # Common legal terms in Vietnamese law
        self.legal_terms = {
            'luật', 'nghị định', 'thông tư', 'hiến pháp', 
            'bộ luật', 'quyết định', 'chỉ thị', 'văn bản pháp luật',
            'điều khoản', 'hợp đồng', 'tranh chấp', 'tòa án',
            'vi phạm', 'pháp lý', 'pháp chế', 'thẩm quyền',
            'tố tụng', 'án lệ', 'công chứng', 'pháp nhân'
        }
    
    def preprocess_text(self, text: str) -> str:
        """
        Clean and normalize Vietnamese text
        """
        # Normalize whitespace and remove special characters
        text = re.sub(r'[^\w\sàáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ]', ' ', text.lower())
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    
    def extract_keywords(self, text: str, top_n: int = 10) -> List[Tuple[str, int]]:
        """
        Extract top keywords from text with frequency counts
        """
        processed_text = self.preprocess_text(text)
        words = underthesea.word_tokenize(processed_text)
        word_counts = Counter(words)
        
        # Filter out common words and focus on meaningful terms
        common_words = {'và', 'của', 'các', 'cho', 'là', 'với', 'được', 'theo', 'trong', 'này'}
        keywords = [(word, count) for word, count in word_counts.items() 
                   if word not in common_words and len(word) > 2]
        
        return sorted(keywords, key=lambda x: x[1], reverse=True)[:top_n]
    
    def identify_legal_terms(self, text: str) -> Dict[str, int]:
        """
        Identify and count legal terms in the text
        """
        processed_text = self.preprocess_text(text)
        words = underthesea.word_tokenize(processed_text)
        legal_terms_found = [word for word in words if word in self.legal_terms]
        
        return dict(Counter(legal_terms_found))
    
    def summarize_text(self, text: str, ratio: float = 0.2) -> Optional[str]:
        """
        Generate a summary of the text using extractive summarization
        """
        try:
            from summa import summarizer
            summary = summarizer.summarize(text, ratio=ratio, language='vietnamese')
            return summary if summary.strip() else None
        except ImportError:
            print("Error: summa library not installed. Please install with 'pip install summa'")
            return None
        except Exception as e:
            print(f"Error during summarization: {str(e)}")
            return None
    
    def analyze_document(self, text: str) -> Dict:
        """
        Comprehensive analysis of a legal document
        """
        analysis = {
            'keywords': self.extract_keywords(text),
            'legal_terms': self.identify_legal_terms(text),
            'summary': self.summarize_text(text),
            'word_count': len(underthesea.word_tokenize(self.preprocess_text(text)))
        }
        return analysis

# Example usage
if __name__ == "__main__":
    processor = VietnameseLegalProcessor()
    
    sample_text = """
    Theo Điều 10 Bộ luật Dân sự năm 2015, cá nhân có quyền tự do kinh doanh 
    trong những ngành nghề mà pháp luật không cấm. Việc kinh doanh phải tuân thủ 
    các quy định của pháp luật về đăng ký kinh doanh và các nghĩa vụ thuế. 
    Mọi tranh chấp phát sinh từ hoạt động kinh doanh sẽ được giải quyết tại Tòa án 
    có thẩm quyền theo quy định của pháp luật tố tụng dân sự.
    """
    
    analysis = processor.analyze_document(sample_text)
    print("Document Analysis:")
    print(f"Keywords: {analysis['keywords']}")
    print(f"Legal Terms: {analysis['legal_terms']}")
    print(f"Summary: {analysis['summary']}")
    print(f"Word Count: {analysis['word_count']}")
```
