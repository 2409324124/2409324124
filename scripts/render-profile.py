from pathlib import Path
from html import escape
from base64 import b64encode
from aircraft_art import AIRCRAFT, AIRCRAFT_COLORS
from profile_art import ART, ART_COLORS

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
BG, PANEL, LINE = '#ffffff', '#f8f9fa', '#dadce0'
INK, GRAY, TEAL, BLUE, GREEN, AMBER, MAGENTA = '#202124', '#5f6368', '#006b76', '#1a73e8', '#137333', '#9c5700', '#8430a0'
FONT = "'DejaVu Sans Mono','Noto Sans Mono CJK SC',monospace"

ICONS = {
    'tu22': ['       ▲       ', '       █       ', '      ▐█▌      ', '      ▐█▌      ', '    ▄▄███▄▄    ', ' ▄███████████▄ ', '▀▀▀▀  ▐█▌  ▀▀▀▀', '      ▐█▌      ', '    ▄█████▄    ', '    ▀  █  ▀    '],
    'cat': ['    ▄█████▄    ', '  ▄██▀ ▀ ▀██▄  ', ' ▐██ ▄█ █▄ ██▌ ', ' ██ ▀ ▄█▄ ▀ ██ ', ' ▐██ █ ▀ █ ██▌ ', '  ▀██▄ █ ▄██▀  ', '    ▀█████▀    ', '      ▐█▌      ', '  ▄▄▄▄███▄▄▄▄  ', '  ▀▀▀▀▀▀▀▀▀▀▀  '],
    'prep': ['   ▄██████▄    ', ' ▄██▀    ▀██▄  ', ' ██    ┌───██─┐', ' ██    │ 3/7  │', ' ▼     │ ───  │', '       │ ──   │', ' ▲     └──────┘', ' ██         ██ ', ' ▀██▄     ▄██▀ ', '   ▀███████▀   '],
    'xeon': ['   │ │ │ │ │   ', ' ┌─┴─┴─┴─┴─┴─┐ ', '─┤ ▄▄▄▄▄▄▄▄▄ ├─', '─┤ █       █ ├─', '─┤ █  HBM  █ ├─', '─┤ █  AMX  █ ├─', '─┤ █▄▄▄▄▄▄▄█ ├─', '─┤           ├─', ' └─┬─┬─┬─┬─┬─┘ ', '   │ │ │ │ │   '],
    'nano': [' ┌────────────┐', ' │ ▄ ▄ ▄      │', ' ├────────────┤', ' │            │', ' │  >_        │', ' │     { }    │', ' │            │', ' └─────┬┬─────┘', '    ▄▄▄██▄▄▄   ', '    ▀▀▀▀▀▀▀▀   '],
    'latex': [' ┌───────────┐ ', ' │  ▄▄▄▄▄▄   │ ', ' │   ▀█▄     │ ', ' │     █►    │ ', ' │   ▄█▀     │ ', ' │  ▀▀▀▀▀▀   │ ', ' │   x + y   │ ', ' │  ───────  │ ', ' │     n     │ ', ' └───────────┘ '],
    'viz': [' ┌───────────┐ ', ' │ > run()   │ ', ' │ ───────── │ ', ' │    █      │ ', ' │    █  █   │ ', ' │ █  █  █   │ ', ' │ █  █  █ █ │ ', ' │ █  █  █ █ │ ', ' └───────────┘ ', '    TRACE →    '],
    'router': ['    ┌─────┐    ', '    │ CLI │    ', '    └──┬──┘    ', '       │       ', '  ┌────┼────┐  ', '  │    │    │  ', ' ┌┴┐  ┌┴┐  ┌┴┐ ', ' │A│  │B│  │C│ ', ' └─┘  └─┘  └─┘ ', '    ROUTING    '],
    'deepseek': [' ┌───┐   ┌───┐ ', ' │API│   │API│ ', ' │   │   │   │ ', ' └─┬─┘   └─┬─┘ ', '   │       │   ', '   └──►◄───┘   ', '    ┌─────┐    ', '    │ MCP │    ', '    └─────┘    ', '    ARCHIVE    '],
    'mahjong': ['  ┌─────────┐  ', '  │ ┌─────┐ │  ', '  │ │  │  │ │  ', '  │ │ ─┼─ │ │  ', '  │ │  │  │ │  ', '  │ └─────┘ │  ', '  │   ███   │  ', '  │   █ █   │  ', '  │   ███   │  ', '  └─────────┘  '],
    'voice': ['       │       ', '   │   █   │   ', '   █ │ █ │ █   ', ' │ █ █ █ █ █ │ ', ' █ █ █ █ █ █ █ ', ' █ █ █ █ █ █ █ ', ' │ █ █ █ █ █ │ ', '   █ │ █ │ █   ', '   │   █   │   ', '       │       '],
    'lstm': [' ┌───┐   ┌───┐ ', ' │ A │   │ B │ ', ' └─┬─┘   └─▲─┘ ', '   │       │   ', '   ▼       │   ', ' ┌───┬───┬───┐ ', ' │ h │ h │ h │ ', ' └───┴───┴───┘ ', '   →   →   →   ', '    SEQ2SEQ    '],
}

