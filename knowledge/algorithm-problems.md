---
title: 算法题库
updated: 2026-05-29
description: 测试岗位面试常见算法题，按分类组织。每道题包含详细讲解、多种解法和测试场景关联。
difficulty_guide:
  Easy: 基础题，测试面试高频，必须掌握
  Medium: 进阶题，部分公司测试岗会考，选择性掌握
  Hard: 不在测试岗考察范围，题库不收录
---

# 算法题库

> **使用说明**: 星标 ★ 为测试面试高频题，优先练习。

---

## 一、数组与字符串 (8 题)

### P001. 两数之和 ★ [哈希表] [Easy]

**题目**: 给定一个整数数组 `nums` 和一个目标值 `target`，请你在数组中找出和为目标值的两个数的下标。假设每种输入只会对应一个答案，且同一个元素不能使用两次。

**示例**:
```
输入: nums = [2, 7, 11, 15], target = 9
输出: [0, 1]
解释: nums[0] + nums[1] = 2 + 7 = 9
```

**函数签名**: `def two_sum(nums: List[int], target: int) -> List[int]`

**提示**:
1. 暴力法：两层循环遍历所有组合
2. 优化法：用哈希表记录"target - 当前值"是否已出现过

**解法一：暴力枚举**
```python
def two_sum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
```
- 时间复杂度: O(n²)
- 空间复杂度: O(1)

**解法二：哈希表（推荐）**
```python
def two_sum(nums, target):
    seen = {}  # {值: 下标}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```
- 时间复杂度: O(n)
- 空间复杂度: O(n)

**易错点**:
- 不能先建完整哈希表再查，那样同一个元素可能被用两次
- 必须边遍历边查，确保 `seen` 里只存当前元素之前的数

**测试场景关联**: 类似测试中"验证两个配置项的组合是否满足条件"，哈希表快速查找的思路等同于用索引加速数据验证。

---

### P002. 买卖股票的最佳时机 ★ [数组] [Easy]

**题目**: 给定一个数组 `prices`，其第 i 个元素表示一支股票第 i 天的价格。你只能选择某一天买入，并在未来的某一天卖出。求你能获得的最大利润。如果无法获利，返回 0。

**示例**:
```
输入: prices = [7, 1, 5, 3, 6, 4]
输出: 5
解释: 第2天买入(价格=1)，第5天卖出(价格=6)，利润=6-1=5
```

**函数签名**: `def max_profit(prices: List[int]) -> int`

**提示**:
1. 不是求最大值和最小值的差，因为卖出必须在买入之后
2. 遍历时记录"迄今为止的最小价格"，计算"当天卖出能赚多少"

**解法**:
```python
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
    return max_profit
```
- 时间复杂度: O(n)
- 空间复杂度: O(1)

**易错点**:
- 不能简单地找最大值和最小值，因为时间顺序不可逆
- 空数组或单元素数组应返回 0

**测试场景关联**: 与性能测试中"找响应时间的最大波动"思路一致，都是在遍历中维护一个最值。

---

### P003. 移动零 [数组] [双指针] [Easy]

**题目**: 给定一个数组 `nums`，将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。必须原地操作。

**示例**:
```
输入: nums = [0, 1, 0, 3, 12]
输出: [1, 3, 12, 0, 0]
```

**函数签名**: `def move_zeroes(nums: List[int]) -> None`

**提示**:
1. 用一个指针标记"下一个非零元素应该放的位置"
2. 遍历数组，遇到非零元素就交换到前面

**解法**:
```python
def move_zeroes(nums):
    slow = 0  # 指向下一个非零元素应放的位置
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
```
- 时间复杂度: O(n)
- 空间复杂度: O(1)

**易错点**:
- 不要用"遇到0就删除再append"的方式，删除操作是 O(n) 的
- 直接交换即可，不需要额外数组

**测试场景关联**: 双指针思想用于"数据清洗中的元素重排"，如测试报告中把失败用例排到前面。

---

### P004. 最大子数组和 [数组] [Easy]

**题目**: 给定一个整数数组 `nums`，找到一个具有最大和的连续子数组（至少包含一个元素），返回其最大和。

**示例**:
```
输入: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
输出: 6
解释: 连续子数组 [4, -1, 2, 1] 的和最大，为 6
```

**函数签名**: `def max_sub_array(nums: List[int]) -> int`

**提示**:
1. 如果前面的累加和是负数，那它对后面的和没有帮助，抛弃它
2. 每一步比较"继续累加"和"重新开始"哪个更大

