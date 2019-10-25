sec_key = ['ေ', 'ှ', 'ြ', 'ှ', 'း', '်', 'ိ', 'ာ', 'ီ', 'ျ', 'ံ', '့', 'ု', 'ူ', 'ဲ', 'ွ', 'ါ']
ans = input()

ans = ans.replace(" ", "")
for i in range(len(ans)):
  if ans[i] in sec_key:
      if i<len(ans)-1:
          if ans[i]!=ans[i+1]:
              print(ans[i], end='')
  else:
      print(ans[i],end='')

print(ans[len(ans)-1])