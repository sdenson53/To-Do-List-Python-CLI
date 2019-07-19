import csv
import argparse
import datetime
import os
from prettytable import from_csv
import pandas as pd


parser = argparse.ArgumentParser()
parser.add_argument('-o', '--option', metavar='', help='-o <option> write either you want to add or view')
parser.add_argument('-t', '--task', metavar='', help='-t <task>Enter the task you want to add', default='error')
parser.add_argument('-s', '--done', metavar='', help='-s Enter the status Complete if it is', default='Incomplete')
parser.add_argument('-p', '--project', metavar='', help='-d <project> Enter the project name')
parser.add_argument('-l', '--select', metavar='', help='-l <used to select the task for modification')
parser.add_argument('-d', '--due', metavar='', help='-d <due date for the task- '
                                                    'today/tomorrow/days to complete', default='tomorrow')
args = parser.parse_args()


with open('csv.csv', 'a+', newline='') as myfile:
    fieldnames = ['T.No', 'Date', 'Task', 'Project', 'Context', 'Status']
    writer = csv.DictWriter(myfile, fieldnames=fieldnames)
    if os.path.getsize('csv.csv') == 0:
        writer.writeheader()


with open('csv.csv', 'r+', newline='') as myfile:
    reader = csv.DictReader(myfile)
    x = len(list(myfile))


with open('csv.csv', 'a+', newline='') as myfile:
    fieldnames = ['T.No', 'Date', 'Task', 'Project', 'Context', 'Status']
    writer = csv.DictWriter(myfile, fieldnames=fieldnames)


    def addtask():
        r = args.task.split()
        qs = []
        for i in r:
            if i.startswith("@"):
                qs.append(i)
        if args.due == 'today':
            time = datetime.datetime.now()
            t = time.strftime("%d/%m/%Y")
        elif args.due == 'tomorrow':
            time = datetime.date.today() + datetime.timedelta(days=1)
            t = time.strftime("%d/%m/%Y")
        else:
            td = args.due
            time = datetime.datetime.now() + datetime.timedelta(days=(int(td)))
            t = time.strftime("%d/%m/%Y")
        q = " & ".join(qs)
        writer.writerow({'T.No': x, 'Date': t, 'Task': args.task, 'Project': args.project,
                         'Context': q, 'Status': args.done})
        print('TASK ADDED SUCCESSFULLY')


    def viewlist():
        print('-' * 35 + 'TO-DO List' + '-' * 35)
        with open('csv.csv') as file:
            table = from_csv(file)
            print(table)


    def modify():
        with open("csv.csv", 'r+') as f:
            lines = f.readlines()
            f.seek(0)

            task = args.select

            for line in lines:
                if not task in line.split(',')[0]:
                    f.write(line)
            for line in lines:
                if task in line.split(',')[0]:
                    f.write('\n' + line.split(',')[0] + ',' + line.split(',')[1] + ',' + line.split(',')[2] + ','
                            + line.split(',')[3] + ',' + line.split(',')[4] + ',' + 'Complete')

            f.truncate()
            with open('csv.csv') as f2, open('demo005.csv', 'w') as f3:
                non_blank = (line for line in f2 if line.strip())
                f3.writelines(non_blank)
            with open('demo005.csv') as f2, open('csv.csv', 'w') as f3:
                non_blank = (line for line in f2 if line.strip())
                f3.writelines(non_blank)

            viewlist()
            print('STATUS OF TASK {} CHANGED SUCCESSFULLY'.format(args.select))

    def sort():
        if args.select == 'due':
            df = pd.read_csv('csv.csv', index_col=False)
            df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%d/%m/%Y')
            df.sort_values('Date', inplace=True)
            df.to_csv('csv.csv', index=False)
            viewlist()
        elif args.select == 'complete':
            with open("csv.csv", 'r+') as f:
                lines = f.readlines()
                with open('result.csv', 'w+') as f3:
                    writer = csv.DictWriter(f3, fieldnames=fieldnames)
                    writer.writeheader()
                    for line in lines:
                        if "Complete" in line.split(',')[5]:
                            f3.write(line)
                with open('result.csv') as f2, open('demo005.csv', 'w') as f3:
                    non_blank = (line for line in f2 if line.strip())
                    f3.writelines(non_blank)
                with open('demo005.csv') as f2, open('result.csv', 'w') as f3:
                    non_blank = (line for line in f2 if line.strip())
                    f3.writelines(non_blank)
                f3 = open("result.csv")
                tb = from_csv(f3)
                print(tb)
        elif args.select == 'incomplete':
            with open("csv.csv", 'r+') as f:
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
                f3 = open("result.csv")
                tb = from_csv(f3)
                print(tb)
        elif args.select == 'project':
            data = pd.read_csv("csv.csv", index_col=False)
            data.sort_values(["Project"], axis=0, ascending=True, inplace=True)
            data.to_csv('result.csv', index=False)
            db = open('result.csv')
            tb = from_csv(db)
            print(tb)
        elif args.select == 'context':
            data = pd.read_csv("csv.csv", index_col=False)
            data.sort_values(["Context"], axis=0, ascending=True, inplace=True)
            data.to_csv('result.csv', index=False)
            db = open('result.csv')
            tb = from_csv(db)
            print(tb)
        elif args.select == 'overdue':
            with open("csv.csv", 'r+') as f:
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
            with open("result.csv", 'r+') as f:
                lines = f.readlines()
                with open('demo005.csv', 'w+') as f3:
                    writer = csv.DictWriter(f3, fieldnames=fieldnames)
                    writer.writeheader()
                    time = datetime.datetime.now()
                    t = time.strftime("%d/%m/%Y")
                    for line in lines:
                        if line.split(',')[1] <= t:
                            f3.write(line)
                with open('demo005.csv') as f2, open('result.csv', 'w') as f3:
                    non_blank = (line for line in f2 if line.strip())
                    f3.writelines(non_blank)
                with open('result.csv') as f2, open('demo005.csv', 'w') as f3:
                    non_blank = (line for line in f2 if line.strip())
                    f3.writelines(non_blank)
                f3 = open("demo005.csv")
                tb = from_csv(f3)
                print(tb)

        else:
            print("PLEASE SPECIFY HOW YOU WANT TO SORT USING A "
                  "VALID ARGUMENT -l <complete/incomplete/due/project/context>")


    def delete():
        with open("csv.csv", 'r+') as f:
            lines = f.readlines()
            f.seek(0)

            task = args.select

            for line in lines:
                if not task in line.split(',')[0]:
                    f.write(line)

            f.truncate()
            viewlist()
            print('TASK {} DELETED SUCCESSFULLY'.format(args.select))


    def main():
        if args.option == 'add':
            if args.task == 'error':
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
