# IDrone
Autonomous Robot scanning the area given and model it in 3D

Robot_Control inclue 3 main things:
1. Control the distance Sensors - get data from the front, and L/R sensorsto measure distance.
2. Control the Wheels - make the abillity to turn left, turn right and drive Forward.
3. Main Algorithm - given the data from the sensors - decides what to do in order to get the data wanted

Model_Built uses the library "Plotly" in order to build the 3D model of the area.
The data is depended on "decisions", meaning each decision affect the next step. by connenting all the steps, we build a map.
