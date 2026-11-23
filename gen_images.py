"""Generates the sample 'camera' images (SVG spaceships with license plates)."""
import random

random.seed(4)
plates = ["12-345-67", "88-777-11", "KRK-2077", "UFO-001", "42-424-24", "NCC-1701"]
cols = ["#4fd1ff", "#ff5c7a", "#3ddc97", "#ffd84a", "#b388ff", "#ff9f43"]
for i, (p, c) in enumerate(zip(plates, cols), 1):
    stars = "".join(
        f'<circle cx="{random.randint(5, 395)}" cy="{random.randint(5, 195)}" r="{random.choice([1, 1.5, 2])}" fill="#fff"/>'
        for _ in range(40)
    )
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 260"><rect width="400" height="260" fill="#070b1a"/>{stars}
<ellipse cx="200" cy="110" rx="120" ry="34" fill="{c}"/><ellipse cx="200" cy="90" rx="55" ry="38" fill="#cfe8ff" opacity=".85"/>
<circle cx="130" cy="115" r="7" fill="#fff"/><circle cx="165" cy="123" r="7" fill="#fff"/><circle cx="235" cy="123" r="7" fill="#fff"/><circle cx="270" cy="115" r="7" fill="#fff"/>
<rect x="130" y="190" width="140" height="44" rx="6" fill="#ffd84a" stroke="#111" stroke-width="3"/>
<text x="200" y="221" font-family="monospace" font-size="26" font-weight="bold" text-anchor="middle" fill="#111">{p}</text></svg>'''
    with open(f"storage/images/car{i}.svg", "w", encoding="utf-8") as f:
        f.write(svg)
