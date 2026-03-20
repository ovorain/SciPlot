import os
import math
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def save_fig(fig, filename, out_dir="figures", formats=["png"], dpi=600):
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    for fmt in formats:
        filepath = os.path.join(out_dir, f"{filename}.{fmt}")
        fig.savefig(filepath, dpi=dpi, bbox_inches='tight', transparent=False)
        print(f"[*] 图表已保存至: {filepath}")

def format_spines_and_ticks(ax, is_bar=False):
    """
    规则6处理：删除上轴/右轴刻度线 (保留边框以形成闭合图表)。
    如果为柱状图，横轴不伸出 tick 线 (保留 label)。
    """
    # 确保图表为四面闭合
    ax.spines['right'].set_visible(True)
    ax.spines['top'].set_visible(True)
    
    # 彻底关闭全图（尤其是上右侧）的多余刻度线，下方和左侧在后续覆盖
    ax.tick_params(right=False, top=False)
    
    if is_bar: # 柱状图
        ax.tick_params(axis='x', length=0)
    else:
        ax.tick_params(axis='x', direction='in')
        
    ax.tick_params(axis='y', direction='in')

def set_scientific_yticks(ax, target_ticks=5):
    """
    规则5处理：强制定义Y轴(左侧)刻度数量精确为 target_ticks (默认5个)，
    生成美观的数字序列，并保证视图在首尾刻度闭合。
    """
    ax.figure.canvas.draw()
    data_min = ax.dataLim.ymin
    data_max = ax.dataLim.ymax
    
    # 过滤无效或过度重叠的数据框
    if data_min >= data_max or math.isclose(data_min, data_max):
        return
        
    target_steps = target_ticks - 1
    range_val = data_max - data_min
    rough_step = range_val / target_steps
    
    # 计算量级映射
    magnitude = 10 ** math.floor(math.log10(rough_step))
    candidates = [1.0, 2.0, 2.5, 5.0, 10.0, 20.0]
    
    final_ticks = []
    for coeff in candidates:
        step = coeff * magnitude
        start_tick = math.floor(data_min / step) * step
        ticks = [start_tick + i * step for i in range(target_ticks)]
        # 必须同时满足第一位比极小值小，最后一位包裹极大值
        if ticks[-1] >= data_max and ticks[0] <= data_min:
            final_ticks = ticks
            break
            
    if not final_ticks:
        # Fallback 硬切
        final_ticks = [data_min + i * rough_step for i in range(target_ticks)]
        
    # 硬性注入这强制的 5 个刻度
    ax.set_yticks(final_ticks)
    
    # 首尾严格闭合，不再出现多余的留白
    ax.set_ylim(bottom=final_ticks[0], top=final_ticks[-1])

def get_data_stats(data, label="Data"):
    """
    计算数据集的描述性统计指标，用于报告解读。
    返回包含 均值、标准差、最大/最小值、样本量的字典。
    """
    import numpy as np
    stats = {
        "label": label,
        "n": len(data),
        "mean": np.mean(data),
        "std": np.std(data),
        "min": np.min(data),
        "max": np.max(data)
    }
    return stats

def format_stats_row(stats):
    """
    将统计指标格式化为 Markdown 表格行。
    """
    return f"| {stats['label']} | {stats['n']} | {stats['mean']:.3f} | {stats['std']:.3f} | {stats['min']:.3f} | {stats['max']:.3f} |"
