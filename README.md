# OS-LAB-SHEETS
📘 Tasks Included
Task 1 – Process Creation
Demonstrates how a parent process can create multiple child processes using the multiprocessing module.
Each child prints its own PID and parent PID, and the parent waits until all child processes complete.

Task 2 – Command Execution
Shows how a parent process can create child processes that execute Linux commands (ls, date, whoami) using the os.execvp() function.
The parent waits for each child to finish before moving to the next.

Task 3 – Zombie and Orphan Process Simulation
Simulates two special types of processes:
Zombie process: Child exits before the parent calls wait().
Orphan process: Parent exits while the child is still running.
This helps to understand process lifecycle management in operating systems.

Task 4 – Process Information
Uses the psutil library to fetch details about running processes, including PID, process name, status, memory usage, CPU percentage, and open files.

Task 5 – Process Prioritization
Demonstrates CPU scheduling priority using the nice() value.
Multiple CPU-intensive processes are created with different priorities to observe how system scheduling affects execution.

⚙️Tools and Technologies Used
1. Python 3.x
2. Visual Studio Code
3. Ubuntu (Windows Subsystem for Linux – WSL)
4. psutil library (for process management)
