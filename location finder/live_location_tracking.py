import folium #creates interactive map
latitude=28.6129
longitude=77.2295
# create map centered at location
# zoom_start=15 sets the zoom level (1 = whole world, 15 = city level, 20 = street level).
map_object=folium.Map(location=[latitude,longitude],zoom_start=15)
# add marker at given location
folium.Marker([latitude,longitude],popup="India Gate").add_to(map_object)
map_object.save("map.html")
print("Map has been saved as 'map.html'. Open it in a browser.")

