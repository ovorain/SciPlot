import numpy as np
import matplotlib.pyplot as plt
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from style_config import apply_scientific_style, COLORS, HATCHES
from plot_utils import save_fig, format_spines_and_ticks, set_scientific_yticks

def main():
    # ==========================
    # 规则1＆2: 黑白图，单图12*8cm尺寸
    # ==========================
    apply_scientific_style(layout="single")
    gray_colors = COLORS["grayscale"]
    
    # 1. 创建折线图
    fig1, ax1 = plt.subplots()
    x = np.linspace(1, 10, 20)
    y_a = np.log(x) + 2
    y_b = np.log(x) + 0.5
    
    # 黑白绘布主要依靠标记形、线型、明暗区分
    ax1.plot(x, y_a, color=gray_colors[0], linestyle='-', marker='D', label='处理 $A$')
    ax1.plot(x, y_b, color=gray_colors[2], linestyle='--', marker='o', label='处理 $B$')
    
    # ==========================
    # 规则3 & 规则7: 字体映射与图内标签强制模板
    # 采用 变量名/（单位） 格式，全角括号由宋体渲染，内部 $ $ 锁死 Times New Roman
    # ==========================
    ax1.set_xlabel(r'时间/（$h$）')
    ax1.set_ylabel(r'生物指示量/（$mg \cdot L^{-1}$）')
    
    # ==========================
    # 规则 8: 统计指标配套解读
    # ==========================
    from plot_utils import get_data_stats, format_stats_row
    stats_a = get_data_stats(y_a, "处理 A")
    stats_b = get_data_stats(y_b, "处理 B")
    print("\n[统计指标报告]")
    print("| 数据系列 | N | 均值 | 标准差 | 最小值 | 最大值 |")
    print("| :--- | :--- | :--- | :--- | :--- | :--- |")
    print(format_stats_row(stats_a))
    print(format_stats_row(stats_b))
    
    ax1.legend()
    out_dir = os.path.join(os.path.dirname(__file__), '..', 'figures') # 指向根目录 figures
    save_fig(fig1, '01_grayscale_line', out_dir=out_dir)

    # 2. 创建柱状图演示 X 轴去刻度线
    fig2, ax2 = plt.subplots()
    labels = ['分类 $1$', '分类 $2$', '分类 $3$']
    means_c = [10.5, 12.2, 8.4]
    means_t = [13.2, 14.1, 9.6]
    
    x_pos = np.arange(len(labels))
    width = 0.35
    
    # 借助 Hatch 图案填充对黑白图进行区分
    ax2.bar(x_pos - width/2, means_c, width, color='w', edgecolor='k', hatch=HATCHES[0], label='Control')
    ax2.bar(x_pos + width/2, means_t, width, color='w', edgecolor='k', hatch=HATCHES[1], label='Treatment')
    
    ax2.set_xticks(x_pos)
    ax2.set_xticklabels(labels)
    ax2.set_ylabel(r'响应频次/（$Freq$）')
    
    # 按照规定柱状图横向不需要刻度线
    format_spines_and_ticks(ax2, is_bar=True)
    set_scientific_yticks(ax2, target_ticks=5)
    
    ax2.legend()
    save_fig(fig2, '02_grayscale_bar', out_dir=out_dir)

if __name__ == "__main__":
    main()
