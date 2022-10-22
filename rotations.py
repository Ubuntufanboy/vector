def get_plane():
    ret = []
    while 1:
        x = float(input("x coord: "))
        y = float(input("y coord:"))
        print("enter 'exit' if finished")
        prompt = input("Enter exit if finished plotting")
        coord = x, y
        ret.append(coord)
        if prompt == "exit":
            break
    return ret
list_of_coords = get_plane()
while 1:
    print("Enter the degrees counterclockwise you want to rotate the image")
    degrees = int(input("Enter here >>> "))
    if degrees != 90 and degrees != 180 and degrees != 270:
        print("Invalid")
    else:
        break

if degrees == 90:
    ret = []
    for coord in list_of_coords:
        new_coord = coord[1] * -1, coord[0]
        ret.append(new_coord)
elif degrees == 180:
    ret = []
    for coord in list_of_coords:
        new_coord = coord[0] * -1, coord[1] * -1
        ret.append(new_coord)
elif degrees == 270:
    ret = []
    for coord in list_of_coords:
        new_coord = coord[1], coord[0] * -1
        ret.append(new_coord)
print(ret)
        
