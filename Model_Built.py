max_dis = 1200


def extract_values(filename):
    array1 = []
    array2 = []
    array3 = []
    array4 = []
    count = 0
    with open(filename, 'r') as file:
        lines = file.readlines()

        for line in lines:
            if (count % 3 == 0):
                values = line.strip().split(',')

                # Assuming each line has exactly four values
                value1, value2, value3, value4 = map(int, values)

                array1.append(value1)
                array2.append(value2)
                array3.append(value3)
                array4.append(value4)
            count += 1

    return array1, array2, array3, array4
# Example usage
filename = './data.txt'
result_array1, result_array2, result_array3, result_array4 = extract_values(filename)

print("Array 1:", result_array1)
print("Array 2:", result_array2)
print("Array 3:", result_array3)
print("Array 4:", result_array4)

def New_Point(a, b):
    num1 = a[0] + b[0]
    num2 = a[1] + b[1]
    return (num1, num2)


def Create_points(data, dis_right, dis_left, width_r, width_l):
    stack = []
    colors = []
    current = (0, 0)

    counter_r = 0
    counter_l = 0
    updated_width_r =[]
    updated_width_l = []
    stack.append(current)
    steps = 0
    direction = 0
    for i in range(len(data)):
        if (data[i] == 0):
            if(direction == 0):
                if(width_r[i] > 100):
                    counter_r += 1
                    if(counter_r >= 2):
                        stack.append(New_Point(current, (width_r[i]/10, 0)))
                        colors.append('red')
                        stack.append(current)
                        colors.append('red')
                        updated_width_r.append(30)
                        updated_width_r.append(30)

                        updated_width_l.append(30)
                        updated_width_l.append(30)
                else:
                    counter_r = 0
                if(width_l[i] > 100):
                    counter_l += 1
                    if(counter_l >= 2):
                        stack.append(New_Point(current, (-width_l[i]/10, 0)))
                        colors.append('red')
                        stack.append(current)
                        colors.append('red')

                        updated_width_r.append(30)
                        updated_width_r.append(30)

                        updated_width_l.append(30)
                        updated_width_l.append(30)
                else:
                    counter_l = 0
                current = New_Point(current, (0,1))
                stack.append(current)
                colors.append('blue')
                updated_width_r.append(width_r[i])
                updated_width_l.append(width_l[i])


            elif(direction == 90):
                if (width_r[i] > 100):
                    counter_r += 1
                    if (counter_r >= 2):
                        stack.append(New_Point(current, (0, -width_r[i]/10)))
                        colors.append('red')
                        stack.append(current)
                        colors.append('red')
                        updated_width_r.append(30)
                        updated_width_r.append(30)

                        updated_width_l.append(30)
                        updated_width_l.append(30)
                else:
                    counter_r = 0
                if (width_l[i] > 100):
                    counter_l += 1
                    if (counter_l >= 2):
                        stack.append(New_Point(current, (0, width_l[i]/10)))
                        colors.append('red')
                        stack.append(current)
                        colors.append('red')

                        updated_width_r.append(30)
                        updated_width_r.append(30)

                        updated_width_l.append(30)
                        updated_width_l.append(30)
                else:
                    counter_l = 0
                current = New_Point(current, (1, 0))
                stack.append(current)
                colors.append('blue')
                updated_width_r.append(width_r[i])
                updated_width_l.append(width_l[i])
            elif (direction == 180):
                if (width_r[i] > 100):
                    counter_r += 1
                    if (counter_r >= 2):
                        stack.append(New_Point(current, (-width_r[i]/10, 0)))
                        colors.append('red')
                        stack.append(current)
                        colors.append('red')
                        updated_width_r.append(20)
                        updated_width_r.append(20)

                        updated_width_l.append(20)
                        updated_width_l.append(20)
                else:
                    counter_r = 0
                if (width_l[i] > 100):
                    counter_l += 1
                    if (counter_l >= 2):
                        stack.append(New_Point(current, (width_l[i]/10, 0)))
                        colors.append('red')
                        stack.append(current)
                        colors.append('red')

                        updated_width_r.append(20)
                        updated_width_r.append(20)

                        updated_width_l.append(20)
                        updated_width_l.append(20)
                else:
                    counter_l = 0
                current = New_Point(current, (0, -1))
                stack.append(current)
                colors.append('blue')
                updated_width_r.append(width_r[i])
                updated_width_l.append(width_l[i])

            elif (direction == 270):
                if (width_r[i] > 100):
                    counter_r += 1
                    if (counter_r >= 2):
                        stack.append(New_Point(current, (0, width_r[i]/10)))
                        colors.append('red')
                        stack.append(current)
                        colors.append('red')
                        updated_width_r.append(20)
                        updated_width_r.append(20)

                        updated_width_l.append(20)
                        updated_width_l.append(20)
                else:
                    counter_r = 0
                if (width_l[i] > 100):
                    counter_l += 1
                    if (counter_l >= 2):
                        stack.append(New_Point(current, (0, -width_l[i]/10)))
                        colors.append('red')
                        stack.append(current)
                        colors.append('red')

                        updated_width_r.append(20)
                        updated_width_r.append(20)

                        updated_width_l.append(20)
                        updated_width_l.append(20)
                else:
                    counter_l = 0
                current = New_Point(current, (-1, 0))
                stack.append(current)
                colors.append('blue')
                updated_width_r.append(width_r[i])
                updated_width_l.append(width_l[i])

        if (data[i] == 1):
            if (direction == 0):
                wall = New_Point(current, (0, 1))
                right = New_Point(wall, (dis_right/100, 0))
                left = New_Point(wall, (-dis_left/100, 0))
                stack.append(wall)
                colors.append('blue')
                stack.append(right)
                colors.append('blue')
                stack.append(left)
                colors.append('blue')
                updated_width_r.append(20)
                updated_width_r.append(20)

                updated_width_l.append(20)
                updated_width_l.append(20)

                updated_width_r.append(20)
                updated_width_l.append(20)

            elif (direction == 90):
                wall = New_Point(current, (1, 0))
                right = New_Point(wall, (0, -dis_right / 100))
                left = New_Point(wall, (0, dis_left / 100))
                stack.append(wall)
                colors.append('blue')
                stack.append(right)
                colors.append('blue')
                stack.append(left)
                colors.append('blue')
                updated_width_r.append(20)
                updated_width_r.append(20)

                updated_width_l.append(20)
                updated_width_l.append(20)

                updated_width_r.append(20)
                updated_width_l.append(20)

            if (direction == 180):
                wall = New_Point(current, (0, -1))
                right = New_Point(wall, (-dis_right/100, 0))
                left = New_Point(wall, (dis_left/100, 0))
                stack.append(wall)
                colors.append('blue')
                stack.append(right)
                colors.append('blue')
                stack.append(left)
                colors.append('blue')
                updated_width_r.append(20)
                updated_width_r.append(20)

                updated_width_l.append(20)
                updated_width_l.append(20)

                updated_width_r.append(20)
                updated_width_l.append(20)

            elif (direction == 270):
                wall = New_Point(current, (-1, 0))
                right = New_Point(wall, (0, dis_right / 100))
                left = New_Point(wall, (0, -dis_left / 100))
                stack.append(wall)
                colors.append('blue')
                stack.append(right)
                colors.append('blue')
                stack.append(left)
                colors.append('blue')
                updated_width_r.append(20)
                updated_width_r.append(20)

                updated_width_l.append(20)
                updated_width_l.append(20)

                updated_width_r.append(20)
                updated_width_l.append(20)

        if(data[i] == 2):
            direction += 90
            direction = direction % 360

        if(data[i] == 3):
            direction += 270
            direction = direction % 360
    return stack, colors, updated_width_r, updated_width_l

