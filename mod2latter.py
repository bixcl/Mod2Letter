st = '128 322 353 235 336 73 198 332 202 285 57 87 262 221 218 405 335 101 256 227 112 140'  
lst = st.split()
cipherLST = 'abcdefghijklmnopqrstuvwxyz0123456789_'
mod = 37

result = ""
for i in range(len(lst)):
    j = int(lst[i]) % mod
    result += cipherLST[j]

print(result)