def get_plane():
    ret = []
    while 1:
        x = float(input("x coord: "))
        y = float(input("y coord:"))
        print("enter 'exit' if finished")
        prompt = input("Enter exit if finished plotting ")
        coord = x, y
        ret.append(coord)
        if prompt == "exit":
            break
    return ret
print("----- Getting original points ----")
list_of_coords = get_plane()

print("")
print("----- Getting Point of rotation -----")
print("Enter the point of rotation")
x = int(input("Enter the x coordnet of the point of rotation"))
y = int(input("Enter the y coordnet of the point of rotation"))
POR = x, y

print("")
print("----- Getting rotation degrees -----")
while 1:
    print("Enter how many degrees you would like to rotate the image")
    degrees = int(input(">>> "))
    if degrees != 90 and degrees != 180 and degrees != 270:
        print("Invalid")
    else:
        break

def vector_list(coords, point):
    ret = []
    for coord in coords:
        x = coord[0] - point[0]
        y = coord[1] - point[1]
        vector = x, y
        ret.append(vector)
    return ret

def rotate_vector(vectors, degrees):
    ret = []
    for vector in vectors:
        if degrees == 90:
            new_vector = vector[1] * -1, vector[0]
        if degrees == 180:
            new_vector = vector[0] * -1, vector[1] * -1
        if degrees == 270:
            new_vector = vector[1], vector[1] * -1
        ret.append(new_vector)
    return ret

def get_prime(rotated_vecs, point):
    ret = []
    for vector in rotated_vecs:
        primex = vector[0] + point[0]
        primey = vector[1] + point[1]
        prime = primex, primey
        ret.append(prime)
    return ret
print(get_prime(rotate_vector(vector_list(list_of_coords, POR), degrees), POR))
