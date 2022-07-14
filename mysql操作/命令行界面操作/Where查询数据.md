# MySQL WHERE 子句

我们知道从 MySQL 表中使用 SQL SELECT 语句来读取数据。

如需有条件地从表中选取数据，可将 WHERE 子句添加到 SELECT 语句中。

### 语法

以下是 SQL SELECT 语句使用 WHERE 子句从数据表中读取数据的通用语法：

```mysql
SELECT field1, field2,...fieldN FROM table_name1, table_name2...
[WHERE condition1 [AND [OR]] condition2.....
```

- 查询语句中你可以使用一个或者多个表，表之间使用逗号**,** 分割，并使用WHERE语句来设定查询条件。
- 你可以在 WHERE 子句中指定任何条件。
- 你可以使用 AND 或者 OR 指定一个或多个条件。
- WHERE 子句也可以运用于 SQL 的 DELETE 或者 UPDATE 命令。
- WHERE 子句类似于程序语言中的 if 条件，根据 MySQL 表中的字段值来读取指定的数据。

以下为操作符列表，可用于 WHERE 子句中。

下表中实例假定 A 为 10, B 为 20

| 操作符 | 描述                                                         | 实例                 |
| :----- | :----------------------------------------------------------- | :------------------- |
| =      | 等号，检测两个值是否相等，如果相等返回true                   | (A = B) 返回false。  |
| <>, != | 不等于，检测两个值是否相等，如果不相等返回true               | (A != B) 返回 true。 |
| >      | 大于号，检测左边的值是否大于右边的值, 如果左边的值大于右边的值返回true | (A > B) 返回false。  |
| <      | 小于号，检测左边的值是否小于右边的值, 如果左边的值小于右边的值返回true | (A < B) 返回 true。  |
| >=     | 大于等于号，检测左边的值是否大于或等于右边的值, 如果左边的值大于或等于右边的值返回true | (A >= B) 返回false。 |
| <=     | 小于等于号，检测左边的值是否小于或等于右边的值, 如果左边的值小于或等于右边的值返回true | (A <= B) 返回 true。 |

如果我们想在 MySQL 数据表中读取指定的数据，WHERE 子句是非常有用的。

使用主键来作为 WHERE 子句的条件查询是非常快速的。

如果给定的条件在表中没有任何匹配的记录，那么查询不会返回任何数据。

------

## 从命令提示符中读取数据

我们将在SQL SELECT语句使用WHERE子句来读取MySQL数据表 runoob_tbl 中的数据：

实例

以下实例将读取 runoob_tbl 表中 runoob_author 字段值为 Sanjay 的所有记录：

## SQL SELECT WHERE 子句

SELECT * from runoob_tbl WHERE runoob_author='菜鸟教程';

输出结果：

![img](https://www.runoob.com/wp-content/uploads/2014/03/CED9CA9C-E4C7-4809-875C-A7E48F430059.jpg)



MySQL 的 WHERE 子句的字符串比较是不区分大小写的。 你可以使用 BINARY 关键字来设定 WHERE 子句的字符串比较是区分大小写的。

如下实例:

## BINARY 关键字

mysql> SELECT * from runoob_tbl WHERE BINARY runoob_author='runoob.com'; Empty set (0.01 sec)  mysql> SELECT * from runoob_tbl WHERE BINARY runoob_author='RUNOOB.COM'; +-----------+---------------+---------------+-----------------+ | runoob_id | runoob_title  | runoob_author | submission_date | +-----------+---------------+---------------+-----------------+ | 3         | JAVA 教程   | RUNOOB.COM    | 2016-05-06      | | 4         | 学习 Python | RUNOOB.COM    | 2016-03-06      | +-----------+---------------+---------------+-----------------+ 2 rows in set (0.01 sec)

实例中使用了 **BINARY** 关键字，是区分大小写的，所以 **runoob_author='runoob.com'** 的查询条件是没有数据的。

注意：

**where：**数据库中常用的是where关键字，用于在初始表中筛选查询。它是一个约束声明，用于约束数据，在返回结果集之前起作用。

**group by:**对select查询出来的结果集按照某个字段或者表达式进行分组，获得一组组的集合，然后从每组中取出一个指定字段或者表达式的值。

**having：**用于对where和group by查询出来的分组经行过滤，查出满足条件的分组结果。它是一个过滤声明，是在查询返回结果集以后对查询结果进行的过滤操作。

例子1：

update 语句可用来修改表中的数据, 简单来说基本的使用形式为:

update 表名称 set 列名称=新值 where 更新条件;

以下是在表 students 中的实例:

将 id 为 5 的手机号改为默认的 **-** : update students settel=default where id=5;

将所有人的年龄增加 1: update students set age=age+1;

将手机号为 13288097888 的姓名改为 "小明", 年龄改为 19: update students setname="小明", age=19 wheretel="13288097888";

例子2：

**UPDATE替换某个字段中的某个字符**

当我们需要将字段中的特定字符串批量修改为其他字符串时，可已使用以下操作：

```mysql
UPDATE table_name SET field=REPLACE(field, 'old-string', 'new-string') 
[WHERE Clause]
```

**实例：**

以下实例将更新 runoob_id 为 3 的runoob_title 字段值的 "C++" 替换为 "Python"：

```mysql
UPDATE runoob_tbl SET runoob_title = REPLACE(runoob_title, 'C++', 'Python') where 
runoob_id = 3;
```