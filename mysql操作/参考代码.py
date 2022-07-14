# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 19:40:00 2022

@author: HYF
"""

import pandas as pd
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.types import NVARCHAR, Float, Integer

#----------连接---------------
connect = pymysql.connect(host='localhost',   # 本地数据库
                          user='root',
                          password='15926378q',
                          db='yf',
                          charset='utf8') #服务器名,账户,密码，数据库名称
'''connect = pymysql.connect('localhost',"root",'15926378q',"")'''
cur = connect.cursor()
print(cur)



'''创建数据库的操作'''
try:
    create_db = "CREATE DATABASE IF NOT EXISTS yf" 
    cur.execute(create_db)
except Exception as e:
    print("创建数据库失败:", e)
else:
    print("创建数据库成功;")





'''创建数据表的操作'''
try:
    create_table1 = "create table sys (id int, name varchar(30),phone int);"
    cur.execute(create_table1)
except Exception as e:
    print("创建数据表失败:", e)
else:
    print("创建数据表成功;")
    
sql = "CREATE DATABASE IF NOT EXISTS db_name" 

cur.execute("use yf;")
try:
    create_table2 = '''CREATE TABLE `employee` (
  `id` INT NOT NULL AUTO_INCREMENT,  -- 自增
  `topic` INT ,
  `ptid` INT NOT NULL,
  `level` INT NOT NULL,
  `time` TIME,
  `consume` INT NOT NULL,
  `err` INT NOT NULL,
  `points` INT NOT NULL,
  `gid` INT NOT NULL,
  PRIMARY KEY (`id`)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
  '''
    cur.execute(create_table2)
except Exception as e:
    print("创建数据表失败:", e)
else:
    print("创建数据表成功;")


    
'''查询数据表的记录'''
sql = "select * from employee"
try:
    cur.execute(sql)  # 执行sql语句

    results = cur.fetchall()  # 获取查询的所有记录
    print("time", "consume", "err")
    # 遍历结果
    for row in results:
        time = row[4]
        consume = row[5]
        err = row[5]
        print(time, consume, err)
except Exception as e:
    raise e


'''插入数据表的记录'''


# sql插入语句 表名blogs
sql_insert ="""insert into employee(id,topic,ptid,level,time,consume,err,points,gid) values (0,1,1,2,'1999-01-09 11:50:36',2,3,4,5)"""

try:
    cur.execute(sql_insert)
    # 提交
    connect.commit()   #提交事务
    print('开始数据库插入操作')
except Exception as e:
    connect.rollback()    #回退操作
    print('数据库插入操作错误回滚',e)
finally:
    connect.close()



'''更新数据表的记录'''

sql_update = "update awesome.blogs set name = '%s' where user_id = '%s'"
try:
    cur.execute(sql_update % ("update_test_name", "test_user_id"))
    # 提交
    connect.commit()
    print('开始数据库更新操作')
except Exception as e:
    connect.rollback()
    print('数据库更新操作错误回滚')
finally:
    connect.close()


'''删除数据表的记录'''

sql_delete = "delete from awesome.blogs where name = '%s'"

try:
    cur.execute(sql_delete % ("update_test_name"))  # 像sql语句传递参数
    # 提交
    connect.commit()
    print('开始数据库删除操作')
except Exception as e:
    connect.rollback()
    print('数据库删除操作错误回滚')
finally:
    connect.close()



'''Dataframe导入mysql'''

'''方法一'''
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import NVARCHAR, Float, Integer
 
def pd2sql():
    """
    to_sql目前只支持两类mysql引擎一个是sqlalchemy和sqlliet3
    :return:
    """
    # 初始化数据库连接，使用pymysql模块
    # MySQL的用户：root, 密码:147369, 端口：3306,数据库：mydb
    # ?charset=utf8 指定数据库编码
    engine = create_engine('mysql+pymysql://root:15926378q@localhost:3306/yf?charset=utf8')
    '''
    engine = create_engine('dialect+driver://username:password@host:port/database')
    dialect -- 数据库类型
    driver -- 数据库驱动选择
    username -- 数据库用户名
    password -- 用户密码
    host --服务器地址
    port --端口
    database --数据库
    '''
    conn = engine.connect()
    for i in range(1, 10):
        # 指定字段的数据类型
        dtypedict = {
            'index_code': NVARCHAR(length=255),
            'date': NVARCHAR(length=255),
            'open': NVARCHAR(length=255),
            'close': NVARCHAR(length=255),
            'low': NVARCHAR(length=255),
            'high': NVARCHAR(length=255),
            'volume': NVARCHAR(length=255),
            'money': NVARCHAR(length=255),
            'change': NVARCHAR(length=255)
        }
 
        csv_path = r'E:\data\yucezhe\trading-data-push.20190201\2019-02-01 index data.csv'
 
        # 读取本地CSV文件
        df = pd.read_csv(csv_path).head()
 
        # 将DataFrame储存为MySQL中的数据表，不储存index列
        df.to_sql(f'csv_table{i}', engine, if_exists='replace', index=False, dtype=dtypedict)
 
        # 执行原生sql语句
        
        # 设置主键
        conn.execute(f"alter table csv_table{i} add constraint p_key primary key (index_code)")
 
        # 从表设置外键
        if i%2 == 0:
            conn.execute(
                f"alter table csv_table{i-1} add  foreign key (index_code) references csv_table{i}(index_code)")
 
        print(f"Write to MySQL successfully! ---- csv_table{i}")
        
        
    engine.dispose()
 
 
pd2sql()

'''方法二'''
import pymysql
import pandas as pd
def con_sql(db,sql):
# 创建连接
    db = pymysql.connect(host='127.0.0.1', port=3308, user='name', passwd='password', db=db, charset='utf8')
# 创建游标
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
#执行结果转化为dataframe
    df = pd.DataFrame(list(result))
# 关闭连接
    db.close()
#返回dataframe
    return df

db = 'database'
sql = 'select * from table'
result = con_sql(db,sql)
print(result.loc[2,2])#打印（3,3）位置的值）




'''mysql中的表导出成Dataframe'''


a = pd.read_sql_table('mt', 'mysql://root:123456@172.17.0.2:3306/zy) # mt 为所查表的表名，zy为所要查询的表所在的数据库名。
pandas.read_sql_table(table_name, con, schema=None, index_col=None, coerce_float=True, parse_dates=None, columns=None, chunksize=None)








































