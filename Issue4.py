text1 = "e\u0301"  # 'e' followed by combining acute accent
text2 = "\u00e9"   # 'é' single character
print(text1 == text2)  # Output: False

"""
Solution: Normalize Unicode strings to a standard form (NFC or NFD).

import unicodedata
normalized_text1 = unicodedata.normalize('NFC', text1)
print(normalized_text1 == text2)  # Output: True

"""

