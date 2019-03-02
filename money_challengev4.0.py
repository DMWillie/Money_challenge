"""
    作者:北辰
    功能:52周存钱挑战
    版本:4.0
    日期:14/06/2018
    2.0新增功能:记录每周存钱数
    3.0新增功能:使用循环直接计数
    4.0新增功能:灵活设置每周的存款数,增加的存款数及存款周数
"""

import math

def save_money_in_n_weeks(money_per_week,increase_money,total_week):
    """
    计算n周内的存钱金额
    """
    saving = 0  # 账户累计
    money_list = []  # 记录每周存款数的列表

   # 存钱操作
    for i in range(total_week):
        money_list.append(money_per_week)
        saving = math.fsum(money_list)  # 计算列表中所有元素的和
        # 输出信息
        # print('第{}周,存入{}元,账户累计{}元'.format(i + 1, money_per_week, saving))
        # 更新下一周存钱金额
        money_per_week += increase_money
    return saving

def main():
    """
    主函数
    """
    money_per_week = float(input('请输入每周存入的金额数: ')) #每周存入的金额
    increase_money = float(input('请输入每周递增的金额: ')) # 递增的金额
    total_week = int(input('请输入存钱的周数: ')) # 存钱的周数

    # 调用函数
    saving = save_money_in_n_weeks(money_per_week,increase_money,total_week)
    print('总存款金额: ',saving)

if __name__=='__main__':
    main()