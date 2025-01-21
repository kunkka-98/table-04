import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
from IPython.core.interactiveshell import InteractiveShell


#计算时间，当星期等于星期六或日，则输出“周末”，否则输出“工作日”。
data['时间'] = '工作日'
data.loc[data['星期'].isin(['星期六', '星期日']), '时间'] = '周末'

'''
data['星期'].isin(['星期六', '星期日'])：

    data['星期']：从 DataFrame data 中选取 星期 列。
    .isin(['星期六', '星期日'])：使用 isin 方法检查 星期 列中的元素是否在 ['星期六', '星期日'] 列表中，返回一个布尔型的 Series，其中 True 表示元素在列表中，False 表示不在。

data.loc[..., '时间']：

    data.loc 是 pandas 中的一个基于标签的索引器，用于根据标签进行数据的选择和赋值。
    data.loc[..., '时间'] 表示选取 时间 列，其中 ... 部分是前面的布尔型 Series，即 data['星期'].isin(['星期六', '星期日']) 的结果。

data.loc[data['星期'].isin(['星期六', '星期日']), '时间'] = '周末'：

    整体上，这行代码的作用是将 data 中 星期 列的值为 星期六 或 星期日 的行的 时间 列的值更新为 周末。

'''


'''
df.plot是pandas自带的绘图方法，可以按照dataframe列值的分类不同，生成多组列表不同的柱状图
'''
#示例

'''
data['性别群体'].isin(['女','男'])：使用 pandas 的 isin() 方法检查 性别群体 列中的元素是否在 ['女','男'] 列表中。
data[data['性别群体'].isin(['女','男'])]：将筛选出 性别群体 列中元素为 女 或 男 的行，形成一个新的 DataFrame。
'''
gender_channel_customer = data[data['性别群体'].isin(['女','男'])].groupby(["性别群体","渠道"])['客户数量'].sum()
'''
unstack() 是 pandas 中的一个方法，主要用于将 Series 或 DataFrame 的层级索引（Hierarchical Index）进行重塑操作，将内层的索引转换为列。
当你对一个 Series 或 DataFrame 进行分组操作（例如使用 groupby()）并执行聚合操作后，
结果可能是一个具有多层索引的 Series 或 DataFrame。
unstack() 方法可以将其中的一个层级的索引转换为列，从而将结果重塑为更方便查看和分析的表格形式。
'''
gender_channel_customer_un = gender_channel_customer.unstack()
#绘制柱状图
#stacked=False不堆叠，stacked=True堆叠
gender_channel_customer_un.plot(kind = 'bar',stacked=False,figsize=(20,10))
plt.title('不同性别群体不同渠道的客户数量分布')
plt.xlabel('性别群体')
plt.ylabel('客户数量')
plt.xticks(rotation=0)
for p in plt.gca().patches:
    plt.gca().annotate(
        format(p.get_height(), '.0f'), 
        (p.get_x() + p.get_width() / 2., p.get_height()), 
        ha = 'center', va = 'center', 
        xytext = (0, 5), 
        textcoords = 'offset points')
plt.show()

city_channel_customer =data.groupby(["门店所在城市", "渠道"])['客户数量'].sum()
city_channel_customer

#绘制柱状图
city_channel_customer.unstack().plot(kind='bar', stacked=False, figsize=(20, 10))
plt.title('城市-渠道客户数量')
plt.xlabel('城市')
plt.ylabel('客户数量')
plt.xticks(rotation=0)
for p in plt.gca().patches:
    plt.gca().annotate(
        format(p.get_height(), '.0f'), 
        (p.get_x() + p.get_width() / 2., 
         p.get_height()), 
        ha = 'center', 
        va = 'center', 
        xytext = (0, 5), 
        textcoords = 'offset points')
plt.show()

'''
plt.bar() 这是matplotlib.pyplot生成柱状图的方法，需要指定x轴y轴，如果需要分为多个组按不同颜色显示柱状图，则需要用for循环生成每个柱子
'''
#示例
# 计算每个产品类别的平均利润和成本
profit_max = data.groupby("产品类别").agg({"利润":"mean", "成本":"mean"}).reset_index()
# 绘制双柱状图
#plt.subplots(figsize=(20, 10))：创建一个大小为 (20, 10) 的图形，并返回 fig（图形对象）和 ax（轴对象）
fig, ax = plt.subplots(figsize=(20, 10))
# 计算柱状图的宽度和位置
bar_width = 0.35  # 柱状图的宽度
index = np.arange(len(profit_max))  # x轴的位置
# 绘制平均利润柱状图
bars1 = ax.bar(index, profit_max['利润'], bar_width, label='平均利润')

# 绘制平均成本柱状图
bars2 = ax.bar(index + bar_width+0.05, profit_max['成本'], bar_width, label='平均成本', color='orange')
plt.title('不同产品类别的平均利润与成本的比对')
plt.xlabel('产品类别')
plt.ylabel('平均利润/成本')

# 设置x轴标签
plt.xticks(index + bar_width / 2, profit_max['产品类别'])  # 设置x轴刻度标签和位置

# 在柱状图上添加数值标签
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        # 格式化字符串，只显示整数部分，不显示小数点
        ax.annotate('{}'.format(int(height)),  # 使用int()函数转换为整数
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3点垂直偏移
                    textcoords="offset points",
                    ha='center', va='bottom')

add_labels(bars1)
add_labels(bars2)
# 添加图例
plt.legend()

plt.show()

##利用循环生成多个图表（通过for循环循环列，在通过seaborn制图）


features = data.select_dtypes(include=['object']).columns.tolist()

plt.figure(figsize=(20,8))
for i,col in enumerate(features[1:],1):
    plt.subplot(2,3,i)
    sns.countplot(x=col,data=data,palette='Set2')
    plt.title(f'{col}的柱形图',fontsize=14)
    plt.ylabel('频数',fontsize=14)
    for p in plt.gca().patches:
        plt.gca().annotate(
            format(p.get_height(), '.0f'), 
            #label = '{:.0f}'.format(p.get_height())
            (p.get_x() + p.get_width() / 2., p.get_height()), 
            ha = 'center', 
            va = 'center', 
            xytext = (0, 5), 
            textcoords = 'offset points')
plt.tight_layout()
plt.show()