**解法**:
```python
def max_sub_array(nums):
    cur_sum = max_sum = nums[0]
    for i in range(1, len(nums)):
        # 如果之前的和是负数，不如从当前元素重新开始
        cur_sum = max(nums[i], cur_sum + nums[i])
        max_sum = max(max_sum, cur_sum)
    return max_sum
```
- 时间复杂度: O(n)
- 空间复杂度: O(1)

**易错点**:
- 全负数数组：算法仍然有效，会返回最大的那个负数
- 初始化 cur_sum 和 max_sum 为 nums[0]，不能用 0

**测试场景关联**: 等同于"找日志中错误最密集的时间段"，滑动累加思想用于异常检测。

---

### P005. 合并两个有序数组 [数组] [双指针] [Easy]

**题目**: 给你两个有序整数数组 `nums1` 和 `nums2`，将 `nums2` 合并到 `nums1` 中，使 `nums1` 成为一个有序数组。`nums1` 有足够的空间（尾部有 m+n 的长度，其中后 n 个位置为 0 占位）。

**示例**:
```
输入: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出: [1,2,2,3,5,6]
```

**函数签名**: `def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None`

**提示**:
1. 从后往前填充，避免覆盖 nums1 中还未处理的数据
2. 三个指针：p1 指向 nums1 有效尾部，p2 指向 nums2 尾部，p 指向填充位置

**解法**:
```python
def merge(nums1, m, nums2, n):
    p1, p2 = m - 1, n - 1
    p = m + n - 1
    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
```
- 时间复杂度: O(m + n)
- 空间复杂度: O(1)

**易错点**:
- 从前往后合并会覆盖 nums1 的数据，必须从后往前
- 循环条件是 `p2 >= 0`（nums2 没放完就继续），不是 p1

**测试场景关联**: 合并两个测试报告的数据，保持时间顺序排列。

---

### P006. 有效的括号 ★ [栈] [Easy]

**题目**: 给定一个只包含 `()`、`{}`、`[]` 的字符串，判断字符串中的括号是否有效。有效条件：左括号必须用相同类型的右括号闭合，且左括号必须以正确的顺序闭合。

**示例**:
```
输入: s = "()[]{}"  → 输出: True
输入: s = "([)]"    → 输出: False
输入: s = "{[]}"    → 输出: True
```

**函数签名**: `def is_valid(s: str) -> bool`

**提示**:
1. 栈：遇到左括号入栈，遇到右括号检查栈顶是否匹配
2. 三种括号的配对关系可以用字典表示

**解法**:
```python
def is_valid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in pairs:  # 右括号
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:  # 左括号
            stack.append(ch)
    return len(stack) == 0  # 栈为空才表示完全匹配
```
- 时间复杂度: O(n)
- 空间复杂度: O(n)

**易错点**:
- 最后要检查栈是否为空（多余的左括号）
- 遇到右括号时栈为空的情况（多余的右括号）

**测试场景关联**: 可用于验证 JSON/XML 格式是否正确，或检查配置文件中标签是否配对。

---

### P007. 反转字符串 [双指针] [Easy]

**题目**: 编写一个函数，将输入的字符串反转过来。要求原地修改（使用 O(1) 额外空间）。

**示例**:
```
输入: s = ["h","e","l","l","o"]
输出: ["o","l","l","e","h"]
```

**函数签名**: `def reverse_string(s: List[str]) -> None`

**解法**:
```python
def reverse_string(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
```
- 时间复杂度: O(n)
- 空间复杂度: O(1)

**易错点**:
- Python 中字符串不可变，所以题目用字符列表 `List[str]`
- 直接用 `s.reverse()` 当然可以，但面试中通常要求手写

**测试场景关联**: 双指针是数组/字符串问题的万能工具，等同于测试中"两端对比验证数据对称性"。

---

### P008. 最长公共前缀 [字符串] [Easy]

**题目**: 编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀，返回空字符串。

**示例**:
```
输入: strs = ["flower","flow","flight"]
输出: "fl"

输入: strs = ["dog","racecar","car"]
输出: ""
```

**函数签名**: `def longest_common_prefix(strs: List[str]) -> str`

**提示**:
1. 纵向扫描：逐列比较所有字符串同一位置的字符
2. 以第一个字符串为基准，与其他字符串逐一比较

**解法**:
```python
def longest_common_prefix(strs):
    if not strs:
        return ""
    # 以第一个字符串为基准
    for i, ch in enumerate(strs[0]):
        for other in strs[1:]:
            # 超出长度或字符不匹配
            if i >= len(other) or other[i] != ch:
                return strs[0][:i]
    return strs[0]
```
- 时间复杂度: O(S)，S 为所有字符总数
- 空间复杂度: O(1)

**易错点**:
- 注意某个字符串比基准短的情况
- 空数组的边界处理

