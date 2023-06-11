message = "Hello World"
and_result = ""
xor_result = ""
for char in message:
 and_value = ord(char) & 127
 xor_value = ord(char) ^ 127
 and_result += chr(and_value)
 xor_result += chr(xor_value)

print("Original message:", message)
print("AND result:", and_result)
print("XOR result:", xor_result)