ICONS.update({
    'python': ['    ▄██████▄   ', '    █ ▀ ████   ', '    ▀▀▀▀████   ', ' ▄██████████▄▄ ', ' ████▀▀▀▀▀▀███ ', ' ████▄▄▄▄▄▄███ ', ' ▀▀██████████▀ ', '   ████▄▄▄▄    ', '   ████ ▄ █    ', '   ▀██████▀    '],
    'pytorch': ['       ▄█      ', '      ▄█▀  ▄   ', '     ▄█▀   ▀   ', '   ▄██         ', '  ██▀      ▄▄  ', ' ▐██        ██ ', ' ▐██        ██ ', '  ██▄      ▄██ ', '   ▀██▄▄▄▄██▀  ', '     ▀▀▀▀▀▀    '],
    'fastapi': ['        ▄███   ', '       ▄███▀   ', '      ▄███▀    ', '     ▄███▀     ', '    █████████  ', '       ▄███▀   ', '      ▄██▀     ', '     ▄██▀      ', '    ▄█▀        ', '   ▄▀          '],
    'mcp': [' ┌───┐   ┌───┐ ', ' │ A ├───┤ B │ ', ' └─┬─┘   └─┬─┘ ', '   │       │   ', '   └───┬───┘   ', '     ┌─┴─┐     ', '     │ + │     ', '     └─┬─┘     ', '       │       ', '      >_       '],
    'linux': ['     ▄████▄    ', '    ██▀██▀██   ', '    ██ ▀▀ ██   ', '    █▀ ▄▄ ▀█   ', '   ██ ████ ██  ', '  ██ ██████ ██ ', ' ▐██ ██████ ██▌', '  ██▄██████▄██ ', ' ▄███▀▀▀▀▀▀███▄', ' ▀▀▀▀      ▀▀▀▀'],
    'docker': ['        ▄▄     ', '     ▄▄ ██     ', '  ▄▄ ██ ██     ', '  ██ ██ ██     ', ' ────────── ▄█ ', ' ████████████▀ ', ' ███████████▀  ', ' ▀█████████▀   ', '  ▀██████▀     ', '    ▀▀▀▀       '],
})
TECH = [('python', 'Python', TEAL), ('pytorch', 'PyTorch', '#c43c21'),
        ('fastapi', 'FastAPI', GREEN), ('mcp', 'MCP', MAGENTA),
        ('ubuntu', 'Ubuntu', '#c34113'), ('docker', 'Docker', TEAL)]

ICONS['memoh'] = ICONS['router']
ICONS['milksu'] = ICONS['nano']

PROJECTS = [
    ('tu22', 'TU22', 'FLIGHT GAME', TEAL, ['Tu-22M3 浏览器飞行游戏', '飞行、座舱与任务实验'], 'DESKTOP + KEYBOARD'),
    ('cat', 'CAT-Psych', 'ADAPTIVE ASSESSMENT', MAGENTA, ['中文大五人格自适应测评', 'MIRT / CAT · 心理学 × 机器学习'], 'APPLICATION / MIRT + CAT'),
    ('prep', 'PrepLoop', 'SPACED REPETITION', GREEN, ['算法、Agent Harness 与系统设计', '把知识放进每日复习循环'], 'APPLICATION / DAILY REVIEW'),
    ('xeon', 'Xeon Max 9470C', 'HARDWARE LAB', AMBER, ['稀有硬件 Bench 测评 + CPU 推理', 'Xeon Max · HBM / AMX / NUMA'], 'BENCHMARK / 52C + 104T'),
    ('nano', 'Nanocoder', 'OPEN SOURCE / MAINTAINER', TEAL, ['Nano Collective 终端 Coding Agent', '自选模型 · 本机代码 · 我参与维护'], 'ROLE / MAINTAINER'),
    ('latex', 'Qwen3 LaTeX', 'FORMULA CORRECTION', MAGENTA, ['自然语言数学描述 → 规范 LaTeX', 'Qwen3-4B · LoRA SFT · 评测与推理'], 'RESEARCH / MODEL + EVALUATION'),
    ('memoh', 'Memoh', 'COMMUNITY', TEAL, ['开源多智能体平台', '维护者社群参与 · 产品建议与反馈'], 'ROLE / MAINTAINER COMMUNITY'),
    ('milksu', 'MilkSU', 'COMMUNITY', MAGENTA, ['本地 AI Agent 工作台', '维护者社群参与 · 产品建议与反馈'], 'ROLE / MAINTAINER COMMUNITY'),
]