**测试场景关联**: 类似"找一组测试用例名称的共同前缀"以做分组管理。

---

## 二、哈希表 (4 题)

### P009. 存在重复元素 [哈希表] [Easy]

**题目**: 给定一个整数数组，判断是否存在重复元素。如果存在任一值在数组中出现至少两次，返回 true；否则返回 false。

**示例**:
```
输入: [1, 2, 3, 1]  → True
输入: [1, 2, 3, 4]  → False
```

**函数签名**: `def contains_duplicate(nums: List[int]) -> bool`

**解法**:
```python
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```
- 时间复杂度: O(n)
- 空间复杂度: O(n)

**测试场景关联**: 验证测试数据是否重复生成、检查用例ID是否唯一。

---

### P010. 两个数组的交集 [哈希表] [Easy]

**题目**: 给定两个数组，返回它们的交集。结果中的每个元素必须唯一。

**示例**:
```
输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2]
```

**函数签名**: `def intersection(nums1: List[int], nums2: List[int]) -> List[int]`

**解法**:
```python
def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    return list(set1 & set2)
```
- 时间复杂度: O(m + n)
- 空间复杂度: O(m + n)

**手写版本（不用 set 运算符）**:
```python
def intersection(nums1, nums2):
    seen = set(nums1)
    result = []
    for num in nums2:
        if num in seen:
            result.append(num)
            seen.remove(num)  # 保证不重复
    return result
```

**测试场景关联**: 找两个测试计划中共同覆盖的测试点。

---

### P011. 字符串中的第一个唯一字符 [哈希表] [Easy]

**题目**: 给定一个字符串，找到它的第一个不重复的字符，返回它的索引。如果不存在，返回 -1。

**示例**:
```
输入: "leetcode"     → 输出: 0 (l是第一个不重复字符)
输入: "loveleetcode" → 输出: 2 (v是第一个不重复字符)
```

**函数签名**: `def first_uniq_char(s: str) -> int`

**解法**:
```python
def first_uniq_char(s):
    # 第一遍：统计频率
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    # 第二遍：找第一个频率为1的字符
    for i, ch in enumerate(s):
        if count[ch] == 1:
            return i
    return -1
```
- 时间复杂度: O(n)
- 空间复杂度: O(字符集大小)，实际 O(1) 因为只有 26 个字母

**易错点**:
- 不能只遍历一次，因为需要知道"第一个"不重复的
- 两次遍历是必要的：第一次统计，第二次找第一个

**测试场景关联**: 查找日志中首次出现的异常事件。

---

### P012. 字母异位词 [哈希表] [Easy]

**题目**: 给定两个字符串 s 和 t，判断 t 是否是 s 的字母异位词（即字母相同但排列不同）。

**示例**:
```
输入: s = "anagram", t = "nagaram"  → True
输入: s = "rat", t = "car"          → False
```

**函数签名**: `def is_anagram(s: str, t: str) -> bool`

**解法一：排序法**
```python
def is_anagram(s, t):
    return sorted(s) == sorted(t)
```
- O(n log n) 时间, O(n) 空间

**解法二：计数法（推荐）**
```python
def is_anagram(s, t):
    if len(s) != len(t):
        return False
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    for ch in t:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] < 0:
            return False
    return True
```
- 时间复杂度: O(n)
- 空间复杂度: O(1)

**测试场景关联**: 验证两个测试数据集的分布是否一致。

---

## 三、双指针与滑动窗口 (4 题)

### P013. 验证回文串 [双指针] [Easy]

**题目**: 给定一个字符串，验证它是否是回文串。只考虑字母和数字字符，忽略大小写。

**示例**:
```
输入: "A man, a plan, a canal: Panama"  → True
输入: "race a car"                       → False
```

**函数签名**: `def is_palindrome(s: str) -> bool`

**解法**:
```python
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        # 跳过非字母数字字符
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
```
- 时间复杂度: O(n)
- 空间复杂度: O(1)

**易错点**:
- `isalnum()` 用于过滤非字母数字字符
- 忽略大小写用 `.lower()`
- 注意内外两层的 `left < right` 条件，防止越界

**测试场景关联**: 验证对称的配置文件格式（如 XML 标签名是否对称）。

---

### P014. 反转字符串中的元音字母 [双指针] [Easy]

**题目**: 编写一个函数，反转字符串中的元音字母（a/e/i/o/u，大小写都算）。只反转元音，其他字符位置不变。

**示例**:
```
输入: "hello"     → "holle"
输入: "leetcode"  → "leotcede"
```

**函数签名**: `def reverse_vowels(s: str) -> str`

