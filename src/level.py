import json

class Level:
    def __init__(self, name="Unnamed", obstacles=None, properties=None):
        self.name = name
        self.obstacles = obstacles if obstacles is not None else []
        self.properties = properties if properties is not None else {}  

    def load_from_json(self, json_file):
        with open(json_file, 'r') as file:
            data = json.load(file)
            self.name = data.get('name', self.name)
            self.obstacles = data.get('obstacles', self.obstacles)
            self.properties = data.get('properties', self.properties)

    def save_to_json(self, json_file):
        data = {
            'name': self.name,
            'obstacles': self.obstacles,
            'properties': self.properties
        }
        with open(json_file, 'w') as file:
            json.dump(data, file, indent=4)

    def manage_obstacles(self, obstacle):
        self.obstacles.append(obstacle)  
        # Additional logic to manage obstacles can be added here

    def __str__(self):
        return f"Level(name={self.name}, obstacles={self.obstacles}, properties={self.properties})"