import json
import csv
import pandas

filename1 = 'data/sitka_weather_2018_simple.csv'
filename2 = 'data/eq_data_30_day_m1.json'

#将json文件重新格式化后写入json文件中
# with open(filename2) as f:
#     reader_eq = json.load(f)  # 此时的数据是一个很乱的字典
    # print(reader_eq)

# with open('new_earthquake.json','w') as g:  # 创建一个新json文件
#     json.dump(reader_eq,g,indent=4)  # 使用dump输出

with open(filename1) as f:
    reader_weather = csv.reader(f)  # csv.reader 读出来的是一个可迭代对象
    line_list = next(reader_weather)


    dates,highs,lows = [],[],[]
    for row in reader_weather:
        date = row[2]  # 获取日期信息
        high = int(row[5])  # 获取最高温度
        low = int(row[6])  # 获取最低温第

        dates.append(date)
        highs.append(high)
        lows.append(low)

    # print(dates)
    # print(highs)
    # print(lows)


with open(filename2) as f:  # 打开整理后的和整理前的json文件是一样的
    reader_eq = json.load(f)
    print(reader_eq)
mags,places,lons,lats = [],[],[],[] # 震级,地点,经度,维度

for eq_dict in reader_eq['features']:
    mag = eq_dict['properties']['mag']
    place = eq_dict['properties']['place']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]

    mags.append(mag)
    places.append(place)
    lons.append(lon)
    lats.append(lat)

    # print(mags)
    # print(places)
    # print(lons)
    # print(lats)



