# coding=utf-8
"""
配置文件
"""
# 黑名单
black_list = ['com', 'cn', 'net', 'www']
# 密码母本
passwd_m_list = ["admin", "test", "123456", "666666", "123123", "123", "guest", "administrator"]
# 生成密码中间规则
pwd_middle_pattern = r"[@#]"
# 生成密码的最后的规则
pwd_last_pattern = "[@^]"
