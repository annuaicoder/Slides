text = "こんにちは"
encoded_text = text.encode('shift_jis')
try:
    decoded_text = encoded_text.decode('utf-8')
except UnicodeDecodeError as e:
    print(e)  # Output: 'utf-8' codec can't decode byte 0x82 in position 0: invalid start byte

#Solution

"""
Solution: Use the correct encoding for both encoding and decoding.

decoded_text = encoded_text.decode('shift_jis')

"""