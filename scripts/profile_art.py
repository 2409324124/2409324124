import math
import re

ART = {}
ART_COLORS = {}


def _canvas():
    return [[None for _ in range(40)] for _ in range(40)]


def _polygon(canvas, points, color):
    for y in range(40):
        for x in range(40):
            px, py = x + .5, y + .5
            inside = False
            for i, (ax, ay) in enumerate(points):
                bx, by = points[i - 1]
                if (ay > py) != (by > py):
                    crossing = (bx - ax) * (py - ay) / (by - ay) + ax
                    if px < crossing:
                        inside = not inside
            if inside:
                canvas[y][x] = color


def _rect(canvas, x1, y1, x2, y2, color):
    for y in range(y1, y2):
        for x in range(x1, x2):
            canvas[y][x] = color


def _stroke(canvas, points, width, color):
    for y in range(40):
        for x in range(40):
            for (ax, ay), (bx, by) in zip(points, points[1:]):
                dx, dy = bx-ax, by-ay
                t = max(0, min(1, ((x+.5-ax)*dx+(y+.5-ay)*dy)/(dx*dx+dy*dy)))
                if math.hypot(x+.5-ax-t*dx, y+.5-ay-t*dy) <= width/2:
                    canvas[y][x] = color
                    break


def _export(key, canvas):
    rows, colors = [], []
    for y in range(0, 40, 2):
        chars, inks = [], []
        for x in range(40):
            top, bottom = canvas[y][x], canvas[y+1][x]
            chars.append('█' if top and bottom else '▀' if top else '▄' if bottom else ' ')
            inks.append(top or bottom or '#24292f')
        rows.append(''.join(chars))
        colors.append(inks)
    ART[key], ART_COLORS[key] = rows, colors


def _python():
    canvas = _canvas()
    blue = [(13,1),(27,1),(30,4),(30,16),(27,19),(16,19),(12,23),(12,31),(8,31),(4,27),(4,16),(7,12),(11,12),(11,9),(23,9),(23,7),(11,7),(11,4)]
    _polygon(canvas, blue, '#24618c')
    _polygon(canvas, [(40-x,40-y) for x,y in blue], '#a67508')
    _rect(canvas, 15, 4, 18, 6, None)
    _rect(canvas, 22, 34, 25, 36, None)
    _export('python', canvas)


def _fastapi():
    canvas = _canvas()
    for y in range(40):
        for x in range(40):
            if math.hypot(x-19.5,y-19.5) <= 18.5:
                canvas[y][x] = '#008576'
    _polygon(canvas, [(24,5),(10,23),(19,23),(15,35),(30,16),(21,16)], None)
    _export('fastapi', canvas)


def _mcp():
    canvas = _canvas()
    ink = '#35313c'
    upper = [(7,21),(22,6),(24,4),(27,3),(30,4),(32,6),(33,9),(32,12),(30,14),(17,27)]
    lower = [(23,12),(10,25),(8,27),(7,30),(8,33),(10,35),(13,36),(16,35),(31,20)]
    _stroke(canvas, upper, 3.2, ink)
    _stroke(canvas, lower, 3.2, ink)
    _stroke(canvas, [(13,17),(22,8),(24,7),(27,7),(29,9),(29,11),(28,13)], 1.1, None)
    _stroke(canvas, [(15,26),(18,29),(21,32),(23,35)], 3.2, ink)
    _export('mcp', canvas)


def _docker():
    canvas = _canvas()
    ink = '#1266a5'
    for x,y in [(17,3),(12,9),(17,9),(2,15),(7,15),(12,15),(17,15),(22,15)]:
        _rect(canvas, x,y,x+4,y+5,ink)
    _polygon(canvas, [(1,22),(29,22),(32,20),(31,17),(32,12),(35,15),(36,19),(39,18),(39,22),(36,25),(32,26),(29,31),(25,35),(19,37),(12,37),(6,34),(3,30)], ink)
    _rect(canvas, 6, 25, 8, 27, None)
    _stroke(canvas, [(9,32),(14,33),(21,32)], 1, None)
    _export('docker', canvas)


# Ubuntu character artwork adapted from https://github.com/dylanaraps/neofetch
# Copyright (c) 2015-2021 Dylan Araps
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

_UBUNTU = r'''${c1}            .-/+oossssoo+\-.
        ´:+ssssssssssssssssss+:`
      -+ssssssssssssssssssyyssss+-
    .ossssssssssssssssss${c2}dMMMNy${c1}sssso.
   /sssssssssss${c2}hdmmNNmmyNMMMMh${c1}ssssss\
  +sssssssss${c2}hm${c1}yd${c2}MMMMMMMNddddy${c1}ssssssss+
 /ssssssss${c2}hNMMM${c1}yh${c2}hyyyyhmNMMMNh${c1}ssssssss\
.ssssssss${c2}dMMMNh${c1}ssssssssss${c2}hNMMMd${c1}ssssssss.
+ssss${c2}hhhyNMMNy${c1}ssssssssssss${c2}yNMMMy${c1}sssssss+
oss${c2}yNMMMNyMMh${c1}ssssssssssssss${c2}hmmmh${c1}ssssssso
oss${c2}yNMMMNyMMh${c1}sssssssssssssshmmmh${c1}ssssssso
+ssss${c2}hhhyNMMNy${c1}ssssssssssss${c2}yNMMMy${c1}sssssss+
.ssssssss${c2}dMMMNh${c1}ssssssssss${c2}hNMMMd${c1}ssssssss.
 \ssssssss${c2}hNMMM${c1}yh${c2}hyyyyhdNMMMNh${c1}ssssssss/
  +sssssssss${c2}dm${c1}yd${c2}MMMMMMMMddddy${c1}ssssssss+
   \sssssssssss${c2}hdmNNNNmyNMMMMh${c1}ssssss/
    .ossssssssssssssssss${c2}dMMMNy${c1}sssso.
      -+sssssssssssssssss${c2}yyy${c1}ssss+-
        `:+ssssssssssssssssss+:`
            .-\+oossssoo+/-.
'''


def _ubuntu():
    rows, colors = [], []
    color = '#c34216'
    for row in _UBUNTU.splitlines():
        chars, inks = [], []
        for part in re.split(r'(\$\{c[12]\})', row):
            if part == '${c1}':
                color = '#c34216'
            elif part == '${c2}':
                color = '#66231c'
            else:
                chars.extend(part)
                inks.extend([color] * len(part))
        rows.append(''.join(chars).ljust(40))
        colors.append(inks + ['#24292f'] * (40-len(inks)))
    ART['ubuntu'], ART_COLORS['ubuntu'] = rows, colors


_python()
_fastapi()
_mcp()
_docker()
_ubuntu()
