import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np
import base64
from io import BytesIO

fig, ax = plt.subplots(1, 1, figsize=(10, 7.5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 7.5)
ax.set_aspect('equal')
ax.axis('off')
fig.patch.set_facecolor('#F8F8F8')

# Title
ax.text(5, 7.1, 'RthJC TEST FIXTURE  -  CROSS SECTION ASSEMBLY', fontsize=9.5, fontweight='bold',
        ha='center', va='center', color='#1a1a2e', fontfamily='monospace')
ax.text(5, 6.78, 'SolidWorks / Flow Simulation  |  100W Heat Load  |  2 L/min Coolant', fontsize=7,
        ha='center', va='center', color='#666', fontfamily='monospace')
ax.axhline(6.65, xmin=0.05, xmax=0.95, color='#ccc', linewidth=0.8)

# DUT / Package (bottom center)
pkg = FancyBboxPatch((3.2, 0.5), 3.6, 0.7, boxstyle="square,pad=0",
                     linewidth=1.5, edgecolor='#333', facecolor='#CBD5E0')
ax.add_patch(pkg)
ax.text(5.0, 0.85, 'DUT / SEMICONDUCTOR PACKAGE', fontsize=6.5, ha='center', va='center',
        color='#1a202c', fontweight='bold', fontfamily='monospace')

# Die inside package
die = FancyBboxPatch((4.25, 0.62), 1.5, 0.46, boxstyle="square,pad=0",
                     linewidth=1, edgecolor='#555', facecolor='#A0AEC0')
ax.add_patch(die)
ax.text(5.0, 0.85, 'DIE', fontsize=5.5, ha='center', va='center',
        color='#fff', fontweight='bold', fontfamily='monospace', zorder=5)

# TIM layer
tim = FancyBboxPatch((3.2, 1.2), 3.6, 0.2, boxstyle="square,pad=0",
                     linewidth=1, edgecolor='#805AD5', facecolor='#E9D8FD', alpha=0.85)
ax.add_patch(tim)
ax.text(5.0, 1.30, 'THERMAL INTERFACE MATERIAL  (k = 5 W/mK)', fontsize=5.8, ha='center', va='center',
        color='#553c9a', fontweight='bold', fontfamily='monospace')

# Copper Cold Plate
cp_outer = FancyBboxPatch((2.4, 1.4), 5.2, 1.55, boxstyle="square,pad=0",
                           linewidth=1.5, edgecolor='#B7791F', facecolor='#FEFCE8')
ax.add_patch(cp_outer)

# Serpentine channels
for xi in np.arange(2.65, 7.4, 0.38):
    chan = FancyBboxPatch((xi, 1.52), 0.22, 1.28, boxstyle="square,pad=0",
                          linewidth=0, facecolor='#93C5FD', alpha=0.7)
    ax.add_patch(chan)

# Flow arrows
ax.annotate('', xy=(2.1, 2.17), xytext=(2.4, 2.17),
            arrowprops=dict(arrowstyle='<-', color='#2563EB', lw=1.5))
ax.annotate('', xy=(7.9, 2.17), xytext=(7.6, 2.17),
            arrowprops=dict(arrowstyle='->', color='#2563EB', lw=1.5))
ax.text(1.95, 2.17, 'IN', fontsize=6.5, ha='center', va='center', color='#2563EB',
        fontweight='bold', fontfamily='monospace')
ax.text(8.05, 2.17, 'OUT', fontsize=6.5, ha='center', va='center', color='#2563EB',
        fontweight='bold', fontfamily='monospace')

ax.text(5.0, 2.45, 'COPPER COLD PLATE  C101  |  Serpentine Channels  |  w/h = 0.9', fontsize=6.2,
        ha='center', va='center', color='#744210', fontweight='bold', fontfamily='monospace', zorder=5)

# Aluminum Load Frame - left column
lf_l = FancyBboxPatch((1.7, 1.4), 0.7, 3.6, boxstyle="square,pad=0",
                       linewidth=1.5, edgecolor='#4A5568', facecolor='#E2E8F0')
ax.add_patch(lf_l)
# Right column
lf_r = FancyBboxPatch((7.6, 1.4), 0.7, 3.6, boxstyle="square,pad=0",
                       linewidth=1.5, edgecolor='#4A5568', facecolor='#E2E8F0')
ax.add_patch(lf_r)
# Top bridge
lf_t = FancyBboxPatch((1.7, 5.0), 6.6, 0.5, boxstyle="square,pad=0",
                       linewidth=1.5, edgecolor='#4A5568', facecolor='#E2E8F0')
ax.add_patch(lf_t)

ax.text(5.0, 5.25, 'Al 6061-T6 LOAD FRAME', fontsize=6.5,
        ha='center', va='center', color='#2d3748', fontweight='bold', fontfamily='monospace')

# Springs
for sx in [2.6, 3.7, 6.3, 7.4]:
    for ky in np.linspace(3.1, 4.85, 10):
        coil = plt.Line2D([sx-0.13, sx+0.13], [ky, ky+0.12],
                          color='#718096', linewidth=1.2, solid_capstyle='round')
        ax.add_line(coil)
    ax.plot([sx, sx], [3.05, 3.1], color='#718096', linewidth=1.5)
    ax.plot([sx, sx], [4.85, 4.98], color='#718096', linewidth=1.5)

ax.text(5.0, 4.0, '<--  CALIBRATED SPRINGS  |  +/-5 mm HEIGHT ADJ.  -->', fontsize=6.2,
        ha='center', va='center', color='#4A5568', fontweight='bold', fontfamily='monospace')

# Spring force annotation
ax.annotate('', xy=(5.0, 2.95), xytext=(5.0, 3.4),
            arrowprops=dict(arrowstyle='->', color='#E53E3E', lw=1.5))
ax.text(5.35, 3.15, 'F_spring (uniform)', fontsize=6.2, ha='left', va='center', color='#E53E3E',
        fontfamily='monospace')

# Dimension lines - height
ax.annotate('', xy=(8.55, 1.4), xytext=(8.55, 5.5),
            arrowprops=dict(arrowstyle='<->', color='#555', lw=0.9))
ax.text(8.72, 3.45, 'H', fontsize=7, ha='left', va='center', color='#555',
        fontfamily='monospace')
ax.plot([8.3, 8.6], [1.4, 1.4], color='#aaa', linewidth=0.7, linestyle='--')
ax.plot([8.3, 8.6], [5.5, 5.5], color='#aaa', linewidth=0.7, linestyle='--')

# Dimension lines - width
ax.annotate('', xy=(1.7, 0.25), xytext=(8.3, 0.25),
            arrowprops=dict(arrowstyle='<->', color='#555', lw=0.9))
ax.text(5.0, 0.12, 'W', fontsize=7, ha='center', va='center', color='#555',
        fontfamily='monospace')
ax.plot([1.7, 1.7], [0.2, 0.45], color='#aaa', linewidth=0.7, linestyle='--')
ax.plot([8.3, 8.3], [0.2, 0.45], color='#aaa', linewidth=0.7, linestyle='--')

# Legend
leg_items = [
    mpatches.Patch(facecolor='#CBD5E0', edgecolor='#333', label='DUT Package'),
    mpatches.Patch(facecolor='#E9D8FD', edgecolor='#805AD5', label='TIM (k=5 W/mK)'),
    mpatches.Patch(facecolor='#FEFCE8', edgecolor='#B7791F', label='Cu Cold Plate C101'),
    mpatches.Patch(facecolor='#93C5FD', edgecolor='#2563EB', label='Coolant Channels'),
    mpatches.Patch(facecolor='#E2E8F0', edgecolor='#4A5568', label='Al 6061-T6 Frame'),
]
ax.legend(handles=leg_items, loc='upper left', fontsize=5.8, framealpha=0.9,
          edgecolor='#ccc', bbox_to_anchor=(0.01, 0.995), handlelength=1.2, borderpad=0.6)

ax.text(9.85, 0.1, 'SolidWorks  |  FEA  |  GD&T', fontsize=5.5, ha='right', va='bottom',
        color='#aaa', fontfamily='monospace')

buf = BytesIO()
plt.tight_layout(pad=0.2)
plt.savefig(buf, format='png', dpi=150, bbox_inches='tight', facecolor='#F8F8F8')
buf.seek(0)
b64 = base64.b64encode(buf.read()).decode('utf-8')
print(b64[:50], '...', len(b64), 'chars')

with open('C:/Users/admin/Desktop/website/thermal_fixture_cad.b64', 'w') as f:
    f.write(b64)
print("Saved.")
plt.close()
