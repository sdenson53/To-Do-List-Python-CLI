# import statements
import csv
import argparse
import datetime
import os
from prettytable import from_csv
import pandas as pd

# argparse
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--option', metavar='', help='-o <option> write either you want to add or view')
parser.add_argument('-t', '--task', metavar='', help='-t <task>Enter the task you want to add', default='error')
parser.add_argument('-s', '--done', metavar='', help='-s Enter the status Complete if it is', default='Incomplete')
parser.add_argument('-p', '--project', metavar='', help='-d <project> Enter the project name')
parser.add_argument('-l', '--select', metavar='', help='-l <used to select the task for modification')
parser.add_argument('-d', '--due', metavar='', help='-d <due date for the task- '
                                                    'today/tomorrow/days to complete', default='tomorrow')
args = parser.parse_args()

# checks if file is empty; Writes headers in case it is empty
with open('csv.csv', 'a+', newline='') as myfile:
    fieldnames = ['T.No', 'Date', 'Task', 'Project', 'Context', 'Status']
    writer = csv.DictWriter(myfile, fieldnames=fieldnames)
    if os.path.getsize('csv.csv') == 0:
        writer.writeheader()

# checks number of entries in the file and the value is taken as x; to be used for auto incrementing task IDs
with open('csv.csv', 'r+', newline='') as myfile:
    reader = csv.DictReader(myfile)
    x = len(list(myfile))

