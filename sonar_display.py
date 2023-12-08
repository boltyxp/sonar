"""Visualisation for input sonars"""

from cv2 import imread, rectangle, addWeighted
from matplotlib.pyplot import show, imshow
from numpy import ndarray

def annotate_image(sensor_numbers:list[int], image:ndarray, annotation_colour:tuple[int,int,int], relative_coordinates=list[tuple[float,float,float,float]]) -> ndarray:
    """iterate through each room and if sensor is on draw a rectangle on that room's coordinates"""
    rooms_annotated = image.copy()
    max_width,max_height,_ = rooms_annotated.shape
    for sensor_value,relative_coord in zip(sensor_numbers,relative_coordinates):
        if not sensor_value:
            continue
        absolute_width_start = int(relative_coord['width']['start']* max_width)
        absolute_width_end = int(relative_coord['width']['end']*max_width)
        absolute_height_start = int(relative_coord['height']['start']*max_height)
        absolute_height_end = int(relative_coord['height']['end']*max_height)
        start_coordinates = (absolute_width_start, absolute_height_start)
        end_coordinates = (absolute_width_end, absolute_height_end)
        rectangle(rooms_annotated, start_coordinates, end_coordinates, annotation_colour, -1)
    return addWeighted(image, 0.5, rooms_annotated, 0.5, 1.0)
    return rooms_annotated


rooms = imread("carehome_map.png")
coordinates = [
    dict(
        width=dict(
            start=0.45,
            end=0.5
        ),
        height=dict(
            start=1.2,
            end=1.25
        )
    ),
    dict(
        width=dict(
            start=0.18,
            end=0.23
        ),
        height=dict(
            start=1.2,
            end=1.25
        )
    ),
    dict(
        width=dict(
            start=0.52,
            end=0.58
        ),
        height=dict(
            start=1.05,
            end=1.1
        )
    ),
    dict(
        width=dict(
            start=0.35,
            end=0.4
        ),
        height=dict(
            start=1.05,
            end=1.1
        )
    ),
    dict(
        width=dict(
            start=0.18,
            end=0.23
        ),
        height=dict(
            start=1.05,
            end=1.1
        )
    ),
    dict(
        width=dict(
            start=0.21,
            end=0.26
        ),
        height=dict(
            start=0.1,
            end=0.15
        )
    ),
    dict(
        width=dict(
            start=0.37,
            end=0.42
        ),
        height=dict(
            start=0.1,
            end=0.15
        )
    ),
    dict(
        width=dict(
            start=0.52,
            end=0.57
        ),
        height=dict(
            start=0.1,
            end=0.15
        )
    ),
    dict(
        width=dict(
            start=0.2,
            end=0.25
        ),
        height=dict(
            start=0.5,
            end=0.55
        )
     ),
    dict(
        width=dict(
            start=0.52,
            end=0.57
        ),
        height=dict(
            start=0.5,
            end=0.55
        )
    ),
    dict(
        width=dict(
            start=0.35,
            end=0.4
        ),
        height=dict(
            start=0.5,
            end=0.55
        )
    ),
    dict(
        width=dict(
            start=0.2,
            end=0.22
        ),
        height=dict(
            start=0.85,
            end=0.9
        )
    ),
    dict(
        width=dict(
            start=0.36,
            end=0.41
        ),
        height=dict(
            start=0.82,
            end=0.87
        )
    ),
    dict(
        width=dict(
            start=0.51,
            end=0.57
        ),
        height=dict(
            start=0.82,
            end=0.87
        )
    )    
]
rooms_annotated = annotate_image(
    sensor_numbers=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 
    image=rooms, 
    relative_coordinates=coordinates,
    annotation_colour=(255,0,12)
)
imshow(rooms_annotated)
show()


