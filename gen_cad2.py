import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle
import matplotlib.patheffects as pe
import numpy as np
import base64
from io import BytesIO

fig, ax = plt.subplots(figsize=(9, 5.0))
ax.set_xlim(0, 11)
ax.set_ylim(0.5, 5.3)
ax.set_aspect('equal')
ax.axis('off')
fig.patch.set_facecolor('white')

# ── Drawing border & title block ──────────────────────────────────────────────
border = plt.Polygon([[0.15,0.60],[10.85,0.60],[10.85,5.22],[0.15,5.22]],
                      fill=False, edgecolor='#222', linewidth=1.5, zorder=10)
ax.add_patch(border)
# Title block bottom
ax.plot([0.15,10.85],[1.02,1.02], color='#222', lw=0.8)
ax.plot([7.2,7.2],[0.60,1.02], color='#222', lw=0.8)
ax.plot([9.0,9.0],[0.60,1.02], color='#222', lw=0.8)
ax.text(3.7,  0.80, 'RθJC THERMAL RESISTANCE TEST FIXTURE', fontsize=7.5, fontweight='bold',
        ha='center', va='center', color='#111', fontfamily='monospace')
ax.text(8.1,  0.80, 'CROSS-SECTION VIEW', fontsize=6.5,
        ha='center', va='center', color='#444', fontfamily='monospace')
ax.text(9.95, 0.80, 'SCALE: NTS', fontsize=6,
        ha='center', va='center', color='#444', fontfamily='monospace')

# ── Main drawing area (y from 1.0 to 7.0) ─────────────────────────────────────

# Component y-positions
y_sink_bot  = 1.10
y_sink_top  = 2.30   # heat sink top
y_tim_top   = 2.50   # TIM top (thin layer)
y_pkg_bot   = 2.50
y_pkg_top   = 3.40
y_chip_bot  = 3.02
y_chip_top  = 3.40
y_die_bot   = 3.10
y_die_top   = 3.36
x_left      = 2.20
x_right     = 8.80
x_center    = (x_left + x_right) / 2   # 5.5

# ── Heat Sink (copper/orange) ────────────────────────────────────────────────
sink = FancyBboxPatch((x_left, y_sink_bot), x_right-x_left, y_sink_top-y_sink_bot,
                      boxstyle="square,pad=0", linewidth=1.4,
                      edgecolor='#8B4513', facecolor='#E8834A')
ax.add_patch(sink)

# Serpentine channel slots inside heat sink
for xi in np.arange(x_left+0.22, x_right-0.15, 0.38):
    ch = FancyBboxPatch((xi, y_sink_bot+0.12), 0.22, (y_sink_top-y_sink_bot)-0.25,
                        boxstyle="square,pad=0", linewidth=0,
                        facecolor='#BFDCF5', alpha=0.85)
    ax.add_patch(ch)

# Water-cooled label inside sink
ax.text(x_center-0.3, (y_sink_bot+y_sink_top)/2, 'Water Cooled Heat Sink',
        fontsize=8, fontweight='bold', ha='center', va='center',
        color='white', fontfamily='sans-serif',
        path_effects=[pe.withStroke(linewidth=2, foreground='#8B4513')])

# Water flow arrow inside sink
ax.annotate('', xy=(x_left+0.1, (y_sink_bot+y_sink_top)/2),
            xytext=(x_left+0.9, (y_sink_bot+y_sink_top)/2),
            arrowprops=dict(arrowstyle='->', color='white', lw=2.0))

# ── TIM / Thermal Grease (thin gray layer) ───────────────────────────────────
tim = FancyBboxPatch((x_left+0.5, y_sink_top), x_right-x_left-1.0, 0.20,
                     boxstyle="square,pad=0", linewidth=1.2,
                     edgecolor='#555', facecolor='#D0D0D0')
ax.add_patch(tim)

# ── Package body (gray) ──────────────────────────────────────────────────────
pkg = FancyBboxPatch((x_left+0.3, y_pkg_bot), x_right-x_left-0.6, y_pkg_top-y_pkg_bot,
                     boxstyle="square,pad=0", linewidth=1.4,
                     edgecolor='#444', facecolor='#888888')
ax.add_patch(pkg)

