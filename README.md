# 田口正交表自定义生成 · 实验设计探索

按输入的因素数量与水平数生成候选实验表，提供 Python 命令行示例和 Tkinter 图形界面。适合学习因素与水平、比较表格生成方式，以及阅读正交性和平衡性检查代码的读者。

> 当前实现属于算法与界面探索。生成结果需要独立检查，不能将“完全均衡”选项等同于严格正交性，也不应直接作为已验证的工程实验方案。

## 从哪里开始

代码位于 [Taguchi-Orthogonal-Array-Custom-Generation/](Taguchi-Orthogonal-Array-Custom-Generation/)：

- [orthogonal_array_gui.py](Taguchi-Orthogonal-Array-Custom-Generation/orthogonal_array_gui.py)：输入因素和水平，生成表格并显示检查结果。
- [orthogonal_array_v1.py](Taguchi-Orthogonal-Array-Custom-Generation/orthogonal_array_v1.py)：NumPy 实现，含正交性、平衡性与不平衡率检查及示例。
- [orthogonal_array_v2.py](Taguchi-Orthogonal-Array-Custom-Generation/orthogonal_array_v2.py)：按水平数最小公倍数生成重复序列，含独立示例与检查函数。

## 本地尝试

需要带 Tkinter 的 Python、NumPy；`v2` 使用 `math.lcm`，因此 Python 至少为 3.9。仓库没有固定依赖版本或安装包。

在仓库根目录、自己的 Python 环境中，可参考代码入口尝试：

```sh
python3 -m pip install numpy
python3 Taguchi-Orthogonal-Array-Custom-Generation/orthogonal_array_v1.py
python3 Taguchi-Orthogonal-Array-Custom-Generation/orthogonal_array_v2.py
```

两个命令行示例默认使用 3 个因素、3/2/3 水平。图形入口为：

```sh
python3 Taguchi-Orthogonal-Array-Custom-Generation/orthogonal_array_gui.py
```

以上命令依据源文件的导入和 `__main__` 入口整理，尚未进行运行验证；Tkinter 是否可用取决于自己的 Python 安装。

## 当前限制

- GUI 的“完全均衡”分支从 `v2` 获取 Python 列表，却调用 `v1` 中按 NumPy 二维数组索引的正交性检查函数；按当前代码存在类型不匹配，需要修复与验证后再依赖该分支。
- `v2` 的周期序列生成并不保证因素两两组合的等频出现；应对输出另行验证严格正交性。
- 输入范围、无效水平、较大组合的资源消耗与导出能力未形成完整说明。当前界面展示表格，未提供文件导出入口。

## 参与、许可与署名

欢迎通过 [Issues](https://github.com/Ming-Sir-69/Taguchi-Orthogonal-Array-Custom-Generation/issues) 或 Pull Request 提交小规模可复现案例、数学性质验证与界面改进。请同时写出因素、水平、期望组合频数和实际输出，便于核对。

仓库维护：[Ming-Sir-69](https://github.com/Ming-Sir-69)。当前未提供 LICENSE/NOTICE，复用授权待确认；维护署名不新增授权或版权归属结论。

## Original overview

Taguchi-Orthogonal-Array-Custom-Generation

Generate an orthogonal array based on the number of factors and levels input.
