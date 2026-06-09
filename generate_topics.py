#!/usr/bin/env python3
"""Generate knowledge/topics.md from extracted topic data."""
import os
from pathlib import Path

# All extracted topics organized by category: (知识, 章节, 来源文件)
# Data compiled from 5 agents reading all 86 md files

JAVA_SE = [
    # 1.初始Java.md
    ("Java语言概述", "Java语言概述", "java/1.SE基础语法课件/1.初始Java.md"),
    ("main方法", "main方法", "java/1.SE基础语法课件/1.初始Java.md"),
    ("注释（单行/多行/文档注释）", "注释", "java/1.SE基础语法课件/1.初始Java.md"),
    ("标识符", "标识符", "java/1.SE基础语法课件/1.初始Java.md"),
    ("关键字", "关键字", "java/1.SE基础语法课件/1.初始Java.md"),
    ("JDK (Java Development Kit)", "运行Java程序", "java/1.SE基础语法课件/1.初始Java.md"),
    ("JRE (Java Runtime Environment)", "运行Java程序", "java/1.SE基础语法课件/1.初始Java.md"),
    ("JVM (Java虚拟机)", "Java语言特性", "java/1.SE基础语法课件/1.初始Java.md"),
    ("字节码 (.class文件)", "Java语言特性", "java/1.SE基础语法课件/1.初始Java.md"),
    ("javac编译器", "运行Java程序", "java/1.SE基础语法课件/1.初始Java.md"),
    ("java命令", "运行Java程序", "java/1.SE基础语法课件/1.初始Java.md"),
    ("Write once, Run anywhere", "Java语言特性", "java/1.SE基础语法课件/1.初始Java.md"),
    ("面向对象 (OOP)", "Java语言特性", "java/1.SE基础语法课件/1.初始Java.md"),
    ("多线程", "Java语言特性", "java/1.SE基础语法课件/1.初始Java.md"),
    ("反射", "Java语言特性", "java/1.SE基础语法课件/1.初始Java.md"),
    ("JIT (即时编译)", "Java语言特性", "java/1.SE基础语法课件/1.初始Java.md"),
    ("跨平台", "Java语言概述", "java/1.SE基础语法课件/1.初始Java.md"),
    ("public/static/void修饰符", "main方法", "java/1.SE基础语法课件/1.初始Java.md"),
    ("String[] args", "main方法", "java/1.SE基础语法课件/1.初始Java.md"),
    ("javadoc", "注释", "java/1.SE基础语法课件/1.初始Java.md"),
    ("大驼峰/小驼峰命名", "标识符", "java/1.SE基础语法课件/1.初始Java.md"),
    # 2.数据类型与变量.md
    ("字面常量", "字面常量", "java/1.SE基础语法课件/2.数据类型与变量.md"),
    ("数据类型（基本/引用）", "数据类型", "java/1.SE基础语法课件/2.数据类型与变量.md"),
    ("byte/short/int/long", "基本数据类型", "java/1.SE基础语法课件/2.数据类型与变量.md"),
    ("float/double", "基本数据类型", "java/1.SE基础语法课件/2.数据类型与变量.md"),
    ("char", "基本数据类型", "java/1.SE基础语法课件/2.数据类型与变量.md"),
    ("boolean", "基本数据类型", "java/1.SE基础语法课件/2.数据类型与变量.md"),
    ("变量", "变量", "java/1.SE基础语法课件/2.数据类型与变量.md"),
    ("null", "字面常量", "java/1.SE基础语法课件/2.数据类型与变量.md"),
    ("包装类型 (Integer等)", "整型变量", "java/1.SE基础语法课件/2.数据类型与变量.md"),
    ("二进制/字节/bit", "数据类型", "java/1.SE基础语法课件/2.数据类型与变量.md"),
    # 3.运算符.md
    ("算术运算符 (+,-,*,/,%)", "算术运算符", "java/1.SE基础语法课件/3. 运算符.md"),
    ("关系运算符 (==,!=,<,>,<=,>=)", "关系运算符", "java/1.SE基础语法课件/3. 运算符.md"),
    ("逻辑运算符 (&&,||,!)", "逻辑运算符", "java/1.SE基础语法课件/3. 运算符.md"),
    ("短路求值", "逻辑运算符", "java/1.SE基础语法课件/3. 运算符.md"),
    ("位运算符 (&,|,~,^)", "位运算符", "java/1.SE基础语法课件/3. 运算符.md"),
    ("移位运算符 (<<,>>,>>>)", "移位运算符", "java/1.SE基础语法课件/3. 运算符.md"),
    ("条件运算符 (?:)", "条件运算符", "java/1.SE基础语法课件/3. 运算符.md"),
    ("自增/自减运算符 (++/--)", "自增/自减运算符", "java/1.SE基础语法课件/3. 运算符.md"),
    ("增量赋值 (+=, -=, *=, %=)", "增量运算符", "java/1.SE基础语法课件/3. 运算符.md"),
    ("运算符优先级", "运算符优先级", "java/1.SE基础语法课件/3. 运算符.md"),
    # 4.程序逻辑控制.md
    ("顺序结构", "顺序结构", "java/1.SE基础语法课件/4.程序逻辑控制.md"),
    ("if/else if/else语句", "if语句", "java/1.SE基础语法课件/4.程序逻辑控制.md"),
    ("switch语句", "switch语句", "java/1.SE基础语法课件/4.程序逻辑控制.md"),
    ("while循环", "while循环", "java/1.SE基础语法课件/4.程序逻辑控制.md"),
    ("for循环", "for循环", "java/1.SE基础语法课件/4.程序逻辑控制.md"),
    ("do-while循环", "do-while循环", "java/1.SE基础语法课件/4.程序逻辑控制.md"),
    ("break/continue", "break/continue", "java/1.SE基础语法课件/4.程序逻辑控制.md"),
    ("Scanner输入", "输入输出", "java/1.SE基础语法课件/4.程序逻辑控制.md"),
    ("System.out.println/print/printf", "输入输出", "java/1.SE基础语法课件/4.程序逻辑控制.md"),
    ("Random类", "综合案例", "java/1.SE基础语法课件/4.程序逻辑控制.md"),
    ("嵌套循环", "循环结构", "java/1.SE基础语法课件/4.程序逻辑控制.md"),
    # 5.方法的使用.md
    ("方法（method）", "方法概念及使用", "java/1.SE基础语法课件/5.方法的使用.md"),
    ("方法定义（修饰符/返回值/参数列表）", "方法定义", "java/1.SE基础语法课件/5.方法的使用.md"),
    ("形参与实参", "方法定义", "java/1.SE基础语法课件/5.方法的使用.md"),
    ("方法重载 (Overload)", "方法重载", "java/1.SE基础语法课件/5.方法的使用.md"),
    ("方法签名", "方法重载", "java/1.SE基础语法课件/5.方法的使用.md"),
    ("递归", "递归", "java/1.SE基础语法课件/5.方法的使用.md"),
    ("栈帧", "方法调用的执行过程", "java/1.SE基础语法课件/5.方法的使用.md"),
    ("栈溢出 (StackOverflowError)", "递归", "java/1.SE基础语法课件/5.方法的使用.md"),
    # 6.数组的定义与使用.md
    ("数组", "数组的基本概念", "java/1.SE基础语法课件/6.数组的定义与使用.md"),
    ("数组创建与初始化（动态/静态）", "数组的创建及初始化", "java/1.SE基础语法课件/6.数组的定义与使用.md"),
    ("new关键字", "数组的创建", "java/1.SE基础语法课件/6.数组的定义与使用.md"),
    ("数组遍历 (for-each)", "数组的使用", "java/1.SE基础语法课件/6.数组的定义与使用.md"),
    ("Arrays工具类", "数组的初阶使用", "java/1.SE基础语法课件/6.数组的定义与使用.md"),
    ("Arrays.toString/sort/binarySearch/copyOf", "数组的初阶使用", "java/1.SE基础语法课件/6.数组的定义与使用.md"),
    ("NullPointerException", "数组的初阶使用", "java/1.SE基础语法课件/6.数组的定义与使用.md"),
    ("JVM内存分布（栈/堆/方法区/程序计数器）", "JVM内存分布", "java/1.SE基础语法课件/6.数组的定义与使用.md"),
    ("二维数组", "二维数组", "java/1.SE基础语法课件/6.数组的定义与使用.md"),
    ("冒泡排序", "数组练习", "java/1.SE基础语法课件/6.数组的定义与使用.md"),
    ("二分查找", "数组练习", "java/1.SE基础语法课件/6.数组的定义与使用.md"),
    # 7.类和对象.md
    ("类 (class)", "类定义和使用", "java/1.SE基础语法课件/7.类和对象.md"),
    ("对象/实例化", "类定义和使用", "java/1.SE基础语法课件/7.类和对象.md"),
    ("成员变量/成员方法", "类的定义格式", "java/1.SE基础语法课件/7.类和对象.md"),
    ("构造方法", "对象的构造及初始化", "java/1.SE基础语法课件/7.类和对象.md"),
    ("this关键字", "this引用", "java/1.SE基础语法课件/7.类和对象.md"),
    ("封装", "封装", "java/1.SE基础语法课件/7.类和对象.md"),
    ("private/public/protected/default", "封装", "java/1.SE基础语法课件/7.类和对象.md"),
    ("getter/setter", "封装", "java/1.SE基础语法课件/7.类和对象.md"),
    ("包 (package) / import", "封装", "java/1.SE基础语法课件/7.类和对象.md"),
    ("static（静态成员/类变量/类方法）", "static成员", "java/1.SE基础语法课件/7.类和对象.md"),
    ("代码块（静态/实例/构造/普通）", "代码块", "java/1.SE基础语法课件/7.类和对象.md"),
    ("内部类（实例/静态/局部/匿名）", "内部类", "java/1.SE基础语法课件/7.类和对象.md"),
    # 8.继承和多态.md
    ("继承 (extends)", "继承", "java/1.SE基础语法课件/8.继承和多态.md"),
    ("父类/基类 与 子类/派生类", "继承概念", "java/1.SE基础语法课件/8.继承和多态.md"),
    ("super关键字", "super关键字", "java/1.SE基础语法课件/8.继承和多态.md"),
    ("方法重写 (Override)", "方法重写", "java/1.SE基础语法课件/8.继承和多态.md"),
    ("@Override注解", "方法重写", "java/1.SE基础语法课件/8.继承和多态.md"),
    ("多态 (polymorphism)", "多态", "java/1.SE基础语法课件/8.继承和多态.md"),
    ("向上转型/向下转型", "多态", "java/1.SE基础语法课件/8.继承和多态.md"),
    ("动态绑定/静态绑定", "多态", "java/1.SE基础语法课件/8.继承和多态.md"),
    ("instanceof运算符", "多态", "java/1.SE基础语法课件/8.继承和多态.md"),
    ("final关键字（类/方法/变量）", "final关键字", "java/1.SE基础语法课件/8.继承和多态.md"),
    ("组合", "组合", "java/1.SE基础语法课件/8.继承和多态.md"),
    ("单继承/多层继承", "继承的语法", "java/1.SE基础语法课件/8.继承和多态.md"),
    # 9.抽象类和接口.md
    ("抽象类 (abstract class)", "抽象类", "java/1.SE基础语法课件/9.抽象类和接口.md"),
    ("抽象方法 (abstract method)", "抽象类", "java/1.SE基础语法课件/9.抽象类和接口.md"),
    ("接口 (interface)", "接口", "java/1.SE基础语法课件/9.抽象类和接口.md"),
    ("implements（接口实现）", "接口", "java/1.SE基础语法课件/9.抽象类和接口.md"),
    ("Comparable接口", "接口", "java/1.SE基础语法课件/9.抽象类和接口.md"),
    ("Comparator接口", "接口", "java/1.SE基础语法课件/9.抽象类和接口.md"),
    ("Cloneable接口", "接口", "java/1.SE基础语法课件/9.抽象类和接口.md"),
    ("浅拷贝/深拷贝", "接口", "java/1.SE基础语法课件/9.抽象类和接口.md"),
    ("Object类", "Object类", "java/1.SE基础语法课件/9.抽象类和接口.md"),
    ("toString/equals/hashCode方法", "Object类", "java/1.SE基础语法课件/9.抽象类和接口.md"),
    ("default方法 (接口)", "接口", "java/1.SE基础语法课件/9.抽象类和接口.md"),
    ("适配器设计模式", "接口", "java/1.SE基础语法课件/9.抽象类和接口.md"),
    # 10.认识String类.md
    ("String类", "String类", "java/1.SE基础语法课件/10.认识String类.md"),
    ("字符串构造", "字符串构造", "java/1.SE基础语法课件/10.认识String类.md"),
    ("equals/compareTo/compareToIgnoreCase", "String对象的比较", "java/1.SE基础语法课件/10.认识String类.md"),
    ("indexOf/lastIndexOf/charAt", "字符串查找", "java/1.SE基础语法课件/10.认识String类.md"),
    ("valueOf/toCharArray/toUpperCase/toLowerCase", "字符串转化", "java/1.SE基础语法课件/10.认识String类.md"),
    ("replace/replaceAll/replaceFirst", "字符串替换", "java/1.SE基础语法课件/10.认识String类.md"),
    ("split（字符串拆分）", "字符串拆分", "java/1.SE基础语法课件/10.认识String类.md"),
    ("substring（字符串截取）", "字符串截取", "java/1.SE基础语法课件/10.认识String类.md"),
    ("字符串常量池 (StringTable)", "字符串常量池", "java/1.SE基础语法课件/10.认识String类.md"),
    ("intern()", "字符串常量池", "java/1.SE基础语法课件/10.认识String类.md"),
    ("StringBuilder/StringBuffer", "StringBuilder和StringBuffer", "java/1.SE基础语法课件/10.认识String类.md"),
    ("字符串不可变", "String类的特性", "java/1.SE基础语法课件/10.认识String类.md"),
    # 11.认识异常.md
    ("异常 (Exception)", "异常的概念与体系结构", "java/1.SE基础语法课件/11.认识异常.md"),
    ("Throwable/Error/Exception", "异常的体系结构", "java/1.SE基础语法课件/11.认识异常.md"),
    ("RuntimeException（运行时异常）", "异常的分类", "java/1.SE基础语法课件/11.认识异常.md"),
    ("编译时异常（受检查异常）", "异常的分类", "java/1.SE基础语法课件/11.认识异常.md"),
    ("try-catch-finally", "异常的处理", "java/1.SE基础语法课件/11.认识异常.md"),
    ("throws/throw", "异常的处理", "java/1.SE基础语法课件/11.认识异常.md"),
    ("自定义异常", "自定义异常类", "java/1.SE基础语法课件/11.认识异常.md"),
    ("try-with-resources", "异常的处理", "java/1.SE基础语法课件/11.认识异常.md"),
    ("防御式编程 (LBYL/EAFP)", "异常的处理", "java/1.SE基础语法课件/11.认识异常.md"),
    ("printStackTrace", "异常的处理", "java/1.SE基础语法课件/11.认识异常.md"),
]

