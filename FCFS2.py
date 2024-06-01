class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def calculate_completion_times(processes):
    current_time=0
    for process in processes:
        if current_time<process.arrival_time:
            current_time=process.arrival_time
        current_time+=process.burst_time
        process.completion_time=current_time
    
def calculate_turnaround_times(processes):
    for process in processes:
        process.turnaround_time=process.completion_time-process.arrival_time

def calculate_waiting_times(processes):
    for process in processes:
        process.waiting_time=process.turnaround_time-process.burst_time

def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x.arrival_time)  # Sort by arrival time
    calculate_completion_times(processes)
    calculate_turnaround_times(processes)
    calculate_waiting_times(processes)

    print("PID\tArrival\tBurst\tCompletion\tTurnaround\tWaiting")
    for process in processes:
        print(f"{process.pid}\t{process.arrival_time}\t{process.burst_time}\t"
              f"{process.completion_time}\t\t{process.turnaround_time}\t\t{process.waiting_time}")

processes = [
    Process(1, 6, 2),
    Process(2, 8, 5),
    Process(3, 7, 1),
    Process(4, 3, 0)
]

fcfs_scheduling(processes)
