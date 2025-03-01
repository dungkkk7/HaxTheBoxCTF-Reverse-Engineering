import gdb

# Đặt breakpoint tại hàm check_flag
gdb.execute("break *0x000055555555d1cd")
gdb.execute("run")

# Lặp qua từng hàm trong mảng con trỏ hàm
for i in range(31):
    # Lấy địa chỉ của hàm thứ i
    func_addr = int(gdb.parse_and_eval(f"*(void**)($rsp + 0x10 + {i} * 8)"))

    # Disassemble hàm
    print(f"Function {i} at 0x{func_addr:x}:")
    gdb.execute(f"disassemble 0x{func_addr:x}")

    # Tìm lệnh cmp và trích xuất giá trị
    output = gdb.execute(f"disassemble 0x{func_addr:x}", to_string=True)
    for line in output.splitlines():
        if "cmp" in line and "dil" in line:
            parts = line.split(",")
            if len(parts) > 1:
                value = parts[1].strip()
                print(f"Character {i}: {value}")
                break
