import math


class Line:

    def __init__(self, line_dictionary):
        self.x1 = line_dictionary.get("x1")
        self.y1 = line_dictionary.get("y1")
        self.x2 = line_dictionary.get("x2")
        self.y2 = line_dictionary.get("y2")
        self.line_length_dict = {}

    def line_length(self):
        length = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)

        self.line_length_dict.update()
        return length

    def __eq__(self, line_object):
        return self.line_length() == line_object.line_length()

    def __gt__(self, line_object):
        return self.line_length() > line_object.line_length()

    def __lt__(self, line_object):
        return self.line_length() < line_object.line_length()


def add_line():
    x1 = int(input("Enter x1 : "))
    y1 = int(input("Enter y1 : "))
    x2 = int(input("Enter x2 : "))
    y2 = int(input("Enter y2 : "))

    print(f'Co-ordinates of the line are (x1, y1): ({x1}, {y1}), (x2, y2): ({x2}, {y2})')

    line_dict = {"x1": x1, "y1": y1, "x2": x2, "y2": y2}
    line_object = Line(line_dict)

    return line_object


if __name__ == "__main__":
    print("Enter co-ordinates of first line")
    first_line_object = add_line()
    print("Enter co-ordinates of second line")
    second_line_object = add_line()

    if first_line_object == second_line_object:
        print("Both the lines are of equal size")
    elif first_line_object > second_line_object:
        print("First line is greater than second line")
    else:
        print("Second line is greater than first line")
        