def text(x, y, value, size=18, color=INK, extra=''):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" {extra}>{escape(value)}</text>'


def rect(x, y, w, h, fill, stroke=None):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"' + (f' stroke="{stroke}"' if stroke else '') + '/>'


def save(name, w, h, content, title):
    (ASSETS / name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(title, quote=True)}"><title>{escape(title)}</title>' + rect(0, 0, w, h, BG) + f'<g font-family="{FONT}">' + ''.join(content) + '</g></svg>\n')


def sprite(key, x, y, size, color):
    result = []
    for i, row in enumerate(ICONS[key]):
        ink = color
        if (key == 'python' and i >= 5) or (key == 'linux' and i >= 8):
            ink = AMBER
        elif key not in {item[0] for item in TECH} and i % 4 == 0:
            ink = INK
        result.append(text(x, y + i * size, row, size, ink, 'xml:space="preserve"'))
    return result


def rule(w, y, char='-'):
    count = 92 if w > 600 else 52
    return text(10, y, '+' + char * (count-2) + '+', 14 if w > 600 else 12, GRAY,
                f'textLength="{w-20}" lengthAdjust="spacingAndGlyphs"')


def frame(w, h, separators=()):
    out = [rule(w, 18), rule(w, h-8)]
    for y in range(34, h-17, 16):
        out += [text(10, y, '|', 14, GRAY), text(w-18, y, '|', 14, GRAY)]
    out += [rule(w, y, char) for y, char in separators]
    return out


def art(rows, colors, x, y, size, default=INK):
    out = []
    for row_index, row in enumerate(rows):
        for col_index, char in enumerate(row):
            if char == ' ':
                continue
            color = colors[row_index][col_index] if isinstance(colors, list) else colors.get(char, default)
            out.append(text(x+col_index*size*0.602, y+row_index*size, char, size, color))
    return out


nano_uri = 'data:image/png;base64,' + b64encode((ASSETS/'nanocoder-upstream.png').read_bytes()).decode()
for n, (key, title, category, color, desc, status) in enumerate(PROJECTS, 1):
    for mobile in (False, True):
        w = 420 if mobile else 840
        h = (370 if mobile else 470) if key == 'tu22' else (300 if mobile else 230)
        out = frame(w, h, [(48, '='), (h-48, '-')])
        out += [text(28, 38, f'{n:02}  {title}', 19 if mobile else 22)]
        if key == 'tu22':
            size = 5.5 if mobile else 11
            out += art(AIRCRAFT, AIRCRAFT_COLORS, (w-112*size*0.602)/2, 86, size)
            out += [text(28, h-105+i*27, line, 17 if mobile else 19) for i, line in enumerate(desc)]
        elif key == 'nano':
            side = 132 if mobile else 156
            out += [f'<image x="28" y="60" width="{side}" height="{side}" href="{nano_uri}"/>']
            if mobile:
                out += [text(180, 112, 'MAINTAINER', 16, INK), text(180, 141, 'Nano Collective', 14, GRAY)]
                out += [text(28, 214, '终端 Coding Agent · 我参与维护', 17)]
            else:
                out += [text(215, 98, 'Nano Collective / MAINTAINER', 20)]
                out += [text(215, 132+i*26, line, 18) for i, line in enumerate(desc)]
        elif mobile:
            out += sprite(key, 28, 75, 11, color)
            out += [text(160, 108, category.split(' / ')[0], 13, GRAY)]
            out += [text(28, 208+i*25, line, 17) for i, line in enumerate(desc)]
        else:
            out += sprite(key, 28, 72, 11, color)
            out += [text(200, 100+i*29, line, 19) for i, line in enumerate(desc)]
        out += [text(28, h-25, status, 12 if mobile else 14, GRAY)]
        save(f'project-{key}{"-mobile" if mobile else ""}.svg', w, h, out, f'{title} / {"；".join(desc)}')