# opening file in append mode for all operations
with open('csv.csv', 'a+', newline='') as myfile:
    fieldnames = ['T.No', 'Date', 'Task', 'Project', 'Context', 'Status']
    writer = csv.DictWriter(myfile, fieldnames=fieldnames)

    # function to add task
    def addtask():
        r = args.task.split()   # splits all values of task (to check for context using '@')
        qs = []         # list for all words starting with @
        for i in r:     # i = iterator
            if i.startswith("@"):    # checking for context
                qs.append(i)    # adding all words starting with @ into list qs
        if args.due == 'today':     # if due date is inputted as today
            time = datetime.datetime.now()
            t = time.strftime("%d/%m/%Y")
        elif args.due == 'tomorrow':    # if due date is inputted as tomorrow
            time = datetime.date.today() + datetime.timedelta(days=1)
            t = time.strftime("%d/%m/%Y")
        else:
            td = args.due   # if date is inputted as neither today or tomorrow, takes a numeric value as time delta
            time = datetime.datetime.now() + datetime.timedelta(days=(int(td)))
            t = time.strftime("%d/%m/%Y")
        q = " & ".join(qs)      # joins all words starting with '@' with '&' symbol to be entered into the table
        writer.writerow({'T.No': x, 'Date': t, 'Task': args.task, 'Project': args.project,
                         'Context': q, 'Status': args.done})
        print('TASK ADDED SUCCESSFULLY')

    # function to view the To-Do List
    def viewlist():
        print('-' * 35 + 'TO-DO List' + '-' * 35)
        with open('csv.csv') as file:
            table = from_csv(file)      # using prettytable method
            print(table)

    # function to change the status of a task to 'Complete'
    def modify():
        with open("csv.csv", 'r+') as f:
            lines = f.readlines()
            f.seek(0)   # points to the beginning of the entry

            task = args.select      # taken as input with -l

            for line in lines:
                if task in line.split(',')[0]:          # changing status to complete for the selected entry
                    f.write('\n' + line.split(',')[0] + ',' + line.split(',')[1] + ',' + line.split(',')[2] + ','
                            + line.split(',')[3] + ',' + line.split(',')[4] + ',' + 'Complete')
                else:
                    f.write('\n' + line)

            f.truncate()
            with open('csv.csv') as f2, open('demo005.csv', 'w') as f3:     # removal
                non_blank = (line for line in f2 if line.strip())           # of
                f3.writelines(non_blank)                                    # potential
            with open('demo005.csv') as f2, open('csv.csv', 'w') as f3:     # blank
                non_blank = (line for line in f2 if line.strip())           # lines
                f3.writelines(non_blank)

            viewlist()
            print('STATUS OF TASK {} CHANGED SUCCESSFULLY'.format(args.select))

    # function to sort the table according to different inputs
    def sort():
        if args.select == 'due':    # sorting according to due date using pandas
            df = pd.read_csv('csv.csv', index_col=False)
            df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%d/%m/%Y')
            df.sort_values('Date', inplace=True)
            df.to_csv('csv.csv', index=False)
            viewlist()
        elif args.select == 'complete':     # views all completed tasks
            with open("csv.csv", 'r+') as f:
                lines = f.readlines()
                with open('result.csv', 'w+') as f3:
                    writer = csv.DictWriter(f3, fieldnames=fieldnames)
                    writer.writeheader()
                    for line in lines:
                        if "Complete" in line.split(',')[5]:    # checking for completed tasks
                            f3.write(line)
                with open('result.csv') as f2, open('demo005.csv', 'w') as f3:  # next 6 lines:
                    non_blank = (line for line in f2 if line.strip())           # removing accidental blank lines
                    f3.writelines(non_blank)
                with open('demo005.csv') as f2, open('result.csv', 'w') as f3:
                    non_blank = (line for line in f2 if line.strip())
                    f3.writelines(non_blank)
                f3 = open("result.csv")
                tb = from_csv(f3)   # printing result
                print(tb)
        elif args.select == 'incomplete':   # printing all incomplete tasks
            with open("csv.csv", 'r+') as f:
                lines = f.readlines()
                with open('result.csv', 'w+') as f3:
                    writer = csv.DictWriter(f3, fieldnames=fieldnames)
                    writer.writeheader()
                    for line in lines:
                        if "Incomplete" in line.split(',')[5]:  # checking for incomplete tasks
                            f3.write(line)
                with open('result.csv') as f2, open('demo005.csv', 'w') as f3:  # next 6 lines:
                    non_blank = (line for line in f2 if line.strip())           # removing accidental blank lines
                    f3.writelines(non_blank)
                with open('demo005.csv') as f2, open('result.csv', 'w') as f3:
                    non_blank = (line for line in f2 if line.strip())
                    f3.writelines(non_blank)
                f3 = open("result.csv")
                tb = from_csv(f3)   # printing result
                print(tb)
        elif args.select == 'project':  # sorting data by project using pandas
            data = pd.read_csv("csv.csv", index_col=False)
            data.sort_values(["Project"], axis=0, ascending=True, inplace=True)
            data.to_csv('result.csv', index=False)
            db = open('result.csv')
            tb = from_csv(db)
            print(tb)
        elif args.select == 'context':   # sorting data by context using pandas
            data = pd.read_csv("csv.csv", index_col=False)
            data.sort_values(["Context"], axis=0, ascending=True, inplace=True)
            data.to_csv('result.csv', index=False)
            db = open('result.csv')
            tb = from_csv(db)
            print(tb)
        elif args.select == 'overdue':  # shows all data which are overdue or are due today
            with open("csv.csv", 'r+') as f:    # taking only Incomplete tasks
                lines = f.readlines()
                with open('result.csv', 'w+') as f3:
                    writer = csv.DictWriter(f3, fieldnames=fieldnames)
                    writer.writeheader()
                    for line in lines:
                        if "Incomplete" in line.split(',')[5]:
                            f3.write(line)
                with open('result.csv') as f2, open('demo005.csv', 'w') as f3:
                    non_blank = (line for line in f2 if line.strip())
                    f3.writelines(non_blank)
                with open('demo005.csv') as f2, open('result.csv', 'w') as f3:
                    non_blank = (line for line in f2 if line.strip())
                    f3.writelines(non_blank)
            with open("result.csv", 'r+') as f:      # checking for today's or past day's date
                lines = f.readlines()
                with open('demo005.csv', 'w+') as f3:
                    writer = csv.DictWriter(f3, fieldnames=fieldnames)
                    writer.writeheader()
                    time = datetime.datetime.now()
                    t = time.strftime("%d/%m/%Y")
                    for line in lines:
                        if line.split(',')[1] <= t:
                            f3.write(line)
                with open('demo005.csv') as f2, open('result.csv', 'w') as f3:      # next 6 lines:
                    non_blank = (line for line in f2 if line.strip())               # removing accidental blank lines
                    f3.writelines(non_blank)
                with open('result.csv') as f2, open('demo005.csv', 'w') as f3:
                    non_blank = (line for line in f2 if line.strip())
                    f3.writelines(non_blank)
                f3 = open("demo005.csv")
                tb = from_csv(f3)   # printing result
                print(tb)

        else:
            print("PLEASE SPECIFY HOW YOU WANT TO SORT USING A "
                  "VALID ARGUMENT -l <complete/incomplete/due/project/context>")

    # function to delete an entry
    def delete():
        with open("csv.csv", 'r+') as f:
            lines = f.readlines()
            f.seek(0)

            task = args.select

            for line in lines:
                if not task in line.split(',')[0]:  # prints all entries which are not selected
                    f.write(line)

            f.truncate()
            viewlist()
            print('TASK {} DELETED SUCCESSFULLY'.format(args.select))

    # main function
    def main():
        if args.option == 'add':
            if args.task == 'error':    # shows an error if no task is specified after add argument
                print('ERROR TASK NOT SPECIFIED')
            else:
                addtask()
        elif args.option == 'view':
            viewlist()
        elif args.option == 'modify':
            modify()
        elif args.option == 'delete':
            delete()
        elif args.option == 'sort':
            sort()
        else:
            print('Invalid Arguments\n input add <task> <description> <status done/not done(0/1)>\n '
                  'OR\n view(to view to-do list)')

    if __name__ == '__main__':
        main()
