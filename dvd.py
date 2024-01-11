class DVListType:
    def __init__(self, title, actors, producers, director, production_company, number_of_copies):
        self.title = title
        self.actors = actors
        self.producers = producers
        self.director = director
        self.production_company = production_company
        self.number_of_copies = number_of_copies
    #Setters and Getters
    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_actors(self, actors):
        self.actors = actors

    def get_actors(self):
        return self.actors

    def set_producers(self, producers):
        self.producers = producers

    def get_producers(self):
        return self.producers

    def set_director(self, director):
        self.director = director

    def get_director(self):
        return self.director

    def set_production_company(self,production_company):
        self.production_company = production_company

    def get_production_company(self):
        return self.production_company

    def set_number_of_copies(self,number_of_copies):
        self.number_of_copies = number_of_copies

    def get_number_of_copies(self):
        return self.number_of_copies

    #Operation functions
    def checkin_dvd(self):
        self.number_of_copies = self.number_of_copies + 1

    def checkout_dvd(self):
        self.number_of_copies = self.number_of_copies - 1

    def update_copies(self, new_num):
        self.number_of_copies = self.number_of_copies + new_num

    def print_title(self):
        print("Title of the movie is ", self.title)

    #String Override function
    def __str__(self):
        output = f"Movie: {self.title}, " \
                 f"Actors: {self.actors},  " \
                 f"Producer: {self.producers}, " \
                 f"Director: {self.director}, " \
                 f"Production By: {self.production_company}, " \
                 f"Number of copies: {self.number_of_copies}"
        return output