**解法**:
```python
def reverse_vowels(s):
    vowels = set('aeiouAEIOU')
    chars = list(s)
    left, right = 0, len(chars) - 1
    while left < right:
        while left < right and chars[left] not in vowels:
            left += 1
        while left < right and chars[right] not in vowels:
            right -= 1
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return ''.join(chars)
```
- 时间复杂度: O(n)
- 空间复杂度: O(n)（转为list）

**测试场景关联**: 双指针在特定条件下筛选和交换，类似测试中的"排除干扰项后验证核心数据"。

---

### P015. 无重复字符的最长子串 [滑动窗口] [Medium]

**题目**: 给定一个字符串，找出其中不含有重复字符的最长子串的长度。

**示例**:
```
输入: "abcabcbb"  → 3 ("abc")
输入: "bbbbb"     → 1 ("b")
输入: "pwwkew"    → 3 ("wke")
```

**函数签名**: `def length_of_longest_substring(s: str) -> int`

**提示**:
1. 滑动窗口：维护一个"没有重复字符"的窗口
2. 右指针不断右移扩大窗口，遇到重复字符时左指针右移缩小窗口

**解法**:
```python
def length_of_longest_substring(s):
    char_index = {}
    left = 0
    max_len = 0
    for right, ch in enumerate(s):
        # 如果字符在窗口内重复，收缩左边界
        if ch in char_index and char_index[ch] >= left:
            left = char_index[ch] + 1
        char_index[ch] = right
        max_len = max(max_len, right - left + 1)
    return max_len
```
- 时间复杂度: O(n)
- 空间复杂度: O(字符集大小)

**易错点**:
- `char_index[ch] >= left` 是关键条件，确保只在窗口内重复时才移动 left
- 用字典记录字符最近一次出现的位置

**测试场景关联**: 找日志中"不重复的错误类型的最长连续序列"。

---

### P016. 两数之和 II - 输入有序数组 [双指针] [Medium]

**题目**: 给定已升序排列的数组，找出两个数使它们的和等于 target，返回下标（从 1 开始）。

**示例**:
```
输入: numbers = [2, 7, 11, 15], target = 9
输出: [1, 2]
```

**函数签名**: `def two_sum_ii(numbers: List[int], target: int) -> List[int]`

**解法**:
```python
def two_sum_ii(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        cur_sum = numbers[left] + numbers[right]
        if cur_sum == target:
            return [left + 1, right + 1]
        elif cur_sum < target:
            left += 1
        else:
            right -= 1
    return []
```
- 时间复杂度: O(n)
- 空间复杂度: O(1)

**易错点**:
- 利用"有序"这个关键条件，两端夹逼
- 和小于 target 就增大 left（让和变大），大于就减小 right（让和变小）

**测试场景关联**: 理解"利用数据有序性优化查找"，等同于在排序后的测试日志中快速定位。

---

## 四、链表 (4 题)

### P017. 反转链表 ★ [链表] [Easy]

**题目**: 反转一个单链表。分别用迭代和递归实现。

**示例**:
```
输入: 1 → 2 → 3 → 4 → 5 → None
输出: 5 → 4 → 3 → 2 → 1 → None
```

**链表节点定义**:
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

**解法一：迭代（推荐）**
```python
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_temp = curr.next  # 保存下一个节点
        curr.next = prev       # 反转指针
        prev = curr            # prev 前进
        curr = next_temp       # curr 前进
    return prev
```
- 时间复杂度: O(n)
- 空间复杂度: O(1)

**解法二：递归**
```python
def reverse_list(head):
    # 基础情况：空链表或只有一个节点
    if not head or not head.next:
        return head
    # 递归反转后面的链表
    new_head = reverse_list(head.next)
    # 把当前节点接到后面链表的尾部
    head.next.next = head
    head.next = None
    return new_head
```

**易错点**:
- 迭代法中，必须先保存 `next_temp` 再修改 `curr.next`，否则链表会断
- 递归法中，`head.next = None` 不能忘，否则会产生环

**测试场景关联**: 链表反转的"三指针法"等同于测试中"回溯验证调用链"的思维。

---

### P018. 环形链表 ★ [链表] [快慢指针] [Easy]

**题目**: 给定一个链表，判断链表中是否有环。如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。

**函数签名**: `def has_cycle(head: ListNode) -> bool`

**解法（Floyd 判圈算法）**:
```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next        # 慢指针每次走1步
        fast = fast.next.next   # 快指针每次走2步
        if slow == fast:        # 相遇说明有环
            return True
    return False
```
- 时间复杂度: O(n)
- 空间复杂度: O(1)

