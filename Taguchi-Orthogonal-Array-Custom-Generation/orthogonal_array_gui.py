import tkinter as tk
from tkinter import ttk, messagebox
from orthogonal_array_v1 import generate_orthogonal_array_v1, check_orthogonality, check_balance, calculate_imbalance_rate
from orthogonal_array_v2 import generate_orthogonal_array_v2

class OrthogonalArrayGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("正交表生成器")
        self.factors = {}
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.master, text="因素数量:").grid(row=0, column=0, padx=5, pady=5)
        self.n_factors_entry = ttk.Entry(self.master)
        self.n_factors_entry.grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(self.master, text="设置因素", command=self.set_factors).grid(row=0, column=2, padx=5, pady=5)

        self.factors_frame = ttk.Frame(self.master)
        self.factors_frame.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        self.balance_var = tk.BooleanVar()
        self.balance_switch = ttk.Checkbutton(self.master, text="完全均衡", variable=self.balance_var, style="Switch.TCheckbutton", command=self.update_warning)
        self.balance_switch.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

        self.warning_label = ttk.Label(self.master, text="生成的正交表可能不完全符合均衡性", foreground="orange")
        self.warning_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

        ttk.Button(self.master, text="生成正交表", command=self.generate_array).grid(row=4, column=0, columnspan=3, padx=5, pady=5)

        self.result_text = tk.Text(self.master, height=20, width=50)
        self.result_text.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

        self.check_text = tk.Text(self.master, height=10, width=50)
        self.check_text.grid(row=6, column=0, columnspan=3, padx=5, pady=5)

    def set_factors(self):
        try:
            n_factors = int(self.n_factors_entry.get())
        except ValueError:
            messagebox.showerror("错误", "请输入有效的因素数量")
            return

        for widget in self.factors_frame.winfo_children():
            widget.destroy()

        for i in range(n_factors):
            ttk.Label(self.factors_frame, text=f"因素 {chr(65+i)} 水平数:").grid(row=i, column=0, padx=5, pady=2)
            level_entry = ttk.Entry(self.factors_frame)
            level_entry.grid(row=i, column=1, padx=5, pady=2)
            self.factors[i] = level_entry

    def update_warning(self):
        if self.balance_var.get():
            self.warning_label.config(text="生成的正交表完全符合均衡性，但实验次数较多", foreground="blue")
        else:
            self.warning_label.config(text="生成的正交表可能不完全符合均衡性", foreground="orange")

    def generate_array(self):
        try:
            factors = {chr(65+i): int(level_entry.get()) for i, level_entry in self.factors.items() if level_entry.get().strip()}
            if not factors:
                raise ValueError("请输入因素的水平数")
        except ValueError as e:
            messagebox.showerror("错误", str(e))
            return
        
        try:
            if self.balance_var.get():
                oa = generate_orthogonal_array_v2(factors)
            else:
                oa = generate_orthogonal_array_v1(factors)

            is_orthogonal = check_orthogonality(oa, factors)
            is_balanced = check_balance(oa, factors)

            self.display_result(oa, factors, is_orthogonal, is_balanced)
        except Exception as e:
            messagebox.showerror("错误", f"生成正交表时发生错误: {str(e)}")

    def display_result(self, oa, factors, is_orthogonal, is_balanced):
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "生成的正交表:\n")
        self.result_text.insert(tk.END, " ".join(factors.keys()) + "\n")
        for row in oa:
            self.result_text.insert(tk.END, " ".join(f"{chr(65+i)}{x+1}" for i, x in enumerate(row)) + "\n")

        self.check_text.delete(1.0, tk.END)
        self.check_text.insert(tk.END, f"正交性: {'符合' if is_orthogonal else '不符合'}\n")
        self.check_text.insert(tk.END, f"均衡性: {'符合' if is_balanced else '不符合'}\n\n")

        if self.balance_var.get():
            self.check_text.insert(tk.END, "平衡性验证:\n")
            for i, factor in enumerate(factors.keys()):
                column = [row[i] for row in oa]
                self.check_text.insert(tk.END, f"  因素 {factor}:\n")
                for level in range(factors[factor]):
                    count = column.count(level)
                    self.check_text.insert(tk.END, f"    水平 {level+1}: 出现 {count} 次\n")
        else:
            self.check_text.insert(tk.END, "不平衡率:\n")
            for i, factor in enumerate(factors.keys()):
                column = [row[i] for row in oa]
                imbalance_rate = calculate_imbalance_rate(column)
                self.check_text.insert(tk.END, f"  因素 {factor}: {imbalance_rate:.4f}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = OrthogonalArrayGUI(root)
    style = ttk.Style(root)
    style.configure("Switch.TCheckbutton", indicatorsize=20)
    root.mainloop()