class Star_Cinema:
    hall_list =[]

    def add_hall(self, hall):
        self.hall_list.append(hall)

class Hall:
    def __init__(self, rows, colm, hall_no):
        self._seats={}
        self._show_list=[]
        self.rows= rows
        self.colm =colm
        self._hall_no=hall_no
    def hall_no(self):
        return self._hall_no
    def entry_show(self, show_id, movie_name, time):
        show = (show_id, movie_name, time)
        self._show_list.append(show)
        self._seats[show_id] = [['0' for i in range(self.colm)] for i in range(self.rows)]

    def book_seats(self, show_id, seat_list):
        if show_id not in self._seats:
            print('Invalid Show ID.')
            return

        for row, col in seat_list:
            if row >= self.rows or col >= self.colm or row < 0 or col < 0:
                print(f"Invalid seat position ({row}, {col}).")
                continue


            if self._seats[show_id][row][col] == 'X':
                print(f"Seat at position ({row}, {col}) is already bookeed.")
                continue

            self._seats[show_id][row][col] = 'X'

    def view_show_list(self):
        for show in self._show_list:
            print(f'Id: {show[0]}, Movie: {show[1]}, Time: {show[2]}')

    def view_available_seats(self, show_id):
        if show_id not in self._seats:
            print('Invalid show ID.')
            return

        seats = self._seats[show_id]
        for row_ind, row in enumerate(seats):
            for col_ind, seat in enumerate(row):
                print(f'Seat ({row_ind},{col_ind}): {"Available" if seat == "0" else "Booked"}')


# Example
hall1 = Hall(5,5,"Hall 01")
hall1.entry_show(101,"Jawan Majhi",'6:00')
hall1.entry_show(107,"3 Idiots",'21:00')

star_cinema = Star_Cinema()
star_cinema.add_hall(hall1)

run = True

while run:
    print("----Welcome To Star Cinema---- \nOptions:")
    print("1: Book Teckat")
    print('2: View All Shows Today')
    print('3: View Available Seats')
    print('4: Exit')

    choice = int(input("\nEnter Option: "))

    if choice == 1:
        show_id = int(input("Enter Show ID: "))
        row = int(input("Enter Row: "))
        col = int(input('Enter Column: '))
        hall1.book_seats(show_id, [(row, col)])
    elif choice == 2:
        hall1.view_show_list()
    elif choice == 3:
        show_id = int(input("\tEnter Show ID: "))
        hall1.view_available_seats(show_id)
    elif choice == 4:
        run = False
    else:
        print('Invalid Option!')
