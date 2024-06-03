class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def round_robin(processes, time_quantum):
    time = 0
    queue = []
    completed_processes = []
    n = len(processes)

    # Sort processes by arrival time
    processes.sort(key=lambda x: x.arrival_time)
    
    while len(completed_processes) < n:
        # Add processes to the queue that have arrived by current time
        for process in processes:
            if process.arrival_time <= time and process not in queue and process not in completed_processes:
                queue.append(process)

        if queue:
            current_process = queue.pop(0)
            
            if current_process.remaining_time > time_quantum:
                time += time_quantum
                current_process.remaining_time -= time_quantum
                # Add process back to the queue
                queue.append(current_process)
            else:
                time += current_process.remaining_time
                current_process.remaining_time = 0
                current_process.completion_time = time
                completed_processes.append(current_process)
        else:
            time += 1

    # Calculate turnaround and waiting times
    for process in completed_processes:
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time

    # Print results
    print("PID\tArrival\tBurst\tCompletion\tTurnaround\tWaiting")
    for process in completed_processes:
        print(f"{process.pid}\t{process.arrival_time}\t{process.burst_time}\t"
              f"{process.completion_time}\t\t{process.turnaround_time}\t\t{process.waiting_time}")

# Example usage
processes = [
    Process(1, 0, 5),
    Process(2, 1, 4),
    Process(3, 2, 2),
    Process(4, 3, 1),
]

time_quantum = 2
round_robin(processes, time_quantum)