JAVA_COLLECTIONS = [
    # 1.初始集合框架.md
    ("Java集合框架 (Collections Framework)", "什么是集合框架", "java/2.集合及数据结构/1.初始集合框架.md"),
    ("Collection接口", "容器背后对应的数据结构", "java/2.集合及数据结构/1.初始集合框架.md"),
    ("List接口", "容器背后对应的数据结构", "java/2.集合及数据结构/1.初始集合框架.md"),
    ("Set接口", "容器背后对应的数据结构", "java/2.集合及数据结构/1.初始集合框架.md"),
    ("Map接口 (K-V模型)", "容器背后对应的数据结构", "java/2.集合及数据结构/1.初始集合框架.md"),
    ("Queue/Deque接口", "容器背后对应的数据结构", "java/2.集合及数据结构/1.初始集合框架.md"),
    ("CRUD操作", "什么是集合框架", "java/2.集合及数据结构/1.初始集合框架.md"),
    # 2.时间复杂度空间复杂度.md
    ("时间复杂度", "时间复杂度", "java/2.集合及数据结构/2.时间复杂度空间复杂度.md"),
    ("空间复杂度", "空间复杂度", "java/2.集合及数据结构/2.时间复杂度空间复杂度.md"),
    ("大O渐进表示法 (Big O)", "大O的渐进表示法", "java/2.集合及数据结构/2.时间复杂度空间复杂度.md"),
    ("O(1)/O(N)/O(N^2)/O(logN)", "常见时间复杂度", "java/2.集合及数据结构/2.时间复杂度空间复杂度.md"),
    ("最好/平均/最坏情况", "推导大O阶方法", "java/2.集合及数据结构/2.时间复杂度空间复杂度.md"),
    ("斐波那契数列", "算法效率分析", "java/2.集合及数据结构/2.时间复杂度空间复杂度.md"),
    # 3.初识泛型.md
    ("泛型 (Generic)", "什么是泛型", "java/2.集合及数据结构/3.初识泛型.md"),
    ("包装类 (Wrapper Class)", "包装类", "java/2.集合及数据结构/3.初识泛型.md"),
    ("装箱/拆箱（自动装箱/拆箱）", "装箱和拆箱", "java/2.集合及数据结构/3.初识泛型.md"),
    ("类型参数化 (E/K/V/N/T)", "语法", "java/2.集合及数据结构/3.初识泛型.md"),
    ("类型推导 (Type Inference)", "类型推导", "java/2.集合及数据结构/3.初识泛型.md"),
    ("裸类型 (Raw Type)", "裸类型", "java/2.集合及数据结构/3.初识泛型.md"),
    ("擦除机制 (Type Erasure)", "擦除机制", "java/2.集合及数据结构/3.初识泛型.md"),
    # 4.List的介绍.md
    ("List接口", "什么是List", "java/2.集合及数据结构/4.List的介绍.md"),
    ("add/remove/get/set/clear/contains", "常见接口介绍", "java/2.集合及数据结构/4.List的介绍.md"),
    ("indexOf/lastIndexOf/subList", "常见接口介绍", "java/2.集合及数据结构/4.List的介绍.md"),
    ("ArrayList", "List的使用", "java/2.集合及数据结构/4.List的介绍.md"),
    ("LinkedList", "List的使用", "java/2.集合及数据结构/4.List的介绍.md"),
    # 5.ArrayList与顺序表.md
    ("线性表", "线性表", "java/2.集合及数据结构/5. ArrayList与顺序表.md"),
    ("顺序表 (SeqList)", "顺序表", "java/2.集合及数据结构/5. ArrayList与顺序表.md"),
    ("ArrayList源码分析", "ArrayList简介", "java/2.集合及数据结构/5. ArrayList与顺序表.md"),
    ("动态扩容（1.5倍）", "ArrayList的扩容机制", "java/2.集合及数据结构/5. ArrayList与顺序表.md"),
    ("RandomAccess接口", "ArrayList简介", "java/2.集合及数据结构/5. ArrayList与顺序表.md"),
    ("Serializable接口（序列化）", "ArrayList简介", "java/2.集合及数据结构/5. ArrayList与顺序表.md"),
    ("迭代器遍历 (Iterator)", "ArrayList的遍历", "java/2.集合及数据结构/5. ArrayList与顺序表.md"),
    ("洗牌算法 (Shuffle)", "简单的洗牌算法", "java/2.集合及数据结构/5. ArrayList与顺序表.md"),
    # 6.LinkedList与链表.md
    ("链表 (Linked List)", "链表的概念及结构", "java/2.集合及数据结构/6.LinkedList与链表.md"),
    ("单向链表/双向链表", "链表的概念及结构", "java/2.集合及数据结构/6.LinkedList与链表.md"),
    ("带头/不带头链表", "链表的概念及结构", "java/2.集合及数据结构/6.LinkedList与链表.md"),
    ("循环/非循环链表", "链表的概念及结构", "java/2.集合及数据结构/6.LinkedList与链表.md"),
    ("头插法/尾插法", "链表的实现", "java/2.集合及数据结构/6.LinkedList与链表.md"),
    ("LinkedList的使用", "LinkedList的使用", "java/2.集合及数据结构/6.LinkedList与链表.md"),
    ("反转链表", "链表面试题", "java/2.集合及数据结构/6.LinkedList与链表.md"),
    ("快慢指针", "链表面试题", "java/2.集合及数据结构/6.LinkedList与链表.md"),
    ("链表带环判断", "链表面试题", "java/2.集合及数据结构/6.LinkedList与链表.md"),
    ("ArrayList vs LinkedList", "ArrayList和LinkedList的区别", "java/2.集合及数据结构/6.LinkedList与链表.md"),
    # 7.Stack和Queue.md
    ("栈 (Stack) / LIFO", "栈", "java/2.集合及数据结构/7.Stack和Queue.md"),
    ("push/pop/peek", "栈的使用", "java/2.集合及数据结构/7.Stack和Queue.md"),
    ("队列 (Queue) / FIFO", "队列", "java/2.集合及数据结构/7.Stack和Queue.md"),
    ("offer/poll/peek", "队列的使用", "java/2.集合及数据结构/7.Stack和Queue.md"),
    ("循环队列", "循环队列", "java/2.集合及数据结构/7.Stack和Queue.md"),
    ("双端队列 (Deque/ArrayDeque)", "双端队列", "java/2.集合及数据结构/7.Stack和Queue.md"),
    ("括号匹配（栈应用）", "栈的应用场景", "java/2.集合及数据结构/7.Stack和Queue.md"),
    ("逆波兰表达式求值", "栈的应用场景", "java/2.集合及数据结构/7.Stack和Queue.md"),
    ("用队列实现栈/用栈实现队列", "面试题", "java/2.集合及数据结构/7.Stack和Queue.md"),
    # 8.二叉树.md
    ("树 (Tree)", "树型结构", "java/2.集合及数据结构/8.二叉树.md"),
    ("二叉树 (Binary Tree)", "二叉树", "java/2.集合及数据结构/8.二叉树.md"),
    ("满二叉树/完全二叉树", "两种特殊的二叉树", "java/2.集合及数据结构/8.二叉树.md"),
    ("二叉树性质 (n0=n2+1等)", "二叉树的性质", "java/2.集合及数据结构/8.二叉树.md"),
    ("前序遍历 (Preorder/NLR)", "二叉树的遍历", "java/2.集合及数据结构/8.二叉树.md"),
    ("中序遍历 (Inorder/LNR)", "二叉树的遍历", "java/2.集合及数据结构/8.二叉树.md"),
    ("后序遍历 (Postorder/LRN)", "二叉树的遍历", "java/2.集合及数据结构/8.二叉树.md"),
    ("层序遍历 (Level Order)", "层序遍历", "java/2.集合及数据结构/8.二叉树.md"),
    ("递归遍历/非递归遍历", "二叉树的基本操作", "java/2.集合及数据结构/8.二叉树.md"),
    ("二分搜索树 (BST)", "搜索树", "java/2.集合及数据结构/8.二叉树.md"),
    # 9.PriorityQueue.md
    ("优先级队列 (PriorityQueue)", "优先级队列", "java/2.集合及数据结构/9.PriorityQueue.md"),
    ("堆 (Heap) / 大根堆/小根堆", "堆的概念", "java/2.集合及数据结构/9.PriorityQueue.md"),
    ("向下调整 (shiftDown)", "堆向下调整", "java/2.集合及数据结构/9.PriorityQueue.md"),
    ("向上调整 (shiftUp)", "堆的插入", "java/2.集合及数据结构/9.PriorityQueue.md"),
    ("建堆时间复杂度 O(N)", "建堆的时间复杂度", "java/2.集合及数据结构/9.PriorityQueue.md"),
    ("堆排序 (Heap Sort)", "堆的应用", "java/2.集合及数据结构/9.PriorityQueue.md"),
    ("Top-K问题", "Top-K问题", "java/2.集合及数据结构/9.PriorityQueue.md"),
    # 10.java对象的比较.md
    ("Comparable接口 (compareTo)", "基于Comparable接口", "java/2.集合及数据结构/10.java对象的比较.md"),
    ("Comparator接口 (compare)", "基于比较器比较", "java/2.集合及数据结构/10.java对象的比较.md"),
    ("内部比较 vs 外部比较", "三种方式对比", "java/2.集合及数据结构/10.java对象的比较.md"),
    ("equals方法覆写", "覆写基类的equals", "java/2.集合及数据结构/10.java对象的比较.md"),
    # 11.排序.md
    ("排序算法概述", "排序的概念", "java/2.集合及数据结构/11.排序.md"),
    ("稳定性（稳定/不稳定）", "排序的概念", "java/2.集合及数据结构/11.排序.md"),
    ("插入排序（直接插入排序）", "插入排序", "java/2.集合及数据结构/11.排序.md"),
    ("希尔排序 (缩小增量排序)", "希尔排序", "java/2.集合及数据结构/11.排序.md"),
    ("选择排序", "选择排序", "java/2.集合及数据结构/11.排序.md"),
    ("堆排序", "堆排序", "java/2.集合及数据结构/11.排序.md"),
    ("冒泡排序", "冒泡排序", "java/2.集合及数据结构/11.排序.md"),
    ("快速排序 (Quicksort/Hoare)", "快速排序", "java/2.集合及数据结构/11.排序.md"),
    ("归并排序 (Merge Sort)", "归并排序", "java/2.集合及数据结构/11.排序.md"),
    ("计数排序", "其他非基于比较排序", "java/2.集合及数据结构/11.排序.md"),
    ("基数排序/桶排序", "其他非基于比较排序", "java/2.集合及数据结构/11.排序.md"),
    ("三数取中法（快排优化）", "快速排序优化", "java/2.集合及数据结构/11.排序.md"),
    # 12.Map和Set讲解.md
    ("Map接口 (HashMap/TreeMap)", "概念及场景", "java/2.集合及数据结构/12.Map和Set讲解.md"),
    ("Set接口 (HashSet/TreeSet)", "Set的说明", "java/2.集合及数据结构/12.Map和Set讲解.md"),
    ("Map.Entry<K,V>", "关于Map.Entry", "java/2.集合及数据结构/12.Map和Set讲解.md"),
    ("哈希表/散列表", "哈希表", "java/2.集合及数据结构/12.Map和Set讲解.md"),
    ("哈希函数/哈希冲突", "哈希表", "java/2.集合及数据结构/12.Map和Set讲解.md"),
    ("负载因子 (Load Factor)", "冲突-避免", "java/2.集合及数据结构/12.Map和Set讲解.md"),
    ("闭散列/开放定址法（线性探测/二次探测）", "冲突-解决-闭散列", "java/2.集合及数据结构/12.Map和Set讲解.md"),
    ("开散列/链地址法/哈希桶", "冲突-解决-开散列", "java/2.集合及数据结构/12.Map和Set讲解.md"),
    ("红黑树", "和java类集的关系", "java/2.集合及数据结构/12.Map和Set讲解.md"),
    # 13.再谈String.md
    ("字符串常量池深入 (JDK6/7/8变化)", "字符串常量池", "java/2.集合及数据结构/13.再谈String.md"),
    ("intern()方法深入", "再谈String对象创建", "java/2.集合及数据结构/13.再谈String.md"),
    ("HotSpot JVM", "再谈String对象创建", "java/2.集合及数据结构/13.再谈String.md"),
    # 14.反射,枚举,Lambda.md
    ("反射 (Reflection)", "反射的定义", "java/2.集合及数据结构/14.反射,枚举,Lambda的使用.md"),
    ("Class类/Field/Method/Constructor", "反射基本信息", "java/2.集合及数据结构/14.反射,枚举,Lambda的使用.md"),
    ("Class.forName()/.class/getClass()", "获得Class对象的三种方式", "java/2.集合及数据结构/14.反射,枚举,Lambda的使用.md"),
    ("setAccessible(true)", "反射的使用", "java/2.集合及数据结构/14.反射,枚举,Lambda的使用.md"),
    ("枚举 (enum)", "枚举的使用", "java/2.集合及数据结构/14.反射,枚举,Lambda的使用.md"),
    ("values()/ordinal()/valueOf()", "枚举常用方法", "java/2.集合及数据结构/14.反射,枚举,Lambda的使用.md"),
    ("Lambda表达式 (Java 8)", "Lambda表达式", "java/2.集合及数据结构/14.反射,枚举,Lambda的使用.md"),
    ("函数式接口 (@FunctionalInterface)", "函数式接口", "java/2.集合及数据结构/14.反射,枚举,Lambda的使用.md"),
    ("变量捕获", "变量捕获", "java/2.集合及数据结构/14.反射,枚举,Lambda的使用.md"),
    # 15.泛型进阶.md
    ("泛型上界 (bounded type parameters)", "泛型的上界", "java/2.集合及数据结构/15.泛型进阶.md"),
    ("通配符 (?) / 通配符上界/下界", "通配符", "java/2.集合及数据结构/15.泛型进阶.md"),
    ("泛型方法/静态泛型方法", "泛型方法", "java/2.集合及数据结构/15.泛型进阶.md"),
]