**易错点**:
- while 条件要检查 `fast` 和 `fast.next` 都不为空
- 快慢指针也叫"龟兔赛跑"，有环时快的一定追上慢的

**测试场景关联**: 检测测试用例之间是否存在循环依赖。

---

### P019. 合并两个有序链表 [链表] [Easy]

**题目**: 将两个升序链表合并为一个新的升序链表并返回。

**示例**:
```
输入: 1→2→4, 1→3→4
输出: 1→1→2→3→4→4
```

**解法**:
```python
def merge_two_lists(l1, l2):
    dummy = ListNode(0)  # 哨兵节点，简化边界处理
    curr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    # 把剩余部分接上
    curr.next = l1 if l1 else l2
    return dummy.next
```
- 时间复杂度: O(m + n)
- 空间复杂度: O(1)

**易错点**:
- 哨兵节点（dummy）技巧可以避免处理空链表的特殊情况
- 最后不要忘记把剩余链表接上

**测试场景关联**: 合并两个有序测试结果列表。

---

### P020. 删除链表中的节点 [链表] [Easy]

**题目**: 给定一个单链表中要删除的节点（非尾节点），请原地删除它。注意：你无法访问链表的头节点。

**示例**:
```
输入: 4→5→1→9, 要删除节点值为5
输出: 4→1→9
```

**解法**:
```python
def delete_node(node):
    # 把下一个节点的值复制过来，再跳过下一个节点
    node.val = node.next.val
    node.next = node.next.next
```
- 时间复杂度: O(1)
- 空间复杂度: O(1)

**测试场景关联**: 考察"换思路解决问题"的能力——不能直接删除自己，就用替身法。

---

## 五、栈与队列 (3 题)

### P021. 用栈实现队列 [栈] [Easy]

**题目**: 请你仅用两个栈实现一个先进先出（FIFO）的队列，实现 push、pop、peek、empty 四个方法。

**解法**:
```python
class MyQueue:
    def __init__(self):
        self.in_stack = []   # 入队栈
        self.out_stack = []  # 出队栈

    def push(self, x):
        self.in_stack.append(x)

    def pop(self):
        self._transfer()
        return self.out_stack.pop()

    def peek(self):
        self._transfer()
        return self.out_stack[-1]

    def empty(self):
        return not self.in_stack and not self.out_stack

    def _transfer(self):
        """当out_stack为空时，把in_stack的全部倒入out_stack"""
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
```
- push: O(1), pop/peek: 均摊 O(1)

**易错点**:
- 只在 `out_stack` 为空时才倒数据，保证 FIFO 顺序不乱
- 不要每次 push 都倒，那样 pop 不是 O(1) 均摊

**测试场景关联**: 模拟任务队列的处理顺序验证（如 CI 中多个测试任务排队执行）。

---

### P022. 最小栈 [栈] [Easy]

**题目**: 设计一个支持 push、pop、top 和常数时间内检索最小元素的栈。

**解法（双栈法）**:
```python
class MinStack:
    def __init__(self):
        self.stack = []      # 主栈
        self.min_stack = []  # 辅助栈，存每一步的最小值

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack:
            self.min_stack.append(x)
        else:
            self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_stack[-1]
```
- 所有操作 O(1)

**易错点**:
- pop 时两个栈都要弹出
- push 时 min_stack 存的是"到目前为止的最小值"，不是当前值

**测试场景关联**: 在测试数据流中实时维护最值（如"当前最低响应时间"）。

---

### P023. 删除字符串中的所有相邻重复项 [栈] [Easy]

**题目**: 给定一个字符串，反复删除相邻的两个相同字符，直到不能再删除。返回最终字符串。

**示例**:
```
输入: "abbaca"  → "ca"
解释: 删除"bb"得"aaca"，再删除"aa"得"ca"
```

**解法**:
```python
def remove_duplicates(s):
    stack = []
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()  # 相邻重复，删除
        else:
            stack.append(ch)
    return ''.join(stack)
```
- 时间复杂度: O(n)
- 空间复杂度: O(n)

**测试场景关联**: 类似"消除测试用例中的重复断言"，栈用于处理递归嵌套的消除。

---

## 六、二叉树 (3 题)

### P024. 二叉树的最大深度 [二叉树] [Easy]

**题目**: 给定一棵二叉树，找出其最大深度（即从根节点到最远叶子节点的最长路径上的节点数）。

**示例**:
```
    3
   / \
  9  20
    /  \
   15   7
→ 最大深度为 3
```

**解法一：递归（推荐）**
```python
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

**解法二：层序遍历（BFS）**
```python
from collections import deque

def max_depth(root):
    if not root:
        return 0
    queue = deque([root])
    depth = 0
    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return depth
