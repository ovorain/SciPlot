import matplotlib.pyplot as plt

def apply_scientific_style(layout="single", color_theme="grayscale"):
    """
    配置核心 matplotlib rcParams
    满足用户规则：强制8pt，中英字分离，指定版式规格，默认黑白图机制。
    
    layout: 'single' (12x8cm), '2x1' (15x7cm), '3x1' (15x6cm), '2x2' (15x12cm)
    """
    cm2in = 1 / 2.54
    layout_sizes = {
        "single": (12 * cm2in, 8 * cm2in),
        "2x1": (15 * cm2in, 7 * cm2in),
        "3x1": (15 * cm2in, 6 * cm2in),
        "2x2": (15 * cm2in, 12 * cm2in)
    }
    
    # 规则4：全图强制 8pt
    font_size = 8
    
    params = {
        # 规则3：中文字体宋体(SimSun)，英文/符号Times New Roman。
        # 这里借助 font.serif 优先列表回退，以及 mathtext.default 定制来实现英文隔离
        "font.family": "serif",
        "font.serif": ["SimSun", "宋体", "Times New Roman"],
        "font.sans-serif": ["SimSun", "宋体", "Times New Roman"],
        "mathtext.fontset": "custom",
        "mathtext.rm": "Times New Roman",
        "mathtext.it": "Times New Roman:italic",
        "mathtext.bf": "Times New Roman:bold",
        "mathtext.default": "rm",
        "axes.formatter.use_mathtext": True,
        "axes.unicode_minus": False,
        "axes.unicode_minus": False,
        
        # 规则2：排版尺寸
        "figure.figsize": layout_sizes.get(layout, layout_sizes["single"]),
        
        # 规则4：统一字号
        "font.size": font_size,
        "axes.titlesize": font_size,
        "axes.labelsize": font_size,
        "xtick.labelsize": font_size,
        "ytick.labelsize": font_size,
        "legend.fontsize": font_size,
        "legend.title_fontsize": font_size,
        "figure.titlesize": font_size,
        
        # 边框
        "axes.linewidth": 0.8,
        
        # 规则6：必须保留边框构筑闭合图表，仅通过代码管理刻度线
        "axes.spines.top": True,
        "axes.spines.right": True,
        
        # 规则6：刻度线默认朝内
        "xtick.direction": "in",
        "ytick.direction": "in",
        "xtick.major.width": 0.8,
        "ytick.major.width": 0.8,
        "xtick.major.size": 3.5,
        "ytick.major.size": 3.5,
        "xtick.bottom": True,
        "ytick.left": True,
        "xtick.top": False,
        "ytick.right": False,
        
        # 一些精美的线体配置
        "lines.linewidth": 1.2,
        "lines.markersize": 4.5,
        "lines.markeredgewidth": 0.6,
        "legend.frameon": False,
        
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.05,
        "savefig.transparent": False,
        "savefig.dpi": 600,
    }
    plt.rcParams.update(params)

# 规则1：黑白绘图配色板
COLORS = {
    # 深浅不一的黑白灰级联，供描边和填充使用
    "grayscale": ["#000000", "#4D4D4D", "#737373", "#999999", "#C0C0C0"]
}
# 补充提供图案填充集，以便柱状图区分不同数据系列
HATCHES = ['', '///', '\\\\\\', 'xx', '---', '+++', '...']
