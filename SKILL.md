---
name: Standard Scientific Plotting
description: 封装了标准的科研绘图规范、样式配置和可复用的渲染工具，默认采用黑白宋体/Times New Roman排版以生成最佳论文级别图表。
---

# Standard Scientific Plotting Skill

## 1. 概述 (Overview)

此 Skill 旨在提供一个标准化、可复用、出版级别的科研绘图框架。已严格更新图表尺寸比例、8pt字体锁定、单轴黑体显示法则、以及严格的中英文混合排版的字体映射规则。

## 2. 目录结构 (Directory Structure)

- `configs/`：全局配置中枢。存储 `plotting_params.yaml` 等外部参数文件，将字号、分辨率、尺寸比例与 Python 逻辑剥离，方便非技术人员快速调整绘图风格。
- `data/`：标准化数据处理中枢枢栏。包含内部的 `raw` 子文件夹（只读，存储不可修改的元数据）、`processed`（二次清洗提取的过程数据归档）以及向用户提供详细工作日志或作图解释的综合性报告文本（`.md` 文本形式）。
- `figures/`：科研图表集中存放中心。所有 Python 分析脚本依托框架引擎统一生成的 600 DPI 高清 **PNG 格式图表**将默认输出至此目录。
- `environment.yml` / `requirements.txt`：标准环境配置清单。用于一键部署依赖，确保 Matplotlib 功能与科学核心库稳定。
- `scripts/`
  - `style_config.py`：核心样式模块。支持按不同排版版式输出特定尺寸，严格设定中英文字体并默认输出黑白灰色系图表。
  - `plot_utils.py`：绘图工具模块。实现纵轴首位标签闭合、单轴图边框去除以及柱状图无刻度线的精确控制。
- `examples/`
  - `plot_example.py`：示例文件，包含标准折线图与柱状图的绘制，演示了混排文字如何依靠工具分离字体。

## 3. 科研绘图核心规则 (Core Rules)

**环境与配置机制 (Environment Setup)**
为了确保绘图参数无缝衔接且支持 LaTeX 高级数学解析渲染，请在画图前严格检查所需依赖。

1. **Conda 初始化 (强烈推荐)**: 运行 `conda env create -f environment.yml` 创建隔离环境 `sciplot_env`，然后通过 `conda activate sciplot_env` 激活。
2. **Pip 快速安装**: 使用 `pip install -r requirements.txt` 补全当前环境所需的 matplotlib 与 numpy 库依赖。

**规则 1：颜色默认配置 (Grayscale Default)**

- 本框架默认绘制黑白图（内部含深浅不同的黑白灰，同时提供图案填充 `hatch` 或者虚实线型）。若非用户强烈要求，坚决不默认构建彩色图。

**规则 2：统一画布排版尺寸 (Dimensions)**
包含以下默认尺寸（自动换算为英寸用于 matplotlib figsize 配置）：

- 单图：12cm \* 8cm
- 2*1 组合排版：15cm * 7cm
- 3*1 组合排版：15cm * 6cm
- 2*2 组合排版：15cm * 12cm

**规则 0：输出与导出 (Export)**

- 框架**强制且仅导出 PNG 格式**，不再保留 PDF/SVG 等矢量中间档，以确保图片在报告与文档中的直观展示。
- 分辨率**严格规定为 600 DPI**，采用 `bbox_inches='tight'` 以切除冗余白边。

**规则 3：严格字体混排控制 (Fonts)**

- 中文字体统一为宋体 (SimSun)。
- 英文字母、符号及数字统一为 Time News Roman。
- _注意_：由于 Matplotlib 渲染机制，对包含中英文混排的标签，推荐通过原生的备用字体回退池实现；或者显式对英文部分加上数学格式符 (例如 `标签值 ($Label$)` ) 实现强制分轨采用 Times New Roman。

**规则 4：锁定字号 (Font Size)**

- 图表内部所有字体（含图例、坐标轴刻度数字、坐标轴标题题注）统一设定全局 **8 pt**，不进行任何等级区分。

**规则 5：纵向刻度标签闭合约束 (Y-ticks Closure)**

- 如果纵轴存在刻度值，一般强制重算为 5 个有效标签刻度。
- 图表的 Y 轴显示范围必须 **以首位的标签值闭合**（即图表底部 Y 轴极小值等价于生成的最底端刻度标签。不允许多余下延留白）。

**规则 6：边框刻度简化处理 (Spines & Formatting)**

- 单轴图强制要求删除上侧 (top) 和右侧 (right) 的 **刻度线 (Ticks)**，但必须保留四面边框以构筑 **闭合图表**。
- 四边所有刻度线标（Tick线）朝内 (direction='in')。
- 柱状图特殊的 X 轴（横轴）必须隐去往里或往外伸出的刻度线，仅保留下方文字。

**规则 7：图内坐标轴标签模板 (Label Formatting)**

- 坐标轴或涉及单位说明的图内标，必须精准遵循 **`中文名称/（英文单位）`** 的标准（注意斜杠后无多余空格，并使用全角括号即中文括号）。
- 示例语法：`时间/（$h$）` 或者 `生物指示量/（$mg \cdot L^{-1}$）`。
- 将内部的英文/单位通过 `$ $` 设为数学模式以绑定 Times New Roman，而外圈的全角括号连同中文一起自然降级采用宋体显示，完美贴合严苛的学术排版规范。

**规则 8：统计指标配套解读 (Statistical Reporting)**

- 每一张产出的 `figure` 必须配套对应的统计指标解读（存储于 `data/` 报告中）。
- 强制报告指标包括：样本量 ($N$)、均值 ($\text{Mean}$)、标准差 ($\text{Std}$) 或标准误 ($\text{SE}$)、以及数值范围（$\text{Min/Max}$）。
- 推荐使用 `plot_utils.get_data_stats` 自动提取指标并维护 Markdown 统计表格。
