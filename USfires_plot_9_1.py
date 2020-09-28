import json
import plotly

in_file = open("US_fires_9_1.json",'r')
out_file = open("Readable_fires_9_1.json",'w')

fire_data=json.load(in_file)

json.dump(fire_data,out_file,indent=4)

lats,lons,bright=[],[],[]

for fires in fire_data:
    lat = fires['latitude']
    lon = fires['longitude']
    bri = fires['brightness']
    if bri >450:
        lats.append(lat)
        lons.append(lon)
        bright.append(bri)

print("lats")
print(lats[:10])

print("lons")
print(lons[:10])

print("bright")
print(bright[:10])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data=[{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'marker':{
        
        'color':bright,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title':'Brightness'}
    }
}]


my_layout = Layout(title='US Fires- 9/1/2020 through 9/13/2020')
fig = {'data':data, 'layout':my_layout}

offline.plot(fig, filename='us_fires.html')