JAVA_EE_BASIC = [
    # 1.计算机是如何工作的.md
    ("冯诺依曼体系结构", "计算机是如何工作的", "java/3.JavaEE初阶课件/1. 计算机是如何工作的.md"),
    ("CPU/ALU/寄存器/控制单元", "计算机是如何工作的", "java/3.JavaEE初阶课件/1. 计算机是如何工作的.md"),
    ("内存/外存（RAM/硬盘）", "计算机是如何工作的", "java/3.JavaEE初阶课件/1. 计算机是如何工作的.md"),
    ("逻辑门 (AND/OR/NOT/XOR)", "计算机是如何工作的", "java/3.JavaEE初阶课件/1. 计算机是如何工作的.md"),
    ("加法器/半加器/全加器", "计算机是如何工作的", "java/3.JavaEE初阶课件/1. 计算机是如何工作的.md"),
    ("缓存 (L2/L3 Cache)", "计算机是如何工作的", "java/3.JavaEE初阶课件/1. 计算机是如何工作的.md"),
    ("操作系统/进程管理/内存管理", "计算机是如何工作的", "java/3.JavaEE初阶课件/1. 计算机是如何工作的.md"),
    ("进程 (Process) / PCB", "计算机是如何工作的", "java/3.JavaEE初阶课件/1. 计算机是如何工作的.md"),
    ("上下文切换/时间片/中断", "计算机是如何工作的", "java/3.JavaEE初阶课件/1. 计算机是如何工作的.md"),
    ("并发与并行", "计算机是如何工作的", "java/3.JavaEE初阶课件/1. 计算机是如何工作的.md"),
    ("内核态与用户态/系统调用", "计算机是如何工作的", "java/3.JavaEE初阶课件/1. 计算机是如何工作的.md"),
    # 2.多线程-初阶.md
    ("线程 (Thread)", "多线程-初阶", "java/3.JavaEE初阶课件/2.多线程-初阶.md"),
    ("进程 (Process)", "多线程-初阶", "java/3.JavaEE初阶课件/2.多线程-初阶.md"),
    ("Thread类/Runnable接口/Callable接口", "多线程-初阶", "java/3.JavaEE初阶课件/2.多线程-初阶.md"),
    ("线程创建与启动 (start)", "多线程-初阶", "java/3.JavaEE初阶课件/2.多线程-初阶.md"),
    ("线程状态（6种）", "多线程-初阶", "java/3.JavaEE初阶课件/2.多线程-初阶.md"),
    ("线程安全 (Thread Safety)", "多线程-初阶", "java/3.JavaEE初阶课件/2.多线程-初阶.md"),
    ("synchronized关键字", "多线程-初阶", "java/3.JavaEE初阶课件/2.多线程-初阶.md"),
    ("volatile关键字", "多线程-初阶", "java/3.JavaEE初阶课件/2.多线程-初阶.md"),
    ("JMM (Java内存模型)", "多线程-初阶", "java/3.JavaEE初阶课件/2.多线程-初阶.md"),
    ("wait/notify/notifyAll", "多线程-初阶", "java/3.JavaEE初阶课件/2.多线程-初阶.md"),
    ("join/sleep/yield", "多线程-初阶", "java/3.JavaEE初阶课件/2.多线程-初阶.md"),
    ("死锁 (Deadlock)", "多线程-初阶", "java/3.JavaEE初阶课件/2.多线程-初阶.md"),
    ("守护线程 (Daemon Thread)", "多线程-初阶", "java/3.JavaEE初阶课件/2.多线程-初阶.md"),
    # 3.多线程-进阶.md
    ("线程池 (Thread Pool)", "多线程-进阶", "java/3.JavaEE初阶课件/3. 多线程-进阶.md"),
    ("ThreadPoolExecutor/ExecutorService", "多线程-进阶", "java/3.JavaEE初阶课件/3. 多线程-进阶.md"),
    ("核心线程数/最大线程数/keepAliveTime", "多线程-进阶", "java/3.JavaEE初阶课件/3. 多线程-进阶.md"),
    ("阻塞队列 (BlockingQueue)", "多线程-进阶", "java/3.JavaEE初阶课件/3. 多线程-进阶.md"),
    ("拒绝策略 (4种)", "多线程-进阶", "java/3.JavaEE初阶课件/3. 多线程-进阶.md"),
    ("CAS (Compare And Swap)", "多线程-进阶", "java/3.JavaEE初阶课件/3. 多线程-进阶.md"),
    ("AtomicInteger/AtomicReference", "多线程-进阶", "java/3.JavaEE初阶课件/3. 多线程-进阶.md"),
    ("ABA问题", "多线程-进阶", "java/3.JavaEE初阶课件/3. 多线程-进阶.md"),
    ("ReentrantLock/公平锁/非公平锁", "多线程-进阶", "java/3.JavaEE初阶课件/3. 多线程-进阶.md"),
    ("Semaphore/CountDownLatch/CyclicBarrier", "多线程-进阶", "java/3.JavaEE初阶课件/3. 多线程-进阶.md"),
    ("ConcurrentHashMap", "多线程-进阶", "java/3.JavaEE初阶课件/3. 多线程-进阶.md"),
    ("ThreadLocal", "多线程-进阶", "java/3.JavaEE初阶课件/3. 多线程-进阶.md"),
    ("锁升级（偏向锁/轻量级锁/重量级锁）", "多线程-进阶", "java/3.JavaEE初阶课件/3. 多线程-进阶.md"),
    ("Fork/Join框架/工作窃取算法", "多线程-进阶", "java/3.JavaEE初阶课件/3. 多线程-进阶.md"),
    # 4.文件操作和IO.md
    ("File类", "文件操作和IO", "java/3.JavaEE初阶课件/4. 文件操作和IO.md"),
    ("字节流 (InputStream/OutputStream)", "文件操作和IO", "java/3.JavaEE初阶课件/4. 文件操作和IO.md"),
    ("字符流 (Reader/Writer)", "文件操作和IO", "java/3.JavaEE初阶课件/4. 文件操作和IO.md"),
    ("BufferedInputStream/BufferedReader", "文件操作和IO", "java/3.JavaEE初阶课件/4. 文件操作和IO.md"),
    ("序列化 (Serializable/transient)", "文件操作和IO", "java/3.JavaEE初阶课件/4. 文件操作和IO.md"),
    ("ObjectInputStream/ObjectOutputStream", "文件操作和IO", "java/3.JavaEE初阶课件/4. 文件操作和IO.md"),
    ("NIO (Channel/Buffer/Selector)", "文件操作和IO", "java/3.JavaEE初阶课件/4. 文件操作和IO.md"),
    ("Files/Paths工具类", "文件操作和IO", "java/3.JavaEE初阶课件/4. 文件操作和IO.md"),
    # 5.网络原理-初识.md
    ("IP地址/端口号 (Port)", "网络原理-初识", "java/3.JavaEE初阶课件/5. 网络原理 - 初识.md"),
    ("TCP/UDP协议", "网络原理-初识", "java/3.JavaEE初阶课件/5. 网络原理 - 初识.md"),
    ("OSI七层模型", "网络原理-初识", "java/3.JavaEE初阶课件/5. 网络原理 - 初识.md"),
    ("TCP/IP四层模型", "网络原理-初识", "java/3.JavaEE初阶课件/5. 网络原理 - 初识.md"),
    ("DNS (域名系统)", "网络原理-初识", "java/3.JavaEE初阶课件/5. 网络原理 - 初识.md"),
    ("NAT/子网掩码/网关", "网络原理-初识", "java/3.JavaEE初阶课件/5. 网络原理 - 初识.md"),
    ("MAC地址/ARP协议", "网络原理-初识", "java/3.JavaEE初阶课件/5. 网络原理 - 初识.md"),
    ("封装与分用", "网络原理-初识", "java/3.JavaEE初阶课件/5. 网络原理 - 初识.md"),
    # 6.网络编程套接字.md
    ("Socket (套接字)", "网络编程套接字", "java/3.JavaEE初阶课件/6. 网络编程套接字.md"),
    ("UDP Socket (DatagramSocket/DatagramPacket)", "网络编程套接字", "java/3.JavaEE初阶课件/6. 网络编程套接字.md"),
    ("TCP Socket (ServerSocket/Socket)", "网络编程套接字", "java/3.JavaEE初阶课件/6. 网络编程套接字.md"),
    ("bind/connect/listen/accept", "网络编程套接字", "java/3.JavaEE初阶课件/6. 网络编程套接字.md"),
    ("InetAddress", "网络编程套接字", "java/3.JavaEE初阶课件/6. 网络编程套接字.md"),
    # 7.网络原理-TCP_IP.md
    ("TCP报文格式（序号/确认号/标志位/窗口）", "网络原理-TCP_IP", "java/3.JavaEE初阶课件/7. 网络原理 - TCP_IP.md"),
    ("三次握手/四次挥手", "网络原理-TCP_IP", "java/3.JavaEE初阶课件/7. 网络原理 - TCP_IP.md"),
    ("确认应答 (ACK) / 超时重传", "网络原理-TCP_IP", "java/3.JavaEE初阶课件/7. 网络原理 - TCP_IP.md"),
    ("滑动窗口/流量控制", "网络原理-TCP_IP", "java/3.JavaEE初阶课件/7. 网络原理 - TCP_IP.md"),
    ("拥塞控制（慢启动/拥塞避免/快重传/快恢复）", "网络原理-TCP_IP", "java/3.JavaEE初阶课件/7. 网络原理 - TCP_IP.md"),
    ("IP报文格式/TTL/分片与重组", "网络原理-TCP_IP", "java/3.JavaEE初阶课件/7. 网络原理 - TCP_IP.md"),
    ("ICMP/Ping/Traceroute", "网络原理-TCP_IP", "java/3.JavaEE初阶课件/7. 网络原理 - TCP_IP.md"),
    ("MTU/MSS/RTT", "网络原理-TCP_IP", "java/3.JavaEE初阶课件/7. 网络原理 - TCP_IP.md"),
    # 8.网络原理-HTTP_HTTPS.md
    ("HTTP协议/URL/URI", "网络原理-HTTP_HTTPS", "java/3.JavaEE初阶课件/8. 网络原理 - HTTP_HTTPS.md"),
    ("HTTP请求/响应格式", "网络原理-HTTP_HTTPS", "java/3.JavaEE初阶课件/8. 网络原理 - HTTP_HTTPS.md"),
    ("HTTP状态码 (1xx-5xx)", "网络原理-HTTP_HTTPS", "java/3.JavaEE初阶课件/8. 网络原理 - HTTP_HTTPS.md"),
    ("GET/POST方法", "网络原理-HTTP_HTTPS", "java/3.JavaEE初阶课件/8. 网络原理 - HTTP_HTTPS.md"),
    ("Cookie/Session", "网络原理-HTTP_HTTPS", "java/3.JavaEE初阶课件/8. 网络原理 - HTTP_HTTPS.md"),
    ("HTTPS/SSL/TLS", "网络原理-HTTP_HTTPS", "java/3.JavaEE初阶课件/8. 网络原理 - HTTP_HTTPS.md"),
    ("对称加密/非对称加密/CA证书", "网络原理-HTTP_HTTPS", "java/3.JavaEE初阶课件/8. 网络原理 - HTTP_HTTPS.md"),
    ("HTTP2.0/HTTP3.0", "网络原理-HTTP_HTTPS", "java/3.JavaEE初阶课件/8. 网络原理 - HTTP_HTTPS.md"),
    # 9.JVM.md
    ("JVM运行时数据区（堆/栈/方法区/程序计数器）", "JVM", "java/3.JavaEE初阶课件/9. JVM.md"),
    ("类加载机制/双亲委派模型", "JVM", "java/3.JavaEE初阶课件/9. JVM.md"),
    ("类加载器 (Bootstrap/Extension/Application)", "JVM", "java/3.JavaEE初阶课件/9. JVM.md"),
    ("GC (垃圾回收)", "JVM", "java/3.JavaEE初阶课件/9. JVM.md"),
    ("标记-清除/标记-复制/标记-整理算法", "JVM", "java/3.JavaEE初阶课件/9. JVM.md"),
    ("分代收集（新生代/老年代/Eden/Survivor）", "JVM", "java/3.JavaEE初阶课件/9. JVM.md"),
    ("GC收集器 (Serial/Parallel/CMS/G1/ZGC)", "JVM", "java/3.JavaEE初阶课件/9. JVM.md"),
    ("STW (Stop-The-World)", "JVM", "java/3.JavaEE初阶课件/9. JVM.md"),
    ("引用类型（强/软/弱/虚引用）", "JVM", "java/3.JavaEE初阶课件/9. JVM.md"),
    ("OOM (OutOfMemoryError) / StackOverflowError", "JVM", "java/3.JavaEE初阶课件/9. JVM.md"),
    ("JVM参数调优 (-Xms/-Xmx)", "JVM", "java/3.JavaEE初阶课件/9. JVM.md"),
]

