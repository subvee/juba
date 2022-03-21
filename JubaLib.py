import json
from colored import fg

green = fg("#0abf1f")
white = fg("#FFFFFF")

class Juba(object):
    def __init__(self, data):
        with open(data) as f:
            self.data = json.load(f)
            
    def Parse(self, column):
        return self.data[column]

    class OnConnect:
        def __init__(self, color) -> None:
            from datetime import date
            d = date.today()
            
            print(f"""
{green}{d} {white}| {color}
     ██╗██╗   ██╗██████╗  █████╗ 
     ██║██║   ██║██╔══██╗██╔══██╗
     ██║██║   ██║██████╔╝███████║
██   ██║██║   ██║██╔══██╗██╔══██║
╚█████╔╝╚██████╔╝██████╔╝██║  ██║
 ╚════╝  ╚═════╝ ╚═════╝ ╚═╝  ╚═╝
""")
            
if __name__ == "__main__":
    Juba = Juba("config.json")