def Create_Thickness(dis_r, dis_l):
    thickness = []
    for i in range(len(dis_r)):
        #print(dis_r[i])
        #print(dis_l[i])
        if(dis_r[i] > 300 or dis_l[i] > 300):
            #print("in")
            thickness.append(30)
        elif(dis_r[i] + dis_l[i] < 60):
            thickness.append(70)
        else:
            thickness.append(70)
        #print(thickness[i] , "tot")
    return thickness

import plotly.graph_objects as go
# Define the set of points
#points = [(0, 0), (1, 4), (2, 2), (3, 5), (4, 6)]
#moves = [0,0,0,0,0,0,0,2,0,0,0,0,0,0,2,0,0,0,0,2,0,0,0,0,2,0,0,0,0,3,0,0,2,0,0,0,3,0,0,0,0,0,2,0,0,0,2,0,0,0,2,0,0,0,3,0,0,3,0,0,0,0,0,2,0,0,0,2,0,0,0,0,3,0,0,3,0,0,3,0,0,2,0,0]
moves = result_array4

#print(len(room_moves))
#moves = [0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,3,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,1]
#width_r = [20,10,30,10,30,20,400,400,10,60,40,5,20,20,20,20,5,20,20,20,20,20,20,20,20,20,50,20,340,340,20,20,20,10,30]
#width_l = [20,410,305,80,30,30,10,10,10,5,20,20,20,400,400,20,5,20,20,20,20,20,20,20,20,20,10,10,400,400,400,10,50,30,30]

#width_r = [20,20,20,20,20,20,20,20,20,20,320,320,320,320,20,320,320,320,320,20,320,320,320,320,20,320,320,320,320,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20]
width_r = result_array1
#width_l = [20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20]
width_l = result_array2
dis_r = 50
dis_l = 50
points, colors, width_r, width_l = Create_points(moves, dis_r, dis_l, width_r,width_l)

tot_width = Create_Thickness(width_r,width_l)

# Extract the x, y, and z coordinates of the points
x = [point[0] for point in points]
y = [point[1] for point in points]
z = [20] * len(points)  # Set a fixed height of 1 for all points

fig = go.Figure()
# Add markers to the plot
fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='markers', marker=dict(size=6)))

z_range = (0, 55)


fig.update_layout(scene=dict(
    aspectmode='manual',
    aspectratio=dict(x=1, y=1, z=1),
    zaxis=dict(range=z_range)
))
# Add lines to connect the points
for i in range(len(points) - 1):
    fig.add_trace(go.Scatter3d(
        x=[x[i], x[i + 1]],
        y=[y[i], y[i + 1]],
        z=[z[i], z[i + 1]],
        mode='lines',
        line=dict(width=tot_width[i], color=colors[i])
    ))

# Display the plot
fig.show()