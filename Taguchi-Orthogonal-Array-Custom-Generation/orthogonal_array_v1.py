import numpy as np
from itertools import product

def generate_orthogonal_array_v1(factors):
    levels = list(factors.values())
    N = max(level**2 for level in levels)
    
    # 生成所有可能的组合
    all_combinations = list(product(*[range(level) for level in levels]))
    
    # 选择一个正交子集
    orthogonal_subset = []
    for combo in all_combinations:
        if all(any((row[i], row[j]) == (combo[i], combo[j]) for row in orthogonal_subset)
               for i in range(len(levels)) for j in range(i+1, len(levels))):
            continue
        orthogonal_subset.append(combo)
        if len(orthogonal_subset) == np.prod(levels) // max(levels):
            break
    
    # 如果需要更多行来满足 N，重复整个设计
    oa = orthogonal_subset * (N // len(orthogonal_subset) + 1)
    oa = oa[:N]
    
    return np.array(oa)

def check_orthogonality(oa, factors):
    n_factors = len(factors)
    for i in range(n_factors):
        for j in range(i+1, n_factors):
            combinations = set(map(tuple, oa[:, [i, j]]))
            if len(combinations) != factors[chr(65+i)] * factors[chr(65+j)]:
                return False
    return True

def check_balance(oa, factors):
    for i, (factor, levels) in enumerate(factors.items()):
        column = oa[:, i]
        expected_count = len(oa) / levels
        if any(abs(np.sum(column == level) - expected_count) > 1 for level in range(levels)):
            return False
    return True

def calculate_imbalance_rate(column):
    n_levels = max(column) + 1
    ideal_count = len(column) / n_levels
    actual_counts = [np.sum(column == i) for i in range(n_levels)]
    imbalance = sum(abs(count - ideal_count) for count in actual_counts)
    return imbalance / (len(column) * (1 - 1/n_levels))

if __name__ == "__main__":
    factors = {'A': 3, 'B': 2, 'C': 3}
    oa = generate_orthogonal_array_v1(factors)
    print("生成的正交表:")
    print(oa)
    
    is_orthogonal = check_orthogonality(oa, factors)
    is_balanced = check_balance(oa, factors)
    
    print(f"\n正交性: {'符合' if is_orthogonal else '不符合'}")
    print(f"均衡性: {'符合' if is_balanced else '不符合'}")
    
    print("\n不平衡率:")
    for i, factor in enumerate(factors.keys()):
        imbalance_rate = calculate_imbalance_rate(oa[:, i])
        print(f"  因素 {factor}: {imbalance_rate:.4f}")