JAVA_EE_ADVANCED = [
    # 1.JavaEE导读.md
    ("JavaEE/JakartaEE", "JavaEE导读", "java/4.JavaEE进阶课件/1. JavaEE 导读.md"),
    ("B/S架构 / C/S架构", "JavaEE导读", "java/4.JavaEE进阶课件/1. JavaEE 导读.md"),
    ("SSM框架 (Spring+SpringMVC+MyBatis)", "JavaEE导读", "java/4.JavaEE进阶课件/1. JavaEE 导读.md"),
    ("三层架构 (Controller/Service/Dao)", "JavaEE导读", "java/4.JavaEE进阶课件/1. JavaEE 导读.md"),
    # 2.HTML+CSS+JS.md
    ("HTML标签 (h1-h6/p/a/img/div/input/form/table)", "HTML+CSS+JS", "java/4.JavaEE进阶课件/2. HTML + CSS + JavaScript.md"),
    ("CSS选择器 (id/class/标签/属性/伪类)", "HTML+CSS+JS", "java/4.JavaEE进阶课件/2. HTML + CSS + JavaScript.md"),
    ("CSS盒模型 (margin/padding/border)", "HTML+CSS+JS", "java/4.JavaEE进阶课件/2. HTML + CSS + JavaScript.md"),
    ("CSS布局 (float/position/flex)", "HTML+CSS+JS", "java/4.JavaEE进阶课件/2. HTML + CSS + JavaScript.md"),
    ("JavaScript/DOM/BOM", "HTML+CSS+JS", "java/4.JavaEE进阶课件/2. HTML + CSS + JavaScript.md"),
    ("Ajax/jQuery", "HTML+CSS+JS", "java/4.JavaEE进阶课件/2. HTML + CSS + JavaScript.md"),
    ("JSON数据格式", "HTML+CSS+JS", "java/4.JavaEE进阶课件/2. HTML + CSS + JavaScript.md"),
    # 3.SpringBoot快速上手.md
    ("SpringBoot", "SpringBoot快速上手", "java/4.JavaEE进阶课件/3. SpringBoot 快速上手.md"),
    ("Maven (POM/坐标/生命周期/依赖管理)", "SpringBoot快速上手", "java/4.JavaEE进阶课件/3. SpringBoot 快速上手.md"),
    ("Spring Initializr", "SpringBoot快速上手", "java/4.JavaEE进阶课件/3. SpringBoot 快速上手.md"),
    ("@SpringBootApplication", "SpringBoot快速上手", "java/4.JavaEE进阶课件/3. SpringBoot 快速上手.md"),
    ("SpringApplication.run()", "SpringBoot快速上手", "java/4.JavaEE进阶课件/3. SpringBoot 快速上手.md"),
    ("application.properties/yml", "SpringBoot快速上手", "java/4.JavaEE进阶课件/3. SpringBoot 快速上手.md"),
    ("内嵌Tomcat", "SpringBoot快速上手", "java/4.JavaEE进阶课件/3. SpringBoot 快速上手.md"),
    ("Lombok (@Data/@Slf4j)", "SpringBoot快速上手", "java/4.JavaEE进阶课件/3. SpringBoot 快速上手.md"),
    ("java -jar运行", "SpringBoot快速上手", "java/4.JavaEE进阶课件/3. SpringBoot 快速上手.md"),
    # 4.Spring Web MVC入门.md
    ("Spring MVC / DispatcherServlet", "Spring Web MVC入门", "java/4.JavaEE进阶课件/4. Spring Web MVC入门.md"),
    ("@Controller/@RestController", "Spring Web MVC入门", "java/4.JavaEE进阶课件/4. Spring Web MVC入门.md"),
    ("@RequestMapping/@GetMapping/@PostMapping", "Spring Web MVC入门", "java/4.JavaEE进阶课件/4. Spring Web MVC入门.md"),
    ("@RequestParam/@RequestBody/@PathVariable", "Spring Web MVC入门", "java/4.JavaEE进阶课件/4. Spring Web MVC入门.md"),
    ("RESTful API设计", "Spring Web MVC入门", "java/4.JavaEE进阶课件/4. Spring Web MVC入门.md"),
    # 5.Spring IoC&DI.md
    ("IoC (控制反转)", "Spring IoC&DI", "java/4.JavaEE进阶课件/5. Spring IoC&DI.md"),
    ("DI (依赖注入)", "Spring IoC&DI", "java/4.JavaEE进阶课件/5. Spring IoC&DI.md"),
    ("Bean/ApplicationContext/BeanFactory", "Spring IoC&DI", "java/4.JavaEE进阶课件/5. Spring IoC&DI.md"),
    ("@Component/@Controller/@Service/@Repository", "Spring IoC&DI", "java/4.JavaEE进阶课件/5. Spring IoC&DI.md"),
    ("@Autowired/@Qualifier/@Resource", "Spring IoC&DI", "java/4.JavaEE进阶课件/5. Spring IoC&DI.md"),
    ("@Scope（单例/原型）", "Spring IoC&DI", "java/4.JavaEE进阶课件/5. Spring IoC&DI.md"),
    ("构造方法注入/Setter注入/字段注入", "Spring IoC&DI", "java/4.JavaEE进阶课件/5. Spring IoC&DI.md"),
    # 6.SpringBoot配置文件.md
    ("配置文件 (properties vs yml)", "SpringBoot配置文件", "java/4.JavaEE进阶课件/6. SpringBoot 配置文件.md"),
    ("@Value/@ConfigurationProperties", "SpringBoot配置文件", "java/4.JavaEE进阶课件/6. SpringBoot 配置文件.md"),
    ("多环境配置 (application-{env}.yml)", "SpringBoot配置文件", "java/4.JavaEE进阶课件/6. SpringBoot 配置文件.md"),
    # 7.Spring Boot日志.md
    ("SLF4J/Logback", "Spring Boot日志", "java/4.JavaEE进阶课件/7. Spring Boot 日志.md"),
    ("日志级别 (FATAL/ERROR/WARN/INFO/DEBUG/TRACE)", "Spring Boot日志", "java/4.JavaEE进阶课件/7. Spring Boot 日志.md"),
    ("日志格式/日志持久化/日志滚动", "Spring Boot日志", "java/4.JavaEE进阶课件/7. Spring Boot 日志.md"),
    # 8.MyBatis入门.md
    ("MyBatis", "MyBatis操作数据库(入门)", "java/4.JavaEE进阶课件/8. MyBatis 操作数据库(入门).md"),
    ("JDBC/DataSource/PreparedStatement", "MyBatis操作数据库(入门)", "java/4.JavaEE进阶课件/8. MyBatis 操作数据库(入门).md"),
    ("@Mapper/@Select/@Insert/@Update/@Delete", "MyBatis操作数据库(入门)", "java/4.JavaEE进阶课件/8. MyBatis 操作数据库(入门).md"),
    ("#{} 与 ${} 参数占位符", "MyBatis操作数据库(入门)", "java/4.JavaEE进阶课件/8. MyBatis 操作数据库(入门).md"),
    ("XML映射文件（<mapper>/<select>/<resultMap>）", "MyBatis操作数据库(入门)", "java/4.JavaEE进阶课件/8. MyBatis 操作数据库(入门).md"),
    ("数据库连接池 (HikariCP/Druid)", "MyBatis操作数据库(入门)", "java/4.JavaEE进阶课件/8. MyBatis 操作数据库(入门).md"),
    ("驼峰命名转换 (mapUnderscoreToCamelCase)", "MyBatis操作数据库(入门)", "java/4.JavaEE进阶课件/8. MyBatis 操作数据库(入门).md"),
    # 9.MyBatis进阶.md
    ("动态SQL (<if>/<trim>/<where>/<set>/<foreach>)", "MyBatis操作数据库(进阶)", "java/4.JavaEE进阶课件/9. MyBatis 操作数据库(进阶).md"),
    ("逻辑删除 vs 物理删除", "MyBatis操作数据库(进阶)", "java/4.JavaEE进阶课件/9. MyBatis 操作数据库(进阶).md"),
    ("分页查询/PageRequest/PageResult", "MyBatis操作数据库(进阶)", "java/4.JavaEE进阶课件/9. MyBatis 操作数据库(进阶).md"),
    # 10.MyBatis-Plus使用.md
    ("MyBatis-Plus (MP)", "MyBatis-Plus使用", "java/4.JavaEE进阶课件/10. MyBatis-Plus使用.md"),
    ("BaseMapper接口", "MyBatis-Plus使用", "java/4.JavaEE进阶课件/10. MyBatis-Plus使用.md"),
    ("条件构造器 (QueryWrapper/UpdateWrapper)", "MyBatis-Plus使用", "java/4.JavaEE进阶课件/10. MyBatis-Plus使用.md"),
    ("LambdaQueryWrapper/LambdaUpdateWrapper", "MyBatis-Plus使用", "java/4.JavaEE进阶课件/10. MyBatis-Plus使用.md"),
    ("eq/ne/gt/ge/lt/le/like/in/orderBy", "MyBatis-Plus使用", "java/4.JavaEE进阶课件/10. MyBatis-Plus使用.md"),
    ("@TableName/@TableField/@TableId", "MyBatis-Plus使用", "java/4.JavaEE进阶课件/10. MyBatis-Plus使用.md"),
    # 11.SpringBoot统一功能处理.md
    ("拦截器 (Interceptor/HandlerInterceptor)", "SpringBoot统一功能处理", "java/4.JavaEE进阶课件/11. SpringBoot 统一功能处理.md"),
    ("WebMvcConfigurer/addInterceptors", "SpringBoot统一功能处理", "java/4.JavaEE进阶课件/11. SpringBoot 统一功能处理.md"),
    ("@ControllerAdvice/统一异常处理", "SpringBoot统一功能处理", "java/4.JavaEE进阶课件/11. SpringBoot 统一功能处理.md"),
    ("统一数据返回格式 (ResponseBodyAdvice)", "SpringBoot统一功能处理", "java/4.JavaEE进阶课件/11. SpringBoot 统一功能处理.md"),
    ("适配器模式", "SpringBoot统一功能处理", "java/4.JavaEE进阶课件/11. SpringBoot 统一功能处理.md"),
    # 12.Spring AOP.md
    ("AOP (面向切面编程)", "Spring AOP", "java/4.JavaEE进阶课件/12. Spring AOP.md"),
    ("@Aspect/@Around/@Before/@After", "Spring AOP", "java/4.JavaEE进阶课件/12. Spring AOP.md"),
    ("切点表达式 (execution/@annotation)", "Spring AOP", "java/4.JavaEE进阶课件/12. Spring AOP.md"),
    ("JDK动态代理 (InvocationHandler/Proxy)", "Spring AOP", "java/4.JavaEE进阶课件/12. Spring AOP.md"),
    ("CGLIB动态代理 (Enhancer/MethodInterceptor)", "Spring AOP", "java/4.JavaEE进阶课件/12. Spring AOP.md"),
    ("代理模式 (Proxy Pattern)", "Spring AOP", "java/4.JavaEE进阶课件/12. Spring AOP.md"),
    # 13.Spring事务.md
    ("Spring事务/@Transactional", "Spring事务", "java/4.JavaEE进阶课件/13. Spring事务和事务传播机制.md"),
    ("事务隔离级别 (READ_UNCOMMITTED/READ_COMMITTED/REPEATABLE_READ/SERIALIZABLE)", "Spring事务", "java/4.JavaEE进阶课件/13. Spring事务和事务传播机制.md"),
    ("事务传播机制 (REQUIRED/SUPPORTS/REQUIRES_NEW/NESTED等)", "Spring事务", "java/4.JavaEE进阶课件/13. Spring事务和事务传播机制.md"),
    ("脏读/不可重复读/幻读", "Spring事务", "java/4.JavaEE进阶课件/13. Spring事务和事务传播机制.md"),
    # 14.博客系统案例.md
    ("JWT (JSON Web Token)", "博客系统", "java/4.JavaEE进阶课件/14. 案例综合练习-博客系统.md"),
    ("密码加密 (MD5/加盐加密/SHA)", "博客系统", "java/4.JavaEE进阶课件/14. 案例综合练习-博客系统.md"),
    ("对称加密(AES/DES) vs 非对称加密(RSA/DSA)", "博客系统", "java/4.JavaEE进阶课件/14. 案例综合练习-博客系统.md"),
    ("统一返回结果/统一异常处理", "博客系统", "java/4.JavaEE进阶课件/14. 案例综合练习-博客系统.md"),
    ("@CrossOrigin跨域", "博客系统", "java/4.JavaEE进阶课件/14. 案例综合练习-博客系统.md"),
    # 15.Linux和部署.md
    ("Linux操作系统 (CentOS/Ubuntu)", "Linux和程序部署", "java/4.JavaEE进阶课件/15. Linux基本使用和程序部署.md"),
    ("常用命令 (ls/pwd/cd/mkdir/rm/cp/mv/touch/cat/tail/grep/ps/netstat)", "Linux和程序部署", "java/4.JavaEE进阶课件/15. Linux基本使用和程序部署.md"),
    ("vim编辑器", "Linux和程序部署", "java/4.JavaEE进阶课件/15. Linux基本使用和程序部署.md"),
    ("SSH/XShell", "Linux和程序部署", "java/4.JavaEE进阶课件/15. Linux基本使用和程序部署.md"),
    ("systemctl服务管理", "Linux和程序部署", "java/4.JavaEE进阶课件/15. Linux基本使用和程序部署.md"),
    ("nohup后台运行", "Linux和程序部署", "java/4.JavaEE进阶课件/15. Linux基本使用和程序部署.md"),
    ("Maven打包部署 (mvn package)", "Linux和程序部署", "java/4.JavaEE进阶课件/15. Linux基本使用和程序部署.md"),
    ("spring.profiles.active多环境", "Linux和程序部署", "java/4.JavaEE进阶课件/15. Linux基本使用和程序部署.md"),
    # 16.Spring原理.md
    ("Bean生命周期（实例化→属性赋值→初始化→销毁）", "Spring原理", "java/4.JavaEE进阶课件/16. Spring原理.md"),
    ("@PostConstruct/@PreDestroy", "Spring原理", "java/4.JavaEE进阶课件/16. Spring原理.md"),
    ("BeanPostProcessor", "Spring原理", "java/4.JavaEE进阶课件/16. Spring原理.md"),
    ("SpringBoot自动配置原理 (@EnableAutoConfiguration)", "Spring原理", "java/4.JavaEE进阶课件/16. Spring原理.md"),
    ("AutoConfigurationImportSelector", "Spring原理", "java/4.JavaEE进阶课件/16. Spring原理.md"),
    ("@Conditional条件装配", "Spring原理", "java/4.JavaEE进阶课件/16. Spring原理.md"),
    ("元注解 (@Target/@Retention/@Documented/@Inherited)", "Spring原理", "java/4.JavaEE进阶课件/16. Spring原理.md"),
]

