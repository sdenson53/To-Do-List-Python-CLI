# To-Do-List-Python-CLI-
To-Do List CLI App using python<br>
You should have prettytable installed if you don't have run:<br>
pip install prettytable<br>
your basic commands should be:<br>
python todoarg.py -o <option><br>
  To add:<br>
  python todoarg.py -o add -t "<task>" -p "<project name>" -s <status>(optional) -d <due today/tomorrow><br>
  note: '@' is a context identifier whatever you write with @ will be included in the context field<br>
  Eg: task is "Meet @Sam and @Jack" then context will come out as "@Sam & @Jack"<br>
  To view the list:<br>
  python todoarg.py -o view<br>
  To delete an entry:<br>
  python todoarg.py -o delete -l <task number of entry to be deleted><br>
  To change status of a task from Incomplete to complete:<br>
  python todoarg.py -o modify -l <task number of the task><br>
  To sort list accroding to due date:<br>
  python todoarg.py -o sort -l due<br>
  To view Completed tasks:<br>
  python todoarg.py -o sort -l complete<br>
  To view Incomplete tasks:<br>
  python todoarg.py -o sort -l incomplete<br>
  To sort by project:<br>
  python todoarg.py -o sort -l project<br>
  To sort by context:<br>
  python todoarg.py -o sort -l context<br>
  To show overdue tasks(due today or before today):<br>
  python todoarg.py -o sort -l overdue<br>
  
    
