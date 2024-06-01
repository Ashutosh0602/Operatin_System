class process:
    def __init__(self, id, at, bt, ct):
        self.id=id
        self.at=at
        self.bt=bt
        self.ct=ct
        self.tat=self.ct-self.at
        self.wt=self.tat-self.bt

    def turnaround(self):
        return self.tat
    
    def waiting(self):
        return self.wt
    

n=int(input("Enter the number of Processess: "))

processes=[]
ct=0
for i in range(n):
    print(f'Process {i+1}')
    at = int(input("Enter the Arrival Time:-"))
    bt = int(input("Enter the Burst Time:-"))
    if (len(processes) == 0):
        ct = bt
        processes.append(process(i, at, bt, ct))
    else:
        ct += bt
        processes.append(process(i, at, bt, ct))
 
    print("\n")

avg_wt=0
avg_tat=0

for process in processes:
    avg_wt+=process.waiting()
    avg_tat+=process.turnaround()

print(f"Avg_turnaround:{avg_tat/n}\nAvg_Waitingtime:{avg_wt/n}")