MYSQL = [
    # MySQL安装 + 数据库基础
    ("MySQL安装（Windows/Linux）", "MySQL安装", "mysql/MySQL课件-2024/0. MySQL的安装 - Linux.md"),
    ("systemctl/yum/apt包管理", "MySQL安装", "mysql/MySQL课件-2024/0. MySQL的安装 - Linux.md"),
    ("MySQL Workbench/Navicat", "数据库基础", "mysql/MySQL课件-2024/1. 数据库基础.md"),
    ("数据库 (Database) / DBMS", "数据库基础", "mysql/MySQL课件-2024/1. 数据库基础.md"),
    ("关系型数据库 vs 非关系型数据库 (NoSQL)", "数据库基础", "mysql/MySQL课件-2024/1. 数据库基础.md"),
    ("SQL分类 (DDL/DML/DCL/DQL)", "数据库基础", "mysql/MySQL课件-2024/1. 数据库基础.md"),
    ("存储引擎 (InnoDB/MyISAM/MEMORY)", "数据库基础", "mysql/MySQL课件-2024/1. 数据库基础.md"),
    ("表/行/列/主键/外键/索引/视图", "数据库基础", "mysql/MySQL课件-2024/1. 数据库基础.md"),
    # 库的操作
    ("CREATE/ALTER/DROP DATABASE", "库的操作", "mysql/MySQL课件-2024/2. 库的操作.md"),
    ("SHOW DATABASES/USE/SELECT DATABASE()", "库的操作", "mysql/MySQL课件-2024/2. 库的操作.md"),
    ("字符集 (utf8mb4/gbk/latin1)", "库的操作", "mysql/MySQL课件-2024/2. 库的操作.md"),
    ("校验规则 (Collation: ci/cs/bin/ai)", "库的操作", "mysql/MySQL课件-2024/2. 库的操作.md"),
    # 数据类型
    ("整型 (TINYINT/SMALLINT/INT/BIGINT)", "数据类型", "mysql/MySQL课件-2024/3. 数据类型.md"),
    ("浮点型 (FLOAT/DOUBLE/DECIMAL)", "数据类型", "mysql/MySQL课件-2024/3. 数据类型.md"),
    ("字符串 (CHAR/VARCHAR/TEXT/BLOB)", "数据类型", "mysql/MySQL课件-2024/3. 数据类型.md"),
    ("日期时间 (DATE/TIME/DATETIME/TIMESTAMP)", "数据类型", "mysql/MySQL课件-2024/3. 数据类型.md"),
    ("ENUM/SET", "数据类型", "mysql/MySQL课件-2024/3. 数据类型.md"),
    ("UNSIGNED/ZEROFILL", "数据类型", "mysql/MySQL课件-2024/3. 数据类型.md"),
    # 表的操作
    ("CREATE TABLE/ALTER TABLE/DROP TABLE", "表的操作", "mysql/MySQL课件-2024/4. 表的操作.md"),
    ("DESC/SHOW TABLES/SHOW CREATE TABLE", "表的操作", "mysql/MySQL课件-2024/4. 表的操作.md"),
    ("AUTO_INCREMENT/COMMENT/ENGINE", "表的操作", "mysql/MySQL课件-2024/4. 表的操作.md"),
    # CRUD
    ("INSERT/REPLACE INTO", "增删改查", "mysql/MySQL课件-2024/5. 增删改查操作.md"),
    ("SELECT/DISTINCT/AS别名", "增删改查", "mysql/MySQL课件-2024/5. 增删改查操作.md"),
    ("WHERE子句 (比较/= /!=/IS NULL/LIKE/AND/OR/NOT)", "增删改查", "mysql/MySQL课件-2024/5. 增删改查操作.md"),
    ("BETWEEN AND/IN/NOT IN", "增删改查", "mysql/MySQL课件-2024/5. 增删改查操作.md"),
    ("ORDER BY (ASC/DESC)", "增删改查", "mysql/MySQL课件-2024/5. 增删改查操作.md"),
    ("LIMIT/OFFSET分页", "增删改查", "mysql/MySQL课件-2024/5. 增删改查操作.md"),
    ("GROUP BY/HAVING", "增删改查", "mysql/MySQL课件-2024/5. 增删改查操作.md"),
    ("UPDATE/DELETE/TRUNCATE", "增删改查", "mysql/MySQL课件-2024/5. 增删改查操作.md"),
    ("聚合函数 (COUNT/SUM/AVG/MAX/MIN)", "增删改查", "mysql/MySQL课件-2024/5. 增删改查操作.md"),
    ("日期函数 (NOW/CURDATE/DATEDIFF/DATE_FORMAT)", "增删改查", "mysql/MySQL课件-2024/5. 增删改查操作.md"),
    ("字符串函数 (CONCAT/SUBSTR/REPLACE/LENGTH/TRIM)", "增删改查", "mysql/MySQL课件-2024/5. 增删改查操作.md"),
    ("数学函数 (ABS/CEIL/FLOOR/ROUND/RAND)", "增删改查", "mysql/MySQL课件-2024/5. 增删改查操作.md"),
    # 约束
    ("NOT NULL/DEFAULT/UNIQUE/PRIMARY KEY", "数据库约束", "mysql/MySQL课件-2024/6. 数据库约束.md"),
    ("FOREIGN KEY/REFERENCES", "数据库约束", "mysql/MySQL课件-2024/6. 数据库约束.md"),
    ("CHECK约束", "数据库约束", "mysql/MySQL课件-2024/6. 数据库约束.md"),
    ("ON DELETE CASCADE/SET NULL", "数据库约束", "mysql/MySQL课件-2024/6. 数据库约束.md"),
    # 数据库设计
    ("范式 (1NF/2NF/3NF/BCNF)", "数据库设计", "mysql/MySQL课件-2024/7. 数据库设计.md"),
    ("E-R图（实体/属性/关系）", "数据库设计", "mysql/MySQL课件-2024/7. 数据库设计.md"),
    ("1:1/1:N/M:N关系", "数据库设计", "mysql/MySQL课件-2024/7. 数据库设计.md"),
    ("函数依赖/部分依赖/传递依赖", "数据库设计", "mysql/MySQL课件-2024/7. 数据库设计.md"),
    # 联合查询
    ("INNER JOIN/LEFT JOIN/RIGHT JOIN", "联合查询", "mysql/MySQL课件-2024/8. 联合查询.md"),
    ("CROSS JOIN/自连接", "联合查询", "mysql/MySQL课件-2024/8. 联合查询.md"),
    ("UNION/UNION ALL", "联合查询", "mysql/MySQL课件-2024/8. 联合查询.md"),
    ("子查询 (单行/多行/多列/关联子查询)", "联合查询", "mysql/MySQL课件-2024/8. 联合查询.md"),
    ("EXISTS/NOT EXISTS", "联合查询", "mysql/MySQL课件-2024/8. 联合查询.md"),
    # 索引
    ("索引类型（主键/唯一/普通/复合/全文）", "索引", "mysql/MySQL课件-2024/9. 索引.md"),
    ("B+Tree/B-Tree/哈希索引", "索引", "mysql/MySQL课件-2024/9. 索引.md"),
    ("聚簇索引 vs 非聚簇索引", "索引", "mysql/MySQL课件-2024/9. 索引.md"),
    ("索引覆盖/回表查询", "索引", "mysql/MySQL课件-2024/9. 索引.md"),
    ("最左匹配原则", "索引", "mysql/MySQL课件-2024/9. 索引.md"),
    ("索引下推 (ICP)", "索引", "mysql/MySQL课件-2024/9. 索引.md"),
    ("EXPLAIN执行计划", "索引", "mysql/MySQL课件-2024/9. 索引.md"),
    # 事务
    ("事务 (Transaction/ACID)", "事务", "mysql/MySQL课件-2024/10. 事务.md"),
    ("START TRANSACTION/COMMIT/ROLLBACK", "事务", "mysql/MySQL课件-2024/10. 事务.md"),
    ("隔离级别（读未提交/读已提交/可重复读/串行化）", "事务", "mysql/MySQL课件-2024/10. 事务.md"),
    ("脏读/不可重复读/幻读", "事务", "mysql/MySQL课件-2024/10. 事务.md"),
    ("MVCC (多版本并发控制)", "事务", "mysql/MySQL课件-2024/10. 事务.md"),
    ("Undo Log/Redo Log", "事务", "mysql/MySQL课件-2024/10. 事务.md"),
    ("锁（行锁/间隙锁/临键锁/乐观锁/悲观锁）", "事务", "mysql/MySQL课件-2024/10. 事务.md"),
    # 视图
    ("视图 (CREATE VIEW/DROP VIEW)", "视图", "mysql/MySQL课件-2024/11. 视图.md"),
    ("WITH CHECK OPTION", "视图", "mysql/MySQL课件-2024/11. 视图.md"),
    # 用户和权限
    ("CREATE USER/GRANT/REVOKE/FLUSH PRIVILEGES", "用户和权限管理", "mysql/MySQL课件-2024/12. 用户和权限管理.md"),
    ("权限级别（全局/数据库/表/列）", "用户和权限管理", "mysql/MySQL课件-2024/12. 用户和权限管理.md"),
    # JDBC
    ("JDBC (DriverManager/DataSource)", "JDBC编程", "mysql/MySQL课件-2024/13. JDBC编程.md"),
    ("Connection/Statement/PreparedStatement/ResultSet", "JDBC编程", "mysql/MySQL课件-2024/13. JDBC编程.md"),
    ("executeQuery/executeUpdate", "JDBC编程", "mysql/MySQL课件-2024/13. JDBC编程.md"),
    ("SQL注入与参数化查询 (?占位符)", "JDBC编程", "mysql/MySQL课件-2024/13. JDBC编程.md"),
    ("mysql-connector-java", "JDBC编程", "mysql/MySQL课件-2024/13. JDBC编程.md"),
    ("连接池 (Connection Pool)", "JDBC编程", "mysql/MySQL课件-2024/13. JDBC编程.md"),
    ("批处理 (addBatch/executeBatch)", "JDBC编程", "mysql/MySQL课件-2024/13. JDBC编程.md"),
]

