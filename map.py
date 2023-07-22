import folium

m= folium.Map(loction=[7.9499962, 4.7833302], zoom_start = 12)


tooltip='Click For More Info'
address = '<strong>5, Eboka street</strong'

#create markers
folium.Marker([7.9499962, 4.7833302], 
              popup=address,
              tooltip=tooltip, icon=folium.Icon(color='red',  icon='info-sign')).add_to(m)

m.save('map.html')
