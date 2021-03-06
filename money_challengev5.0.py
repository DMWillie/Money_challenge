"""
    作者:北辰
    功能:52周存钱挑战
    版本:5.0
    日期:14/06/2018
    2.0新增功能:记录每周存钱数
    3.0新增功能:使用循环直接计数
    4.0新增功能:灵活设置每周的存款数,增加的存款数及存款周数
    5.0新增功能:根据用户输入的日期,判断是一年中的第几周,然后输出相应的存款金额
"""

import math
from datetime import datetime

def save_money_in_n_weeks(money_per_week,increase_money,total_week):
    """
    计算n周内的存钱金额
    """
    saving = 0  # 账户累计
    money_list = []  # 记录每周存款数的列表
    saved_money_list = [] # 记录每周账户累计的列表

   # 存钱操作
    for i in range(total_week):
        money_list.append(money_per_week)
        saving = math.fsum(money_list)  # 计算列表中所有元素的和
        saved_money_list.append(saving)
        # 输出信息
        # print('第{}周,存入{}元,账户累计{}元'.format(i + 1, money_per_week, saving))
        # 更新下一周存钱金额
        money_per_week += increase_money
    return saved_money_list

def main():
    """
    主函数
    """
    money_per_week = float(input('请输入每周存入的金额数: ')) #每周存入的金额
    increase_money = float(input('请输入每周递增的金额: ')) # 递增的金额
    total_week = int(input('请输入存钱的周数: ')) # 存钱的周数

    # 调用函数
    saved_money_list = save_money_in_n_weeks(money_per_week,increase_money,total_week)
    input_date_str = input('请输入日期(yyyy/mm/dd):')
    input_date = datetime.strptime(input_date_str,'%Y/%m/%d')
    # datetime对象的isocalendar()方法会返回一个元组,(年份,第几周,星期几)
    week_num = input_date.isocalendar()[1]
    print('第{}周的存款金额是{}'.format(week_num,saved_money_list[week_num-1]))

if __name__=='__main__':
    main()