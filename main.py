from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.mapview import MapView,MapSource,MapMarker,MapMarkerPopup
import nearby_station
from kivy.uix.label import Label
from kivy.uix.button import Button

class PoliceApp(App):
    def build(self):
        box_layout = BoxLayout()
        map_view = MapView(lat=13.1345613974711, lon=80.24637305490332,zoom = 15)
        map_view.map_source = "osm"
        lat1,lon1,phone = self.police_nearby(13.1345613974711,80.24637305490332)
        map_marker = MapMarkerPopup(lat = lat1 , lon = lon1 , source = "images/marker1.png")
        self.value_label = Label(text=f"phone:{phone}",size=(200,100) )
        btn = Button(size =( 0.2,0.05),pos =(map_marker.pos[0],map_marker.pos[1]))
        map_marker.add_widget(btn)
        map_view.add_widget(map_marker)
        box_layout.add_widget(map_view)
        box_layout.add_widget(self.value_label)
        return box_layout
    


    
    def police_nearby(self,lat,lon):
        list1 = nearby_station.get_nearby_police_station(lat,lon)
        latitude = list1[0][0]
        longitude = list1[0][1]
        phone = list1[0][2]
        return latitude,longitude,phone



if __name__ == "__main__":
    PoliceApp().run()