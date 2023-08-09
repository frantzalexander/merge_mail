class GetMail:
    
    def __init__(self, mailing_list_filepath ):
        self.file = open(mailing_list_filepath, "r")
        self.guest_list = self.process_mail()
        
    def process_mail(self):
        self.name_list = self.file.readlines()
        self.guest_name_list = []
        
        for name in self.name_list:
            guest_name = str(name).strip("\n")
            self.guest_name_list.append(guest_name)
        
        return self.guest_name_list
        
