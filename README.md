# To-Do-List-Python-CLI-
To-Do List CLI App using python
Yoi should have prettytable installed if you don't have run:
pip install prettytable
your basic commands should be:
python todoarg.py -o <option>
  To add:
  python todoarg.py -o add -t "<task>" -p "<project name>" -s <status>(optional) -d <due today/tomorrow>
  note: '@' is a context identifier whatever you write with @ will be included in the context field
  Eg: task is "Meet @Sam and @Jack" then context will come out as "@Sam & @Jack"
  To view the list:
  python todoarg.py -o view
  To delete an entry:
  python todoarg.py -o delete -l <task number of entry to be deleted>
  To change status of a task from Incomplete to complete:
  python todoarg.py -o modify -l <task number of the task>
  To sort list accroding to due date:
  python todoarg.py -o sort -l due
  To view Completed tasks:
  python todoarg.py -o sort -l status0
  To view Incomplete tasks:
  python todoarg.py -o sort -l status1
    