for i, key in enumerate(ICONS):
    save(f'icon-{key}.svg', 180, 156, sprite(key, 8, 17, 14, [TEAL,MAGENTA,GREEN,AMBER][i%4]), key+' ANSI icon')

for mobile in (False, True):
    w, h = (420, 132) if mobile else (840, 142)
    out = frame(w, h)
    out += [text(28, 72, 'Shinonome / 东云', 29 if mobile else 38), text(28, 108, 'shinonome.xyz', 17, GRAY)]
    save(f'shinonome-bbs{"-mobile" if mobile else ""}.svg', w, h, out, 'Shinonome / 东云')

for mobile in (False, True):
    w, cols, tile_w, tile_h = (420, 1, 396, 312) if mobile else (840, 2, 408, 320)
    rows = 6 if mobile else 3
    h = rows * tile_h + 30
    out = frame(w, h)
    for i, (key, label, color) in enumerate(TECH):
        x, y = 12+(i%cols)*tile_w, 16+(i//cols)*tile_h
        out += [text(x+18, y+23, f'[{i+1:02}] {label}', 19, INK)]
        if key == 'pytorch':
            size = 20
            out += sprite(key, x+(tile_w-15*size*0.602)/2, y+63, size, color)
        else:
            rows_art = ART[key]
            size = 10.5 if key == 'ubuntu' else 11
            art_width = max(map(len, rows_art))*size*0.602
            out += art(rows_art, ART_COLORS[key], x+(tile_w-art_width)/2, y+62, size, color)
        if i//cols < rows-1:
            count = 44
            out += [text(x+14, y+tile_h-4, '+'+'-'*(count-2)+'+', 13, GRAY,
                         f'textLength="{tile_w-28}" lengthAdjust="spacingAndGlyphs"')]
    save(f'tech-stack{"-mobile" if mobile else ""}.svg', w, h, out,
         'ANSI 技术栈：Python、PyTorch、FastAPI、MCP、Ubuntu、Docker')

for name, label in [('projects','01 / PROJECT DIRECTORY'),('about','02 / TOOLBOX'),('archive','03 / ARCHIVE'),('snake','04 / CONTRIBUTION SNAKE')]:
    for mobile in (False,True):
        w,h = (420,70) if mobile else (840,76)
        out = frame(w,h)
        out += [text(28,44,label,17 if mobile else 21,INK)]
        save(f'section-{name}{"-mobile" if mobile else ""}.svg',w,h,out,label)

ARCHIVE = [
    ('viz', ['Programming', 'Visualization'], '算法执行与调用栈可视化'),
    ('router', ['Claude Code', 'Multi-Provider'], '多模型路由与诊断'),
    ('deepseek', ['DeepSeek Codex', 'Adapter'], '早期适配实验 / 历史记录'),
    ('mahjong', ['Riichi Mahjong', 'Recognition'], '牌面识别、规则与牌效计算'),
    ('voice', ['GPT-SoVITS', 'PR #2767'], 'Windows 单卡 LoRA 训练改进'),
    ('lstm', ['LSTM', 'Translator'], 'Seq2Seq / Attention 翻译实践'),
]
for key, title_lines, desc in ARCHIVE:
    for mobile in (False, True):
        w,h = (420,238) if mobile else (840,180)
        out=frame(w,h)
        out+=sprite(key,28,42,11,TEAL)
        if mobile:
            out += [text(156,65+i*27,line,16) for i,line in enumerate(title_lines)]
            out += [text(28,201,desc,16)]
        else:
            out += [text(190,65,' '.join(title_lines),21),text(190,107,desc,18,GRAY)]
        save(f'archive-{key}{"-mobile" if mobile else ""}.svg',w,h,out,' '.join(title_lines)+' / '+desc)

ansi=[]
for i, (key, rows) in enumerate(ICONS.items()):
    code = [96, 95, 92, 93][i % 4]
    ansi.append('\x1b[0;97m' + key + '\n' + f'\x1b[{code}m' + '\n'.join(row.rstrip() for row in rows) + '\x1b[0m\n')
(ASSETS/'project-icons.ans').write_text('\n'.join(ansi))
