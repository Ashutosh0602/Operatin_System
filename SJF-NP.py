class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def calculate_waiting_time(processes):
    n = len(processes)
    processes.sort(key=lambda x: (x.arrival_time, x.burst_time))
    complete = 0
    current_time = 0
    waiting_time = [0] * n

    while complete != n:
        # Find process with minimum burst time among processes that arrived by the current time
        shortest = -1
        min_burst_time = float('inf')
        for i in range(n):
            if processes[i].arrival_time <= current_time and processes[i].burst_time < min_burst_time and waiting_time[i] == 0:
                min_burst_time = processes[i].burst_time
                shortest = i

        if shortest == -1:
            current_time += 1
            continue

        current_time += processes[shortest].burst_time
        processes[shortest].turnaround_time = current_time - processes[shortest].arrival_time
        processes[shortest].waiting_time = processes[shortest].turnaround_time - processes[shortest].burst_time
        waiting_time[shortest] = 1
        complete += 1

def calculate_turnaround_time(processes):
    for process in processes:
        process.turnaround_time = process.burst_time + process.waiting_time

def calculate_average_times(processes):
    total_waiting_time = 0
    total_turnaround_time = 0
    n = len(processes)

    calculate_waiting_time(processes)
    calculate_turnaround_time(processes)

    for process in processes:
        total_waiting_time += process.waiting_time
        total_turnaround_time += process.turnaround_time

    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n

    return avg_waiting_time, avg_turnaround_time

def print_processes(processes):
    print(f"{'PID':<5}{'Burst Time':<12}{'Arrival Time':<14}{'Waiting Time':<14}{'Turnaround Time':<17}")
    for process in processes:
        print(f"{process.pid:<5}{process.burst_time:<12}{process.arrival_time:<14}{process.waiting_time:<14}{process.turnaround_time:<17}")

# Example usage
if __name__ == "__main__":
    processes = [
        Process(1, 6, 2),
        Process(2, 8, 5),
        Process(3, 7, 1),
        Process(4, 3, 0)
    ]

    avg_waiting_time, avg_turnaround_time = calculate_average_times(processes)
    print_processes(processes)
    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")
    