"""
Generated Code Metadata:
========================
Original URL: https://metatask.co.kr
Prompt: "Create a simple Korean language processing script that could be part of a larger AI solution like 메타태스크."
Generated: DETERMINISTIC_679262c36337098c
Batch ID: 20250622_204946
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
Korean Language Processing Module

This module provides basic Korean language processing functionalities that can be
integrated into larger AI solutions like 메타태스크 (MetaTask).

Features:
- Hangul character decomposition
- Basic tokenization
- Romanization (Korean to English characters)
"""

import re
from typing import List, Tuple, Union

# Constants for Hangul processing
HANGUL_START = 0xAC00  # Unicode value for '가'
HANGUL_END = 0xD7A3    # Unicode value for '힣'
CHOSUNG_LIST = [
    'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 
    'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
]
JUNGSUNG_LIST = [
    'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 
    'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ'
]
JONGSUNG_LIST = [
    '', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 
    'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 
    'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
]

ROMANIZATION_MAP = {
    'ㄱ': 'g', 'ㄲ': 'kk', 'ㄴ': 'n', 'ㄷ': 'd', 'ㄸ': 'tt',
    'ㄹ': 'r', 'ㅁ': 'm', 'ㅂ': 'b', 'ㅃ': 'pp', 'ㅅ': 's',
    'ㅆ': 'ss', 'ㅇ': '', 'ㅈ': 'j', 'ㅉ': 'jj', 'ㅊ': 'ch',
    'ㅋ': 'k', 'ㅌ': 't', 'ㅍ': 'p', 'ㅎ': 'h',
    'ㅏ': 'a', 'ㅐ': 'ae', 'ㅑ': 'ya', 'ㅒ': 'yae', 'ㅓ': 'eo',
    'ㅔ': 'e', 'ㅕ': 'yeo', 'ㅖ': 'ye', 'ㅗ': 'o', 'ㅘ': 'wa',
    'ㅙ': 'wae', 'ㅚ': 'oe', 'ㅛ': 'yo', 'ㅜ': 'u', 'ㅝ': 'wo',
    'ㅞ': 'we', 'ㅟ': 'wi', 'ㅠ': 'yu', 'ㅡ': 'eu', 'ㅢ': 'ui',
    'ㅣ': 'i'
}

def is_hangul(char: str) -> bool:
    """Check if a character is a Hangul syllable."""
    return HANGUL_START <= ord(char) <= HANGUL_END

def decompose_hangul(char: str) -> Tuple[str, str, str]:
    """
    Decompose a Hangul character into its components (초성, 중성, 종성).
    
    Args:
        char: A single Hangul character
        
    Returns:
        Tuple of (chosung, jungsung, jongsung)
        
    Raises:
        ValueError: If input is not a Hangul character
    """
    if not is_hangul(char):
        raise ValueError(f"'{char}' is not a Hangul character")
    
    code = ord(char) - HANGUL_START
    jongsung_index = code % 28
    jungsung_index = (code // 28) % 21
    chosung_index = code // (28 * 21)
    
    return (
        CHOSUNG_LIST[chosung_index],
        JUNGSUNG_LIST[jungsung_index],
        JONGSUNG_LIST[jongsung_index]
    )

def tokenize_korean(text: str) -> List[str]:
    """
    Tokenize Korean text into words and punctuation.
    
    Args:
        text: Input Korean text
        
    Returns:
        List of tokens
    """
    # Simple tokenizer that splits on whitespace and keeps Korean words together
    tokens = re.findall(r'[\w가-힣]+|[^\w가-힣\s]', text)
    return [token for token in tokens if token.strip()]

def romanize_korean(text: str) -> str:
    """
    Convert Korean text to Romanized form (English characters).
    
    Args:
        text: Input Korean text
        
    Returns:
        Romanized version of the text
    """
    result = []
    for char in text:
        if is_hangul(char):
            chosung, jungsung, jongsung = decompose_hangul(char)
            
            # Handle initial consonant
            if chosung in ROMANIZATION_MAP:
                result.append(ROMANIZATION_MAP[chosung])
            
            # Handle vowel
            if jungsung in ROMANIZATION_MAP:
                result.append(ROMANIZATION_MAP[jungsung])
            
            # Handle final consonant
            if jongsung and jongsung in ROMANIZATION_MAP:
                result.append(ROMANIZATION_MAP[jongsung])
        else:
            result.append(char)
    
    return ''.join(result)

def process_korean_text(text: str) -> dict:
    """
    Process Korean text with various analyses.
    
    Args:
        text: Input Korean text
        
    Returns:
        Dictionary containing processed information:
        {
            'original': original text,
            'tokens': tokenized text,
            'romanized': romanized text,
            'char_analysis': list of decomposed characters
        }
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    tokens = tokenize_korean(text)
    romanized = romanize_korean(text)
    
    char_analysis = []
    for char in text:
        if is_hangul(char):
            try:
                decomposed = decompose_hangul(char)
                char_analysis.append({
                    'char': char,
                    'components': decomposed
                })
            except ValueError:
                char_analysis.append({'char': char, 'components': None})
        else:
            char_analysis.append({'char': char, 'components': None})
    
    return {
        'original': text,
        'tokens': tokens,
        'romanized': romanized,
        'char_analysis': char_analysis
    }

# Example usage
if __name__ == "__main__":
    sample_text = "안녕하세요! 이것은 테스트 문장입니다."
    processed = process_korean_text(sample_text)
    
    print(f"Original: {processed['original']}")
    print(f"Tokens: {processed['tokens']}")
    print(f"Romanized: {processed['romanized']}")
    print("Character Analysis:")
    for analysis in processed['char_analysis']:
        if analysis['components']:
            print(f"{analysis['char']}: {analysis['components']}")
```
