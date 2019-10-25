main_key = ['က', 'ခ', 'ဂ', 'ဃ', 'င', 'စ', 'ဇ', 'ဈ', 'ည', 'ဋ', 'ဌ', 'ဍ', 'တ', 'ထ', 'ဒ', 'ဓ', 'န', 'ပ', 'ဖ', 'ဗ', 'ဘ',
            'မ', 'ယ', 'ရ', 'လ', 'ဝ', 'သ', 'ဋ္ဌ', 'အ', '၏']
sec_key = ['ေ', 'ှ', 'ြ', 'ှ', 'း', '်', '္']
inp = input()
ans = ''
for i in range(len(inp)):
    if not (inp[i] in main_key):
        ans += inp[i]
    else:
        if i < len(inp) - 1:
            if inp[i + 1] in sec_key:
                ans += inp[i]
            else:
                print(ans)
                ans = inp[i]
        elif i == len(inp) - 1:
            print(ans)
            ans = inp[i]
print(ans)
