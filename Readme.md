# Map of the trash pieces and trash cans in Nelson Mandela Park

## Dependencies 

The following modules are required to run the application and can be installed by copying the commands given after each module into terminal


### Pandas 2.2.1 or later
#### pip
pip install pandas

#### conda

conda install pandas

### plotly.express 0.4.1
#### pip

pip install plotly.express

#### conda

conda install plotly::plotly_express


## How to use

Just install dependencies and run the project with python. It can be run either directly from IDE you are using or from the folder that the program is: run

python3 main.py
or
python main.py 

with termanal opened from the folder with this program. For more information consult google or similar.

## Overview

The project visualises the locations  of trash and trash cans in Nelson Mandela Park near Bijmerplein in Amsterdam. It uses dataset collected by us exported in format of csv. The dataset is processed to fit the template of plotly library which is used to create the map with all locations from dataset. The location precision is highly accurate since the coordinates used are 7 decimal digits. 


### How to replace the dataset

This code is hardly maintanable, although if needed the csv can be replaced with csv containing different data. No columns should be changed as behaviour is not tested with altered csv heading. The look of the map can be changed through changing the values on lines 34-39. Consult https://python-charts.com/spatial/bubble-map-plotly/ and https://plotly.com/python/plotly-express/ for more information.