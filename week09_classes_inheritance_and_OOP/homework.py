class Robot():
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def print_name(self):
        print('Robot name: ' + self.name)


class RobotGroup():
    def __init__(self, list_of_robots):
        self.list_of_robots = list_of_robots


class NewRobot(Robot):
    def __init__(self, name, age=0, year_of_birth=2000):  # Why do I need to give a predefined age here as well even though it has a standard value in Robot()?
        Robot.__init__(self, name, age)
        self.year_of_birth = year_of_birth

    def print_age(self, current_year=2025):
        print(f'Robot age: {self.age}')
        print(f'Robot alternate age: {current_year-self.year_of_birth}')


robot1 = Robot('Fred')
robot2 = Robot('John', 1)
newRobot1 = NewRobot('Viggo')

robot_group = RobotGroup([robot1, robot2])

print(robot_group.list_of_robots)

robot1.print_name()

newRobot1.print_age()
