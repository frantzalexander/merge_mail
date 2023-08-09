class GetLetter:
    
    def __init__(self, letter_filepath):
        self.letter_path = letter_filepath
        self.contents = self.process_letter()
        
    def process_letter(self):
        with open(self.letter_path, mode = "r") as data:
            self.letter_contents = data.read()
    
        return self.letter_contents
        
    