```
- 时间复杂度: O(n)，每个节点访问一次

**易错点**:
- 空树的深度是 0，只有一个节点的树深度是 1
- 递归时不要忘了 +1（当前节点这一层）

**测试场景关联**: 递归思想用于处理嵌套结构，如测试多层级的 JSON 响应。

---

### P025. 对称二叉树 [二叉树] [Easy]

**题目**: 给定一个二叉树，检查它是否是镜像对称的。

**示例**:
```
    1
   / \
  2   2
 / \ / \
3  4 4  3
→ True（镜像对称）
```

**解法**:
```python
def is_symmetric(root):
    if not root:
        return True

    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val and
                is_mirror(left.left, right.right) and
                is_mirror(left.right, right.left))

    return is_mirror(root.left, root.right)
```
- 时间复杂度: O(n)
- 空间复杂度: O(h)，h 为树的高度

**易错点**:
- 对称不是比较左右子节点值相同，而是"左的左 == 右的右 且 左的右 == 右的左"
- 两个节点都为空是对称的，只有一个为空是不对称的

**测试场景关联**: 验证两个系统的输出是否成镜像对应关系。

---

### P026. 二叉树的中序遍历 [二叉树] [Easy]

**题目**: 给定二叉树的根节点，返回中序遍历的结果（左 → 根 → 右）。

**解法一：递归**
```python
def inorder_traversal(root):
    result = []
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        result.append(node.val)
        inorder(node.right)
    inorder(root)
    return result
```

**解法二：迭代（栈）**
```python
def inorder_traversal(root):
    result, stack = [], []
    curr = root
    while curr or stack:
        # 一路向左
        while curr:
            stack.append(curr)
            curr = curr.left
        # 弹出并访问
        curr = stack.pop()
        result.append(curr.val)
        # 转向右子树
        curr = curr.right
    return result
```
- 时间复杂度: O(n)
- 空间复杂度: O(h)

**易错点**:
- 递归版：注意遍历顺序是 left → 访问当前 → right
- 迭代版：内层 while 是"一路向左入栈"，不是"一路向左访问"

**测试场景关联**: 二叉搜索树的中序遍历结果是有序的，可用于验证树结构是否正确。

---

## 七、排序与搜索 (4 题)

### P027. 二分查找 ★ [二分搜索] [Easy]

**题目**: 给定一个 n 个元素有序（升序）的整型数组 nums 和一个目标值 target，用二分查找找出 target 的下标。如果不存在则返回 -1。

**示例**:
```
输入: nums = [-1, 0, 3, 5, 9, 12], target = 9  → 4
输入: nums = [-1, 0, 3, 5, 9, 12], target = 2  → -1
```

**解法**:
```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2  # 防止溢出
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```
- 时间复杂度: O(log n)
- 空间复杂度: O(1)

**易错点**:
- `mid = left + (right - left) // 2` 而不是 `(left + right) // 2`，防止整型溢出
- while 条件是 `<=` 还是 `<`？用 `<=` 是因为搜索区间为 [left, right]
- 找不到时 left 和 right 会交错

**测试场景关联**: 二分查找的思想用于"快速缩小问题范围"，等同于测试中的"二分定位法"排查 bug。

---

### P028. 搜索插入位置 [二分搜索] [Easy]

**题目**: 给定一个排序数组和一个目标值，在数组中找到目标值并返回索引。如果不存在，返回按顺序插入的位置。

**示例**:
```
输入: nums = [1,3,5,6], target = 5  → 2
输入: nums = [1,3,5,6], target = 2  → 1
```

**解法**:
```python
def search_insert(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left  # left 就是插入位置
```
- 时间复杂度: O(log n)
- 空间复杂度: O(1)

**易错点**:
- 与标准二分查找的唯一区别：找不到时返回 left 而不是 -1
- 为什么返回 left？因为 while 结束时 left > right，left 刚好是 target 应该插入的位置

**测试场景关联**: 在排序后的测试数据中确定新增用例应该插入的位置。

---

### P029. 第一个错误的版本 [二分搜索] [Easy]

**题目**: 假设你有 n 个版本 [1, 2, ..., n]，每个版本基于前一个版本开发。第一个错误版本导致之后所有版本都错。给定一个 `is_bad_version(version)` API，找出第一个错误的版本。

**解法**:
```python
def first_bad_version(n):
    left, right = 1, n
    while left < right:  # 注意：不是 <=
        mid = left + (right - left) // 2
        if is_bad_version(mid):
            right = mid  # 可能是第一个，不要跳过
        else:
            left = mid + 1
    return left
```
- 时间复杂度: O(log n)
- 空间复杂度: O(1)

