from pathlib import Path

import matplotlib.pyplot as plt
from cycler import cycler
from matplotlib import font_manager

font_path = [Path(__file__).parent / "fonts"]
font_files = font_manager.findSystemFonts(font_path)
for font_file in font_files:
    font_manager.fontManager.addfont(font_file)

palettes = {
    "categorical_light": [
        "#6929c4",
        "#1192e8",
        "#005d5d",
        "#9f1853",
        "#fa4d56",
        "#570408",
        "#198038",
        "#002d9c",
        "#ee538b",
        "#b28600",
        "#009d9a",
        "#012749",
        "#8a3800",
        "#a56eff",
    ],
    "categorical_dark": [
        "#8a3ffc",
        "#33b1ff",
        "#007d79",
        "#ff7eb6",
        "#fa4d56",
        "#fff1f1",
        "#6fdc8c",
        "#4589ff",
        "#d12771",
        "#d2a106",
        "#08bdba",
        "#bae6ff",
        "#ba4e00",
        "#d4bbff",
    ],
    "sequential_blue": [
        "#edf5ff",
        "#d0e2ff",
        "#a6c8ff",
        "#78a9ff",
        "#4589ff",
        "#0f62fe",
        "#0043ce",
        "#002d9c",
        "#001d6c",
        "#001141",
    ],
    "sequential_purple": [
        "#f6f2ff",
        "#e8daff",
        "#d4bbff",
        "#be95ff",
        "#a56eff",
        "#8a3ffc",
        "#6929c4",
        "#491d8b",
        "#31135e",
        "#1c0f30",
    ],
    "sequential_cyan": [
        "#e5f6ff",
        "#bae6ff",
        "#82cfff",
        "#33b1ff",
        "#1192e8",
        "#0072c3",
        "#00539a",
        "#003a6d",
        "#012749",
        "#1c0f30",
    ],
    "sequential_teal": [
        "#d9fbfb",
        "#9ef0f0",
        "#3ddbd9",
        "#08bdba",
        "#009d9a",
        "#007d79",
        "#005d5d",
        "#004144",
        "#022b30",
        "#081a1c",
    ],
    "pastel": [
        "#fd7f6f",
        "#7eb0d5",
        "#b2e061",
        "#bd7ebe",
        "#ffb55a",
        "#ffee65",
        "#beb9db",
        "#fdcce5",
        "#8bd3c7",
    ],
    "bright": [
        "#e60049",
        "#0bb4ff",
        "#50e991",
        "#e6d800",
        "#9b19f5",
        "#ffa300",
        "#dc0ab4",
        "#b3d4ff",
        "#00bfa0",
    ],
}


def set_color_palette(palette_name="pastel"):
    plt.rcParams["axes.prop_cycle"] = cycler(color=palettes[palette_name])


def available_palettes():
    print("Available palettes:")
    for k in palettes.keys():
        print(f"{k.replace('_', ' ').capitalize()}: {k}")


plt.rcParams["axes.prop_cycle"] = cycler(color=palettes["pastel"])

# Typography
plt.rcParams["font.family"] = "IBM Plex Sans"
plt.rcParams["font.size"] = 8
plt.rcParams["figure.dpi"] = 200
plt.rcParams["font.weight"] = "normal"

# Line style
plt.rcParams["lines.linewidth"] = 1
plt.rcParams["axes.xmargin"] = 0


def pt_to_inch(pt):
    return pt / 72.27


def figsize(wratio=1, width_to_height=3 / 2, text_width_pt=397):
    w = pt_to_inch(text_width_pt) * wratio
    h = w / width_to_height
    return (w, h)
