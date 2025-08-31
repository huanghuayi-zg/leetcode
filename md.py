# 模块注释 → 注释（绿斜体）
from typing import List  # namespace（淡黄） + comment

PI: float = 3.14        # variable（天蓝） = number（浅绿）

class Point:             # className（青）
    """点"""            # docstring（深绿斜体）

    def __init__(self, x: int, y: int) -> None:  # keyword（蓝） …
        self.x = x       # self（蓝） .property（淡蓝）
        self.y = y

    @property            # meta（黄）
    def length(self) -> float:  # function（黄）
        return (self.x ** 2 + self.y ** 2) ** 0.5  # operator（白）

s = "hello"             # string（橙）
if __name__ == "__main__":
    p = Point(1, 2)     # variable（天蓝）
    print(p.length)     # function call（黄）