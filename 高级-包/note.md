高级 - 包
# 1. 模块
 - 一个模块就是包含Python代码的文件，后缀名为“.py”，模块就是python文件。
 - 为什么用模块
   - 程序太大，不利于维护
   - 模块可以增加代码重复利用的方式
   - 当作命名空间使用，避免命名冲突
 - 如何定义模块
   - 模块就是一个普通文件，直接书写
   - 不过根据模块的规范，应当在模块中编写以下内容
     - 函数（单一功能）
     - 类（相似功能的组合，或类似业务模块）
     - 测试代码
 - 如何使用模块
   - 模块直接导入
   - 语法1
     - import module_name
     - module_name.function_name
     - module_name.class_name
   （模块不能用数字开头，如果必要则需要importlib协助）
   - 语法2
     - import module_name as 别名
        （导入同时重命名）
   - 语法3
     - form module_name import func_name
          (导入某一函数或其他)
   - 语法4
     - form module_name import *(全部)
   - 注：1.form 方式导入后 ， 使用不需要加前缀
         2.若在主线进程中的模块有些内容不想在调用后显示，加入下列作为函数入口
   - 下列 
       - if __name__ == "__main__" (可以有效避免模块代码被导入时被执行的问题，应当作为所有程序的入口)
# 2. 模块的搜索路径于储存
 - 什么是搜索路径
   - 加载模块的时候，系统会在哪些地方寻找此模块。
 - 系统默认的模块搜索路径
   - 使用 import sys
          sys.path 来获取路径列表（案例p04)
 - 添加搜索路径
   - sys.path.append(dir)
 - 模块的加载顺序
   - 首先搜索内存中已加载的模块，其次搜索python的内置模块，最后搜索默认路径
# 3. 包
 - 包是一种组织管理代码的方式，包里面存放的是模块
 - 用于将模块包含在一起的文件夹就是包
 - 自定义包的结构
   - /---包
     /---/---__init__.py(包的标志文件)
             模块1
             模块2
             模块---
 - 包的导入操作
   - 1.import package_name as XX(仅仅能使用__init__中的内容)
   - 2.import package.module  as  XXX（导入包中某一具体模块）使用方式：package.module.func_name
   - 3.form package_name import module1,module2.....（此种方法不执行init中的内容）
   - 4.form package_name import *(当 __init__中为空或者没有__all__时，仅仅导入了init中的内容，若其中有__all__则按照其指定的子包进行导入)
   - 5.form package_name.module_name import *(导入指定模块所有内容)
         -使用 func_name()
               class.func_name()
    