PYTHON = [
    # 1.认识Python.md
    ("Python语言概述", "认识Python", "python/Python课件/1.认识Python.md"),
    ("冯诺依曼体系结构", "计算机基础概念", "python/Python课件/1.认识Python.md"),
    ("CPU/存储器/输入输出设备", "计算机基础概念", "python/Python课件/1.认识Python.md"),
    ("编程语言分类（机器/汇编/高级/编译型/解释型）", "编程语言", "python/Python课件/1.认识Python.md"),
    ("Python环境搭建/PyCharm/IDE", "搭建Python环境", "python/Python课件/1.认识Python.md"),
    ("print/注释/标识符/关键字/缩进", "Python语法特点", "python/Python课件/1.认识Python.md"),
    # 2.基础语法(1).md
    ("变量/数据类型 (int/float/str/bool)", "变量和数据类型", "python/Python课件/2.基础语法(1).md"),
    ("动态类型/类型推导", "变量", "python/Python课件/2.基础语法(1).md"),
    ("运算符（算术/关系/逻辑/赋值）", "运算符", "python/Python课件/2.基础语法(1).md"),
    ("// 整除/** 幂运算", "算术运算符", "python/Python课件/2.基础语法(1).md"),
    ("and/or/not", "逻辑运算符", "python/Python课件/2.基础语法(1).md"),
    ("input/print/f-string/format/%格式化", "输入输出", "python/Python课件/2.基础语法(1).md"),
    ("type()/类型转换 (int/float/str/bool)", "数据类型", "python/Python课件/2.基础语法(1).md"),
    ("None", "数据类型", "python/Python课件/2.基础语法(1).md"),
    # 3.基础语法(2).md
    ("if/elif/else", "条件语句", "python/Python课件/3.基础语法(2).md"),
    ("while/for循环", "循环语句", "python/Python课件/3.基础语法(2).md"),
    ("range()/可迭代对象", "for循环", "python/Python课件/3.基础语法(2).md"),
    ("break/continue/pass", "循环控制", "python/Python课件/3.基础语法(2).md"),
    ("random模块/time模块", "综合案例", "python/Python课件/3.基础语法(2).md"),
    # 4.基础语法(3).md
    ("函数 (def/参数/返回值)", "函数", "python/Python课件/4.基础语法(3).md"),
    ("局部变量/全局变量/global关键字", "变量作用域", "python/Python课件/4.基础语法(3).md"),
    ("递归/递归结束条件", "函数递归", "python/Python课件/4.基础语法(3).md"),
    ("列表 (list) 与元组 (tuple)", "列表和元组", "python/Python课件/4.基础语法(3).md"),
    ("列表操作 (append/insert/pop/remove/extend)", "列表操作", "python/Python课件/4.基础语法(3).md"),
    ("切片 [:] / 步长", "切片操作", "python/Python课件/4.基础语法(3).md"),
    ("字典 (dict) / 键值对", "字典", "python/Python课件/4.基础语法(3).md"),
    ("文件操作 (open/read/write/close/with)", "文件操作", "python/Python课件/4.基础语法(3).md"),
    ("文件模式 (r/w/a/rb/wb)", "文件操作", "python/Python课件/4.基础语法(3).md"),
    ("字符编码 (UTF-8/ASCII/GBK/Unicode)", "文件操作", "python/Python课件/4.基础语法(3).md"),
    # 5.使用库.md
    ("标准库与第三方库", "使用库", "python/Python课件/5.使用库.md"),
    ("import/from import", "使用import导入模块", "python/Python课件/5.使用库.md"),
    ("pip/pip install/PyPI", "使用pip", "python/Python课件/5.使用库.md"),
    ("datetime/os模块", "标准库示例", "python/Python课件/5.使用库.md"),
    ("第三方库 (qrcode/xlrd/xlwt/pynput/playsound)", "第三方库", "python/Python课件/5.使用库.md"),
    ("pyinstaller打包exe", "打包程序", "python/Python课件/5.使用库.md"),
]

