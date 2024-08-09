from math import lcm

def generate_orthogonal_array_v2(factors):
    # 步骤1：确定实验次数
    # N = lcm(L1, L2, ..., Ln)
    n_rows = lcm(*factors.values())

    # 步骤2：生成基本列
    base_columns = []
    for level in factors.values():
        # 创建一个包含0到level-1的重复序列，长度为n_rows
        column = [i % level for i in range(n_rows)]
        base_columns.append(column)

    # 步骤3：组合基本列
    oa = list(zip(*base_columns))

    return oa

def check_orthogonality(oa, factors):
    n_factors = len(factors)
    for i in range(n_factors):
        for j in range(i+1, n_factors):
            combinations = set((row[i], row[j]) for row in oa)
            if len(combinations) != factors[chr(65+i)] * factors[chr(65+j)]:
                return False
    return True

def check_balance(oa, factors):
    for i, (factor, levels) in enumerate(factors.items()):
        column = [row[i] for row in oa]
        expected_count = len(oa) / levels
        if any(column.count(level) != expected_count for level in range(levels)):
            return False
    return True

if __name__ == "__main__":
    # 示例：3因素，分别为3、2、3水平
    factors = {'A': 3, 'B': 2, 'C': 3}

    oa = generate_orthogonal_array_v2(factors)
    is_orthogonal = check_orthogonality(oa, factors)
    is_balanced = check_balance(oa, factors)

    print("\n生成的正交表:")
    print(" ".join(factors.keys()))
    for row in oa:
        print(" ".join(f"{chr(65+i)}{x+1}" for i, x in enumerate(row)))

    print(f"\n正交性: {'符合' if is_orthogonal else '不符合'}")
    print(f"均衡性: {'符合' if is_balanced else '不符合'}")

    print("\n平衡性验证:")
    for i, factor in enumerate(factors.keys()):
        column = [row[i] for row in oa]
        print(f"  因素 {factor}:")
        for level in range(factors[factor]):
            count = column.count(level)
            print(f"    水平 {level+1}: 出现 {count} 次")