# Package leads (left & right)
for lx, ldir in [(x_left+0.3, -1), (x_right-0.3, 1)]:
    lead = FancyBboxPatch((lx + ldir*0.05, y_pkg_bot+0.20),
                          ldir*0.55, 0.12,
                          boxstyle="square,pad=0", linewidth=1.0,
                          edgecolor='#555', facecolor='#aaa')
    ax.add_patch(lead)

# Die paddle (dark gray, inside package)
paddle = FancyBboxPatch((3.80, y_pkg_bot+0.08), 3.40, 0.70,
                        boxstyle="square,pad=0", linewidth=1.0,
                        edgecolor='#333', facecolor='#555')
ax.add_patch(paddle)

# Die attach (thin yellow)
die_attach = FancyBboxPatch((4.10, y_pkg_bot+0.56), 2.80, 0.10,
                             boxstyle="square,pad=0", linewidth=0.8,
                             edgecolor='#B8860B', facecolor='#FFD700', alpha=0.9)
ax.add_patch(die_attach)

# Chip (dark blue-gray on top)
chip = FancyBboxPatch((4.10, y_pkg_bot+0.66), 2.80, 0.54,
                      boxstyle="square,pad=0", linewidth=1.2,
                      edgecolor='#1a1a4a', facecolor='#2d2d7a')
ax.add_patch(chip)

# Chip label
ax.text(x_center, y_pkg_bot+0.93, 'CHIP', fontsize=7, fontweight='bold',
        ha='center', va='center', color='white', fontfamily='monospace')

# ── Pressure arrow (orange, from top) ────────────────────────────────────────
ax.annotate('', xy=(x_center, y_pkg_top+0.05),
            xytext=(x_center, y_pkg_top+1.05),
            arrowprops=dict(arrowstyle='->', color='#E8834A',
                            lw=3.0, mutation_scale=22))
ax.text(x_center+0.18, y_pkg_top+0.58, 'Pressure', fontsize=9,
        ha='left', va='center', color='#C05000', fontfamily='sans-serif', fontweight='bold')

# ── Callout lines & labels ────────────────────────────────────────────────────
def callout(ax, xy_tip, xy_text, label, fontsize=7.5, side='right'):
    """Draw a callout leader line and label."""
    ax.annotate('', xy=xy_tip, xytext=xy_text,
                arrowprops=dict(arrowstyle='-', color='#222', lw=0.9,
                                connectionstyle='arc3,rad=0.0'))
    ha = 'left' if side == 'right' else 'right'
    ax.text(xy_text[0] + (0.12 if side == 'right' else -0.12),
            xy_text[1], label,
            fontsize=fontsize, ha=ha, va='center',
            color='#111', fontfamily='sans-serif')

# Chip callout
ax.plot([4.10, 3.55], [y_pkg_bot+0.95, y_pkg_bot+0.95], color='#222', lw=0.9)
ax.plot([3.55, 2.65], [y_pkg_bot+0.95, 3.85], color='#222', lw=0.9)
ax.text(2.55, 3.85, 'Chip', fontsize=7.5, ha='right', va='center', color='#111')

# Die Attach callout
ax.plot([4.10, 3.55], [y_pkg_bot+0.61, y_pkg_bot+0.61], color='#222', lw=0.9)
ax.plot([3.55, 2.65], [y_pkg_bot+0.61, 3.50], color='#222', lw=0.9)
ax.text(2.55, 3.50, 'Die Attach', fontsize=7.5, ha='right', va='center', color='#111')

# Die paddle callout
ax.plot([3.80, 3.35], [y_pkg_bot+0.28, y_pkg_bot+0.28], color='#222', lw=0.9)
ax.plot([3.35, 2.65], [y_pkg_bot+0.28, 3.15], color='#222', lw=0.9)
ax.text(2.55, 3.15, 'Die Paddle', fontsize=7.5, ha='right', va='center', color='#111')

# Package callout (right side)
ax.plot([x_right-0.3, x_right+0.15], [y_pkg_bot+0.55, y_pkg_bot+0.55], color='#222', lw=0.9)
ax.plot([x_right+0.15, x_right+0.55], [y_pkg_bot+0.55, 3.55], color='#222', lw=0.9)
ax.text(x_right+0.60, 3.55, 'Package', fontsize=7.5, ha='left', va='center', color='#111')

