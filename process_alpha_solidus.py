import sys

pts = []
with open('alpha solidus.csv', 'r') as f:
    for line in f:
        line = line.strip()
        if not line: continue
        parts = line.split(',')
        if len(parts) >= 2:
            try:
                pts.append((float(parts[0]), float(parts[1])))
            except:
                pass

print(f"Total rows: {len(pts)}")
print(f"Comp range: {pts[0][0]:.4f} -> {pts[-1][0]:.4f}  wt.% Mg")
print(f"Temp range: {min(p[1] for p in pts):.2f} -> {max(p[1] for p in pts):.2f}  deg C")
print(f"\nFirst 3 rows:  {pts[:3]}")
print(f"Last  3 rows:  {pts[-3:]}")

def rdp(points, epsilon):
    if len(points) < 3:
        return list(points)
    start, end = points[0], points[-1]
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    norm = (dx*dx + dy*dy)**0.5 or 1e-9
    max_dist, max_idx = 0, 0
    for i in range(1, len(points)-1):
        dist = abs(dy*points[i][0] - dx*points[i][1] + end[0]*start[1] - end[1]*start[0]) / norm
        if dist > max_dist:
            max_dist = dist
            max_idx = i
    if max_dist > epsilon:
        left  = rdp(points[:max_idx+1], epsilon)
        right = rdp(points[max_idx:], epsilon)
        return left[:-1] + right
    return [start, end]

sys.setrecursionlimit(50000)
simplified = rdp(pts, 0.1)
print(f"\nRDP epsilon=0.1 -> {len(simplified)} points")

with open('alpha_solidus_js.txt', 'w') as out:
    out.write(f"// alpha solidus.csv: {len(pts)} pts -> RDP {len(simplified)} pts\n")
    out.write(f"// Range: {pts[0][0]:.4f} to {pts[-1][0]:.4f} wt.% Mg\n")
    for p in simplified:
        out.write(f"    [{p[0]:.4f}, {p[1]:.4f}],\n")

print("Written to alpha_solidus_js.txt")
print(f"\nFirst 5 simplified:")
for p in simplified[:5]: print(f"  {p}")
print(f"Last 5 simplified:")
for p in simplified[-5:]: print(f"  {p}")
