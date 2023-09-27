class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
    
    def set_height(self, height: int):
        self.height = height
    
    def set_width(self, width: int):
        self.width = width
    
    def get_area(self) -> int:
        return self.width * self.height
    
    def get_perimeter(self) -> int:
        return (2*self.height)+(2*self.width)
    
    def get_diagonal(self) -> float:
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self) -> str:
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        picture = ""
        for rows in range(self.height):
            picture += ("*"*self.width)+"\n"
        return picture
    
    def get_amount_inside(self, obj) -> int:
        return self.get_area()//obj.get_area()
    
    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, side: int):
        self.side = self.width = self.height = side
    
    def set_side(self, side: int):
        self.side = self.height = self.width = side

    def set_height(self, height: int):
        self.side = height
    
    def set_width(self, width: int):
        self.side = width
    
    def __str__(self) -> str:
        return f"Square(side={self.side})"