# Thermal Grease callout (right side)
ax.plot([x_right-0.5, x_right+0.15], [y_sink_top+0.10, y_sink_top+0.10], color='#222', lw=0.9)
ax.plot([x_right+0.15, x_right+0.55], [y_sink_top+0.10, 2.65], color='#222', lw=0.9)
ax.text(x_right+0.60, 2.65, 'Thermal Grease', fontsize=7.5, ha='left', va='center', color='#111')
ax.text(x_right+0.60, 2.48, '(k = 5 W/mK)', fontsize=6.5, ha='left', va='center', color='#555')

# Thermocouple measurement (right side, bottom)
ax.plot([x_right-0.5, x_right+0.15], [(y_sink_bot+y_sink_top)/2, (y_sink_bot+y_sink_top)/2], color='#222', lw=0.9)
ax.plot([x_right+0.15, x_right+0.55], [(y_sink_bot+y_sink_top)/2, 1.95], color='#222', lw=0.9)
ax.text(x_right+0.60, 1.95, 'Thermocouple measurement', fontsize=7, ha='left', va='center', color='#111')
ax.text(x_right+0.60, 1.78, 'of case temperature  $T_C$', fontsize=7, ha='left', va='center', color='#111')

# T_J label (top of chip)
ax.text(x_center-1.95, y_pkg_top+0.85, '$T_J$', fontsize=11, ha='center', va='center',
        color='#111', style='italic')
ax.plot([x_center-1.95, x_center-1.95], [y_pkg_top+0.72, y_pkg_top+0.12], color='#555', lw=0.8, linestyle='--')
ax.plot([x_center-1.95, 4.10], [y_pkg_top+0.12, y_pkg_top+0.05], color='#555', lw=0.8, linestyle='--')

# T_C label (bottom of fixture)
ax.text(x_center, y_sink_bot-0.30, '$T_C$', fontsize=11, ha='center', va='center',
        color='#111', style='italic')
ax.plot([x_center, x_center], [y_sink_bot-0.18, y_sink_bot], color='#555', lw=0.8, linestyle='--')

# ── Spring / Load frame schematic (simplified, sides) ─────────────────────────
for sx in [x_left-0.05, x_right+0.05]:
    # vertical bar representing frame
    bar = FancyBboxPatch((sx-0.12, y_sink_bot), 0.12, y_pkg_top-y_sink_bot+0.1,
                          boxstyle="square,pad=0", linewidth=1.0,
                          edgecolor='#4A5568', facecolor='#CBD5E0', alpha=0.7)
    ax.add_patch(bar)
    # coil spring lines above package
    for ky in np.linspace(y_pkg_top+0.10, y_pkg_top+0.85, 8):
        coil = plt.Line2D([sx-0.18, sx+0.06], [ky, ky+0.07],
                          color='#718096', linewidth=1.0)
        ax.add_line(coil)

# ── Dimension / annotation line: RθJC ────────────────────────────────────────
ax.annotate('', xy=(1.55, y_sink_top+0.10), xytext=(1.55, y_pkg_top-0.05),
            arrowprops=dict(arrowstyle='<->', color='#1a56db', lw=1.2))
ax.text(1.42, (y_sink_top+y_pkg_top)/2, r'$R_{\theta JC}$', fontsize=9,
        ha='center', va='center', color='#1a56db', style='italic')
ax.plot([1.55, x_left+0.3], [y_sink_top+0.10, y_sink_top+0.10], color='#1a56db', lw=0.7, linestyle=':')
ax.plot([1.55, x_left+0.3], [y_pkg_top-0.05, y_pkg_top-0.05], color='#1a56db', lw=0.7, linestyle=':')

# ── Section title ─────────────────────────────────────────────────────────────
ax.text(x_center, 5.05, 'SECTION A-A   |   THERMAL RESISTANCE CHARACTERIZATION FIXTURE',
        fontsize=8, ha='center', va='center', color='#1a1a2e',
        fontweight='bold', fontfamily='monospace')
ax.axhline(4.88, xmin=0.03, xmax=0.97, color='#bbb', lw=0.7)

# ── Save ──────────────────────────────────────────────────────────────────────
buf = BytesIO()
plt.tight_layout(pad=0.0)
plt.savefig(buf, format='png', dpi=120, bbox_inches='tight', pad_inches=0.05, facecolor='white')
buf.seek(0)
b64 = base64.b64encode(buf.read()).decode('utf-8')
print(len(b64), 'chars')

with open('C:/Users/admin/Desktop/website/thermal_fixture_cad2.b64', 'w') as f:
    f.write(b64)
print("Saved.")
plt.close()
