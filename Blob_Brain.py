import math

nearest_food = (12, 8)
self_position = (27, 38)
speed = 5

movement_vector = (nearest_food[0] - self_position[0], nearest_food[1] - self_position[1])
movement_magnitude = math.sqrt(movement_vector[0] ** 2 + movement_vector[1] ** 2)
movement_unit_vector = (movement_vector[0] / movement_magnitude, movement_vector[1] / movement_magnitude)

actual_movement = (movement_unit_vector[0] * speed, movement_unit_vector[1] * speed)
