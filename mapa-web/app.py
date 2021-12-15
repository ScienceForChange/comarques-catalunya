from flask import Flask, render_template, url_for
import folium

app = Flask(__name__)

@app.route("/")
def index():
    # https://stackoverflow.com/questions/37379374/insert-the-folium-maps-into-the-jinja-template
    start_coords = (41.3874, 2.1686)
    folium_map = folium.Map(location=start_coords, zoom_start=8, width="100%", height="100%")
    provincies = ["Barcelona", "Girona", "Lleida", "Tarragona"]
    for provincia in provincies: 
        geogson = f"../amb-capital/data/{provincia.lower()}_comarques.geojson"
        if provincia == "Girona":
            group = folium.FeatureGroup(name=f"{provincia}") 
            folium.GeoJson(geogson).add_to(group)
            folium.Marker(location=[41.8129, 2.9071], icon=folium.Icon(color="red", icon="plus", prefix='fa')).add_to(group)
            group.add_to(folium_map)
        else:
            folium.GeoJson(geogson, name=f"{provincia}").add_to(folium_map)
    folium.LayerControl().add_to(folium_map)
    return render_template('index.html', folium_map=folium_map._repr_html_())


if __name__ == '__main__':
    app.run(debug=True)
