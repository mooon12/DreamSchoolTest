def shortestWay(source, target):
    source_set = set(source)
    i = 0  # target中的指针
    num_subsequences = 0

    while i < len(target):
        # 检查当前target字符是否在source中，如果不在，则无法完成匹配
        if target[i] not in source_set:
            return -1
        
        j = 0  # source中的指针
        # 开始新的子序列
        num_subsequences += 1
        while i < len(target) and j < len(source):
            if source[j] == target[i]:
                i += 1  # 移动target指针
            j += 1  # 总是移动source指针
        
    return num_subsequences

# 示例
source = "xyz"
target = "xzyxz"
print(shortestWay(source, target))  # 输出应该为 2
