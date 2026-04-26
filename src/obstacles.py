import json
from enum import Enum

class ObstacleType(Enum):
    SPIKE = 'spike'
    WALL = 'wall'
    SAW = 'saw'
    MOVING_PLATFORM = 'moving_platform'
    SINE_GATE = 'sine_gate'
    DOUBLE_SPIKE = 'double_spike'

class ObstacleFactory:
    @staticmethod
    def create_obstacle(obstacle_json):
        data = json.loads(obstacle_json)
        obstacle_type = ObstacleType[data['type']]
        # Additional properties could be added here based on the JSON structure
        return {'type': obstacle_type, 'properties': data['properties']} # Example of returning the obstacle object
