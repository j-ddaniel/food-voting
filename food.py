"""
A program that will ask users what their favorite food is. Save the answers to a
CSV file called "favorite_food.csv". After answering, display a table of tallied
reslts"""
import csv

def check_exist_file():
    """Check if file exist. if not it create a new file for it"""
    try:
        with open('favorite_food.csv', 'r') as f:
            pass
    except FileNotFoundError:
        with open('favorite_food.csv', 'w', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(['Favorite Food?', '# of votes'])

def get_favorite_food():
    """Accept favorite food from user"""
    favorite_food = input("Enter favorite food: ").title()
    return favorite_food

def add_edit_food(food):
    """Insert favorite in a new edited file"""
    row_found = False
    with open('favorite_food.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        copy_reader = [ row for row in reader]
        for rows in copy_reader:
            if rows[0] == food:
                row_found = True
                rows[1] = int(rows[1])
                rows[1] += 1
        if row_found == False:
            copy_reader.append([food, 1])
        print('Vote added succesfully')
##        print(copy_reader)
    return copy_reader

def edit_csv_file(new_txt):
    """Add the new edited content to the csv file>
Note this program will overwrite the former content of the csv file"""
    with open('favorite_food.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        for rows in new_txt:
            writer.writerow(rows)

def display_favorite_food():
    """Display the list of the favorite food to the user by reading it from
the csv file"""
    print("Collating result....")
    with open('favorite_food.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        print("\n\n Here are the results:\n")
        for rows in reader:
            print("""
                 {} {}""".format(rows[0], rows[1]))

def food_winning():
    """shows the vote with the highest currently vote"""
    winner =  0
    winning_food = []
    with open('favorite_food.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        copy_reader = [row for row in reader]
        for row in copy_reader:
            try:
                row[1] = int(row[1])
            except:
                pass
            else:
                if row[1] > winner:
                    winner =  row[1]
        for row in copy_reader:
            if row[1] == winner:
                winning_food.append(row)
    print("The following food are most voted for: \n")
    for row in winning_food:
        print('{}\t{}'.format(row[0], row[1]))
def sort_food():
    """Sort the food in descending order according to the order of vote"""
    with open('favorite_food.csv', 'r') as f:
        reader = csv.reader(f, delimiter =',')
        copyList =[row for row in reader]
        number_rows =[row[1] for row in copyList]
        sorted_list = []
        number_rows.sort()
        for rows in number_rows:
            for row in copyList:
                if row[1] == rows and row not in sorted_list:
                        sorted_list.append(row)
        return sorted_list
        
def main():
    """The main function that runs the program"""
    check_exist_file()
    choice = None
    while choice != 0:
        print("""
Welcome to the Ultimate Favorite food guest.
Here are what to do:
    0. Quit
    1. Vote for favorite food
    2. Display voters list of favorite food
    3. Show the food most voted for
    4. sort vote
    """)
        try:
            choice = int(input("What do you want to do (0 -2)? "))
            
        except ValueError:
            print("Sorry you can only enter number")
            
        else:
            if choice == 0:
                print("Goodbye\nThanks for using our software")
                
            elif choice == 1:
                food = get_favorite_food()
                new_txt = add_edit_food(food)
                edit_csv_file(new_txt)
                
            elif choice == 2:
                display_favorite_food()

            elif choice ==3:
                food_winning()

            elif choice == 4:
                sorted_food = sort_food()
                edit_csv_file(sorted_food)
                print('sorting vote...')
                print('Voted sorted in descending order')
            
            else:
                print("Number out of range")

#main
main()
















                               
