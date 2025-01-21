# table-04
#df.plot()和plt.bar()的区别

#计算时间，当星期等于星期六或日，则输出“周末”，否则输出“工作日”。
data['时间'] = '工作日'
data.loc[data['星期'].isin(['星期六', '星期日']), '时间'] = '周末'

'''
data['星期'].isin(['星期六', '星期日'])：

#data['星期']：从 DataFrame data 中选取 星期 列。
#.isin(['星期六', '星期日'])：使用 isin 方法检查 星期 列中的元素是否在 ['星期六', '星期日'] 列表中，返回一个布尔型的 Series，其中 True 表示元素在列表中，False 表示不在。

data.loc[..., '时间']：
data.loc 是 pandas 中的一个基于标签的索引器，用于根据标签进行数据的选择和赋值。
data.loc[..., '时间'] 表示选取 时间 列，其中 ... 部分是前面的布尔型 Series，即 data['星期'].isin(['星期六', '星期日']) 的结果。
data.loc[data['星期'].isin(['星期六', '星期日']), '时间'] = '周末'：
整体上，这行代码的作用是将 data 中 星期 列的值为 星期六 或 星期日 的行的 时间 列的值更新为 周末。
'''

'''
data['性别群体'].isin(['女','男'])：使用 pandas 的 isin() 方法检查 性别群体 列中的元素是否在 ['女','男'] 列表中。
data[data['性别群体'].isin(['女','男'])]：将筛选出 性别群体 列中元素为 女 或 男 的行，形成一个新的 DataFrame。
'''
gender_channel_customer = data[data['性别群体'].isin(['女','男'])].groupby(["性别群体","渠道"])['客户数量'].sum()

gender_channel_customer_un = gender_channel_customer.unstack()
'''
unstack() 是 pandas 中的一个方法，主要用于将 Series 或 DataFrame 的层级索引（Hierarchical Index）进行重塑操作，将内层的索引转换为列。
当你对一个 Series 或 DataFrame 进行分组操作（例如使用 groupby()）并执行聚合操作后，
结果可能是一个具有多层索引的 Series 或 DataFrame。
unstack() 方法可以将其中的一个层级的索引转换为列，从而将结果重塑为更方便查看和分析的表格形式。
'''

'''
df.plot是pandas自带的绘图方法，可以按照dataframe列值的分类不同，生成多组列表不同的柱状图
'''

'''
plt.bar() 这是matplotlib.pyplot生成柱状图的方法，需要指定x轴y轴，如果需要分为多个组按不同颜色显示柱状图，则需要用for循环生成每个柱子
'''

