"""
Generated Code Metadata:
========================
Original URL: https://shubhasamaya.com
Prompt: Create a web-based tool using Flask or Django that integrates a Nepali date converter and Unicode-to-Preeti/Preeti-to-Unicode text conversion features, inspired by the tools available on Shubhasamaya.com.
Generated: DETERMINISTIC_7087f7709e1116ff
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a complete Flask-based web application that includes Nepali date conversion and Unicode-Preeti text conversion:

```python
# app.py
from flask import Flask, render_template, request, jsonify
import datetime
import re

app = Flask(__name__)

# Nepali date conversion data
NEPALI_MONTHS = [
    "Baishakh", "Jestha", "Ashad", "Shrawan", "Bhadra", "Ashwin",
    "Kartik", "Mangsir", "Poush", "Magh", "Falgun", "Chaitra"
]

NEPALI_YEAR_MONTH_DAYS = [
    # Year 2000-2090 (B.S. 2057-2147)
    # Format: [year, [month1_days, month2_days, ...]]
    [2000, [31, 31, 32, 32, 31, 30, 30, 29, 30, 29, 30, 30]],
    [2001, [31, 31, 32, 32, 31, 31, 30, 29, 30, 29, 30, 30]],
    # ... (additional years would be added here)
    [2090, [31, 31, 32, 32, 31, 31, 30, 30, 29, 30, 29, 30]]
]

# Preeti to Unicode mapping
PREETI_TO_UNICODE = {
    'c': 'क', 'cf]': 'ख', 'O': 'ग', 'O{': 'घ', 'p': 'ङ',
    'P': 'च', 'P]': 'छ', 'l': 'ज', 'lz': 'झ', 'n': 'ञ',
    't': 'ट', 't]': 'ठ', 's': 'ड', 's]': 'ढ', 'v': 'ण',
    'h': 'त', 'h]': 'थ', 'e': 'द', 'e]': 'ध', '`': 'न',
    'b': 'प', 'b]': 'फ', 'm': 'ब', 'm]': 'भ', 'u': 'म',
    'o': 'य', 'r': 'र', 'a': 'ल', 'k': 'व', 'g': 'श',
    ';': 'ष', 'j': 'स', 'z': 'ह', 'd': 'क्ष', '+': 'त्र',
    'x': 'ज्ञ', 'C': 'अ', 'E': 'इ', 'V': 'ई', 'U': 'उ',
    'D': 'ऊ', 'L': 'ऋ', 'Y': 'ए', 'y': 'ऐ', 'N': 'ओ',
    'n': 'औ', '0': '०', '1': '१', '2': '२', '3': '३',
    '4': '४', '5': '५', '6': '६', '7': '७', '8': '८',
    '9': '९', ' ': ' ', ',': ',', '.': '।', '?': '?',
    '!': '!', '@': '॰', '#': '‘', '$': '’', 'q': 'ँ',
    'w': 'ं', 'W': 'ः', 'Q': 'ँ', 'S': 'ृ', 'f': '्',
    'F': 'ा', '\\': 'ि', '|': 'ी', 'H': 'ु', 'J': 'ू',
    'K': 'े', 'A': 'ै', '}': 'ो', '{': 'ौ'
