# 可以自己import我们平台支持的第三方python模块，比如pandas、numpy等。

# 在这个方法中编写任何的初始化逻辑。context对象将会在你的算法策略的任何方法之间做传递。
def init(context):
    context.s1 = "000001.XSHG"
    #context.s2 =  "600744.XSHG"
    context.s2 = "和而泰"
    #context.s2 = "福建水泥"
    #context.s2 = "002503.XSHE"
    #context.slippage = 0.5
    #context.commission = 0.1
    update_universe([context.s2])
# 你选择的证券的数据更新将会触发此段逻辑，例如日或分钟历史数据切片或者是实时数据切片更新

def handle_bar(context,bar_dict):
    MA_3 = bar_dict[context.s2].mavg(8,frequency = 'day')
    MA_8 = bar_dict[context.s2].mavg(20,frequency = 'day')
    
    curPosition = context.portfolio.positions[context.s2].quantity
    shares = context.portfolio.cash/bar_dict[context.s2].close
    
    if MA_3 > MA_8 and curPosition == 0:
        order_target_percent(context.s2,1)
    
    if MA_3 < MA_8 and curPosition != 0:
        order_target_percent(context.s2,0)
