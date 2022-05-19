import matplotlib.pyplot as plt
import test1

plt.style.use('seaborn')  # 添加背景样式
# subplots 会返回具有两个对象的元组
fig, ax = plt.subplots()  # fig,ax这两个变量就是入口
# print(fig,type(fig))  # figure在这里表示图片
# print(ax,type(ax))  # axes表示坐标轴
ax.plot(test1.dates,test1.highs,c='blue',alpha=0.5)  # plot是绘画折线图
ax.plot(test1.dates,test1.lows,c='red',alpha=0.5)  # 可以修改颜色

# 在折线之间添加填充色,颜色为'blue',透明度为'0.1'
ax.fill_between(test1.dates,test1.highs,test1.lows,facecolor='blue',alpha=0.1)

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 设置字体,如果经常使用中文,可以在库文件中添加,不用每次都输这一行
ax.set_title('2018年每日温度',fontsize=18)  # 设置标题和字体大小
ax.set_xlabel('日期',fontsize=14)  # 添加x轴标签
ax.set_ylabel('温度(F)',fontsize=14)  # 添加y轴标签
ax.tick_params(axis='both',which='major',labelsize=14)  # 不知道干嘛的

# 绘制散点图
# ax.scatter(test1.dates,test1.highs,c='blue')  #  scatter是绘画散点图
# ax.scatter(test1.dates,test1.lows,c='red')

# 倾斜显示x轴
fig.autofmt_xdate()


# 方式1
# 日期全部显示出来非常杂乱,让其只显示部分横坐标
ax.axes.xaxis.set_ticks(range(0,365,60))  # ax.坐标轴.x坐标轴.set_ticks 调整显示的横坐标数值
# 显示自定义的横坐标标签,而不使用它的原始值
ax.axes.xaxis.set_ticklabels(['2018-01','2018-03','2018-05','2018-07','2018-09','2018-11','2019-01'])

# 方式2
# ax.axes.xaxis.set_ticks(
#     range(0,365,60),
#     ['2018-01','2018-03','2018-05','2018-07','2018-09','2018-11','2019-01']
# )

# 方式3
# plt.xticks(range(0,365,60),['2018-01','2018-03','2018-05','2018-07','2018-09','2018-11','2019-01'])
# 三种方式的结果是一样的

plt.show()


