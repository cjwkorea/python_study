from animal import Animal

class Dog(Animal):
    
    count = 0

    def __init__(self,
                 name: str = "멍멍",
                 age: int = 0
                 ):
        """

        Args:
            name (str, optional): _description_. Defaults to "멍멍".
            age (int, optional): _description_. Defaults to 0.
        """

        super().__init__(age)
        
        self.name = name

        Dog.count = Dog.count + 1

        return

    def eat(self):
        print(f"강아지 '{self.name}'이 음식을 먹었습니다.")
       
    @classmethod
    def get_count(cls):
        print(f"강아지가 {cls.count}마리 생성되었습니다.")