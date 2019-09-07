"""
A class using the folium module to visualize the sentiments after new proposal
has been presented to residents in LOU area.
"""


from geopy.geocoders import Nominatim
from pandas.io.json import json_normalize
import folium
import json
import vincent

class MapVisualization:

    def __init__(self, coordinates, precentage, option, location, polygon):
        self.coordinates = coordinates
        self.precentage = precentage
        self.option = option
        self.location = location
        self.polygon = polygon

    def vinPlot(self, data, sch):
        pie_chart = vincent.Pie(data, height =100, width =100, inner_radius = 25)
        pie_chart.colors(brew = 'Set2')
        pie_chart.legend(sch[:-10])  # -10 for elementary, -6 for middle, -4 for high
        pie_json = pie_chart.to_json()

        return pie_json

    def foliumVisual(self, col):

        locationCenter = Nominatim(user_agent='my-application').geocode(self.location)

        initMap = folium.Map(location = [locationCenter.latitude, locationCenter.longitude],
                             zoom_start = 11)

        for school in self.coordinates.keys():

            lat = self.coordinates[school][0]
            lon = self.coordinates[school][1]

            if lat == 'NA' or lon == 'NA':
                continue

            else:
                chart_json = self.vinPlot(self.precentage[school][self.option], school)
                folium.Marker(location = [lat, lon],
                              popup = folium.Popup(max_width = 400).add_child(
                                  folium.Vega(chart_json, width = 200, height =100)),
                              icon = folium.Icon(color = col, icon = 'info-sign')
                             ).add_to(initMap)

        geojson = self.polygon
        folium.GeoJson(geojson, name = 'geojson').add_to(initMap)

        return initMap
