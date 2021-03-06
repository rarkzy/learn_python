OOP
# 1.面向对象概述（object oriented）
  - oop思想
  
         - 接触到一个事物先分析其构成
  - 几个名词

         - OO ：面向对象  
         - OOA ：面向对象分析
         - OOD ：面向对象设计
         - OOI ：面向对象实现
         - OOP : 面向对象编程
  - 类和对象的概念
  
         - 类：抽象名词，代表一个集合，共性的事物。
         - 对象：某个具体事物，单个的个体。
         - 类和对象的关系：一个抽象，代表某一类事物；一类具象，代表一类事物的某一个体
         - 类 应该包含的两个内容：一个表事物的特征，即属性（变量）；一个表功能或动作，即成员方法（函数）
# 2.类的基本实现
  - 类的创建和命名 
         
         - 遵守变量命名规范
         - 使用大驼峰（YouAreFree)
         - 避开系统命名
    
  - 如何声明一个类
         
         - 用Class关键字
         - 类由属性和方法构成
         - 成员属性直接用变量赋值，无值的情况用None。
  - 实例化一个对象
       
         - 变量：累名
  - 访问对象成员
         
         - 使用点操作符
              object.成员属性名称
              obj.成员方法名称
  - 可通过默认内置变量检查内置类和对象所有成员
         
         -对象的所有成员检查
              obj.__dict__
         -类的所有成员检查
              Class_name.__dict__
# 3.anaconda基本使用
  - 它是一个虚拟环境管理器
  - 还是一个安装包管理器
  - conda list :显示anaconda已安装的包
  - conda env list :显示anaconda的虚拟环境列表
  - conda create -n name.python=3.6:创建一个版本为3.6的虚拟环境
# 4.类和对象成员的分析
  - 类和对象都可以存储成员，成员可以归类所有，也可归对象所有
  - 类存储成员时用的是与类相关联的一个对象
  - 独享存储成员是存储在当前对象中的
  - 当对象访问一个成员时，若对象中没有该成员，尝试访问类中的同名成员；若对象中有此成员则访问该成员
  - 创建对象时，类中的成员不会放入对象，而是得到一个空对象
  - 通过对象对类中成员重新赋值，或通过对象添加成员时，对应成员会保存在对象中，不会修改类成员
 # 5.self
   - self在对象的方法中表示对象本身，如果通过对象调用这个方法，那么该对象会自动传入到当前第一个参数中
   - self仅仅是一个形参，可用任何一个普通变量名替换
   - 方法中有self形参的方法称为非绑定类方法，可通过对象访问；没有self则为绑定类方法，调用时只能使用类名来调用
 # 6.面向对象三大特性
   - 封装
   - 继承
   - 多态       
 ## 6.1 封装
     
     - 封装就是对对象的成员进行访问限制
     - 封装的三个级别
       - 公开（public）
       - 受保护的（protected）
       - 私有的（private）
     - 私有是最高级别的封装，只能在当前类或对象中访问
       - 如 name = "ZY"为一个公开属性
            __age =18   为一个私有属性
 ## 6.2 继承
    - 继承就是一个类可以获得使用另一个类中成员的属性和成员方法
    - 作用：减少代码的重复使用，同事可以设置类和类的直接关系
    - 概念：
       - 被继承的叫父类，也叫基类，也叫超类
       - 用于继承的叫子类，也叫派生类
       - 他们存在一个 is - a 的关系
    - 继承的特征
      - 所有的类都继承自object类，即所有的类都是obj的子类
      - 子类一旦继承父类，则可以使用父类中除私有成员外的所有内容（如受保护的，子类仍然可以使用）
      - 子类继承父类后并没有将父类完全赋值子类中，而是通过引用关系访问调用
      - 子类可以定义独有的成员属性和方法
      - 子类中定义的成员和父类成员相同，优先使用子类
      - 子类如果想扩充父类方法，可以定义新方法的同时访问父类成员进行代码重用
         （可用 父类名.父类成员 的格式调用父类成员，也可以使用 super().父类成员格式进行调用）
  
  
    - 继承变量的查找顺序问题
      
      - 优先查找自己的变量
      - 没有则查找父类
      - 构造函数如果本类中没有定义，则自动查找调用父类的构造函数
      - 如果本类中有定义，则不再向上查找
    
    - 单继承与多继承
    
     - 单继承：每个类只能继承一个类
     - 多继承：可以允许继承多个类
    
    - 单继承与多继承优缺点
     - 单继承
      - 优点：传承有序逻辑清晰语法简单隐患少
      - 缺点：功能不能扩展，只能在当前唯一的继承链中扩展
     - 多继承
      - 优点：类的扩展方便
      - 缺点：继承关系混乱，不易排查错误
 ## 6.3 多态
 
  
   - 多态就是同一个对象在不同的情况下出现不同的状态
   - 多态不是语法，是一种设计思想
   - 多态性：指使用一种调用方式，出现不同执行效果
   -  MIXIN设计模式（不改变种族，只增加功能）
       -  使用多继承语法来实现MIXIN
       - 优点：
         - 使用MIXIN可以在不对类进行任何修改的情况下扩展功能
         - 可以方便组织和维护不同功能组件
         - 可以根据需要任意调整功能类组件
         - 可以避免创建很多新的类，导致类的基础混乱
  
# 7. 类相关函数 
   - issubclass(B,A): 用于检测B是否是A的子类
   - isinstance(a,A)：用于检测a是否是A的实例
   - hasattr(a,"name"):用于检测一个对象是否有成员XX
   - getattr
   - setattr
   - delattr
   - dir :  获取对象成员列表
     
     
# 8.类的成员描述符
 
  - 类的成员描述符是为了在类中对成员属性进行相关操作而创建的一种方式
     -  get ：获得属性操作
     -  set ： 修改或添加属性操作
     -  delete ： 删除属性操作
  - 如果想使用成员描述符，三种方式
     - 使用类实现描述器（适用于多个类中多个属性公用一个描述符）
     - 使用属性修改符（控制当前类中一个属性）
     - 使用property函数（控制当前类多个属性）
         - 语法 property（fget,fset,fdel,doc）
         
# 9. 类的内置属性

 - __dict__:以字典形式显示类的成员组成
 - __doc__: 获取类的文档信息
 - __name__:获取类的名称，若在模块中使用，则获取模块名称
 - __bases__:获取某个类的所有父类，以元祖方式显示

# 10. 类的常用魔法函数

 - 魔术方法指不需要人为调用的方法，通常在特定条件下自动触发
 - 魔术方法的统一特征：方法名称被前后两个下划线包括
         