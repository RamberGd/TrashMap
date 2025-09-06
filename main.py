
import pandas as pd
import plotly.express as px


# Read csv with data
dfTrash = pd.read_csv("resources/CSPTrash.csv") 

# Clean up the columns and separate latitude and longtitude
dfTrash["Location"] = dfTrash["Location"].str.replace("(", " ")
dfTrash["Location"] = dfTrash["Location"].str.replace(")", " ")
dfTrash[["Latitude", "Longtitude"]] = dfTrash['Location'].str.split(', ', expand=True)
dfTrash["Number"] = dfTrash["Number"].fillna(1)

# Delete location column (no longer needed) and type (was there for readability, it is faster to just create new one)
del dfTrash["Location"], dfTrash["Type"]

# Add either "trash" or "cans" tags to differentiate colours on the map
dfTrash['Type'] = "Trash"
dfTrash.iloc[[36, 37, 38], [3]] = "Cans"
print(dfTrash)

# Add the bubble map 
map = px.scatter_mapbox(dfTrash, lat = 'Latitude', lon = 'Longtitude', size = 'Number',
                    
                        center = dict(lat = 52.3120982, lon = 4.9538292),
                        zoom = 16,
                        mapbox_style = "open-street-map", #another option is "white-bg" for better readability with relative location (without location)
                        color = "Type")
                        
map.show()