# coding=utf-8
from passwd_dict import Generate_pwd_dict
import sys
from optparse import OptionParser

sys.path.extend(['C:\\Users\\yyf07\\Lib\\site-packages\\exrex.py'])

if __name__ == '__main__':
    banner = """
        version v1.0  author:simmons
                                               _        _ _      _   
     _ __   __ _ ___ _____      _____  _ __ __| |    __| (_) ___| |_ 
    | '_ \ / _` / __/ __\ \ /\ / / _ \| '__/ _` |   / _` | |/ __| __|
    | |_) | (_| \__ \__ \\ V  V / (_) | | | (_| |  | (_| | | (__| |_ 
    | .__/ \__,_|___/___/ \_/\_/ \___/|_|  \__,_|___\__,_|_|\___|\__|
    |_|                                        |_____|                                 
    
        """
    print(banner)

    parser = OptionParser()
    parser.add_option("-u", "--url", dest="url", help="The url for scan")
    parser.add_option("-c", "--count", dest="count", type="int", default=10, help="the count of threads")
    (options, args) = parser.parse_args()
    if options.url is None:
        parser.print_help()
    else:
        print(options.url)
        print(options.count)

pwd_dict = Generate_pwd_dict()
pwd_dict.generate()
# else:
#     print("只能输入一个参数!")
#     sys.exit(-1)
