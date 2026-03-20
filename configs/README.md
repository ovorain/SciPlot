# 全局配置中心 (Configuration Center)

本目录用于存放影响全框架绘图行为的外部参数配置文件。

- **`plotting_params.yaml`**：核心参数文件。包含锁定的 600 DPI 分辨率、8pt 字号、默认版式尺寸以及中英文字体映射方案。
- **`fonts/`**：(可选) 若系统环境缺乏宋体或 Times New Roman，可将 `.ttf` 字体文件存放于此进行备用加载。
- **`.mplstyle`**：(可选) 存储 Matplotlib 原生样式表，用于更底层的样式预设。
