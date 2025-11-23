# Operating Systems Lab Sheets

## Lab Sheet 1 — Process Management

### Objective
To understand and implement fundamental process management operations in an operating system using Python. This includes process creation, command execution, handling process states, retrieving process information, and observing process priorities.

### Tasks

#### 1. Process Creation
Implement multiple processes using the multiprocessing module. Each process performs a simple task, demonstrating process creation and execution.

#### 2. Command Execution
Use the os.execvp() function to execute system-level commands from within a Python process. This simulates how operating systems replace a process image.

#### 3. Zombie and Orphan Processes
Simulate zombie and orphan process conditions:
- A zombie process is created when a child exits before the parent collects its termination status.
- An orphan process is created when the parent terminates while the child is still running.

#### 4. Process Information
Retrieve essential process information using the psutil library:
- Process ID (PID)
- CPU usage
- Memory usage

#### 5. Process Prioritization
Demonstrate assigning priorities to processes using nice() values to understand CPU allocation behavior.

### Conclusion
Lab Sheet 1 provides a practical understanding of process creation, execution, and management. It demonstrates real-time process behavior such as zombie and orphan states and introduces process priority concepts that help in understanding CPU scheduling and resource management.

---

## Lab Sheet 2 — System Simulation and Synchronization

### Objective
To simulate system boot operations using Python processes, logging mechanisms, and parallel execution. The lab covers system logging, multiple process execution, and controlled system shutdown simulation.

### Tasks

#### 1. Logging Configuration
Configure logging to simulate system boot messages. Logs include timestamped status reports for system initialization.

#### 2. System Process Function
Create a function that represents a system-level task. Each simulated task logs its start, execution, and termination.

#### 3. Concurrent Execution
Use the multiprocessing module to execute multiple system tasks simultaneously, representing parallel system operations.

#### 4. Termination and Shutdown
Enable processes to complete and simulate a clean shutdown message once all processes have concluded.

#### 5. Final Integrated Startup Simulation
Combine logging, multiprocessing, and process execution into a complete startup simulation representing boot sequence, service execution, and system shutdown.

### Conclusion
Lab Sheet 2 demonstrates how system-level operations can be simulated using Python. Through logging and concurrent execution, students gain insights into system boot processes and service management within an operating system.

---

## Lab Sheet 3 — Simulation of File Allocation, Memory Management, and CPU Scheduling

### Objective
To simulate and analyze operating system components such as memory management techniques, CPU scheduling policies, and file allocation strategies. This lab focuses on implementing theoretical OS concepts in Python to understand how these mechanisms work internally.

### Tasks

#### CPU Scheduling Algorithms
- Priority Scheduling  
- Round Robin Scheduling  
- Shortest Job First (SJF)  
- First Come First Serve (FCFS)

#### File Allocation Methods
- Sequential File Allocation  
- Indexed File Allocation  

#### Memory Allocation Algorithms
- First-Fit  
- Best-Fit  
- Worst-Fit  

#### Memory Management Techniques
- MFT (Multiprogramming with Fixed Tasks)  
- MVT (Multiprogramming with Variable Tasks)

### Conclusion
Lab Sheet 3 reinforces core OS concepts by simulating file allocation, memory management, and scheduling algorithms. These programs transform theoretical mechanisms into executable Python simulations, deepening practical understanding.

---

## Lab Sheet 4 — System Information, VM Detection, IPC, and CPU Scheduling

### Objective
To execute various operating system operations including batch processing, system startup simulation, inter-process communication (IPC), OS information retrieval, VM detection, and CPU scheduling algorithms.

### Tasks

#### Task 1 — Batch Processing
Execute a set of Python scripts sequentially using the subprocess module. Each script displays a message, demonstrating automated batch execution.

#### Task 2 — System Startup Simulation
Simulate a system boot sequence using multiprocessing and logging. Two or more processes log their lifecycle events, representing system components during startup and shutdown.

#### Task 3 — Inter-Process Communication (IPC)
Implement IPC using multiprocessing.Pipe(). The parent sends data to the child process, which receives and prints it, demonstrating two-way communication.

#### Task 4A — System Information Retrieval 
Retrieve system details using standard Python libraries:
- Operating system name  
- Username  
- Processor information  

#### Task 4B — Virtual Machine Detection
Detect whether the system is running inside a virtual machine by scanning system information. Identify keywords such as:
- Virtual  
- VMware  
- Hyper-V  
- VirtualBox  
- Hypervisor  

#### Task 5 — CPU Scheduling Algorithms
Implement major CPU scheduling techniques:
- FCFS  
- SJF  
- Priority Scheduling  
- Round Robin  

Each algorithm calculates:
- Waiting Time (WT)  
- Turnaround Time (TAT)  
- Execution order based on defined rules  

### Conclusion
Lab Sheet 4 integrates essential operating system functionalities, including batch execution, IPC, virtualization detection, system information extraction, and CPU scheduling. These tasks provide practical exposure to core OS components and strengthen conceptual understanding through direct implementation.

---

# Tools and Technologies Used

- Python 3.x  
- Visual Studio Code  
- Windows / Linux  
- multiprocessing, subprocess, logging, os, psutil, and platform modules  

---

# Overall Conclusion

This repository provides a complete practical foundation in Operating Systems through four structured lab sheets. By implementing process management, system simulation, memory allocation, file allocation, scheduling algorithms, IPC, and system information retrieval, these labs help understand how an operating system manages resources and executes tasks at a low level.