**易错点**:
- while 条件是 `left < right`（不是 `<=`），因为 left == right 时就是答案
- `right = mid`（不是 `mid - 1`），因为 mid 可能就是第一个错误版本

**测试场景关联**: 这题的"二分定位"直接对应测试中的 Git Bisect，用于定位引入 bug 的提交。

---

### P030. 冒泡排序 [排序] [Easy]

**题目**: 实现冒泡排序，对整数数组排序。这是理解排序算法的基础。

**解法**:
```python
def bubble_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        swapped = False
        # 每轮把最大的元素"浮"到最后
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break  # 没有交换说明已经有序
    return nums
```
- 时间复杂度: O(n²)，最好 O(n)（已有序时）
- 空间复杂度: O(1)
- 稳定排序

**易错点**:
- 内层循环范围是 `n - 1 - i`，因为每轮后最后 i 个元素已排好
- `swapped` 标志实现提前终止，优化已有序的情况

**测试场景关联**: 理解"为什么测试用例要排序"以及排序算法的稳定性对测试数据的影响。

---

### P031. 选择排序 [排序] [Easy]

**题目**: 实现选择排序。每轮选择未排序部分的最小值，放到已排序部分的末尾。

**解法**:
```python
def selection_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums
```
- 时间复杂度: O(n²)（任何情况下都是）
- 空间复杂度: O(1)
- 不稳定排序

**易错点**:
- 与冒泡排序的区别：选择排序是不稳定的（交换可能破坏相对顺序）
- 每轮只交换一次，而冒泡排序每轮可能交换多次

**测试场景关联**: 理解"不稳定排序可能导致测试数据顺序变化"，这在测试数据准备中很重要。

---

## 八、动态规划入门 (3 题)

### P032. 爬楼梯 ★ [DP] [Easy]

**题目**: 假设你正在爬楼梯，需要 n 阶才能到达楼顶。每次你可以爬 1 或 2 个台阶。有多少种不同的方法可以爬到楼顶？

**示例**:
```
输入: 2  → 2 (1+1 或 2)
输入: 3  → 3 (1+1+1, 1+2, 2+1)
```

**讲解**: 爬到第 n 阶的方法 = 爬到 n-1 阶的方法 + 爬到 n-2 阶的方法。因为最后一步要么跨 1 阶，要么跨 2 阶。这本质上是斐波那契数列。

**解法一：递归+备忘录**
```python
def climb_stairs(n):
    memo = {}
    def helper(k):
        if k <= 2:
            return k
        if k not in memo:
            memo[k] = helper(k - 1) + helper(k - 2)
        return memo[k]
    return helper(n)
```

**解法二：动态规划（推荐）**
```python
def climb_stairs(n):
    if n <= 2:
        return n
    prev2, prev1 = 1, 2  # dp[1]=1, dp[2]=2
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    return prev1
```
- 时间复杂度: O(n)
- 空间复杂度: O(1)

**易错点**:
- f(1)=1, f(2)=2（不是 1），因为一次跨两步也算一种方法
- 用三个变量滚动更新，不需要 O(n) 的 dp 数组

**测试场景关联**: DP 本质是"用已有结果的组合推导新结果"，等同于测试中的"组合测试覆盖度计算"。

---

### P033. 最大子数组和（DP 视角） [DP] [Easy]

**题目**: 同 P004，但从 DP 角度重新理解：`dp[i]` = 以 nums[i] 结尾的最大子数组和。

**DP 推导**:
```
dp[i] = max(nums[i], dp[i-1] + nums[i])
```

**解法**:
```python
def max_sub_array(nums):
    dp = nums[0]
    max_sum = dp
    for i in range(1, len(nums)):
        dp = max(nums[i], dp + nums[i])
        max_sum = max(max_sum, dp)
    return max_sum
```
- 时间复杂度: O(n)
- 空间复杂度: O(1)

**对比 P004 理解**: 同一个问题，贪心视角和 DP 视角等价——核心都是"前面的和如果是正数就保留，负数就丢弃"。

---

### P034. 打家劫舍 [DP] [Easy]

**题目**: 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都有一定的现金。如果两间相邻的房屋在同一晚上被闯入，系统会自动报警。计算不触动警报装置的情况下，一夜之内能偷窃到的最高金额。

**示例**:
```
输入: [1, 2, 3, 1]  → 4 (偷第1间和第3间: 1+3=4)
输入: [2, 7, 9, 3, 1]  → 12 (偷第1/3/5间: 2+9+1=12)
```

