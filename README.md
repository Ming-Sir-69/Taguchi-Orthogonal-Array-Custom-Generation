<picture>
  <source media="(prefers-color-scheme: dark)" srcset="readme-assets/header-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="readme-assets/header-light.svg">
  <img alt="田口实验表生成探索 · ✦ EricMingle69" src="readme-assets/header-light.svg" width="100%">
</picture>

<p align="center">
  <a href="README.md">简体中文</a> · <a href="README.en.md">English</a> · <a href="PERSONAL-NOTICE.md">✦ EricMingle69</a>
</p>

# 田口实验表生成探索

## 项目定位

根据因素和水平输入生成候选实验表，提供两个 Python 示例与 Tkinter 界面，适合研究表格生成与正交性检查。

## 阅读入口

| 入口 | 内容 |
| --- | --- |
| [图形界面](Taguchi-Orthogonal-Array-Custom-Generation/orthogonal_array_gui.py) | 因素输入、表格与检查展示 |
| [NumPy 实现](Taguchi-Orthogonal-Array-Custom-Generation/orthogonal_array_v1.py) | 正交性、平衡性与不平衡率检查 |
| [LCM 序列实现](Taguchi-Orthogonal-Array-Custom-Generation/orthogonal_array_v2.py) | 按水平数最小公倍数生成重复序列 |

## 从哪里开始

1. 准备带 Tkinter 的 Python ≥3.9 和 NumPy，仓库未锁定依赖版本。
2. 可从命令行示例开始；两份示例使用 3 个因素、3/2/3 水平：

```sh
python3 -m pip install numpy
python3 Taguchi-Orthogonal-Array-Custom-Generation/orthogonal_array_v1.py
python3 Taguchi-Orthogonal-Array-Custom-Generation/orthogonal_array_v2.py
```

3. GUI 入口为 `python3 Taguchi-Orthogonal-Array-Custom-Generation/orthogonal_array_gui.py`。这些是源码入口，不是已通过的运行验证。

## 使用边界

- “完全均衡”不等于严格正交，输出需独立检查两两组合频数。
- GUI 完全均衡分支从 v2 得到列表，却调用 v1 的 NumPy 二维索引检查，按当前源码存在类型不匹配。
- v2 的周期序列不能保证所有因素对的组合等频；不直接将结果作为工程实验方案。
- 当前未提供文件导出入口，输入范围与大规模组合的资源边界待补充。

## 来源与原有许可

原仓库没有 LICENSE/NOTICE，源码和既有说明的复用范围未明确。数学性质应由小规模可复现输入和独立检查支持，而不是由项目名称推定。

---

文档维护：**✦ EricMingle69** · [Ming-Sir-69](https://github.com/Ming-Sir-69)  
[个人标识、许可与权限说明](PERSONAL-NOTICE.md) · 明暗页眉随 GitHub 主题自动切换。