TESTING = [
    # 第1章节 认识测试
    ("软件测试定义", "认识测试", "test/软件测试课件/第1章节 认识测试.md"),
    ("测试工程师/软件测试开发工程师(SDET)", "测试岗位", "test/软件测试课件/第1章节 认识测试.md"),
    ("功能测试/移动端测试/客户端测试", "测试类型", "test/软件测试课件/第1章节 认识测试.md"),
    ("自动化测试/性能测试", "测试技术", "test/软件测试课件/第1章节 认识测试.md"),
    # 第2章节 概念篇
    ("需求/用户需求/软件需求/需求规格说明书", "需求", "test/软件测试课件/第2章节 概念篇.md"),
    ("软件生命周期/软件工程", "软件工程", "test/软件测试课件/第2章节 概念篇.md"),
    ("瀑布模型/螺旋模型/增量模型/迭代模型", "开发模型", "test/软件测试课件/第2章节 概念篇.md"),
    ("敏捷模型/敏捷宣言/Scrum", "敏捷", "test/软件测试课件/第2章节 概念篇.md"),
    ("User Story/Sprint/Product Backlog/每日例会", "Scrum", "test/软件测试课件/第2章节 概念篇.md"),
    ("V模型/W模型（双V模型）", "测试模型", "test/软件测试课件/第2章节 概念篇.md"),
    ("验证和确认 (Verification & Validation)", "测试模型", "test/软件测试课件/第2章节 概念篇.md"),
    # 第3章节 BUG篇
    ("软件测试生命周期", "测试流程", "test/软件测试课件/第3章节 BUG篇.md"),
    ("BUG概念 (error/flaw/mistake/fault)", "BUG", "test/软件测试课件/第3章节 BUG篇.md"),
    ("BUG级别（崩溃/严重/一般/次要）", "BUG", "test/软件测试课件/第3章节 BUG篇.md"),
    ("BUG生命周期 (New/Open/Fixed/Rejected/Closed/Reopen)", "BUG管理", "test/软件测试课件/第3章节 BUG篇.md"),
    ("BUG评审", "BUG管理", "test/软件测试课件/第3章节 BUG篇.md"),
    # 第4章节 用例篇
    ("测试用例 (TestCase) / 测试环境/操作步骤/预期结果", "测试用例", "test/软件测试课件/第4章节 用例篇.md"),
    ("等价类划分（有效/无效等价类）", "黑盒测试方法", "test/软件测试课件/第4章节 用例篇.md"),
    ("边界值分析法", "黑盒测试方法", "test/软件测试课件/第4章节 用例篇.md"),
    ("正交法/正交表 (因素/水平)", "黑盒测试方法", "test/软件测试课件/第4章节 用例篇.md"),
    ("判定表法", "黑盒测试方法", "test/软件测试课件/第4章节 用例篇.md"),
    ("场景法（基本流/备选流）", "黑盒测试方法", "test/软件测试课件/第4章节 用例篇.md"),
    ("错误猜测法/探索式测试", "黑盒测试方法", "test/软件测试课件/第4章节 用例篇.md"),
    ("Postman/接口测试 (GET/POST/请求URL/请求头/请求体)", "接口测试", "test/软件测试课件/第4章节 用例篇.md"),
    ("弱网测试/DNS劫持/超时重连", "专项测试", "test/软件测试课件/第4章节 用例篇.md"),
    ("抓包工具 (Fiddler)", "测试工具", "test/软件测试课件/第4章节 用例篇.md"),
    # 第5章节 测试分类
    ("界面测试(UI测试)/功能测试/性能测试", "按目标分类", "test/软件测试课件/第5章节 测试分类.md"),
    ("可靠性测试 (4个9/5个9)", "按目标分类", "test/软件测试课件/第5章节 测试分类.md"),
    ("SQL注入/XML注入/渗透测试/静态安全测试", "安全性测试", "test/软件测试课件/第5章节 测试分类.md"),
    ("安全测试工具 (OWASP ZAP/HP Fortify/IBM Appscan)", "安全性测试", "test/软件测试课件/第5章节 测试分类.md"),
    ("静态测试 vs 动态测试", "按执行方式分类", "test/软件测试课件/第5章节 测试分类.md"),
    ("白盒测试/黑盒测试/灰盒测试", "按测试方法分类", "test/软件测试课件/第5章节 测试分类.md"),
    ("语句覆盖/判定覆盖/条件覆盖/路径覆盖", "白盒测试", "test/软件测试课件/第5章节 测试分类.md"),
    ("单元测试/集成测试/系统测试/验收测试", "按阶段分类", "test/软件测试课件/第5章节 测试分类.md"),
    ("冒烟测试/回归测试", "测试阶段", "test/软件测试课件/第5章节 测试分类.md"),
    ("Alpha测试/Beta测试", "验收测试", "test/软件测试课件/第5章节 测试分类.md"),
    ("TDD (测试驱动开发)", "单元测试", "test/软件测试课件/第5章节 测试分类.md"),
    ("JUnit/@Test/断言(Assertion)", "单元测试", "test/软件测试课件/第5章节 测试分类.md"),
    ("手工测试 vs 自动化测试", "测试方式", "test/软件测试课件/第5章节 测试分类.md"),
    ("ROI (产出投入比)", "自动化测试", "test/软件测试课件/第5章节 测试分类.md"),
    # 第6章节 自动化测试概念篇
    ("自动化测试/自动化测试金字塔", "自动化测试概念", "test/软件测试课件/第6章节 自动化测试概念篇.md"),
    ("接口自动化/UI自动化/Web自动化/移动端自动化", "自动化分类", "test/软件测试课件/第6章节 自动化测试概念篇.md"),
    ("Selenium/WebDriver", "Selenium", "test/软件测试课件/第6章节 自动化测试概念篇.md"),
    ("WebDriverManager/chromedriver/geckodriver", "驱动管理", "test/软件测试课件/第6章节 自动化测试概念篇.md"),
    ("ChromeOptions/ChromeDriver", "Selenium", "test/软件测试课件/第6章节 自动化测试概念篇.md"),
    ("driver.get()/sendKeys()/click()/quit()", "Selenium操作", "test/软件测试课件/第6章节 自动化测试概念篇.md"),
    # 第7章节 自动化测试常用函数
    ("元素定位 (id/classname/tagname/xpath/cssSelector)", "元素定位", "test/软件测试课件/第7章节 自动化测试常用函数.md"),
    ("XPath路径表达式", "XPath", "test/软件测试课件/第7章节 自动化测试常用函数.md"),
    ("CSS选择器", "CSS Selector", "test/软件测试课件/第7章节 自动化测试常用函数.md"),
    ("操作函数 (click/submit/sendKeys/clear/getText)", "操作函数", "test/软件测试课件/第7章节 自动化测试常用函数.md"),
    ("窗口管理 (getWindowHandle/getWindowHandles/switchTo)", "窗口管理", "test/软件测试课件/第7章节 自动化测试常用函数.md"),
    ("屏幕截图 (TakesScreenshot)", "屏幕截图", "test/软件测试课件/第7章节 自动化测试常用函数.md"),
    ("等待机制（强制等待/隐式等待implicitlyWait/显式等待WebDriverWait）", "等待机制", "test/软件测试课件/第7章节 自动化测试常用函数.md"),
    ("ExpectedConditions (elementToBeClickable/textToBe等)", "显式等待", "test/软件测试课件/第7章节 自动化测试常用函数.md"),
    ("浏览器导航 (navigate().to/back/forward/refresh)", "浏览器导航", "test/软件测试课件/第7章节 自动化测试常用函数.md"),
    ("弹窗处理 (Alert/accept/dismiss/sendKeys)", "弹窗", "test/软件测试课件/第7章节 自动化测试常用函数.md"),
    ("无头模式 (Headless)", "浏览器参数", "test/软件测试课件/第7章节 自动化测试常用函数.md"),
    # 第8章节 自动化测试实战篇
    ("自动化测试脚本开发 (EdgeDriver)", "自动化实战", "test/软件测试课件/第8章节 自动化测试实战篇.md"),
    ("测试报告模板", "测试报告", "test/软件测试课件/第8章节 自动化测试实战篇.md"),
    ("断言 (assert/-ea)", "自动化实战", "test/软件测试课件/第8章节 自动化测试实战篇.md"),
    # 第9章节 性能测试概念篇
    ("性能测试概念", "性能测试", "test/软件测试课件/第9章节 性能测试概念篇.md"),
    ("并发数/吞吐量/响应时间", "性能指标", "test/软件测试课件/第9章节 性能测试概念篇.md"),
    ("TPS (每秒事务数) / QPS (每秒查询率)", "性能指标", "test/软件测试课件/第9章节 性能测试概念篇.md"),
    ("资源利用率 (CPU/内存/磁盘/网络)", "性能指标", "test/软件测试课件/第9章节 性能测试概念篇.md"),
    ("饱和点（拐点）/ 二八定律", "性能指标", "test/软件测试课件/第9章节 性能测试概念篇.md"),
    ("基准测试/并发测试/负载测试/压力测试/稳定性测试", "性能测试分类", "test/软件测试课件/第9章节 性能测试概念篇.md"),
    # 第10章节 性能测试工具篇
    ("JMeter (测试计划/线程组/取样器/监听器)", "JMeter", "test/软件测试课件/第10章节 性能测试工具篇.md"),
    ("线程数/Ramp-up时间/循环次数/调度器", "JMeter线程组", "test/软件测试课件/第10章节 性能测试工具篇.md"),
    ("HTTP取样器/查看结果树", "JMeter元件", "test/软件测试课件/第10章节 性能测试工具篇.md"),
    ("HTTP Cookie管理器/请求默认值", "JMeter配置", "test/软件测试课件/第10章节 性能测试工具篇.md"),
    ("CSV数据文件设置/参数化", "JMeter参数化", "test/软件测试课件/第10章节 性能测试工具篇.md"),
    ("JSON提取器/JSONPath/JSON断言", "JMeter断言", "test/软件测试课件/第10章节 性能测试工具篇.md"),
    ("同步定时器 (集合点)/事务控制器", "JMeter定时器", "test/软件测试课件/第10章节 性能测试工具篇.md"),
    ("聚合报告/Response Times Over Time/TPS图表", "JMeter报告", "test/软件测试课件/第10章节 性能测试工具篇.md"),
    ("无图形化运行 (-n/-t/-l/-e/-o)", "JMeter命令行", "test/软件测试课件/第10章节 性能测试工具篇.md"),
    # 接口自动化测试精品课课件
    ("接口测试概念 (HTTP API/RPC)", "接口测试", "test/软件测试课件/接口自动化测试精品课课件.md"),
    ("接口文档/调用URL/请求方法/参数/响应", "接口组成", "test/软件测试课件/接口自动化测试精品课课件.md"),
    ("HTTP状态码 (200/302/400/401/403/404/500/504)", "HTTP状态码", "test/软件测试课件/接口自动化测试精品课课件.md"),
    ("接口测试用例设计（通过性/参数组合/安全/异常验证）", "接口用例", "test/软件测试课件/接口自动化测试精品课课件.md"),
    ("接口安全测试（绕过验证/参数加密）", "接口安全", "test/软件测试课件/接口自动化测试精品课课件.md"),
    ("接口自动化流程（需求→挑选→设计→搭建→编码→执行→报告）", "接口自动化", "test/软件测试课件/接口自动化测试精品课课件.md"),
    ("requests库 (Response/status_code/json/text/headers)", "requests库", "test/软件测试课件/接口自动化测试精品课课件.md"),
    ("requests请求方法 (GET/POST/PUT/DELETE/PATCH)", "requests库", "test/软件测试课件/接口自动化测试精品课课件.md"),
    ("params/data/json/headers/cookies参数", "requests库", "test/软件测试课件/接口自动化测试精品课课件.md"),
    ("Pytest框架 (@pytest.mark.parametrize/fixture/conftest)", "Pytest", "test/软件测试课件/接口自动化测试精品课课件.md"),
    ("setup/teardown (method/class)", "Pytest前后置", "test/软件测试课件/接口自动化测试精品课课件.md"),
    ("pytest.ini配置", "Pytest配置", "test/软件测试课件/接口自动化测试精品课课件.md"),
    ("Allure Report (allure serve/generate)", "测试报告", "test/软件测试课件/接口自动化测试精品课课件.md"),
    ("YAML/PyYAML (safe_dump/safe_load)", "YAML", "test/软件测试课件/接口自动化测试精品课课件.md"),
    ("JSON Schema (validate/type/required/properties)", "JSON Schema", "test/软件测试课件/接口自动化测试精品课课件.md"),
    ("logging日志模块 (basicConfig/FileHandler/Formatter)", "日志", "test/软件测试课件/接口自动化测试精品课课件.md"),
    # 安装Selenium自动化
    ("Selenium环境搭建 (Maven依赖/selenium-java/webdrivermanager)", "Selenium安装", "test/软件测试课件/教程：安装Selenium自动化.md"),
]

