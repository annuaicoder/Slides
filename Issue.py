text = "Hello, World!"
encoded_text = text.encode('utf-8')
try:
    decoded_text = encoded_text.decode('utf-16')
except UnicodeDecodeError as e:
    print(e)  # Output: 'utf-16' codec can't decode byte 0x21 in position 12: truncated data


#Solution
decoded_text = encoded_text.decode('utf-8')
