import random
import string

# 生成 200 个激活码
for i in range(200):
    chars = string.ascii_letters + string.digits
    code_list = random.sample(chars, 12)
    code = ''.join(code_list)
    print(code)
