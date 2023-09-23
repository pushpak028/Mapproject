import folium
import osmnx as ox
import networkx as nx 
import os
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


def wayy(lat1,lon1,lat2,lon2):

    start_coord = (lat1,lon1)
    end_coord = (lat2,lon2)
    north = 13.2621  # Latitude of northern boundary
    south = 12.8333  # Latitude of southern boundary
    east = 80.3333   # Longitude of eastern boundary
    west = 80.1486 

    graphs = ox.graph_from_bbox(north, south, east, west, network_type='all')

    
    start = ox.nearest_nodes(graphs,X=start_coord[1],Y=start_coord[0])
    end = ox.nearest_nodes(graphs,X=end_coord[1],Y=end_coord[0])

    route = nx.shortest_path(graphs,start,end,weight='length')

    route_coordinates = [(graphs.nodes[node]['y'], graphs.nodes[node]['x']) for node in route]

    m = folium.Map(location=start_coord,zoom_start=15)               

    #ox.plot_graph_folium(graphs, graph_map=m, edge_color='b')
    folium.PolyLine(locations=route_coordinates, color='red', weight=5, opacity=0.7).add_to(m)

    folium.Marker([lat1,lon1],tooltip="mylocation").add_to(m)
    folium.Marker([lat2,lon2],tooltip="policestation").add_to(m)

    if not os.path.exists("images"):
        os.makedirs("images")

    file_name = os.path.join("images","dummy.html")
    m.save(file_name)

    mapUrl = 'file://{0}/{1}'.format(os.getcwd(), "images/dummy.html")
    driver = webdriver.Firefox()
    driver.get(mapUrl)
        # wait for 5 seconds for the maps and other assets to be loaded in the browser
    time.sleep(5)
    action = webdriver.ActionChains(driver)
    action.key_down(Keys.CONTROL).send_keys('+').key_up(Keys.CONTROL).perform()
    driver.save_screenshot('images/outputd.png')
    driver.quit()
    os.remove("images/dummy.html")
    print("done")

