import sys

pts = []
with open('Liquidus Dataset.csv', 'r') as f:
    for i, line in enumerate(f, 1):
        line = line.strip()
        if not line:
            continue
        parts = line.split(',')
        if len(parts) >= 2:
            try:
                c = float(parts[0])
                t = float(parts[1])
                pts.append((c, t))
            except:
                pass

print(f"Total valid rows: {len(pts)}")
print(f"Composition range: {pts[0][0]:.4f} -> {pts[-1][0]:.4f}  wt.% Mg")
print(f"Temperature range: {min(p[1] for p in pts):.4f} -> {max(p[1] for p in pts):.4f}  °C")
print(f"\nFirst 5 rows:")
for p in pts[:5]:
    print(f"  {p[0]:.6f}, {p[1]:.6f}")
print(f"\nMiddle 5 rows (around row {len(pts)//2}):")
mid = len(pts)//2
for p in pts[mid-2:mid+3]:
    print(f"  {p[0]:.6f}, {p[1]:.6f}")
print(f"\nLast 5 rows:")
for p in pts[-5:]:
    print(f"  {p[0]:.6f}, {p[1]:.6f}")

# --- RDP simplification ---
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

sys.setrecursionlimit(100000)
simplified = rdp(pts, 0.1)
print(f"\n--- RDP epsilon=0.1 -> {len(simplified)} points ---")

# Write JS array to file
with open('liquidus_js.txt', 'w') as out:
    out.write(f"// Real data from Liquidus Dataset.csv\n")
    out.write(f"// RDP simplified: {len(pts)} -> {len(simplified)} points\n")
    out.write(f"// Composition range: {pts[0][0]:.2f} to {pts[-1][0]:.2f} wt.% Mg\n")
    for p in simplified:
        out.write(f"    [{p[0]:.4f}, {p[1]:.4f}],\n")

print(f"JS array written to liquidus_js.txt")
print(f"\nFirst 10 simplified points:")
for p in simplified[:10]:
    print(f"  [{p[0]:.4f}, {p[1]:.4f}]")
print(f"\nLast 10 simplified points:")
for p in simplified[-10:]:
    print(f"  [{p[0]:.4f}, {p[1]:.4f}]")
