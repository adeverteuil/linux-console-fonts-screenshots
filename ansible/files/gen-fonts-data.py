#!/usr/bin/env python3

import os
import subprocess
import re

item_format = """\
- name: {name}
  image: {image}
  width: {width}
  height: {height}
"""

# Key for sorting fonts by name and natural numbers.
def sortkey(x):
    # Sample names:
    # 161.cp(8).png ->      ["161", [8]]
    # alt-8x16.png  ->      ["alt", [16, 8]]
    # cp857.08.png  ->      ["cp857", [8, 857]]
    # drdos8x14.psfu.png -> ["drdos8", [14, 8]]
    # koi8-14.psf.png ->    ["koi8", [14, 8]]
    if re.search(r"\d+x\d+", x) is not None:
        part_1 = re.match(r"[^x]*", x)[0]
    else:
        part_1 = re.match(r"[A-Za-z0-9_]*", x)[0]
    numbers = re.findall(r"\d+", x)
    # Sort first by the string until the first punctuation character,
    # then by the last integer in the file name, in natural numbering order.
    return [part_1, [int(i) for i in reversed(numbers)]]

with open("fonts.yaml", "w") as data:
    for f in sorted(os.listdir('screenshots'), key=sortkey):
        p = subprocess.run(['file', 'screenshots/'+f], capture_output=True)
        # Sample output:
        # iso06.14.png: PNG image data, 432 x 293, 8-bit/color RGB, non-interlaced
        dimensions = re.match(r".*: *PNG image data, *(\d*) x (\d*)", p.stdout.decode())
        width = dimensions.group(1)
        height = dimensions.group(2)
        basename = re.sub(r"(.*)\.png$", r"\1", f)
        data.write(item_format.format(name=basename, width=width, height=height, image=f))
