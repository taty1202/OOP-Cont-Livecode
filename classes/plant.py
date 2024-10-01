class Plant:

# Write your plant class here!
    def __init__(self, name, water_level, sunlight_hours, is_blooming=False):
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours
        self.is_blooming = is_blooming
    
    def water(self, water_amount):
        self.water_level += water_amount

        return f'{self.name} new water level: {self.water_level}'
    
    def give_sunlight(self, hours):
        self.sunlight_hours += hours

        return f'{self.name} new sun light hours: {self.sunlight_hours}'
    
    def check_growth(self):
        if self.sunlight_hours > 5 and self.water_level > 5:
            return "mature"
        else:
            return "sprout"




