from collections import deque

# Đọc dữ liệu mê cung từ file nhị phân
with open('maze1.bin', 'rb') as f:
    maze_data = f.read()

# Hàm lấy type của ô tại vị trí (x, y, z)
def get_type(x, y, z):
    offset = 6400 * x + 320 * y + 16 * z + 12  # Tính offset trong dữ liệu
    type_bytes = maze_data[offset:offset+4]
    type_value = int.from_bytes(type_bytes, 'little')  # Chuyển byte sang int
    return type_value

# Các hướng di chuyển trong không gian 3D
directions = {
    'L': (-1, 0, 0),  # Trái
    'R': (1, 0, 0),   # Phải
    'F': (0, 1, 0),   # Tiến
    'B': (0, -1, 0),  # Lùi
    'U': (0, 0, 1),   # Lên
    'D': (0, 0, -1)   # Xuống
}

# Kiểm tra vị trí hợp lệ trong mê cung
def is_valid(x, y, z):
    return 0 <= x < 20 and 0 <= y < 20 and 0 <= z < 20

# Thuật toán BFS tìm đường đi
def bfs(start, target_type):
    queue = deque([start])  # Hàng đợi chứa các ô cần thăm
    visited = set([start])  # Tập hợp các ô đã thăm
    parent = {start: None}  # Lưu ô cha để truy ngược đường đi
    
    while queue:
        current = queue.popleft()  # Lấy ô hiện tại từ đầu hàng đợi
        x, y, z = current
        
        # Nếu ô hiện tại là đích (type = 3)
        if get_type(x, y, z) == target_type:
            path = []
            while current:
                prev = parent[current]
                if prev:
                    dx, dy, dz = current[0] - prev[0], current[1] - prev[1], current[2] - prev[2]
                    for dir, delta in directions.items():
                        if delta == (dx, dy, dz):
                            path.append(dir)
                            break
                current = prev
            return path[::-1]  # Đảo ngược để có đường đi từ start đến end
        
        # Thử di chuyển theo 6 hướng
        for dir, (dx, dy, dz) in directions.items():
            nx, ny, nz = x + dx, y + dy, z + dz
            next_pos = (nx, ny, nz)
            if (is_valid(nx, ny, nz) and 
                get_type(nx, ny, nz) != 2 and 
                next_pos not in visited):
                visited.add(next_pos)
                queue.append(next_pos)
                parent[next_pos] = current
    
    return None  # Không tìm thấy đường đi

# Chạy BFS từ (0,0,0) để tìm ô đích (type = 3)
start = (0, 0, 0)
path = bfs(start, 3)

# In kết quả
if path:
    print("Đường đi:", ''.join(path))
else:
    print("Không tìm thấy đường đi")