PROJECT = [
    # RabbitMQ项目
    ("消息队列 (MQ) / RabbitMQ/Kafka/RocketMQ", "项目背景", "project/Java - 仿 RabbitMQ 的消息队列.md"),
    ("生产者消费者模型/阻塞队列 (BlockingQueue)", "项目背景", "project/Java - 仿 RabbitMQ 的消息队列.md"),
    ("解耦合/削峰填谷", "项目背景", "project/Java - 仿 RabbitMQ 的消息队列.md"),
    ("Producer/Consumer/Broker/Channel", "核心概念", "project/Java - 仿 RabbitMQ 的消息队列.md"),
    ("Exchange/Queue/Binding/Message/routingKey", "核心概念", "project/Java - 仿 RabbitMQ 的消息队列.md"),
    ("ExchangeType (DIRECT/FANOUT/TOPIC)", "核心概念", "project/Java - 仿 RabbitMQ 的消息队列.md"),
    ("durable/autoDelete/exclusive", "核心概念", "project/Java - 仿 RabbitMQ 的消息队列.md"),
    ("basicPublish/basicConsume/basicAck", "核心API", "project/Java - 仿 RabbitMQ 的消息队列.md"),
    ("SQLite/sqlite-jdbc", "技术选型", "project/Java - 仿 RabbitMQ 的消息队列.md"),
    ("ConcurrentHashMap/RandomAccessFile", "数据存储", "project/Java - 仿 RabbitMQ 的消息队列.md"),
    ("自定义二进制应用层协议", "网络通信", "project/Java - 仿 RabbitMQ 的消息队列.md"),
    ("ServerSocket/TCP Socket", "网络通信", "project/Java - 仿 RabbitMQ 的消息队列.md"),
    ("消息持久化/垃圾回收GC", "消息存储", "project/Java - 仿 RabbitMQ 的消息队列.md"),
    ("消息路由匹配 (*和#通配符)", "路由规则", "project/Java - 仿 RabbitMQ 的消息队列.md"),
    ("消费者管理（线程池/扫描线程/令牌队列）", "消费者管理", "project/Java - 仿 RabbitMQ 的消息队列.md"),
    ("@SpringBootTest/单元测试", "测试", "project/Java - 仿 RabbitMQ 的消息队列.md"),
    # 搜索引擎项目
    ("正排索引/倒排索引", "索引模块", "project/基于正倒排索引的 Java 文档搜索引擎.md"),
    ("分词 (分词库ansj)", "搜索流程", "project/基于正倒排索引的 Java 文档搜索引擎.md"),
    ("词频/权重计算", "相关性", "project/基于正倒排索引的 Java 文档搜索引擎.md"),
    ("Spring MVC/HTML解析/JSON序列化", "技术选型", "project/基于正倒排索引的 Java 文档搜索引擎.md"),
    ("多线程制作索引（线程池）", "性能优化", "project/基于正倒排索引的 Java 文档搜索引擎.md"),
    # 自定义协议MQ项目
    ("粘包问题", "网络通信", "project/自定义协议的发布订阅式消息队列.md"),
    ("消息可靠性/手动应答/自动应答", "消息可靠性", "project/自定义协议的发布订阅式消息队列.md"),
    ("消息幂等性/消息顺序性", "消息可靠性", "project/自定义协议的发布订阅式消息队列.md"),
    ("死信队列/消息过期(TTL)/消息积压", "专属问题", "project/自定义协议的发布订阅式消息队列.md"),
    ("推模式(Push) vs 拉模式(Pull)", "消息模型", "project/自定义协议的发布订阅式消息队列.md"),
]

ALL_TOPICS = [
    ("java-se", "Java SE 基础语法", JAVA_SE),
    ("java-collections", "Java 集合与数据结构", JAVA_COLLECTIONS),
    ("java-ee-basic", "Java EE 初阶", JAVA_EE_BASIC),
    ("java-ee-advanced", "Java EE 进阶", JAVA_EE_ADVANCED),
    ("mysql", "MySQL 数据库", MYSQL),
    ("python", "Python", PYTHON),
    ("testing", "软件测试", TESTING),
    ("project", "项目实践", PROJECT),
]


def generate_topics_md(output_path):
    """Generate topics.md from extracted data."""
    lines = []
    lines.append("---")
    lines.append("title: 知识点清单")
    lines.append("updated: 2026-05-25")
    lines.append("description: 从课件中提取的所有技术知识点，掌握度默认为 1（待确认）。包含复习跟踪字段（上次复习、复习次数）。")
    lines.append("category_mapping:")
    for key, name, _ in ALL_TOPICS:
        lines.append(f"  {key}: {name}")
    lines.append("---")
    lines.append("")
    lines.append("## 知识点清单")
    lines.append("")
    lines.append("| # | 分类 | 知识点 | 掌握度 | 上次复习 | 复习次数 | 来源文件 | 备注 |")
    lines.append("|---|------|--------|--------|----------|----------|----------|------|")

    idx = 0
    for key, name, topics in ALL_TOPICS:
        # Sort by topic name
        topics_sorted = sorted(set(topics), key=lambda x: x[0].lower())
        for knowledge, section, source in topics_sorted:
            idx += 1
            # Escape pipe characters in markdown table
            knowledge_escaped = knowledge.replace("|", "\\|")
            section_escaped = section.replace("|", "\\|")
            source_escaped = source.replace("|", "\\|")
            lines.append(f"| {idx} | {name} | {knowledge_escaped} | 1 | - | 0 | {source_escaped} | |")

    lines.append("")
    lines.append(f"> 共 {idx} 个知识点，掌握度默认为 1（1=仅了解 → 5=精通）。上次复习和复习次数由复习流程自动更新。")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Generated {output_path} with {idx} topics.")
    return idx


if __name__ == "__main__":
    out = Path("D:/learning-journal/knowledge/topics.md")
    out.parent.mkdir(parents=True, exist_ok=True)
    total = generate_topics_md(out)
    print(f"Done. {total} knowledge points written.")
