import plotly.express as px
import pandas as pd
import test1

data = pd.DataFrame(data=zip(test1.lons,test1.lats,test1.places,test1.mags),columns=['经度','纬度','位置','震级'])

fig = px.scatter(
    data,
    x = test1.lons,
    y = test1.lats,
    labels={'x':'经度','y':'纬度'},
    range_x = [-200,200],
    range_y = [-90,90],
    width = 1600,
    height = 800,
    title = '全球地震散点图',

    size='震级',
    size_max=10,
    color='震级',
    hover_name='位置',

)





fig.show()