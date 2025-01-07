
#! Created by Fluffik3666
#! 07-01-2024

class Counter:
    def __init__(self, string: str):
        self.string = string.strip()
        self.word_count = 0
    
    def count(self) -> int:
        if not self.string:
            return 0
        
        import re
        cleaned = re.sub(r'\s+', ' ', self.string)
        return cleaned.count(' ') + 1