**DP 推导**:
```
dp[i] = max(dp[i-1],           # 不偷第i间，继承前一个的最大值
            dp[i-2] + nums[i])  # 偷第i间，加上隔一间的最大值
```

**解法**:
```python
def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    prev2 = nums[0]                      # dp[0]
    prev1 = max(nums[0], nums[1])        # dp[1]
    for i in range(2, len(nums)):
        current = max(prev1, prev2 + nums[i])
        prev2, prev1 = prev1, current
    return prev1
```
- 时间复杂度: O(n)
- 空间复杂度: O(1)

**易错点**:
- dp[0] = nums[0], dp[1] = max(nums[0], nums[1])
- 注意数组长度为 1 的边界情况

**测试场景关联**: 学习"在约束条件下做最优选择"的思维，类似于测试中的"用最少用例覆盖最多场景"。

---

## 附录：题目分类速查表

| 分类 | 题号 | 难度 | 关键技巧 | 测试面试频率 |
|------|------|------|----------|------------|
| 数组 | P001 | Easy | 哈希表 | ★★★ |
| 数组 | P002 | Easy | 遍历+维护最值 | ★★★ |
| 数组 | P003 | Easy | 双指针 | ★★ |
| 数组 | P004 | Easy | 贪心/DP | ★★ |
| 数组 | P005 | Easy | 双指针(从后往前) | ★★ |
| 栈 | P006 | Easy | 栈匹配 | ★★★ |
| 双指针 | P007 | Easy | 两端夹逼 | ★★ |
| 字符串 | P008 | Easy | 纵向扫描 | ★★ |
| 哈希表 | P009 | Easy | Set判重 | ★★★ |
| 哈希表 | P010 | Easy | Set交集 | ★★ |
| 哈希表 | P011 | Easy | 频次统计 | ★★ |
| 哈希表 | P012 | Easy | 字符计数 | ★★ |
| 双指针 | P013 | Easy | 两端夹逼+过滤 | ★★★ |
| 双指针 | P014 | Easy | 双指针+条件交换 | ★ |
| 滑动窗口 | P015 | Medium | 滑动窗口 | ★★ |
| 双指针 | P016 | Medium | 有序+两端夹逼 | ★★ |
| 链表 | P017 | Easy | 三指针迭代 | ★★★ |
| 链表 | P018 | Easy | 快慢指针 | ★★★ |
| 链表 | P019 | Easy | 哨兵节点 | ★★ |
| 链表 | P020 | Easy | 替身法 | ★ |
| 栈 | P021 | Easy | 双栈模拟队列 | ★★ |
| 栈 | P022 | Easy | 辅助栈 | ★★ |
| 栈 | P023 | Easy | 消消乐 | ★ |
| 二叉树 | P024 | Easy | DFS/BFS | ★★ |
| 二叉树 | P025 | Easy | 递归比较 | ★ |
| 二叉树 | P026 | Easy | 中序遍历 | ★★ |
| 二分搜索 | P027 | Easy | 二分查找模板 | ★★★ |
| 二分搜索 | P028 | Easy | 二分变体 | ★★ |
| 二分搜索 | P029 | Easy | 二分边界收缩 | ★ |
| 排序 | P030 | Easy | 冒泡排序 | ★★ |
| 排序 | P031 | Easy | 选择排序 | ★ |
| DP | P032 | Easy | 斐波那契/DP入门 | ★★ |
| DP | P033 | Easy | 贪心等价DP | ★★ |
| DP | P034 | Easy | 选或不选模型 | ★ |

---

## 学习路线建议

```
第 1 阶段：热身（前 1-2 周）
├── 数组题: P001(两数之和), P003(移动零), P005(合并有序数组)
├── 哈希表: P009(重复元素), P012(字母异位词)
├── 双指针: P007(反转字符串), P013(验证回文)
└── 目标：熟悉基础数据结构和 Python 语法

第 2 阶段：数据结构（第 3-4 周）
├── 栈: P006(有效括号), P021(用栈实现队列), P022(最小栈)
├── 链表: P017(反转链表), P018(环形链表), P019(合并有序链表)
└── 目标：掌握栈和链表的核心操作

第 3 阶段：算法思维（第 5-6 周）
├── 二分查找: P027(二分查找), P028(搜索插入位置)
├── 滑动窗口: P015(无重复字符最长子串)
├── 二叉树: P024(最大深度), P026(中序遍历)
└── 目标：建立二分、递归、滑动窗口思维

第 4 阶段：综合提升（第 7-8 周）
├── DP 入门: P032(爬楼梯), P033(最大子数组和), P034(打家劫舍)
├── 复习弱项：根据之前的错题针对性练习
└── 目标：掌握 DP 基本套路，能应对测试面试算法题
```
